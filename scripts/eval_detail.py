"""Read one judged run down to a single (fixture, engine) pair.

The eval map shows a delta per cell; this module gathers what the delta is made of,
so a page can show why: the two outputs, the judge's own words about each, the axis
scores, and the exact prompts the models saw.

Every figure comes from `scores.json`. The verdict files are read only for the
judge's prose, and their machine-readable block is checked against `scores.json`
so the prose on a page can never belong to a different score than the numbers
beside it. The join from a pair to the judge's blind label goes through
`cells[].output` and is confirmed by `mapping.json`; nothing is inferred from order.

Parsing is strict on purpose. The judge wrote section 2 in four different shapes
across eleven fixtures; a shape this module does not know stops the build with the
file name instead of silently dropping the judge's reasoning from a page.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "eval"

ARMS = ("control", "skill")

# The map's own words: "quality" is quality_raw. The penalized total is shown
# beside it only where a hard failure made the two differ.
STRUCTURE_AXES = ("top", "key_line_composition", "levels", "order_and_kind")
QUALITY_AXES = ("top", "same_kind_grouping", "explainable_order", "mece", "visible_structure")

# eval/build-prompts.sh, verbatim. The script is the source; these lines are
# checked against it at load so a change there cannot leave the pages stale.
SKILL_PREAMBLE = "Below is a skill written as an instruction. Read it in full and apply it to the task at the end."
CONTROL_PREAMBLE = "You are working on a business document using the Minto Pyramid Principle."
CLOSING = "Return only the result, with no explanation of how you produced it."
SKILL_PARTS = (
    ("SKILL.md", "SKILL.md"),
    ("references/rules.md", "rules.md"),
    ("references/templates.md", "templates.md"),
)

OUT_RE = re.compile(r"out-\d{2}")

# Judge tallies that disagree with the outputs the judge listed; reported, not fatal.
MISCOUNTS: list[str] = []


class DetailError(SystemExit):
    def __init__(self, where: str, message: str) -> None:
        super().__init__(f"ERROR: {where}: {message}")


# ---------------------------------------------------------------- verdicts


@dataclass
class Verdict:
    fixture: str
    decisive_preface: str = ""
    # output -> list of (label or None, answer text)
    decisive: dict[str, list[tuple[str | None, str]]] = field(default_factory=dict)
    notes: dict[str, str] = field(default_factory=dict)
    # each: {"defect", "section", "cause", "outputs": set}
    attribution: list[dict] = field(default_factory=list)
    observation: str = ""
    machine: dict = field(default_factory=dict)


def _sections(text: str, where: str) -> dict[int, str]:
    parts = re.split(r"^## (\d)\. [^\n]*\n", text, flags=re.M)
    found = {int(parts[i]): parts[i + 1].strip() for i in range(1, len(parts), 2)}
    if sorted(found) != [1, 2, 3, 4, 5, 6]:
        raise DetailError(where, f"expected sections 1-6, found {sorted(found)}")
    return found


def _table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip("|"))]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows


def _parse_decisive(block: str, outputs: set[str], where: str) -> tuple[str, dict]:
    lines = block.splitlines()
    answers: dict[str, list[tuple[str | None, str]]] = {}
    preface: list[str] = []

    if any(re.match(r"^\| *out-\d{2} *\|", l) for l in lines):
        # Shape: a table whose header names each question.
        rows = _table_rows(block)
        header, body = rows[0], rows[1:]
        for row in body:
            if len(row) != len(header):
                raise DetailError(where, f"section 2 row has {len(row)} cells, header has {len(header)}")
            answers[row[0]] = [(h, v) for h, v in zip(header[1:], row[1:])]
        preface = [l for l in lines if l.strip() and not l.strip().startswith("|")]
    elif any(l.startswith("### out-") for l in lines):
        # Shape: one subsection per output, numbered answers beneath.
        current = None
        for line in lines:
            head = re.match(r"^### (out-\d{2})\s*$", line)
            item = re.match(r"^(\d+)\. (.+)$", line)
            if head:
                current = head.group(1)
                answers[current] = []
            elif item and current:
                answers[current].append((item.group(1), item.group(2).strip()))
            elif line.strip() and current is None:
                preface.append(line)
            elif line.strip():
                raise DetailError(where, f"unexpected line in section 2: {line[:60]!r}")
    else:
        # Shape: one list item per output, numbered or bulleted.
        for line in lines:
            item = re.match(r"^(?:\d+\.|-) \*\*(out-\d{2}):\*\* (.+)$", line)
            if item:
                answers[item.group(1)] = [(None, item.group(2).strip())]
            elif line.strip():
                if answers:
                    raise DetailError(where, f"unexpected line in section 2: {line[:60]!r}")
                preface.append(line)

    if set(answers) != outputs:
        raise DetailError(where, f"section 2 covers {sorted(answers)}; mapping has {sorted(outputs)}")
    return " ".join(p.strip() for p in preface), answers


def _parse_notes(block: str, outputs: set[str], where: str) -> dict[str, str]:
    notes = {}
    for line in block.splitlines():
        item = re.match(r"^- \*\*(out-\d{2}):\*\* (.+)$", line)
        if item:
            notes[item.group(1)] = item.group(2).strip()
        elif line.strip():
            raise DetailError(where, f"unexpected line in section 3: {line[:60]!r}")
    if set(notes) != outputs:
        raise DetailError(where, f"section 3 covers {sorted(notes)}; mapping has {sorted(outputs)}")
    return notes


def expand_outputs(value: str, outputs: set[str], where: str) -> set[str]:
    """`out-01, out-04–out-16 (12)`, `out-01 through out-13`, `16: all outputs`."""
    text = value.strip()
    count = None
    lead = re.match(r"^(\d+): *(.+)$", text)
    if lead:
        count, text = int(lead.group(1)), lead.group(2)
    tail = re.match(r"^(.+?) *\((\d+)\)$", text)
    if tail:
        text, count = tail.group(1), int(tail.group(2))
    if text == "all outputs":
        found = set(outputs)
    else:
        found = set()
        for part in re.split(r", *", text):
            span = re.fullmatch(r"out-(\d{2}) *(?:–|-|through) *out-(\d{2})", part)
            single = re.fullmatch(r"out-(\d{2})", part)
            if span:
                lo, hi = int(span.group(1)), int(span.group(2))
                found |= {f"out-{n:02d}" for n in range(lo, hi + 1)}
            elif single:
                found.add(part)
            else:
                raise DetailError(where, f"cannot read the output list {value!r}")
    if count is not None and count != len(found):
        # The judge's own tally can be off by one (05-role-of-board says 8, lists 9).
        # The list is what the judge named; the page shows the list, never the tally.
        MISCOUNTS.append(f"{where}: {value!r} says {count}, lists {len(found)}")
    if not found <= outputs:
        raise DetailError(where, f"{value!r} names outputs that do not exist: {sorted(found - outputs)}")
    return found


def parse_verdict(path: Path, outputs: set[str]) -> Verdict:
    where = str(path.relative_to(ROOT))
    sec = _sections(path.read_text(encoding="utf-8"), where)
    verdict = Verdict(fixture=path.stem)
    verdict.decisive_preface, verdict.decisive = _parse_decisive(sec[2], outputs, where)
    verdict.notes = _parse_notes(sec[3], outputs, where)
    rows = _table_rows(sec[4])
    if rows[0] != ["recurring defect", "skill section", "cause", "affected outputs"]:
        raise DetailError(where, f"section 4 header is {rows[0]}")
    for defect, section, cause, affected in rows[1:]:
        verdict.attribution.append(
            {"defect": defect, "section": section, "cause": cause,
             "outputs": expand_outputs(affected, outputs, where)}
        )
    verdict.observation = " ".join(sec[5].split())
    block = re.search(r"```json\n(.+?)\n```", sec[6], flags=re.S)
    if not block:
        raise DetailError(where, "section 6 has no json block")
    verdict.machine = json.loads(block.group(1))
    return verdict


# ---------------------------------------------------------------- the run


@dataclass
class Run:
    name: str
    dir: Path
    scores: dict
    mapping: dict
    pairs: dict  # (fixture, engine) -> {arm: cell}
    verdicts: dict  # fixture -> Verdict
    skill_files: dict  # label -> text, from the run's frozen copy


def _check_build_prompts() -> None:
    script = (EVAL / "build-prompts.sh").read_text(encoding="utf-8")
    for line in (SKILL_PREAMBLE, CONTROL_PREAMBLE, CLOSING):
        if f'echo "{line}"' not in script:
            raise DetailError("eval/build-prompts.sh", f"no longer echoes {line[:40]!r}; update eval_detail.py")
    for label, _ in SKILL_PARTS:
        if f'echo "===== {label} ====="' not in script:
            raise DetailError("eval/build-prompts.sh", f"no longer includes {label}")


def _check_machine(verdict: Verdict, fixture_cells: dict[str, dict], where: str) -> None:
    """The verdict's JSON block and scores.json must describe the same scores.

    The verdict writes `quality` as judged; aggregate.py stores that as quality_raw
    and derives quality_penalized, so the comparison is against quality_raw.
    """
    seen = set()
    for item in verdict.machine["outputs"]:
        out = item["output"]
        cell = fixture_cells.get(out)
        if cell is None:
            raise DetailError(where, f"section 6 scores {out}, which scores.json does not hold")
        seen.add(out)
        for key, source in (("structure", "structure"), ("quality", "quality_raw")):
            for axis, value in item[key].items():
                if cell[source].get(axis) != value:
                    raise DetailError(where, f"{out} {key}.{axis}: verdict {value}, scores.json {cell[source].get(axis)}")
        if sorted(item.get("hard_failures", [])) != sorted(cell["hard_failures"]):
            raise DetailError(where, f"{out} hard failures differ from scores.json")
    if seen != set(fixture_cells):
        raise DetailError(where, f"section 6 misses {sorted(set(fixture_cells) - seen)}")


def load_run(name: str) -> Run:
    run_dir = EVAL / "runs" / name
    scores = json.loads((run_dir / "scores.json").read_text(encoding="utf-8"))
    mapping = json.loads((run_dir / "mapping.json").read_text(encoding="utf-8"))
    _check_build_prompts()

    pairs: dict = {}
    by_fixture: dict[str, dict[str, dict]] = {}
    for cell in scores["cells"]:
        fixture, out = cell["fixture"], cell["output"]
        entry = mapping.get(fixture, {}).get(f"{out}.md")
        if entry is None or entry["engine"] != cell["engine"] or entry["arm"] != cell["arm"]:
            raise DetailError(f"{name}/mapping.json", f"{fixture} {out} does not map to {cell['engine']} {cell['arm']}")
        pairs.setdefault((fixture, cell["engine"]), {})[cell["arm"]] = cell
        by_fixture.setdefault(fixture, {})[out] = cell

    verdicts = {}
    for fixture, cells in by_fixture.items():
        path = run_dir / "verdicts" / f"{fixture}.md"
        verdict = parse_verdict(path, set(cells))
        _check_machine(verdict, cells, str(path.relative_to(ROOT)))
        verdicts[fixture] = verdict

    skill_files = {}
    frozen = run_dir / "prompts"
    for label, filename in SKILL_PARTS:
        path = frozen / filename
        if not path.is_file():
            raise DetailError(str(path.relative_to(ROOT)), "missing; run scripts/freeze_run_prompts.py")
        skill_files[label] = path.read_text(encoding="utf-8")
    digest = hashlib.sha256(skill_files["SKILL.md"].encode("utf-8")).hexdigest()
    recorded = scores["skill_sha256"]
    recorded = recorded if isinstance(recorded, list) else [recorded]
    if not scores.get("skill_unchanged_across_run") or len(set(recorded)) != 1:
        raise DetailError(f"{name}/scores.json", "the skill changed during the run; one frozen copy cannot stand for it")
    if digest != recorded[0]:
        raise DetailError(str((frozen / "SKILL.md").relative_to(ROOT)), f"sha256 {digest[:12]} is not the run's {recorded[0][:12]}")

    return Run(name, run_dir, scores, mapping, pairs, verdicts, skill_files)


def fixture_input(fixture: str) -> str:
    return (EVAL / "fixtures" / fixture / "before.md").read_text(encoding="utf-8")


def fixture_gold(fixture: str) -> str:
    return (EVAL / "fixtures" / fixture / "gold.md").read_text(encoding="utf-8")


def decisive_questions(fixture: str) -> list[str]:
    text = (EVAL / "decisive-questions.md").read_text(encoding="utf-8")
    block = re.search(rf"^## {re.escape(fixture)}\n(.+?)(?=^## |\Z)", text, flags=re.M | re.S)
    if not block:
        raise DetailError("eval/decisive-questions.md", f"no section for {fixture}")
    return [m.group(1).strip() for m in re.finditer(r"^\d+\. (.+)$", block.group(1), flags=re.M)]


def raw_output(run: Run, fixture: str, engine: str, arm: str) -> str:
    return (run.dir / "raw" / f"{fixture}__{engine}__{arm}.md").read_text(encoding="utf-8")


def question_numbers(label: str | None) -> list[int]:
    """`Q4` -> [4]; `Q4–Q6` -> [4, 5, 6]; `Q4, Q5 and Q6` -> [4, 5, 6]; `1. Benefits` -> [1];
    a header with no leading number -> []."""
    m = re.match(r"^Q?(\d+(?:(?:,\s*|\s+and\s+|\s*[–-]\s*)Q?\d+)*)(?:\b|$)", label or "")
    if not m:
        return []
    out: list[int] = []
    for span in re.split(r",\s*|\s+and\s+", m.group(1)):
        ends = [int(x) for x in re.findall(r"\d+", span)]
        out += list(range(ends[0], ends[-1] + 1)) if len(ends) == 2 else ends
    return out


def decisive_rows(verdict: Verdict, questions: list[str], out: str) -> list[tuple[str | None, str | None, str]]:
    """(label, question text, answer) rows for one output, in the judge's own order.

    A table or a numbered subsection already gives one answer per label. A single
    list line is split only where the judge wrote `Q1 …; Q2 …`, so an answer is
    tied to a question only when the judge tied it; otherwise it stays one row.
    """
    def question_for(label: str | None) -> str | None:
        numbers = question_numbers(label)
        if len(numbers) == 1 and 1 <= numbers[0] <= len(questions):
            return questions[numbers[0] - 1]
        return None

    rows = verdict.decisive[out]
    if len(rows) == 1 and rows[0][0] is None:
        parts = re.split(r";\s*(?=Q\d+\b)", rows[0][1])
        if len(parts) > 1 and all(re.match(r"^Q\d+\b", p) for p in parts):
            split = []
            for p in parts:
                # "Q4", "Q4–Q6", or "Q4, Q5 and Q6" when one answer covers several.
                m = re.match(r"^(Q\d+(?:(?:,\s*|\s+and\s+|\s*[–-]\s*)Q?\d+)*)[\s:,—-]*(.*)$", p, flags=re.S)
                split.append((m.group(1), question_for(m.group(1)), m.group(2).strip().rstrip(".")))
            return split
        return [(None, None, rows[0][1])]
    return [(label, question_for(label), answer) for label, answer in rows]


def control_prompt(fixture: str) -> str:
    """Byte for byte what build-prompts.sh writes for the control arm."""
    return f"{CONTROL_PREAMBLE}\n\n{fixture_input(fixture)}\n{CLOSING}\n"


def assemble_skill_prompt(skill_files: dict[str, str], fixture: str) -> str:
    """Byte for byte what build-prompts.sh writes for the skill arm, given the files."""
    parts = [f"{SKILL_PREAMBLE}\n\n"]
    for label, _ in SKILL_PARTS:
        parts.append(f"===== {label} =====\n{skill_files[label]}\n")
    parts.append(f"===== TASK =====\n{fixture_input(fixture)}\n{CLOSING}\n")
    return "".join(parts)


def skill_prompt(run: Run, fixture: str) -> str:
    return assemble_skill_prompt(run.skill_files, fixture)


def pair(run: Run, fixture: str, engine: str) -> dict | None:
    arms = run.pairs.get((fixture, engine))
    if not arms or set(arms) != set(ARMS):
        return None
    verdict = run.verdicts[fixture]
    result = {"fixture": fixture, "engine": engine, "mode": arms["skill"]["mode"], "arms": {}}
    for arm in ARMS:
        cell = arms[arm]
        out = cell["output"]
        result["arms"][arm] = {
            "cell": cell,
            "output": out,
            "text": raw_output(run, fixture, engine, arm),
            "decisive": verdict.decisive[out],
            "note": verdict.notes[out],
            "defects": [a for a in verdict.attribution if out in a["outputs"]],
        }
    return result


# ---------------------------------------------------------------- markdown

# The outputs are model-written markdown. This renderer knows exactly the grammar
# the 172 outputs of v1.7.0-final use and refuses anything else, so a new shape
# fails the build instead of reaching a page mangled. Raw HTML is escaped; only
# <br>, which models write inside table cells, is kept as a line break.

_LIST_RE = re.compile(r"^( *)([-*+]|\d+[.)]) +(.*)$")
_FENCE_RE = re.compile(r"^ *```")
_HR_RE = re.compile(r"^ {0,3}(?:-{3,}|\*{3,}|_{3,}) *$")
_HEAD_RE = re.compile(r"^(#{1,6}) +(.+?) *#* *$")


class MarkdownError(ValueError):
    pass


def inline(text: str) -> str:
    codes: list[str] = []

    def keep_code(m: re.Match) -> str:
        codes.append(f"<code>{html.escape(m.group(1), quote=False)}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"&lt;br */?&gt;", "<br>", text, flags=re.I)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])__(.+?)__(?![\w*])", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?![\s*])(.+?)(?<![\s*])\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"(?<![\w_])_(?![\s_])(.+?)(?<![\s_])_(?![\w_])", r"<em>\1</em>", text)
    text = re.sub(r"~~(.+?)~~", r"<s>\1</s>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)


def _table(lines: list[str]) -> str:
    rows = [[c.strip() for c in re.split(r"(?<!\\)\|", l.strip().strip("|"))] for l in lines]
    if len(rows) < 2 or not all(re.fullmatch(r":?-{2,}:?", c) for c in rows[1]):
        raise MarkdownError(f"table without a separator row: {lines[0][:60]!r}")
    align = ["right" if c.endswith(":") and not c.startswith(":") else "" for c in rows[1]]
    width = len(rows[0])

    def cells(row: list[str], tag: str) -> str:
        row = (row + [""] * width)[:width]
        out = []
        for i, c in enumerate(row):
            cls = ' class="md-num"' if i < len(align) and align[i] else ""
            out.append(f"<{tag}{cls}>{inline(c)}</{tag}>")
        return "".join(out)

    body = "".join(f"<tr>{cells(r, 'td')}</tr>" for r in rows[2:])
    return (f'<div class="md-table"><table><thead><tr>{cells(rows[0], "th")}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")


def _list(items: list[tuple[int, str, str]]) -> str:
    """items: (indent, marker, text). Builds nested lists from indentation."""
    out: list[str] = []
    stack: list[tuple[int, str]] = []  # (indent, tag)

    def tag_of(marker: str) -> str:
        return "ol" if marker[0].isdigit() else "ul"

    for indent, marker, text in items:
        tag = tag_of(marker)
        while stack and indent < stack[-1][0]:
            out.append(f"</li></{stack.pop()[1]}>")
        if stack and indent == stack[-1][0]:
            if stack[-1][1] != tag:
                out.append(f"</li></{stack.pop()[1]}>")
            else:
                out.append("</li>")
        if not stack or indent > stack[-1][0]:
            start = ""
            if tag == "ol":
                n = int(re.match(r"\d+", marker).group(0))
                start = f' start="{n}"' if n != 1 else ""
            out.append(f"<{tag}{start}>")
            stack.append((indent, tag))
        out.append(f"<li>{text}")
    while stack:
        out.append(f"</li></{stack.pop()[1]}>")
    return "".join(out)


def markdown(source: str, heading_base: int = 4) -> str:
    lines = source.replace("\r\n", "\n").rstrip("\n").split("\n")
    # The output's own top heading level maps to heading_base, so a document that
    # opens at ### does not land three levels below the column it sits in.
    levels = [len(m.group(1)) for l in lines if (m := _HEAD_RE.match(l))]
    heading_base -= min(levels, default=1) - 1
    blocks: list[str] = []
    i = 0
    n = len(lines)

    def blank(k: int) -> bool:
        return k >= n or not lines[k].strip()

    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if _FENCE_RE.match(line):
            fence_indent = len(line) - len(line.lstrip())
            body = []
            i += 1
            while i < n and not _FENCE_RE.match(lines[i]):
                body.append(lines[i][fence_indent:] if lines[i][:fence_indent].strip() == "" else lines[i])
                i += 1
            if i >= n:
                raise MarkdownError("unclosed code fence")
            i += 1
            blocks.append(f"<pre><code>{html.escape(chr(10).join(body), quote=False)}</code></pre>")
            continue
        head = _HEAD_RE.match(line)
        if head:
            level = min(6, heading_base + len(head.group(1)) - 1)
            blocks.append(f"<h{level}>{inline(head.group(2))}</h{level}>")
            i += 1
            continue
        if _HR_RE.match(line):
            blocks.append("<hr>")
            i += 1
            continue
        if line.lstrip().startswith("|"):
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(lines[i])
                i += 1
            blocks.append(_table(rows))
            continue
        if line.startswith(">"):
            quoted = []
            while i < n and lines[i].startswith(">"):
                quoted.append(re.sub(r"^> ?", "", lines[i]))
                i += 1
            blocks.append(f"<blockquote>{markdown(chr(10).join(quoted), heading_base + min(levels, default=1) - 1)}</blockquote>")
            continue
        if _LIST_RE.match(line):
            items: list[tuple[int, str, str]] = []
            while i < n:
                cur = lines[i]
                m = _LIST_RE.match(cur)
                if m and not _HR_RE.match(cur):
                    items.append((len(m.group(1)), m.group(2), inline(m.group(3))))
                    i += 1
                elif not cur.strip():
                    # A blank line keeps the list open only if it continues.
                    k = i
                    while k < n and not lines[k].strip():
                        k += 1
                    if k < n and (_LIST_RE.match(lines[k]) or lines[k].startswith(" ")) and not _FENCE_RE.match(lines[k]):
                        i = k
                    else:
                        break
                elif cur.startswith(" ") and not _FENCE_RE.match(cur) and not cur.lstrip().startswith("|"):
                    indent, marker, text = items[-1]
                    items[-1] = (indent, marker, f"{text}<br>{inline(cur.strip())}")
                    i += 1
                elif (not _FENCE_RE.match(cur) and not _HEAD_RE.match(cur) and not _HR_RE.match(cur)
                      and not cur.startswith(("|", ">")) and not blank(i - 1)):
                    # A lazy continuation line directly under an item.
                    indent, marker, text = items[-1]
                    items[-1] = (indent, marker, f"{text}<br>{inline(cur.strip())}")
                    i += 1
                else:
                    break
            blocks.append(_list(items))
            continue
        if line.startswith("    "):
            # An indented block outside a list is code in commonmark; one audit
            # quotes the source's outline this way (07 x qwen3.6-35b-a3b, skill).
            body = []
            while i < n and (lines[i].startswith("    ") or (not lines[i].strip() and i + 1 < n and lines[i + 1].startswith("    "))):
                body.append(lines[i][4:])
                i += 1
            blocks.append(f"<pre><code>{html.escape(chr(10).join(body), quote=False)}</code></pre>")
            continue
        para = []
        while i < n and lines[i].strip():
            cur = lines[i]
            if para and (_FENCE_RE.match(cur) or _HEAD_RE.match(cur) or _HR_RE.match(cur)
                         or cur.lstrip().startswith("|") or cur.startswith(">") or _LIST_RE.match(cur)):
                break
            para.append(inline(cur.strip()))
            i += 1
        # Models break lines on purpose (To:/From:/Subject:), so a newline is kept.
        blocks.append(f"<p>{'<br>'.join(para)}</p>")
    return "\n".join(blocks)
