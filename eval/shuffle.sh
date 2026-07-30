#!/usr/bin/env bash
# Create deterministic blinded copies and a private-to-the-judge mapping.
# Usage: bash eval/shuffle.sh <runs_dir>
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS="${1:?usage: shuffle.sh <runs_dir>}"

python3 - "$ROOT" "$RUNS" <<'PY'
import hashlib
import json
import shutil
import sys
from pathlib import Path

root = Path(sys.argv[1])
runs = Path(sys.argv[2])
mapping = {}

for before in sorted((root / "eval" / "fixtures").glob("*/before.md")):
    name = before.parent.name
    raw = sorted((runs / "raw").glob(f"{name}__*.md"))
    if len(raw) != 8:
        raise SystemExit(f"{name}: expected 8 raw outputs, found {len(raw)}")

    ordered = sorted(raw, key=lambda path: hashlib.sha256(path.name.encode()).hexdigest())
    blind_dir = runs / "blind" / name
    blind_dir.mkdir(parents=True, exist_ok=True)
    for old in blind_dir.glob("out-*.md"):
        old.unlink()

    fixture_mapping = {}
    for index, source in enumerate(ordered, start=1):
        blind_name = f"out-{index:02d}.md"
        shutil.copyfile(source, blind_dir / blind_name)
        _, engine, arm = source.stem.split("__")
        fixture_mapping[blind_name] = {
            "engine": engine,
            "arm": arm,
            "bytes": source.stat().st_size,
        }
    mapping[name] = fixture_mapping
    print(f"{name}: {len(fixture_mapping)} outputs")

(runs / "mapping.json").write_text(
    json.dumps(mapping, indent=2, ensure_ascii=True) + "\n",
    encoding="utf-8",
)
print("mapping.json ok")
PY
