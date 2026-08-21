#!/usr/bin/env python3
"""Compare two aggregated runs cell-for-cell. No language model involved.

Reads the scores.json of a baseline run and a candidate run, verifies the two
scored the same (fixture, engine, arm) cells, and prints what changed: pooled
means per arm, per-check pass rates per arm, per-engine and per-fixture skill
means. The control arms tested identical prompts in both runs, so their drift
is the judge-and-sampling noise floor against which skill-arm movement must be
read.

Usage: compare-runs.py <baseline_runs_dir> <candidate_runs_dir>
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


def load(runs: str) -> dict:
    path = Path(runs) / "scores.json"
    if not path.is_file():
        raise SystemExit(f"{path} is missing; run aggregate.py first")
    return json.loads(path.read_text(encoding="utf-8"))


def cell_key(cell: dict) -> tuple:
    return (cell["fixture"], cell["engine"], cell["arm"])


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def arm_cells(scores: dict, arm: str) -> list[dict]:
    return [cell for cell in scores["cells"] if cell["arm"] == arm]


def pooled(cells: list[dict]) -> dict:
    return {
        "structure": mean([c["structure"]["total"] for c in cells]),
        "quality_raw": mean([c["quality_raw"]["total"] for c in cells]),
        "quality_penalized": mean([c["quality_penalized"]["total"] for c in cells]),
    }


def check_rates(cells: list[dict]) -> dict:
    counts: dict[str, list[int]] = defaultdict(list)
    for cell in cells:
        for name, value in cell["checks"].items():
            if value == "na":
                continue
            if name == "first_level_count":
                counts["first_level_count_within_limit"].append(1 if value <= 4 else 0)
            elif name in ("invented_facts", "unacknowledged_source_loss"):
                counts["no_" + name].append(0 if value else 1)
            else:
                counts[name].append(1 if value else 0)
    return {name: (100.0 * sum(v) / len(v), len(v)) for name, v in sorted(counts.items())}


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    base, cand = load(sys.argv[1]), load(sys.argv[2])

    base_keys = {cell_key(c) for c in base["cells"]}
    cand_keys = {cell_key(c) for c in cand["cells"]}
    if base_keys != cand_keys:
        only_base = sorted(base_keys - cand_keys)
        only_cand = sorted(cand_keys - base_keys)
        print("CELL COMPOSITION DIFFERS — deltas below are not cell-for-cell:")
        for key in only_base:
            print(f"  only in baseline:  {key}")
        for key in only_cand:
            print(f"  only in candidate: {key}")
        print()

    print(f"baseline:  {base['run']}  commit {base['commit'][:12]}  cells {base['cells_used']}")
    print(f"candidate: {cand['run']}  commit {cand['commit'][:12]}  cells {cand['cells_used']}")
    print()

    print("== Pooled means per arm (delta = candidate - baseline) ==")
    header = f"{'measure':34} {'arm':8} {'baseline':>9} {'candidate':>10} {'delta':>7}"
    print(header)
    for arm in ("skill", "control"):
        b, c = pooled(arm_cells(base, arm)), pooled(arm_cells(cand, arm))
        for measure, maximum in (("structure", 8), ("quality_raw", 10), ("quality_penalized", 10)):
            print(
                f"{measure + f' /{maximum}':34} {arm:8} {b[measure]:9.3f} {c[measure]:10.3f} "
                f"{c[measure] - b[measure]:+7.3f}"
            )
    print()

    print("== Check pass rates per arm, pct (delta pp) ==")
    for arm in ("skill", "control"):
        b, c = check_rates(arm_cells(base, arm)), check_rates(arm_cells(cand, arm))
        print(f"-- {arm} arm --")
        for name in sorted(set(b) | set(c)):
            bp, bn = b.get(name, (0.0, 0))
            cp, cn = c.get(name, (0.0, 0))
            note = "" if bn == cn else f"  (n {bn}->{cn})"
            print(f"  {name:36} {bp:5.1f} -> {cp:5.1f}  ({cp - bp:+5.1f} pp, n={cn}){note}")
    print()

    print("== Skill-arm quality_raw mean by engine ==")
    for engine in sorted({c["engine"] for c in base["cells"]}):
        b = mean([c["quality_raw"]["total"] for c in arm_cells(base, "skill") if c["engine"] == engine])
        c_ = mean([c["quality_raw"]["total"] for c in arm_cells(cand, "skill") if c["engine"] == engine])
        print(f"  {engine:18} {b:5.2f} -> {c_:5.2f}  ({c_ - b:+5.2f})")
    print()

    print("== Skill-arm structure+quality by fixture (mean over engines) ==")
    for fixture in sorted({c["fixture"] for c in base["cells"]}):
        bs = [c for c in arm_cells(base, "skill") if c["fixture"] == fixture]
        cs = [c for c in arm_cells(cand, "skill") if c["fixture"] == fixture]
        b_s, c_s = mean([c["structure"]["total"] for c in bs]), mean([c["structure"]["total"] for c in cs])
        b_q, c_q = mean([c["quality_raw"]["total"] for c in bs]), mean([c["quality_raw"]["total"] for c in cs])
        print(
            f"  {fixture:24} structure {b_s:4.2f} -> {c_s:4.2f} ({c_s - b_s:+5.2f})   "
            f"quality {b_q:4.2f} -> {c_q:4.2f} ({c_q - b_q:+5.2f})"
        )
    print()

    print("== Hard failures per arm (token: baseline -> candidate) ==")
    for arm in ("skill", "control"):
        b_tally, c_tally = base["hard_failure_tally"][arm], cand["hard_failure_tally"][arm]
        tokens = sorted(set(b_tally) | set(c_tally))
        row = ", ".join(f"{t}: {b_tally.get(t, 0)}->{c_tally.get(t, 0)}" for t in tokens)
        print(f"  {arm:8} {row or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
