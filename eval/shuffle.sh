#!/usr/bin/env bash
# Create deterministic blinded copies and a private-to-the-judge mapping.
# Usage: bash eval/shuffle.sh <runs_dir> [expected_outputs] [seed]
#
# expected_outputs: a number to assert per fixture, or "auto"/empty to derive it
#   from the valid outputs found. Also read from $EXPECTED_OUTPUTS (positional wins).
# seed: mixed into the blinding order. Also read from $SHUFFLE_SEED (positional wins).
#   The default empty seed reproduces the pre-seed ordering byte for byte.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS="${1:?usage: shuffle.sh <runs_dir> [expected_outputs] [seed]}"
case "$RUNS" in
  /*) ;;
  *) RUNS="$ROOT/$RUNS" ;;
esac
EXPECTED_OUTPUTS="${2:-${EXPECTED_OUTPUTS:-auto}}"
SHUFFLE_SEED="${3:-${SHUFFLE_SEED:-}}"
MIN_OUTPUT_BYTES="${MIN_OUTPUT_BYTES:-10}"

python3 - "$ROOT" "$RUNS" "$EXPECTED_OUTPUTS" "$SHUFFLE_SEED" "$MIN_OUTPUT_BYTES" <<'PY'
import hashlib
import json
import shutil
import sys
import time
from pathlib import Path

root = Path(sys.argv[1])
runs = Path(sys.argv[2])
expected_raw = sys.argv[3].strip()
seed = sys.argv[4]
min_output_bytes = int(sys.argv[5])

if expected_raw in ("", "auto"):
    expected_outputs = None
else:
    expected_outputs = int(expected_raw)


def read_provenance(path, key):
    """Pull a space-separated list off a `key: a b c` line in engines.txt."""
    if not path.exists():
        return None
    prefix = key + ":"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(prefix):
            return line[len(prefix):].split()
    return None


engines_txt = runs / "engines.txt"
# Only blind what belongs to this run: a shared raw/ directory can hold leftovers
# from an aborted run with different engines. No engines.txt means no filtering.
engines = read_provenance(engines_txt, "engines")
declared_arms = read_provenance(engines_txt, "arms")

fixtures = sorted(
    before.parent.name for before in (root / "eval" / "fixtures").glob("*/before.md")
)

problems = []
notes = []
selected = {}
observed_arms = set()
observed_engines = []

for name in fixtures:
    valid = []
    for source in sorted((runs / "raw").glob(f"{name}__*.md")):
        parts = source.stem.split("__")
        if len(parts) != 3:
            problems.append(f"{name}: malformed output name {source.name}")
            continue
        _, engine, arm = parts
        if engines is not None and engine not in engines:
            continue
        size = source.stat().st_size
        if size <= min_output_bytes:
            notes.append(
                f"{name}/{engine}/{arm}: skipped, {size} B <= min_output_bytes"
            )
            continue
        valid.append((source, engine, arm))
        observed_arms.add(arm)
        if engine not in observed_engines:
            observed_engines.append(engine)
    selected[name] = valid

arms = declared_arms if declared_arms else sorted(observed_arms) or ["control", "skill"]

for name in fixtures:
    valid = selected[name]
    if not valid:
        problems.append(f"{name}: no valid outputs found")
        continue
    if expected_outputs is not None and len(valid) != expected_outputs:
        problems.append(
            f"{name}: expected {expected_outputs} raw outputs, found {len(valid)}"
        )

    # The invariant that matters: an unpaired cell biases the skill-vs-control
    # delta, while a uniformly absent engine merely reduces n.
    by_engine = {}
    for _, engine, arm in valid:
        by_engine.setdefault(engine, []).append(arm)
    for engine in sorted(by_engine):
        present = sorted(set(by_engine[engine]))
        missing = [arm for arm in arms if arm not in present]
        if missing:
            problems.append(
                f"{name}/{engine}: unpaired cell, present {' '.join(present)},"
                f" missing {' '.join(missing)}"
            )

for note in notes:
    print(f"note {note}")

if problems:
    print(f"{len(problems)} problem(s) found; nothing was blinded:", file=sys.stderr)
    for problem in problems:
        print(f"  {problem}", file=sys.stderr)
    raise SystemExit(1)

mapping = {}
counts = []

for name in fixtures:
    ordered = sorted(
        selected[name],
        key=lambda item: hashlib.sha256((seed + item[0].name).encode()).hexdigest(),
    )
    blind_dir = runs / "blind" / name
    blind_dir.mkdir(parents=True, exist_ok=True)
    for old in blind_dir.glob("out-*.md"):
        old.unlink()

    fixture_mapping = {}
    for index, (source, engine, arm) in enumerate(ordered, start=1):
        blind_name = f"out-{index:02d}.md"
        shutil.copyfile(source, blind_dir / blind_name)
        fixture_mapping[blind_name] = {
            "engine": engine,
            "arm": arm,
            "bytes": source.stat().st_size,
        }
    mapping[name] = fixture_mapping
    counts.append((name, len(fixture_mapping)))
    print(f"{name}: {len(fixture_mapping)} outputs")

(runs / "mapping.json").write_text(
    json.dumps(mapping, indent=2, ensure_ascii=True) + "\n",
    encoding="utf-8",
)
print("mapping.json ok")

# Provenance in the plain `key: value` style of engines.txt, plus one
# `outputs <fixture> <count>` line per fixture for awk/str.split() consumers.
lines = [
    f"shuffled_utc: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
    f"seed: {seed}",
    f"min_output_bytes: {min_output_bytes}",
    f"expected_outputs: {expected_raw or 'auto'}",
    "engines: {}".format(" ".join(engines if engines is not None else observed_engines)),
]
lines = [line.rstrip() for line in lines]
lines.extend(f"outputs {name} {count}" for name, count in counts)
(runs / "shuffle.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("shuffle.txt ok")
PY
status=$?
exit "$status"
