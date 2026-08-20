#!/usr/bin/env python3
"""Regression tests for the scoring pipeline. Run: python3 eval/test-eval.py

No dependencies and no framework, matching the rest of eval/. These exist because
the pipeline's failure mode is not a crash — it is a plausible wrong number. Every
case below is a mutation that must be rejected; a validator that accepts them all
is indistinguishable from no validator.
"""

from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from checks import applicability_for, fixture_modes, matrix  # noqa: E402
from verdict import (  # noqa: E402
    QUALITY_AXES,
    VerdictError,
    extract_block,
    penalized_quality,
    validate,
)

FIXTURES = HERE / "fixtures"
PASSED: list[str] = []
FAILED: list[str] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    (PASSED if ok else FAILED).append(label)
    mark = "ok  " if ok else "FAIL"
    print(f"{mark} {label}" + (f" — {detail}" if detail and not ok else ""))


GOOD = {
    "schema_version": 1,
    "fixture": "08-techdebt",
    "mode": "write",
    "outputs": [
        {
            "output": "out-01",
            "completed": True,
            "structure": {"total": 8, "top": 2, "key_line_composition": 2, "levels": 2, "order_and_kind": 2},
            "quality": {
                "total": 10, "top": 2, "same_kind_grouping": 2,
                "explainable_order": 2, "mece": 2, "visible_structure": 2,
            },
            "hard_failures": [],
            "checks": {
                "answer_first": True, "first_level_count": 3, "first_level_kind_matches": True,
                "invented_facts": False, "unacknowledged_source_loss": False, "mode_respected": True,
                "readers_question_literal": True, "order_type_named": True,
                "scq_intro_present": True,
            },
        }
    ],
}

MUTATIONS = {
    "axis above 2 is rejected": lambda p: p["outputs"][0]["structure"].update(top=3),
    "axis written as a boolean is rejected": lambda p: p["outputs"][0]["structure"].update(top=True),
    "structure total must equal its axes": lambda p: p["outputs"][0]["structure"].update(total=7),
    "quality total must equal its axes": lambda p: p["outputs"][0]["quality"].update(total=9),
    "unknown hard-failure token is rejected": lambda p: p["outputs"][0]["hard_failures"].append("made_up"),
    "duplicated hard-failure token is rejected": lambda p: p["outputs"][0]["hard_failures"].extend(
        ["invented_facts", "invented_facts"]
    ),
    "invented_facts must agree with hard_failures": lambda p: p["outputs"][0]["checks"].update(invented_facts=True),
    "source loss must agree with hard_failures": lambda p: p["outputs"][0]["checks"].update(
        unacknowledged_source_loss=True
    ),
    "count over the limit needs its failure token": lambda p: p["outputs"][0]["checks"].update(first_level_count=5),
    "failure token needs a count over the limit": lambda p: p["outputs"][0]["hard_failures"].append(
        "more_than_four_first_level"
    ),
    "na on an applicable check is rejected": lambda p: p["outputs"][0]["checks"].update(answer_first="na"),
    "missing check is rejected": lambda p: p["outputs"][0]["checks"].pop("mode_respected"),
    "unexpected check is rejected": lambda p: p["outputs"][0]["checks"].update(invented_vibes=True),
    "boolean check carrying an int is rejected": lambda p: p["outputs"][0]["checks"].update(answer_first=1),
    "negative count is rejected": lambda p: p["outputs"][0]["checks"].update(first_level_count=-1),
    "wrong fixture name is rejected": lambda p: p.update(fixture="04-meeting-note"),
    "unknown schema version is rejected": lambda p: p.update(schema_version=99),
    "missing output is rejected": lambda p: p["outputs"].clear(),
    "extra output is rejected": lambda p: p["outputs"].append(
        copy.deepcopy(p["outputs"][0]) | {"output": "out-99"}
    ),
    "duplicated output is rejected": lambda p: p["outputs"].append(copy.deepcopy(p["outputs"][0])),
    "not-completed cell must null its scores": lambda p: p["outputs"][0].update(completed=False),
}


def test_validator() -> None:
    applies = applicability_for("08-techdebt", "write")
    check(
        "the unmutated payload validates",
        not validate(copy.deepcopy(GOOD), "08-techdebt", {"out-01"}, applies),
        "if this fails, every rejection below is meaningless",
    )
    for label, mutate in MUTATIONS.items():
        payload = copy.deepcopy(GOOD)
        mutate(payload)
        check(label, bool(validate(payload, "08-techdebt", {"out-01"}, applies)))

    # A value where the matrix says "na" needs a fixture that has one.
    payload = copy.deepcopy(GOOD)
    payload["fixture"] = "04-meeting-note"
    check(
        "value on an inapplicable check is rejected",
        bool(validate(payload, "04-meeting-note", {"out-01"}, applicability_for("04-meeting-note", "write"))),
    )

    for label, text in {
        "two json blocks are rejected": "```json\n{}\n```\nprose\n```json\n{}\n```",
        "a missing json block is rejected": "## 1. Score table\nnothing machine-readable",
        "a truncated json block is rejected": '```json\n{"schema_version": 1, "outputs": [\n```',
    }.items():
        try:
            extract_block(text, source="test")
        except VerdictError:
            check(label, True)
        else:
            check(label, False)


def test_penalty_map() -> None:
    quality = {axis: 2 for axis in QUALITY_AXES}
    check(
        "no failures leave quality untouched",
        penalized_quality(quality, [])["total"] == 10,
    )
    check(
        "two failures on one axis zero it once, not twice",
        penalized_quality(quality, ["invented_facts", "unacknowledged_source_loss"])["total"] == 8,
        "the penalty must not be cumulative",
    )
    check(
        "failures on two axes zero both",
        penalized_quality(quality, ["invented_facts", "wrong_language"])["total"] == 6,
    )


def test_applicability() -> None:
    modes = fixture_modes(FIXTURES)
    check("every fixture declares a mode", len(modes) == 11, f"found {len(modes)}")

    counts: dict[str, int] = {name: 0 for name in matrix()["checks"]}
    for fixture, mode in modes.items():
        for name, applies in applicability_for(fixture, mode).items():
            counts[name] += 1 if applies else 0

    universal = [name for name, spec in matrix()["checks"].items() if len(spec["modes"]) == 4]
    check(
        "the three universal checks apply to all eleven fixtures",
        all(counts[name] == 11 for name in universal) and len(universal) == 3,
        f"{ {n: counts[n] for n in universal} }",
    )
    # These denominators encode design decisions, so a silent change to the matrix
    # must break a test rather than quietly move a published percentage.
    for name, expected, why in (
        ("unacknowledged_source_loss", 10, "every mode except digest, whose job is omission"),
        ("answer_first", 9, "write, viz and digest: an audit opens with annotated text"),
        ("first_level_count", 9, "write, viz and digest: audit findings are capped at a different number"),
        ("readers_question_literal", 6, "write only, minus the plain-list override"),
        ("order_type_named", 7, "write and audit, minus the short-note and plain-list overrides"),
        ("scq_intro_present", 6, "write and digest, minus the short-note and plain-list overrides"),
    ):
        check(f"{name} applies to {expected} fixtures ({why})", counts[name] == expected, f"got {counts[name]}")

    # The judge for one fixture must never learn that another exists.
    for fixture, mode in modes.items():
        slice_text = subprocess.run(
            [sys.executable, str(HERE / "checks.py"), fixture, mode],
            capture_output=True, text=True, check=True,
        ).stdout
        others = [other for other in modes if other != fixture and other in slice_text]
        check(f"the {fixture} slice names no other fixture", not others, f"leaked {others}")


def write_run(root: Path, cells: dict[tuple[str, str, str], dict]) -> Path:
    """Build a minimal run directory: mapping.json plus one verdict per fixture."""
    run = root / "run"
    (run / "verdicts").mkdir(parents=True)
    modes = fixture_modes(FIXTURES)
    mapping: dict[str, dict] = {}
    payloads: dict[str, list[dict]] = {}

    for (fixture, engine, arm), overrides in cells.items():
        index = len(mapping.setdefault(fixture, {})) + 1
        name = f"out-{index:02d}"
        mapping[fixture][f"{name}.md"] = {"engine": engine, "arm": arm, "bytes": 1000}
        entry = copy.deepcopy(GOOD["outputs"][0]) | {"output": name} | overrides
        for check_name, applies in applicability_for(fixture, modes[fixture]).items():
            if not applies:
                entry["checks"][check_name] = "na"
        payloads.setdefault(fixture, []).append(entry)

    (run / "mapping.json").write_text(json.dumps(mapping, indent=1), encoding="utf-8")
    for fixture, entries in payloads.items():
        payload = {"schema_version": 1, "fixture": fixture, "mode": modes[fixture], "outputs": entries}
        (run / "verdicts" / f"{fixture}.md").write_text(
            "## 6. Machine-readable scores\n\n```json\n" + json.dumps(payload, indent=2) + "\n```\n",
            encoding="utf-8",
        )
    return run


def run_aggregate(run: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(HERE / "aggregate.py"), str(run), *args],
        capture_output=True, text=True,
    )


def test_aggregator() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        # A balanced two-engine, one-fixture run.
        run = write_run(root, {
            ("08-techdebt", "codex", "skill"): {},
            ("08-techdebt", "codex", "control"): {},
            ("08-techdebt", "kimi", "skill"): {},
            ("08-techdebt", "kimi", "control"): {},
        })
        result = run_aggregate(run)
        check("a balanced run aggregates", result.returncode == 0, result.stderr.strip()[:300])
        if result.returncode == 0:
            scores = json.loads((run / "scores.json").read_text())
            check("every cell is used", scores["cells_used"] == 4)
            check(
                "identical arms produce a zero delta",
                scores["site_metrics"]["quality"]["delta"] == 0,
            )
            check(
                "each site metric carries control, skill and delta",
                all(
                    {"control", "skill", "delta", "label"} <= set(row)
                    for row in scores["site_metrics"].values()
                ),
            )
            check(
                "the delta is the difference of the displayed integers",
                all(
                    row["delta"] == row["skill"] - row["control"]
                    for row in scores["site_metrics"].values()
                ),
            )

        shutil.rmtree(run)
        # One engine with only a skill arm.
        run = write_run(root, {
            ("08-techdebt", "codex", "skill"): {},
            ("08-techdebt", "codex", "control"): {},
            ("08-techdebt", "kimi", "skill"): {},
        })
        strict = run_aggregate(run)
        check("an unpaired arm fails by default", strict.returncode == 1)
        check("the failure names the pair", "08-techdebt/kimi" in strict.stderr, strict.stderr[:200])
        partial = run_aggregate(run, "--allow-partial")
        check("--allow-partial drops the pair instead", partial.returncode == 0, partial.stderr[:200])
        if partial.returncode == 0:
            scores = json.loads((run / "scores.json").read_text())
            check("the dropped pair is recorded with a reason", len(scores["excluded_pairs"]) == 1)
            check("arms stay balanced after the drop",
                  scores["pooled"]["skill"]["n"] == scores["pooled"]["control"]["n"] == 1)

        shutil.rmtree(run)
        # A missing verdict must fail even with --allow-partial: absent evidence is
        # not the same as an absent cell.
        run = write_run(root, {
            ("08-techdebt", "codex", "skill"): {},
            ("08-techdebt", "codex", "control"): {},
        })
        (run / "verdicts" / "08-techdebt.md").unlink()
        result = run_aggregate(run, "--allow-partial")
        check("a missing verdict fails even with --allow-partial", result.returncode == 1)


def main() -> int:
    for suite in (test_validator, test_penalty_map, test_applicability, test_aggregator):
        print(f"\n--- {suite.__name__.removeprefix('test_')} ---")
        suite()
    print(f"\n{len(PASSED)} passed, {len(FAILED)} failed")
    for label in FAILED:
        print(f"  failed: {label}")
    return 1 if FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
