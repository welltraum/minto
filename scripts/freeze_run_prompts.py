#!/usr/bin/env python3
"""Freeze the skill files a judged run was generated with into the run directory.

eval/build-prompts.sh writes the prompts as transient files from whatever skill is
checked out, so the prompts a run actually used exist only at the commit it
recorded. The detail pages show those prompts, and CI checks out shallow, so the
files are copied into `eval/runs/<run>/prompts/` once and committed. The copy is
refused unless SKILL.md hashes to the run's recorded `skill_sha256`.

    python3 scripts/freeze_run_prompts.py --run v1.7.0-final
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = "plugins/minto/skills/minto"
PARTS = (("SKILL.md", "SKILL.md"), ("references/rules.md", "rules.md"), ("references/templates.md", "templates.md"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--run", required=True)
    args = parser.parse_args()

    run_dir = ROOT / "eval" / "runs" / args.run
    scores = json.loads((run_dir / "scores.json").read_text(encoding="utf-8"))
    commits = set(scores["commits"])
    if len(commits) != 1:
        print(f"ERROR: {args.run} was generated at several commits: {sorted(commits)}", file=sys.stderr)
        return 1
    commit = commits.pop()
    recorded = scores["skill_sha256"]
    recorded = recorded[0] if isinstance(recorded, list) else recorded

    out_dir = run_dir / "prompts"
    out_dir.mkdir(exist_ok=True)
    for source, target in PARTS:
        blob = subprocess.run(
            ["git", "show", f"{commit}:{SKILL_DIR}/{source}"],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout
        if source == "SKILL.md":
            digest = hashlib.sha256(blob).hexdigest()
            if digest != recorded:
                print(f"ERROR: SKILL.md at {commit[:7]} hashes to {digest[:12]}, run recorded {recorded[:12]}", file=sys.stderr)
                return 1
        (out_dir / target).write_bytes(blob)
        print(f"{out_dir.relative_to(ROOT)}/{target}  {len(blob):6d} B  from {commit[:7]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
