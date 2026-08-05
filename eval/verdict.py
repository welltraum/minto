#!/usr/bin/env python3
"""Parse and validate the machine-readable block of a judge verdict.

One implementation, two callers: `run-judge.sh` runs it as a CLI to reject a
malformed verdict while a retry is still cheap, and `aggregate.py` imports it.
A second implementation would drift from the first, and the drift would show up as
a silently wrong percentage.

Usage: verdict.py <verdict.md> <fixture> <mode> <out-01,out-02,...>
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BLOCK = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

SCHEMA_VERSION = 1
RUBRIC_PENALTY_VERSION = 1

STRUCTURE_AXES = ("top", "key_line_composition", "levels", "order_and_kind")
QUALITY_AXES = ("top", "same_kind_grouping", "explainable_order", "mece", "visible_structure")

# Mirrors the table in rubric.md. Changing this changes every quality_penalized
# figure, so bump RUBRIC_PENALTY_VERSION with it or cross-run comparison silently
# stops meaning anything.
PENALTY_MAP = {
    "invented_facts": "mece",
    "unacknowledged_source_loss": "mece",
    "more_than_four_first_level": "visible_structure",
    "wrong_language": "visible_structure",
    "audit_returned_rewrite": "top",
    "write_returned_analysis": "top",
    "viz_no_diagram": "top",
    "viz_unrequested_file": "visible_structure",
}
HARD_FAILURE_TOKENS = frozenset(PENALTY_MAP)

CHECK_TYPES = {
    "answer_first": "bool",
    "first_level_count": "int",
    "first_level_kind_matches": "bool",
    "invented_facts": "bool",
    "unacknowledged_source_loss": "bool",
    "mode_respected": "bool",
    "readers_question_literal": "bool",
    "order_type_named": "bool",
}
FIRST_LEVEL_LIMIT = 4


class VerdictError(Exception):
    """A verdict could not be read at all, as distinct from failing validation."""


def extract_block(text: str, source: str = "verdict") -> dict:
    """Return the single fenced json payload, or raise VerdictError."""
    blocks = BLOCK.findall(text)
    if not blocks:
        raise VerdictError(f"{source}: no fenced json block found")
    if len(blocks) > 1:
        raise VerdictError(f"{source}: expected exactly one fenced json block, found {len(blocks)}")
    try:
        payload = json.loads(blocks[0])
    except ValueError as exc:
        raise VerdictError(f"{source}: json block does not parse ({exc})") from exc
    if not isinstance(payload, dict):
        raise VerdictError(f"{source}: json block is not an object")
    return payload


def load(path: Path) -> dict:
    """Read one verdict file and return its payload."""
    return extract_block(path.read_text(encoding="utf-8"), source=path.name)


def merge(payloads: list[dict], source: str = "verdict") -> dict:
    """Combine the parts of a split-judged fixture into one payload."""
    if not payloads:
        raise VerdictError(f"{source}: nothing to merge")
    merged = dict(payloads[0])
    outputs: list[dict] = []
    seen: set[str] = set()
    for payload in payloads:
        for entry in payload.get("outputs", []):
            name = entry.get("output")
            if name in seen:
                raise VerdictError(f"{source}: {name} appears in more than one part")
            seen.add(name)
            outputs.append(entry)
    merged["outputs"] = sorted(outputs, key=lambda entry: str(entry.get("output")))
    return merged


def _is_axis(value: object) -> bool:
    # bool is a subclass of int; an axis written as `true` is a mistake, not a 1.
    return isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 2


def validate(payload: dict, fixture: str, expected_outputs: set[str], applicability: dict[str, bool]) -> list[str]:
    """Return every problem found. An empty list means the payload is usable."""
    problems: list[str] = []
    where = f"{fixture}"

    if payload.get("schema_version") != SCHEMA_VERSION:
        problems.append(f"{where}: schema_version is {payload.get('schema_version')!r}, expected {SCHEMA_VERSION}")
    if payload.get("fixture") != fixture:
        problems.append(f"{where}: json block reports fixture {payload.get('fixture')!r}")

    entries = payload.get("outputs")
    if not isinstance(entries, list):
        problems.append(f"{where}: outputs is not a list")
        return problems

    names = [entry.get("output") for entry in entries if isinstance(entry, dict)]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        problems.append(f"{where}: duplicated outputs {', '.join(map(str, duplicates))}")
    missing = sorted(expected_outputs - set(names))
    if missing:
        problems.append(f"{where}: scored no outputs named {', '.join(missing)}")
    extra = sorted(set(names) - expected_outputs)
    if extra:
        problems.append(f"{where}: scored unknown outputs {', '.join(map(str, extra))}")

    for entry in entries:
        if not isinstance(entry, dict):
            problems.append(f"{where}: an outputs entry is not an object")
            continue
        problems.extend(_validate_entry(entry, where, applicability))

    return problems


def _validate_entry(entry: dict, where: str, applicability: dict[str, bool]) -> list[str]:
    problems: list[str] = []
    name = entry.get("output", "<unnamed>")
    at = f"{where}/{name}"
    completed = entry.get("completed")

    if not isinstance(completed, bool):
        problems.append(f"{at}: completed is not a boolean")
        return problems

    failures = entry.get("hard_failures")
    if not isinstance(failures, list) or not all(isinstance(token, str) for token in failures):
        problems.append(f"{at}: hard_failures is not a list of strings")
        failures = []
    else:
        unknown = sorted(set(failures) - HARD_FAILURE_TOKENS)
        if unknown:
            problems.append(f"{at}: unknown hard-failure tokens {', '.join(unknown)}")
        if len(set(failures)) != len(failures):
            problems.append(f"{at}: duplicated hard-failure tokens")

    if not completed:
        if entry.get("structure") is not None or entry.get("quality") is not None:
            problems.append(f"{at}: completed is false but structure or quality is not null")
        if entry.get("checks") not in ({}, None):
            problems.append(f"{at}: completed is false but checks is not empty")
        return problems

    for field, axes in (("structure", STRUCTURE_AXES), ("quality", QUALITY_AXES)):
        block = entry.get(field)
        if not isinstance(block, dict):
            problems.append(f"{at}: {field} is not an object")
            continue
        bad = [axis for axis in axes if not _is_axis(block.get(axis))]
        if bad:
            problems.append(f"{at}: {field} axes not integers 0-2: {', '.join(bad)}")
            continue
        total = block.get("total")
        expected = sum(block[axis] for axis in axes)
        if total != expected:
            problems.append(f"{at}: {field}.total is {total!r} but its axes sum to {expected}")

    checks = entry.get("checks")
    if not isinstance(checks, dict):
        problems.append(f"{at}: checks is not an object")
        return problems

    unexpected = sorted(set(checks) - set(CHECK_TYPES))
    if unexpected:
        problems.append(f"{at}: unexpected checks {', '.join(unexpected)}")
    absent = sorted(set(CHECK_TYPES) - set(checks))
    if absent:
        problems.append(f"{at}: missing checks {', '.join(absent)}")

    for check, kind in CHECK_TYPES.items():
        if check not in checks:
            continue
        value = checks[check]
        applies = applicability.get(check, True)
        if value == "na":
            if applies:
                problems.append(f"{at}: {check} is \"na\" but applies to this fixture")
            continue
        if not applies:
            problems.append(f"{at}: {check} does not apply to this fixture, expected \"na\"")
            continue
        if kind == "bool" and not isinstance(value, bool):
            problems.append(f"{at}: {check} is {value!r}, expected a boolean")
        if kind == "int" and (not isinstance(value, int) or isinstance(value, bool) or value < 0):
            problems.append(f"{at}: {check} is {value!r}, expected a non-negative integer")

    # The judge restates three decisions it has already made. Disagreement here
    # means one of the two statements is wrong, and there is no way to tell which.
    for token in ("invented_facts", "unacknowledged_source_loss"):
        flagged = token in failures
        checked = checks.get(token)
        if isinstance(checked, bool) and checked != flagged:
            problems.append(
                f"{at}: checks.{token} is {checked} but hard_failures {'lists' if flagged else 'omits'} it"
            )

    count = checks.get("first_level_count")
    if isinstance(count, int) and not isinstance(count, bool):
        over = count > FIRST_LEVEL_LIMIT
        flagged = "more_than_four_first_level" in failures
        if over != flagged:
            problems.append(
                f"{at}: first_level_count is {count} but hard_failures "
                f"{'lists' if flagged else 'omits'} more_than_four_first_level"
            )

    return problems


def penalized_quality(quality: dict, failures: list[str]) -> dict:
    """Apply the rubric penalty map. Two failures on one axis zero it once."""
    zeroed = {PENALTY_MAP[token] for token in failures if token in PENALTY_MAP}
    axes = {axis: (0 if axis in zeroed else quality[axis]) for axis in QUALITY_AXES}
    axes["total"] = sum(axes[axis] for axis in QUALITY_AXES)
    return axes


def main() -> int:
    if len(sys.argv) != 5:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    path, fixture, mode, names = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from checks import applicability_for  # noqa: PLC0415  (CLI-only import)

    try:
        payload = load(Path(path))
    except (VerdictError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    expected = {name.strip() for name in names.split(",") if name.strip()}
    problems = validate(payload, fixture, expected, applicability_for(fixture, mode))
    for problem in problems:
        print(problem, file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
