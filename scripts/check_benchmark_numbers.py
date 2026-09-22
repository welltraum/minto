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
import statistics
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
# The map's rows, columns and measure names are page structure, so they are read
# from the generator that lays them out. Every number below is still re-derived
# from scores.json here, which is the part that has to stay independent.
from build_eval_map import ENGINES, FIXTURES, MEASURES, MINUS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
# Locale pairs, with the checks that apply to each. Adding a page to a flat
# tuple instead would have pushed the old `len(parsed) == 2` guard false and
# silently switched parity off for every pair at once.
PAGE_PAIRS = (
    (
        (SITE / "index.html", SITE / "ru" / "index.html"),
        ("section", "metrics", "figures", "example"),
    ),
    (
        (SITE / "eval-map" / "index.html", SITE / "ru" / "eval-map" / "index.html"),
        ("section", "map"),
    ),
)
DEFAULT_RUN = "v1.7.0-final"

# Attributes carried by the fixture-08 example panels, checked against the cell the
# example claims to quote.
EXAMPLE_ATTRS = ("data-fixture", "data-engine", "data-arm", "data-structure", "data-quality")


VOID_TAGS = frozenset({"br", "img", "input", "hr", "meta", "link", "source", "area", "base", "col", "embed", "param", "track", "wbr"})


class MetricParser(HTMLParser):
    """Collect elements carrying data-metric or data-fixture, with their text."""

    def __init__(self) -> None:
        super().__init__()
        self.rows: list[dict] = []
        self.tags: list[str] = []
        self.paths: list[str] = []
        self.section: dict[str, str] = {}
        self._open: list[str] = []
        self._stack: list[dict] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag)
        values = {key: (value or "") for key, value in attrs}
        if "data-benchmark" in values:
            self.section = {k: v for k, v in values.items() if k.startswith("data-")}
        # Record where in the tree each element sits, not just that it exists. A
        # start-tag sequence alone is blind to nesting: moving a <p> out of its
        # parent <div> leaves the sequence untouched.
        self.paths.append("/".join(self._open + [tag]))
        if tag not in VOID_TAGS:
            self._open.append(tag)
        if values.keys() & {"data-metric", "data-fixture", "data-figure", "data-cell", "data-cell-missing", "data-row-avg"}:
            row = {"tag": tag, "attrs": values, "text": [], "depth": len(self._stack)}
            self._stack.append(row)
            self.rows.append(row)
        elif self._stack:
            self._stack[-1].setdefault("open", 0)
            self._stack[-1]["open"] = self._stack[-1].get("open", 0) + 1
        # Void elements never close, so they must not increment the open count.
        # This must stay the same set as VOID_TAGS: any void tag missing here
        # leaves the counter high for good and the row never pops.
        if tag in VOID_TAGS and self._stack:
            self._stack[-1]["open"] = max(0, self._stack[-1].get("open", 0) - 1)

    def handle_endtag(self, tag: str) -> None:
        if tag in self._open:
            while self._open and self._open.pop() != tag:
                pass
        if self._stack:
            if self._stack[-1].get("open", 0) > 0:
                self._stack[-1]["open"] -= 1
            else:
                self._stack.pop()

    def handle_data(self, data: str) -> None:
        for row in self._stack:
            row["text"].append(data)


def parse_page(path: Path) -> tuple[list[dict], list[str], dict[str, str]]:
    parser = MetricParser()
    parser.feed(path.read_text(encoding="utf-8"))
    for row in parser.rows:
        row["text"] = re.sub(r"\s+", " ", "".join(row["text"])).strip()
    return parser.rows, parser.paths, parser.section


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


def check_figures(page: Path, rows: list[dict], scores: dict, metrics: dict, errors: list[str]) -> None:
    """The headline band is four numbers set large; large is exactly where a stale
    figure does the most damage. Each one names where it comes from and is derived
    here, never transcribed."""
    label = page.relative_to(ROOT)
    figures = [row for row in rows if "data-figure" in row["attrs"]]
    if not figures:
        errors.append(f"{label}: no element carries data-figure, so the headline band is unverifiable")
        return

    for row in figures:
        kind = row["attrs"]["data-figure"]
        text = row["text"]
        if kind == "cells":
            expected = scores["cells_used"]
        elif kind == "engines":
            expected = len(scores["engines"])
        elif kind == "metric-delta":
            slug = row["attrs"].get("data-metric-ref", "")
            if slug not in metrics:
                errors.append(f"{label}: figure data-metric-ref={slug!r} is not in scores.json")
                continue
            expected = metrics[slug]["delta"]
        else:
            errors.append(f"{label}: unknown data-figure kind {kind!r}")
            continue

        shown = figure_value(text)
        if shown != expected:
            errors.append(
                f"{label}: figure {kind}"
                + (f" ({row['attrs'].get('data-metric-ref')})" if kind == "metric-delta" else "")
                + f" reads {shown!r} but scores.json gives {expected}"
            )
        if kind == "metric-delta" and (expected < 0) != ("figure--down" in row["attrs"].get("class", "")):
            errors.append(
                f"{label}: figure {row['attrs'].get('data-metric-ref')} is {expected} but its "
                f"class does not match the sign; a loss must carry figure--down"
            )


def figure_value(text: str) -> int | None:
    """The first signed number in the cell's own visible text."""
    match = re.search(r"([+\u2212\u2013-]?)\s*(\d+)", text)
    if match is None:
        return None
    value = int(match.group(2))
    return -value if match.group(1) in {"\u2212", "\u2013", "-"} else value


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


def check_section(page: Path, section: dict[str, str], scores: dict, errors: list[str]) -> None:
    label = page.relative_to(ROOT)
    if not section:
        errors.append(f"{label}: no element carries data-benchmark, so the run it quotes is unstated")
        return
    run = section.get("data-benchmark")
    if run != scores["run"]:
        errors.append(f"{label}: data-benchmark is {run!r} but scores.json is for {scores['run']!r}")
    cells = as_int(section.get("data-benchmark-cells", ""))
    if cells != scores["cells_used"]:
        errors.append(
            f"{label}: data-benchmark-cells is {cells}, scores.json used {scores['cells_used']}"
        )


MAX_CELL_ERRORS = 20


def check_map(page: Path, rows: list[dict], scores: dict, errors: list[str]) -> None:
    """Re-derive every figure on the eval map straight from the judged cells.

    This is deliberately a second code path. `build_eval_map.py --check` proves the
    page is what the generator renders; it cannot notice that the generator reads
    the wrong measure. Only arithmetic done again from scores.json can.
    """
    label = page.relative_to(ROOT)
    pairs: dict[tuple[str, str], dict[str, dict]] = {}
    for cell in scores.get("cells", []):
        pairs.setdefault((cell["fixture"], cell["engine"]), {})[cell["arm"]] = cell
    complete = {key for key, arms in pairs.items() if {"control", "skill"} <= set(arms)}

    measures = {name: source for name, source, _ in MEASURES}
    expected_rows = [fixture for fixture, *_ in FIXTURES]
    expected_engines = [engine for engine, _ in ENGINES]

    found: dict[str, list[tuple[str, str]]] = {name: [] for name in measures}
    deltas: dict[tuple[str, str, str], int] = {}
    order: dict[str, list[str]] = {name: [] for name in measures}
    cell_errors: list[str] = []

    for row in rows:
        attrs = row["attrs"]
        measure = attrs.get("data-cell-measure")

        if "data-cell" in attrs:
            fixture = attrs.get("data-cell-fixture", "")
            engine = attrs.get("data-cell-engine", "")
            if measure not in measures:
                cell_errors.append(f"{label}: cell {fixture}×{engine} names measure {measure!r}, which is not in this run")
                continue
            found[measure].append((fixture, engine))
            if not order[measure] or order[measure][-1] != fixture:
                order[measure].append(fixture)

            pair = pairs.get((fixture, engine), {})
            if not {"control", "skill"} <= set(pair):
                cell_errors.append(f"{label}: cell {fixture}×{engine} carries numbers but scores.json has no complete pair")
                continue

            for name, source in measures.items():
                control = as_int(attrs.get(f"data-{name}-control", ""))
                skill = as_int(attrs.get(f"data-{name}-skill", ""))
                delta = as_int(attrs.get(f"data-{name}-delta", ""))
                want_control = pair["control"][source]["total"]
                want_skill = pair["skill"][source]["total"]
                if control != want_control:
                    cell_errors.append(f"{label}: cell {fixture}×{engine} data-{name}-control is {control}, scores.json says {want_control}")
                if skill != want_skill:
                    cell_errors.append(f"{label}: cell {fixture}×{engine} data-{name}-skill is {skill}, scores.json says {want_skill}")
                if delta != want_skill - want_control:
                    cell_errors.append(f"{label}: cell {fixture}×{engine} data-{name}-delta is {delta}, scores.json gives {want_skill - want_control}")
                if name == measure and delta is not None:
                    deltas[(measure, fixture, engine)] = delta

            # The attributes are invisible; the number is what a reader acts on.
            shown = figure_value(row["text"].split(",")[0])
            want = pair["skill"][measures[measure]]["total"] - pair["control"][measures[measure]]["total"]
            if shown != want:
                cell_errors.append(f"{label}: cell {fixture}×{engine} renders {row['text'].split(',')[0]!r} but {measure} moved {want:+d}")

        elif "data-cell-missing" in attrs:
            fixture = attrs.get("data-cell-fixture", "")
            engine = attrs.get("data-cell-engine", "")
            if measure not in measures:
                cell_errors.append(f"{label}: empty cell {fixture}×{engine} names measure {measure!r}, which is not in this run")
                continue
            found[measure].append((fixture, engine))
            if not order[measure] or order[measure][-1] != fixture:
                order[measure].append(fixture)
            if (fixture, engine) in complete:
                cell_errors.append(f"{label}: cell {fixture}×{engine} is drawn empty but scores.json judged both arms")
            if any(key.startswith("data-structure-") or key.startswith("data-quality-") for key in attrs):
                cell_errors.append(f"{label}: empty cell {fixture}×{engine} still carries measure attributes")

    # Every declared slot appears exactly once per view, and nothing else does.
    wanted = {(fixture, engine) for fixture in expected_rows for engine in expected_engines}
    for measure in measures:
        seen = found[measure]
        if len(seen) != len(set(seen)):
            errors.append(f"{label}: the {measure} view draws a cell twice")
        missing = wanted - set(seen)
        extra = set(seen) - wanted
        if missing:
            errors.append(f"{label}: the {measure} view is missing {len(missing)} cells, including {sorted(missing)[0]}")
        if extra:
            errors.append(f"{label}: the {measure} view draws {sorted(extra)[0]}, which this page does not declare")
        if order[measure] != expected_rows:
            errors.append(f"{label}: the {measure} view orders its cases {order[measure]} rather than {expected_rows}")

    # The absent pairs are asserted positively, so a dropped column cannot hide
    # behind a hole that looks deliberate.
    drawn_empty = {
        (row["attrs"].get("data-cell-fixture", ""), row["attrs"].get("data-cell-engine", ""))
        for row in rows
        if "data-cell-missing" in row["attrs"]
    }
    # A pair with no cell at all never reaches `pairs`, so the hole has to be
    # computed from the declared grid rather than from what the run contains.
    unjudged = {key for key in wanted if key not in complete}
    if drawn_empty != unjudged:
        errors.append(
            f"{label}: the empty cells are {sorted(drawn_empty)} but scores.json leaves {sorted(unjudged)} unjudged"
        )

    for row in rows:
        attrs = row["attrs"]
        if "data-row-avg" not in attrs:
            continue
        measure = attrs.get("data-row-measure")
        fixture = attrs.get("data-row-fixture", "")
        if measure not in measures:
            errors.append(f"{label}: row mean for {fixture} names measure {measure!r}, which is not in this run")
            continue
        source = measures[measure]
        values = [
            pairs[(fixture, engine)]["skill"][source]["total"] - pairs[(fixture, engine)]["control"][source]["total"]
            for engine in expected_engines
            if (fixture, engine) in complete
        ]
        if not values:
            errors.append(f"{label}: row mean for {fixture} has no judged cells behind it")
            continue
        mean = round(statistics.fmean(values), 1)
        want = f"{'+' if mean > 0 else MINUS if mean < 0 else ''}{abs(mean):.1f}"
        if row["text"] != want:
            errors.append(f"{label}: {fixture} {measure} mean reads {row['text']!r} but its {len(values)} cells give {want!r}")

    if cell_errors:
        errors.extend(cell_errors[:MAX_CELL_ERRORS])
        if len(cell_errors) > MAX_CELL_ERRORS:
            errors.append(f"{label}: and {len(cell_errors) - MAX_CELL_ERRORS} further cell disagreements; the page is out of date with {scores['run']}")


def check_map_parity(first: Path, second: Path, first_rows: list[dict], second_rows: list[dict], errors: list[str]) -> None:
    """check_parity compares tag paths only, so the two locales could carry
    different numbers and go unnoticed. Compare the data streams themselves."""

    def stream(rows: list[dict]) -> list[tuple]:
        return [
            tuple(sorted((k, v) for k, v in row["attrs"].items() if k.startswith("data-")))
            for row in rows
            if row["attrs"].keys() & {"data-cell", "data-cell-missing", "data-row-avg"}
        ]

    left, right = stream(first_rows), stream(second_rows)
    if left != right:
        for index, (a, b) in enumerate(zip(left, right)):
            if a != b:
                errors.append(
                    f"the locales carry different map data at cell {index}: "
                    f"{first.relative_to(ROOT)} has {dict(a)}, {second.relative_to(ROOT)} has {dict(b)}"
                )
                break
        else:
            errors.append(f"the locales draw a different number of map cells: {len(left)} vs {len(right)}")


def check_parity(
    first: Path,
    second: Path,
    first_parsed: tuple[list[dict], list[str]],
    second_parsed: tuple[list[dict], list[str]],
    compare_metric_slugs: bool,
    errors: list[str],
) -> None:
    """The two locales are maintained as line-for-line mirrors; keep them that way."""
    (first_rows, first_tags), (second_rows, second_tags) = first_parsed, second_parsed
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
                    f"the pages diverge at element {index}: {first.relative_to(ROOT)} has "
                    f"{left}, {second.relative_to(ROOT)} has {right}"
                )
                break
        else:
            errors.append(
                f"the pages have different element counts: {len(first_tags)} vs {len(second_tags)}"
            )

    if not compare_metric_slugs:
        return

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
    locales = 0
    for pages, checks in PAGE_PAIRS:
        parsed: dict[Path, tuple[list[dict], list[str]]] = {}
        for page in pages:
            if not page.is_file():
                errors.append(f"missing page: {page.relative_to(ROOT)}")
                continue
            rows, tags, section = parse_page(page)
            parsed[page] = (rows, tags)
            locales += 1
            if "section" in checks:
                check_section(page, section, scores, errors)
            if "metrics" in checks:
                check_metrics(page, rows, metrics, errors)
            if "figures" in checks:
                check_figures(page, rows, scores, metrics, errors)
            if "example" in checks:
                check_example(page, rows, scores, errors)
            if "map" in checks:
                check_map(page, rows, scores, errors)

        if len(parsed) == 2:
            (first, first_parsed), (second, second_parsed) = parsed.items()
            check_parity(first, second, first_parsed, second_parsed, "metrics" in checks, errors)
            if "map" in checks:
                check_map_parity(first, second, first_parsed[0], second_parsed[0], errors)
        else:
            errors.append(
                "a locale pair is incomplete, so parity went unchecked: "
                + ", ".join(str(page.relative_to(ROOT)) for page in pages)
            )

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1

    print(
        f"Validated {len(metrics)} benchmark figures and the eval map across {locales} pages "
        f"against eval/runs/{args.run}/scores.json (commit {scores.get('commit', 'unknown')[:12]})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
