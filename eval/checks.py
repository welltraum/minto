#!/usr/bin/env python3
"""The universal-check matrix: importable resolver plus the judge-facing slice.

The judge sees only its own fixture, as it already does for the decisive
questions. So the check definitions are filtered to the checks that apply to this
fixture's mode, and the applicability matrix is resolved before it is handed over:
no other fixture is named, and no check the judge must answer `"na"` for is left
to inference.

`verdict.py` and `aggregate.py` import `applicability_for` and `matrix`, so the
same bytes of `universal-checks.md` drive the prompt, the validator and the rates.

Usage: checks.py <fixture> <mode>
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CHECKS_FILE = Path(__file__).resolve().parent / "universal-checks.md"
BLOCK = re.compile(r"```json\n(.*?)\n```", re.DOTALL)
HEADING = re.compile(r"^### `([a-z_]+)`", re.MULTILINE)


def load_matrix(text: str) -> dict:
    blocks = BLOCK.findall(text)
    if len(blocks) != 1:
        raise SystemExit(
            f"{CHECKS_FILE.name}: expected exactly one json block, found {len(blocks)}"
        )
    return json.loads(blocks[0])


def resolve(matrix: dict, fixture: str, mode: str) -> dict:
    resolved = {}
    overrides = matrix.get("overrides", {}).get(fixture, {})
    for name, spec in matrix["checks"].items():
        if overrides.get(name) == "na" or mode not in spec["modes"]:
            resolved[name] = "na"
        else:
            resolved[name] = "applicable"
    return resolved


def matrix() -> dict:
    """The whole applicability matrix, for callers that aggregate across fixtures."""
    return load_matrix(CHECKS_FILE.read_text(encoding="utf-8"))


def applicability_for(fixture: str, mode: str) -> dict[str, bool]:
    """{check: applies} for one fixture, as both the validator and rates need it."""
    resolved = resolve(matrix(), fixture, mode)
    return {name: state == "applicable" for name, state in resolved.items()}


def fixture_modes(fixtures_dir: Path) -> dict[str, str]:
    """Read `**Mode:** `x`` from each fixture, keyed by fixture name.

    Globs `*/before.md` like every other script in eval/, so the stale prompt-only
    directories left over from the Russian rounds stay excluded.
    """
    modes = {}
    for before in sorted(fixtures_dir.glob("*/before.md")):
        found = re.search(r"^\*\*Mode:\*\*\s*`([a-z]+)`", before.read_text(encoding="utf-8"), re.MULTILINE)
        if not found:
            raise SystemExit(f"{before}: no `**Mode:** `x`` line")
        modes[before.parent.name] = found.group(1)
    return modes


def slice_prose(text: str, applicable: set[str]) -> list[str]:
    """Return the `### `check`` section of every applicable check, in file order."""
    matches = list(HEADING.finditer(text))
    sections = []
    for index, match in enumerate(matches):
        if match.group(1) not in applicable:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        # Stop at the next `## ` heading so a section never swallows the prose
        # that follows the last check of a group.
        chunk = text[match.start() : end]
        chunk = re.split(r"^## ", chunk, maxsplit=1, flags=re.MULTILINE)[0]
        sections.append(chunk.rstrip())
    return sections


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    fixture, mode = sys.argv[1], sys.argv[2]

    text = CHECKS_FILE.read_text(encoding="utf-8")
    matrix = load_matrix(text)
    resolved = resolve(matrix, fixture, mode)
    applicable = {name for name, state in resolved.items() if state == "applicable"}

    spec = {
        "schema_version": matrix["schema_version"],
        "fixture": fixture,
        "mode": mode,
        "checks": {
            name: {
                "type": matrix["checks"][name]["type"],
                "applicable": resolved[name] == "applicable",
            }
            for name in matrix["checks"]
        },
    }

    print("Record these checks for every output, in the section 6 json block.")
    print("They are counts and booleans, not judgements of merit: report what the")
    print("output did, against the definition given, not what it should have done.")
    print()
    for section in slice_prose(text, applicable):
        print(section)
        print()
    print("## Applicability for this fixture")
    print()
    print("Checks marked `\"applicable\": false` must be reported as the string")
    print('`"na"`. Do not omit them and do not guess a value.')
    print()
    print("```json")
    print(json.dumps(spec, indent=2))
    print("```")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
