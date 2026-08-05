#!/usr/bin/env python3
"""Compute a run's scores from its verdicts. No language model involved.

Reads the machine-readable block of every verdict, joins it to `mapping.json` to
recover which engine and arm each blinded output was, and writes `scores.json` plus
a `scores.md` table. Every percentage published anywhere — report, landing page —
comes from here, so that it can be recomputed from committed artifacts by anyone.

Fails loudly. Every problem is collected, all of them are printed, and nothing is
computed until the list is empty. A benchmark that quietly averages the cells that
happened to parse is worse than one that refuses to answer.

Usage: aggregate.py <runs_dir> [--allow-partial] [--out scores.json] [--md scores.md]
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from checks import applicability_for, fixture_modes, matrix  # noqa: E402
from verdict import (  # noqa: E402
    QUALITY_AXES,
    RUBRIC_PENALTY_VERSION,
    STRUCTURE_AXES,
    VerdictError,
    load,
    merge,
    penalized_quality,
    validate,
)

ROOT = Path(__file__).resolve().parent.parent
STRUCTURE_MAX = 8
QUALITY_MAX = 10
FIRST_LEVEL_LIMIT = 4

# What the landing page is allowed to quote, and the label it carries there.
#
# Chosen on two rules, both of which have to hold:
#   1. the row corresponds to a distinctive, checkable instruction in the skill;
#   2. every metric that moved *against* the skill is included, without exception.
#
# Rule 2 is the one that matters. Picking rows by which direction they point is how
# a benchmark becomes marketing, so a negative result earns its place on the page
# by being negative, not despite it.
#
# Quality uses the raw axes, not the penalized ones. Source loss and invented facts
# already have their own row, so penalizing quality for them too would charge the
# same defect twice — and raw is the more conservative of the two figures.
SITE_METRICS = (
    ("quality", "score", "quality_raw", "Writing quality, share of the judge's 10 points"),
    ("structure", "score", "structure", "Structure, share of the judge's 8 points"),
    ("readers-question", "rate", "readers_question_literal", "The reader's question is written down"),
    ("kind-matches", "rate", "first_level_kind_matches", "First-level points are all the same kind"),
    ("answer-first", "rate", "answer_first", "Answer in the first sentence"),
    ("source-kept", "rate", "no_unacknowledged_source_loss", "No source material lost without saying so"),
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runs_dir", help="run directory, e.g. eval/runs/v1.5.0-wide")
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="drop an unusable (fixture, engine) pair instead of failing; each one is "
        "recorded in scores.json with its reason",
    )
    parser.add_argument("--out", default="scores.json", help="relative to the run directory")
    parser.add_argument("--md", default="scores.md", help="relative to the run directory")
    return parser.parse_args(argv)


def read_kv(path: Path) -> dict[str, str]:
    """Parse the `key: value` provenance files. Repeated keys keep the last."""
    values: dict[str, str] = {}
    if not path.is_file():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" not in line or line.startswith("outputs "):
            continue
        key, _, value = line.partition(":")
        values[key.strip()] = value.strip()
    return values


def read_engine_lines(path: Path) -> dict[str, dict[str, str]]:
    """Pull per-engine provenance out of engines.txt.

    Handles both the flat form (`codex: model=x reasoning_effort=low`) and the
    Claude form (`claude: engine=opus5 model=opus effort=low`).
    """
    engines: dict[str, dict[str, str]] = {}
    if not path.is_file():
        return engines
    for line in path.read_text(encoding="utf-8").splitlines():
        key, _, rest = line.partition(":")
        key, rest = key.strip(), rest.strip()
        if not rest or "=" not in rest:
            continue
        fields = dict(
            part.split("=", 1) for part in rest.split() if "=" in part
        )
        name = fields.pop("engine", None) or key
        if name in {"codex", "kimi", "neuraldeep"} or key in {"codex", "kimi", "claude"} or fields:
            engines.setdefault(name, {}).update(fields)
    return engines


def pct(numerator: float, denominator: float, places: int = 1) -> float:
    """Round half up, not to even. Bankers' rounding puts a delta on the page that
    does not equal the difference of the two numbers a reader can see."""
    if not denominator:
        return 0.0
    quantum = Decimal(1).scaleb(-places)
    value = (Decimal(str(numerator)) / Decimal(str(denominator)) * 100).quantize(
        quantum, rounding=ROUND_HALF_UP
    )
    return float(value) if places else int(value)


def whole(value: float) -> int:
    return int(Decimal(str(value)).quantize(Decimal(1), rounding=ROUND_HALF_UP))


def fmt(value: float, places: int = 2, sign: bool = False) -> str:
    """Render a number half-up.

    Not cosmetic: an f-string rounds half to even, so a mean of exactly 5.625 prints
    as 5.62 while the published figure is 5.63. Every displayed number goes through
    here so the file agrees with itself and with the report.
    """
    quantized = Decimal(str(value)).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)
    text = f"{quantized:f}"
    return f"+{text}" if sign and quantized > 0 else text


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return float(Decimal(str(sum(values) / len(values))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


def collect_cells(runs: Path, problems: list[str]) -> tuple[list[dict], dict[str, str]]:
    """Read every verdict, validate it, and return one record per judged cell."""
    mapping_path = runs / "mapping.json"
    if not mapping_path.is_file():
        problems.append(f"{mapping_path} is missing; run shuffle.sh first")
        return [], {}

    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    modes = fixture_modes(ROOT / "eval" / "fixtures")
    split_fixtures: dict[str, str] = {}
    cells: list[dict] = []

    for fixture in sorted(mapping):
        mode = modes.get(fixture)
        if mode is None:
            problems.append(f"{fixture}: in mapping.json but has no fixture directory")
            continue

        whole_file = runs / "verdicts" / f"{fixture}.md"
        parts = sorted((runs / "verdicts").glob(f"{fixture}.part*.md"))
        sources = [whole_file] if whole_file.is_file() else parts
        if not sources:
            problems.append(f"{fixture}: no verdict at verdicts/{fixture}.md")
            continue
        if whole_file.is_file() and parts:
            problems.append(
                f"{fixture}: both verdicts/{fixture}.md and {len(parts)} part file(s) exist; remove one"
            )
            continue
        if parts:
            split_fixtures[fixture] = f"{len(parts)} parts"

        try:
            payload = merge([load(path) for path in sources], source=fixture)
        except (VerdictError, OSError) as exc:
            problems.append(str(exc))
            continue

        # mapping.json keys carry the .md suffix; the verdict names do not.
        by_output = {name[:-3] if name.endswith(".md") else name: meta for name, meta in mapping[fixture].items()}
        applies = applicability_for(fixture, mode)
        found = validate(payload, fixture, set(by_output), applies)
        if found:
            problems.extend(found)
            continue

        for entry in payload["outputs"]:
            meta = by_output[entry["output"]]
            cells.append(
                {
                    "fixture": fixture,
                    "mode": mode,
                    "engine": meta["engine"],
                    "arm": meta["arm"],
                    "output": entry["output"],
                    "completed": entry["completed"],
                    "structure": entry["structure"],
                    "quality_raw": entry["quality"],
                    "quality_penalized": (
                        penalized_quality(entry["quality"], entry["hard_failures"])
                        if entry["completed"]
                        else None
                    ),
                    "hard_failures": entry["hard_failures"],
                    "checks": entry["checks"],
                    "applicability": applies,
                }
            )

    return cells, split_fixtures


def enforce_pairs(cells: list[dict], allow_partial: bool, problems: list[str]) -> tuple[list[dict], list[dict]]:
    """Keep only (fixture, engine) pairs where both arms are usable.

    An unpaired or incomplete cell shifts the control baseline without shifting the
    skill arm, which is the one quantity this whole run exists to measure. Dropping
    the pair costs n; keeping it corrupts the delta.
    """
    grouped: dict[tuple[str, str], dict[str, dict]] = defaultdict(dict)
    for cell in cells:
        grouped[(cell["fixture"], cell["engine"])][cell["arm"]] = cell

    kept: list[dict] = []
    excluded: list[dict] = []
    for (fixture, engine), arms in sorted(grouped.items()):
        missing = {"skill", "control"} - set(arms)
        incomplete = sorted(arm for arm, cell in arms.items() if not cell["completed"])
        if missing:
            reason = f"only the {', '.join(sorted(arms))} arm was produced"
        elif incomplete:
            reason = f"the {', '.join(incomplete)} arm was not completed"
        else:
            kept.extend(arms.values())
            continue

        excluded.append({"fixture": fixture, "engine": engine, "reason": reason})
        if not allow_partial:
            problems.append(
                f"{fixture}/{engine}: {reason}. Fix the cell, or pass --allow-partial to drop the pair."
            )

    return kept, excluded


def reported_name(name: str, spec: dict) -> str:
    """The name a rate is published under, so every rate reads higher-is-better.

    `invented_facts` at 69% is ambiguous — it could be the defect rate or its
    absence. `no_invented_facts` is not. The renamed forms are the ones listed as
    headline candidates in universal-checks.md.
    """
    if spec["type"] == "int":
        return f"{name}_within_limit"
    return name if spec.get("good", True) else f"no_{name}"


def check_rate(cells: list[dict], name: str) -> dict:
    """Pass rate for one check, reported with the denominator it was computed from."""
    spec = matrix()["checks"][name]
    good = spec.get("good", True)
    applicable = [cell for cell in cells if cell["applicability"].get(name) and cell["checks"].get(name) != "na"]
    if spec["type"] == "int":
        passed = sum(1 for cell in applicable if cell["checks"][name] <= spec.get("limit", FIRST_LEVEL_LIMIT))
    else:
        passed = sum(1 for cell in applicable if bool(cell["checks"][name]) is good)
    return {
        "check": name,
        "pass": passed,
        "applicable": len(applicable),
        "pass_rate_pct": pct(passed, len(applicable)),
    }


def summarize(cells: list[dict]) -> dict:
    """One arm's numbers. Empty input yields zeros with n=0, never a division error."""
    structure = [cell["structure"]["total"] for cell in cells]
    raw = [cell["quality_raw"]["total"] for cell in cells]
    penalized = [cell["quality_penalized"]["total"] for cell in cells]
    # "na" wherever the check does not apply, so the mean is over applicable cells only.
    counts = [
        cell["checks"]["first_level_count"]
        for cell in cells
        if isinstance(cell["checks"].get("first_level_count"), int)
    ]
    clean = sum(1 for cell in cells if not cell["hard_failures"])

    summary = {
        "n": len(cells),
        "structure_mean": mean(structure),
        "structure_pct_of_max": pct(mean(structure), STRUCTURE_MAX),
        "quality_raw_mean": mean(raw),
        "quality_raw_pct_of_max": pct(mean(raw), QUALITY_MAX),
        "quality_penalized_mean": mean(penalized),
        "quality_penalized_pct_of_max": pct(mean(penalized), QUALITY_MAX),
        "first_level_count_mean": mean(counts),
        "first_level_count_n": len(counts),
        "hard_failures_total": sum(len(cell["hard_failures"]) for cell in cells),
        "no_hard_failure": {
            "check": "hard_failures",
            "pass": clean,
            "applicable": len(cells),
            "pass_rate_pct": pct(clean, len(cells)),
        },
        "checks": {
            reported_name(name, spec): check_rate(cells, name)
            for name, spec in matrix()["checks"].items()
        },
    }
    return summary


def delta(control: dict, skill: dict) -> dict:
    """Control → skill, in points, percentage points, and relative terms."""
    out: dict[str, dict] = {}
    for field, maximum in (("structure", STRUCTURE_MAX), ("quality_raw", QUALITY_MAX), ("quality_penalized", QUALITY_MAX)):
        before = control[f"{field}_mean"] if field == "structure" else control[f"{field}_mean"]
        after = skill[f"{field}_mean"]
        out[field] = {
            "control_mean": before,
            "skill_mean": after,
            "points": round(after - before, 4),
            "control_pct_of_max": pct(before, maximum),
            "skill_pct_of_max": pct(after, maximum),
            "pct_points": round(pct(after, maximum) - pct(before, maximum), 1),
            "relative_change_pct": pct(after - before, before) if before else None,
        }
    rates = {}
    for name in list(skill["checks"]) + ["no_hard_failure"]:
        before_rate = (control["checks"] if name != "no_hard_failure" else control)[name]
        after_rate = (skill["checks"] if name != "no_hard_failure" else skill)[name]
        rates[name] = {
            "control_pct": before_rate["pass_rate_pct"],
            "skill_pct": after_rate["pass_rate_pct"],
            "control_applicable": before_rate["applicable"],
            "skill_applicable": after_rate["applicable"],
            "pct_points": round(after_rate["pass_rate_pct"] - before_rate["pass_rate_pct"], 1),
        }
    out["checks"] = rates
    return out


def site_metrics(pooled_delta: dict) -> dict:
    """Whole-number values for the landing page.

    The delta is the difference of the two *displayed* integers, so a reader who
    subtracts what they can see gets the number that is printed.

    Quality uses the raw axes deliberately. The hard-failure rate is already its own
    row, so publishing quality_penalized as well would charge the same defect twice.
    """
    metrics = {}
    for slug, kind, field, label in SITE_METRICS:
        source = pooled_delta[field] if kind == "score" else pooled_delta["checks"][field]
        control = whole(source["control_pct_of_max"] if kind == "score" else source["control_pct"])
        skill = whole(source["skill_pct_of_max"] if kind == "score" else source["skill_pct"])
        metrics[slug] = {
            "label": label,
            "control": control,
            "skill": skill,
            "delta": skill - control,
            "source": field,
            "kind": kind,
        }
    return metrics


def render_md(scores: dict) -> str:
    lines = [
        f"# Deterministic scores: {scores['run']}",
        "",
        f"Generated {scores['generated_utc']} by `eval/aggregate.py` from "
        f"{scores['cells_used']} judged cells. Commit `{scores['commit']}`, worktree "
        f"{scores['worktree']}, rubric penalty version {scores['rubric_penalty_version']}.",
        "",
        "Every number here is computed from the json blocks in `verdicts/`. Quote them; "
        "do not recompute them.",
        "",
        "## Pooled",
        "",
        "| Measure | Control | With skill | Δ | Δ pp | Relative |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    pooled = scores["pooled"]["delta"]
    for field, label, maximum in (
        ("structure", "Structure", STRUCTURE_MAX),
        ("quality_raw", "Quality (as judged)", QUALITY_MAX),
        ("quality_penalized", "Quality (after hard-failure penalty)", QUALITY_MAX),
    ):
        row = pooled[field]
        relative = "n/a" if row["relative_change_pct"] is None else f"{fmt(row['relative_change_pct'], 1, sign=True)}%"
        lines.append(
            f"| {label} /{maximum} | {fmt(row['control_mean'])} ({fmt(row['control_pct_of_max'], 1)}%) "
            f"| {fmt(row['skill_mean'])} ({fmt(row['skill_pct_of_max'], 1)}%) "
            f"| {fmt(row['points'], 2, sign=True)} | {fmt(row['pct_points'], 1, sign=True)} | {relative} |"
        )

    lines += [
        "",
        "## Behaviour pass rates",
        "",
        "`n` is the number of cells the check applies to, per arm. A conditional check "
        "shows a smaller denominator by design.",
        "",
        "| Check | Control | With skill | Δ pp | n per arm |",
        "|---|---:|---:|---:|---:|",
    ]
    for name, row in pooled["checks"].items():
        lines.append(
            f"| `{name}` | {fmt(row['control_pct'], 1)}% | {fmt(row['skill_pct'], 1)}% "
            f"| {fmt(row['pct_points'], 1, sign=True)} | {row['control_applicable']} |"
        )

    lines += [
        "",
        "## By engine",
        "",
        "| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |",
        "|---|---:|---|---|---:|",
    ]
    for engine, arms in scores["by_engine"].items():
        row = arms["delta"]
        lines.append(
            f"| {engine} | {arms['control']['n']} "
            f"| {fmt(row['structure']['control_pct_of_max'], 1)}% → {fmt(row['structure']['skill_pct_of_max'], 1)}% "
            f"| {fmt(row['quality_raw']['control_pct_of_max'], 1)}% → {fmt(row['quality_raw']['skill_pct_of_max'], 1)}% "
            f"| {fmt(row['quality_raw']['pct_points'], 1, sign=True)} |"
        )

    lines += ["", "## Hard failures by type", "", "| Token | Control | With skill |", "|---|---:|---:|"]
    tally = scores["hard_failure_tally"]
    for token in sorted(set(tally["control"]) | set(tally["skill"])):
        lines.append(f"| `{token}` | {tally['control'].get(token, 0)} | {tally['skill'].get(token, 0)} |")
    if not tally["control"] and not tally["skill"]:
        lines.append("| — | 0 | 0 |")

    lines += ["", "## Landing-page figures", "", "| Slug | Label | Control | With skill | Δ pp |", "|---|---|---:|---:|---:|"]
    for slug, row in scores["site_metrics"].items():
        lines.append(f"| `{slug}` | {row['label']} | {row['control']}% | {row['skill']}% | {row['delta']:+d} |")

    if scores["excluded_pairs"]:
        lines += ["", "## Excluded pairs", ""]
        for item in scores["excluded_pairs"]:
            lines.append(f"- `{item['fixture']}` / `{item['engine']}`: {item['reason']}")
    if scores["judge"]["split_fixtures"]:
        lines += ["", "## Split-judged fixtures", ""]
        for fixture, note in scores["judge"]["split_fixtures"].items():
            lines.append(f"- `{fixture}`: {note}")

    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    runs = Path(args.runs_dir)
    if not runs.is_absolute():
        runs = ROOT / runs
    if not runs.is_dir():
        print(f"{runs} is not a directory", file=sys.stderr)
        return 2

    problems: list[str] = []
    cells, split_fixtures = collect_cells(runs, problems)
    kept, excluded = enforce_pairs(cells, args.allow_partial, problems)

    if problems:
        print(f"{len(problems)} problem(s) found; nothing was computed:\n", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        print(
            "\nDelete the affected verdicts and re-run run-judge.sh, or pass --allow-partial "
            "if the gaps are real.",
            file=sys.stderr,
        )
        return 1
    if not kept:
        print("no usable cells", file=sys.stderr)
        return 1

    engines_meta = read_engine_lines(runs / "engines.txt")
    provenance = read_kv(runs / "engines.txt")
    judge_meta = read_kv(runs / "judge.txt")

    by_arm = defaultdict(list)
    for cell in kept:
        by_arm[cell["arm"]].append(cell)
    by_engine_arm = defaultdict(lambda: defaultdict(list))
    for cell in kept:
        by_engine_arm[cell["engine"]][cell["arm"]].append(cell)

    tally: dict[str, dict[str, int]] = {"skill": {}, "control": {}}
    for cell in kept:
        for token in cell["hard_failures"]:
            tally[cell["arm"]][token] = tally[cell["arm"]].get(token, 0) + 1

    pooled_control = summarize(by_arm["control"])
    pooled_skill = summarize(by_arm["skill"])
    pooled_delta = delta(pooled_control, pooled_skill)

    scores = {
        "schema_version": 1,
        "run": runs.name,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "commit": provenance.get("commit", "unknown"),
        "worktree": provenance.get("worktree", "unknown"),
        "rubric_penalty_version": RUBRIC_PENALTY_VERSION,
        "fixtures": sorted({cell["fixture"] for cell in kept}),
        "cells_used": len(kept),
        "judge": {
            "model": judge_meta.get("judge_model", "unknown"),
            "effort": judge_meta.get("judge_effort", "unknown"),
            "attempts": judge_meta.get("judge_attempts", "unknown"),
            "rubric_sha256": judge_meta.get("rubric_sha256", "unknown"),
            "universal_checks_sha256": judge_meta.get("universal_checks_sha256", "unknown"),
            "split_fixtures": split_fixtures,
        },
        "engines": {
            engine: engines_meta.get(engine, {}) for engine in sorted(by_engine_arm)
        },
        "excluded_pairs": excluded,
        "hard_failure_tally": tally,
        "pooled": {"control": pooled_control, "skill": pooled_skill, "delta": pooled_delta},
        "by_engine": {},
        "cells": [
            {key: cell[key] for key in cell if key != "applicability"}
            for cell in sorted(kept, key=lambda c: (c["fixture"], c["engine"], c["arm"]))
        ],
    }
    scores["site_metrics"] = site_metrics(pooled_delta)

    for engine in sorted(by_engine_arm):
        control = summarize(by_engine_arm[engine]["control"])
        skill = summarize(by_engine_arm[engine]["skill"])
        scores["by_engine"][engine] = {"control": control, "skill": skill, "delta": delta(control, skill)}

    (runs / args.out).write_text(json.dumps(scores, indent=2) + "\n", encoding="utf-8")
    (runs / args.md).write_text(render_md(scores), encoding="utf-8")

    print(f"{len(kept)} cells over {len(scores['fixtures'])} fixtures and {len(by_engine_arm)} engines")
    for slug, row in scores["site_metrics"].items():
        print(f"  {slug:14} {row['control']:3d}% -> {row['skill']:3d}%  ({row['delta']:+d} pp)")
    if excluded:
        print(f"  {len(excluded)} pair(s) excluded; see {args.out}")
    print(f"wrote {runs / args.out} and {runs / args.md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
