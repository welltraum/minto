#!/usr/bin/env python3
"""Assert the benchmark figures on the site match the run they claim to come from.

`check_site.py` validates that references resolve. It cannot notice that a
percentage on the page is one re-judged run out of date, which is the failure that
actually matters: a stale number is still a published claim.

Every figure the page shows carries `data-*` attributes naming its value. This
script compares them against `scores.json` — the aggregator's output, not prose —
and then compares them against the *rendered text of the same row*, because
attributes that silently disagree with the visible copy would pass a weaker check
while misleading every reader.
"""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PAGES = (SITE / "index.html", SITE / "ru" / "index.html")
DEFAULT_RUN = "v1.5.0-wide"

# Attributes carried by the fixture-08 example panels, checked against the cell the
# example claims to quote.
EXAMPLE_ATTRS = ("data-fixture", "data-engine", "data-arm", "data-structure", "data-quality")


class MetricParser(HTMLParser):
    """Collect elements carrying data-metric or data-fixture, with their text."""

    def __init__(self) -> None:
        super().__init__()
        self.rows: list[dict] = []
        self.tags: list[str] = []
        self._stack: list[dict] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag)
        values = {key: (value or "") for key, value in attrs}
        if "data-metric" in values or "data-fixture" in values:
            row = {"tag": tag, "attrs": values, "text": [], "depth": len(self._stack)}
            self._stack.append(row)
            self.rows.append(row)
        elif self._stack:
            self._stack[-1].setdefault("open", 0)
            self._stack[-1]["open"] = self._stack[-1].get("open", 0) + 1
        # Void elements never close, so they must not increment the open count.
        if tag in {"br", "img", "input", "hr", "meta", "link"} and self._stack:
            self._stack[-1]["open"] = max(0, self._stack[-1].get("open", 0) - 1)

    def handle_endtag(self, tag: str) -> None:
        if self._stack:
            if self._stack[-1].get("open", 0) > 0:
                self._stack[-1]["open"] -= 1
            else:
                self._stack.pop()

    def handle_data(self, data: str) -> None:
        for row in self._stack:
            row["text"].append(data)


def parse_page(path: Path) -> tuple[list[dict], list[str]]:
    parser = MetricParser()
    parser.feed(path.read_text(encoding="utf-8"))
    for row in parser.rows:
        row["text"] = re.sub(r"\s+", " ", "".join(row["text"])).strip()
    return parser.rows, parser.tags


def as_int(value: str) -> int | None:
    try:
        return int(value.strip().lstrip("+"))
    except ValueError:
        return None


def check_metrics(page: Path, rows: list[dict], metrics: dict, errors: list[str]) -> set[str]:
    label = page.relative_to(ROOT)
    seen: set[str] = set()

    for row in rows:
        slug = row["attrs"].get("data-metric")
        if slug is None:
            continue
        seen.add(slug)
        if slug not in metrics:
            errors.append(f"{label}: data-metric={slug!r} is not in scores.json")
            continue

        expected = metrics[slug]
        control = as_int(row["attrs"].get("data-control", ""))
        skill = as_int(row["attrs"].get("data-skill", ""))
        delta = as_int(row["attrs"].get("data-delta", ""))

        if control != expected["control"]:
            errors.append(f"{label}: {slug} data-control is {control}, scores.json says {expected['control']}")
        if skill != expected["skill"]:
            errors.append(f"{label}: {slug} data-skill is {skill}, scores.json says {expected['skill']}")
        if delta != expected["delta"]:
            errors.append(f"{label}: {slug} data-delta is {delta}, scores.json says {expected['delta']}")
        if None not in (control, skill, delta) and delta != skill - control:
            errors.append(f"{label}: {slug} data-delta {delta} is not data-skill minus data-control")

        # The attributes are invisible; the copy is what a reader acts on.
        for name, value in (("control", control), ("skill", skill)):
            if value is not None and f"{value}%" not in row["text"]:
                errors.append(
                    f"{label}: {slug} claims {name} {value}% but that percentage does not "
                    f"appear in the row text: {row['text'][:90]!r}"
                )

    missing = set(metrics) - seen
    if missing:
        errors.append(f"{label}: scores.json has metrics the page never shows: {', '.join(sorted(missing))}")
    return seen


def check_example(page: Path, rows: list[dict], scores: dict, errors: list[str]) -> None:
    label = page.relative_to(ROOT)
    cells = {
        (cell["fixture"], cell["engine"], cell["arm"]): cell
        for cell in scores.get("cells", [])
    }
    panels = [row for row in rows if "data-fixture" in row["attrs"]]
    if not panels:
        errors.append(f"{label}: no element carries data-fixture, so the quoted example is unverifiable")
        return

    for row in panels:
        attrs = row["attrs"]
        missing = [name for name in EXAMPLE_ATTRS if name not in attrs]
        if missing:
            errors.append(f"{label}: example panel is missing {', '.join(missing)}")
            continue
        key = (attrs["data-fixture"], attrs["data-engine"], attrs["data-arm"])
        cell = cells.get(key)
        if cell is None:
            errors.append(f"{label}: example cites {key} which is not a cell in scores.json")
            continue
        for name, actual in (
            ("data-structure", cell["structure"]["total"]),
            ("data-quality", cell["quality_raw"]["total"]),
        ):
            claimed = as_int(attrs[name])
            if claimed != actual:
                errors.append(f"{label}: example {key} {name} is {claimed}, the verdict says {actual}")
        failures = as_int(attrs.get("data-hard-failures", "0"))
        if failures is not None and failures != len(cell["hard_failures"]):
            errors.append(
                f"{label}: example {key} data-hard-failures is {failures}, "
                f"the verdict lists {len(cell['hard_failures'])}"
            )


def check_parity(pages: dict[Path, tuple[list[dict], list[str]]], errors: list[str]) -> None:
    """The two locales are maintained as line-for-line mirrors; keep them that way."""
    (first, (first_rows, first_tags)), (second, (second_rows, second_tags)) = pages.items()
    first_lines = len(first.read_text(encoding="utf-8").splitlines())
    second_lines = len(second.read_text(encoding="utf-8").splitlines())
    if first_lines != second_lines:
        errors.append(
            f"{first.relative_to(ROOT)} has {first_lines} lines but "
            f"{second.relative_to(ROOT)} has {second_lines}; the pages must stay parallel"
        )
    if first_tags != second_tags:
        for index, (left, right) in enumerate(zip(first_tags, second_tags)):
            if left != right:
                errors.append(
                    f"the pages diverge at tag {index}: {first.relative_to(ROOT)} has <{left}>, "
                    f"{second.relative_to(ROOT)} has <{right}>"
                )
                break
        else:
            errors.append("the pages have different tag counts")

    first_slugs = {row["attrs"]["data-metric"] for row in first_rows if "data-metric" in row["attrs"]}
    second_slugs = {row["attrs"]["data-metric"] for row in second_rows if "data-metric" in row["attrs"]}
    if first_slugs != second_slugs:
        errors.append(f"metric slugs differ between locales: {first_slugs ^ second_slugs}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", default=DEFAULT_RUN, help="run directory name under eval/runs/")
    args = parser.parse_args()

    scores_path = ROOT / "eval" / "runs" / args.run / "scores.json"
    if not scores_path.is_file():
        print(f"ERROR: {scores_path.relative_to(ROOT)} is missing; run eval/aggregate.py first")
        return 1

    scores = json.loads(scores_path.read_text(encoding="utf-8"))
    metrics = scores.get("site_metrics")
    if not metrics:
        print(f"ERROR: {scores_path.relative_to(ROOT)} has no site_metrics block")
        return 1

    errors: list[str] = []
    parsed = {}
    for page in PAGES:
        if not page.is_file():
            errors.append(f"missing page: {page.relative_to(ROOT)}")
            continue
        rows, tags = parse_page(page)
        parsed[page] = (rows, tags)
        check_metrics(page, rows, metrics, errors)
        check_example(page, rows, scores, errors)

    if len(parsed) == 2:
        check_parity(parsed, errors)

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1

    print(
        f"Validated {len(metrics)} benchmark figures across {len(parsed)} locales "
        f"against eval/runs/{args.run}/scores.json (commit {scores.get('commit', 'unknown')[:12]})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
