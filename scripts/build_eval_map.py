#!/usr/bin/env python3
"""Render the Eval Map pages from a judged run.

The site is authored HTML with no build step, and every benchmark number on it is
derived from `scores.json` rather than typed. The map carries 194 figures per locale,
which is far past what a hand kept honest, so this script owns both page files whole.

Whole files, not a spliced region: `check_benchmark_numbers.check_parity` compares the
two locales element for element across the entire document, head and footer included.
One template rendered twice makes that parity true by construction instead of leaving
the chrome to manual mirroring.

`--check` re-renders into memory and diffs against disk, so CI can fail a page that
drifted from the run it claims. That diff is only as good as its determinism: row and
column order come from the constants below, never from iterating a mapping, and every
line of output carries exactly one structural element so the longer Russian copy cannot
change the line count.
"""

from __future__ import annotations

import argparse
import difflib
import html
import json
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
TEMPLATE = Path(__file__).resolve().parent / "eval-map.template.html"
DEFAULT_RUN = "v1.7.0-final"

# The landing page's own `quality` metric reads quality_raw; the map has to mean the
# same thing by the same word or the two pages quietly disagree.
MEASURES = (
    ("structure", "structure", 8),
    ("quality", "quality_raw", 10),
)

# Order is data. Rows render in this sequence and the checker asserts against it.
MODES = ("write", "audit", "digest", "viz")

# fixture, mode, English name, Russian name
FIXTURES = (
    ("01-big-chief", "write", "A proposal to the chief executive", "Предложение генеральному директору"),
    ("02-ttv", "write", "A memo on composing costs", "Записка о&nbsp;наборных издержках"),
    ("04-meeting-note", "write", "A note before a meeting", "Записка перед встречей"),
    ("05-role-of-board", "write", "The role of the board", "Роль совета директоров"),
    ("08-techdebt", "write", "A message about technical debt", "Сообщение о&nbsp;техдолге"),
    ("10-rollout-review", "write", "A review of a large rollout", "Разбор большого запуска"),
    ("11-plain-list", "write", "A plain list, no pyramid", "Простой список без пирамиды"),
    ("03-period-graph-books", "audit", "A set of monthly reports", "Набор ежемесячных отчётов"),
    ("07-headings-audit", "audit", "A set of headings", "Набор заголовков"),
    ("09-sources-digest", "digest", "A digest of several sources", "Выжимка из нескольких источников"),
    ("06-ttw-viz", "viz", "A pyramid of an existing memo", "Пирамида готовой записки"),
)

# mode, English gloss, Russian gloss
MODE_GLOSS = (
    ("write", "Create and rework text", "Создать и&nbsp;переработать текст"),
    ("audit", "Check and find defects", "Проверить и&nbsp;найти дефекты"),
    ("digest", "Report on what was read", "Отчитаться о прочитанном"),
    ("viz", "Show the structure", "Показать структуру"),
)

# engine key, column label. Labels match the per-model table on the landing page.
ENGINES = (
    ("opus5", "Claude Opus 5"),
    ("sonnet5", "Claude Sonnet 5"),
    ("haiku45", "Claude Haiku 4.5"),
    ("codex", "Codex gpt-5.6-terra"),
    ("gpt-oss-120b", "gpt-oss-120b"),
    ("qwen3.6-35b-a3b", "qwen3.6-35b-a3b"),
    ("qwen3.6-fp8", "qwen3.6-fp8"),
    ("qwen3.8-27b", "qwen3.8-27b"),
)

MINUS = "−"


def load_scores(run: str) -> dict:
    path = ROOT / "eval" / "runs" / run / "scores.json"
    if not path.is_file():
        raise SystemExit(f"ERROR: {path.relative_to(ROOT)} is missing; run eval/aggregate.py first")
    return json.loads(path.read_text(encoding="utf-8"))


def index_cells(scores: dict) -> dict[tuple[str, str], dict[str, dict]]:
    """(fixture, engine) -> {arm: cell}. Only complete pairs are usable."""
    pairs: dict[tuple[str, str], dict[str, dict]] = {}
    for cell in scores["cells"]:
        pairs.setdefault((cell["fixture"], cell["engine"]), {})[cell["arm"]] = cell
    return pairs


def assert_shape(scores: dict, pairs: dict) -> None:
    """A future run that adds or drops a fixture must not change this page silently."""
    declared = {fixture for fixture, *_ in FIXTURES}
    present = {cell["fixture"] for cell in scores["cells"]}
    if declared != present:
        raise SystemExit(
            "ERROR: the fixtures in this run do not match the rows this page declares.\n"
            f"  only in the run:  {', '.join(sorted(present - declared)) or '-'}\n"
            f"  only on the page: {', '.join(sorted(declared - present)) or '-'}\n"
            "Update FIXTURES in this script, deliberately, before regenerating."
        )
    declared_modes = {mode for _, mode, *_ in FIXTURES}
    if not declared_modes <= set(MODES):
        raise SystemExit(f"ERROR: FIXTURES names a mode that MODES does not order: {declared_modes - set(MODES)}")
    engines = {cell["engine"] for cell in scores["cells"]}
    if {key for key, _ in ENGINES} != engines:
        raise SystemExit(
            "ERROR: the engines in this run do not match the columns this page declares.\n"
            f"  only in the run:  {', '.join(sorted(engines - {k for k, _ in ENGINES})) or '-'}\n"
            f"  only on the page: {', '.join(sorted({k for k, _ in ENGINES} - engines)) or '-'}"
        )
    for (fixture, engine), arms in pairs.items():
        if set(arms) - {"control", "skill"}:
            raise SystemExit(f"ERROR: unexpected arm in {fixture} x {engine}: {sorted(arms)}")


def delta(pair: dict[str, dict], source: str) -> int:
    return pair["skill"][source]["total"] - pair["control"][source]["total"]


def signed(value: int) -> str:
    """Every figure carries its sign, so colour is never the only channel."""
    if value > 0:
        return f"+{value}"
    if value < 0:
        return f"{MINUS}{abs(value)}"
    return "0"


def signed_mean(values: list[int]) -> str:
    mean = round(statistics.fmean(values), 1)
    body = f"{abs(mean):.1f}"
    if mean > 0:
        return f"+{body}"
    if mean < 0:
        return f"{MINUS}{body}"
    return "0.0"


def heat(value: int) -> int:
    """Nine distinct structure deltas and eight quality ones: steps, not a gradient."""
    return min(abs(value), 5)


# The copy tables are authored, and they carry the same HTML entities the rest of
# the site uses. Escaping has to protect against a stray `&` without turning an
# intentional `&nbsp;` into visible text, which is what a plain html.escape does.
AUTHORED_ENTITIES = ("nbsp", "mdash", "ndash", "middot", "rsquo", "lsquo", "rarr", "darr", "minus")


def esc(text: str) -> str:
    escaped = html.escape(text, quote=True)
    for entity in AUTHORED_ENTITIES:
        escaped = escaped.replace(f"&amp;{entity};", f"&{entity};")
    return escaped


def cell_attrs(fixture: str, engine: str, pair: dict) -> str:
    """Every cell carries both measures, so the checker can re-derive either one."""
    parts = [f'data-cell-fixture="{fixture}"', f'data-cell-engine="{engine}"']
    for name, source, _ in MEASURES:
        parts.append(f'data-{name}-control="{pair["control"][source]["total"]}"')
        parts.append(f'data-{name}-skill="{pair["skill"][source]["total"]}"')
        parts.append(f'data-{name}-delta="{delta(pair, source)}"')
    return " ".join(parts)


def render_table(lang: str, name: str, source: str, maximum: int, pairs: dict, copy: dict) -> list[str]:
    """One structural element per line: the Russian copy must not change the line count."""
    columns = len(ENGINES) + 2
    out: list[str] = []
    out.append('              <table class="mr-table__table map__table">')
    out.append(f'                <caption class="visually-hidden">{copy[f"name_{name}"]}</caption>')
    out.append("                <thead>")
    out.append("                  <tr>")
    out.append(f'                    <th class="mr-table__th map__head map__head--case" scope="col">{copy["col_case"]}</th>')
    for _, label in ENGINES:
        out.append(f'                    <th class="mr-table__th map__head map__head--model" scope="col">{esc(label)}</th>')
    out.append(f'                    <th class="mr-table__th map__head map__head--avg" scope="col">{copy["col_avg"]}</th>')
    out.append("                  </tr>")
    out.append("                </thead>")

    for mode, gloss_en, gloss_ru in MODE_GLOSS:
        gloss = gloss_en if lang == "en" else gloss_ru
        out.append(f'                <tbody class="map__group" data-map-mode="{mode}">')
        out.append("                  <tr>")
        out.append(f'                    <th class="mr-table__td map__mode" scope="rowgroup" colspan="{columns}">')
        out.append('                      <span class="map__mode-inner">')
        out.append(f'                        <code class="map__mode-name">{mode}</code>')
        out.append(f'                        <span class="map__mode-gloss">{esc(gloss)}</span>')
        out.append("                      </span>")
        out.append("                    </th>")
        out.append("                  </tr>")
        for fixture, fixture_mode, name_en, name_ru in FIXTURES:
            if fixture_mode != mode:
                continue
            label = name_en if lang == "en" else name_ru
            out.append("                  <tr>")
            out.append(f'                    <th class="mr-table__td map__case" scope="row">')
            out.append(f'                      <a class="map__case-name" href="./{fixture}/">{esc(label)}</a>')
            out.append(f'                      <code class="map__case-slug">{fixture}</code>')
            out.append("                    </th>")
            present: list[int] = []
            for engine, engine_label in ENGINES:
                pair = pairs.get((fixture, engine), {})
                if "control" in pair and "skill" in pair:
                    value = delta(pair, source)
                    present.append(value)
                    tone = "up" if value > 0 else "down" if value < 0 else "flat"
                    out.append(
                        f'                    <td class="mr-table__td map__td">'
                        f'<a class="map__cell map__cell--{tone}" href="./{fixture}/{engine}/#{name}" data-cell data-cell-measure="{name}"'
                        f' data-heat="{heat(value)}" {cell_attrs(fixture, engine, pair)}>{signed(value)}'
                        f'<span class="visually-hidden">, {esc(engine_label)}</span></a></td>'
                    )
                else:
                    out.append(
                        f'                    <td class="mr-table__td map__td">'
                        f'<span class="map__cell map__cell--na" data-cell-missing data-cell-measure="{name}"'
                        f' data-cell-fixture="{fixture}" data-cell-engine="{engine}">{MINUS}'
                        f'<span class="visually-hidden">{copy["na"]}, {esc(engine_label)}</span></span></td>'
                    )
            out.append(
                f'                    <td class="mr-table__td map__td map__td--avg">'
                f'<span class="map__avg" data-row-avg data-row-measure="{name}" data-row-fixture="{fixture}">'
                f'{signed_mean(present)}</span></td>'
            )
            out.append("                  </tr>")
        out.append("                </tbody>")

    out.append("              </table>")
    return out


# Every value is one line. A newline in any of these would desynchronise the locales.
COPY = {
    "en": {
        "lang": "en",
        "dir_assets": "../assets",
        "dir_home": "../",
        "dir_self": "./",
        "dir_other": "../ru/eval-map/",
        "canonical": "https://welltraum.github.io/minto/eval-map/",
        "title": "Eval Map &mdash; Minto measured case by case",
        "description": "Eleven real writing jobs across eight models, judged with and without Minto. The same skill gains four points on one audit case and loses four on another.",
        "og_title": "Eval Map: Minto measured case by case",
        "skip": "Skip to content",
        "nav_examples": "Examples",
        "nav_evidence": "Evidence",
        "nav_modes": "Capabilities",
        "nav_install": "Install",
        "nav_sections": "Sections",
        "nav_language": "Language",
        "nav_links": "Links",
        "brand_alt": "A pyramid of three rows",
        "h1": "One overall score cannot say whether Minto helps",
        "lede": "Claude Haiku 4.5 ran two audit cases in this run. On a set of headings its structure went from 2 out of 8 to 6. On a set of monthly reports it went from 6 down to 2. Same model, same mode, same skill, opposite results. That is why this evaluation is a map of cases rather than a single figure.",
        "provenance": "Run v1.7.0-final &middot; 11 cases across 4 modes &middot; 8 models &middot; 172 blind verdicts over 86 pairs",
        "measure_label": "Measure",
        "tab_structure": "Structure, out of 8",
        "tab_quality": "Quality, out of 10",
        "heading_structure": "Change in structure, with Minto and without",
        "heading_quality": "Change in writing quality, with Minto and without",
        "name_structure": "Change in structure by case and model, run v1.7.0-final",
        "caption_structure": "Each cell is one judged document: its structure score with Minto minus the same model&rsquo;s score without it. The most structure can score is 8 points.",
        "name_quality": "Change in writing quality by case and model, run v1.7.0-final",
        "caption_quality": "Each cell is one judged document: its writing-quality score with Minto minus the same model&rsquo;s score without it. The most quality can score is 10 points.",
        "col_case": "Case",
        "col_avg": "Mean",
        "na": "no data",
        "legend_label": "Reading the shading",
        "legend_down": "Worse with Minto",
        "legend_zero": "No change",
        "legend_up": "Better with Minto",
        "read_heading": "How to read this map",
        "read_1_title": "One document per cell.",
        "read_1_body": "Each cell is a single judged pair, not an average. A cell of plus or minus one is noise; the row means, over eight models, are the steadier number, and the modes are steadier still.",
        "read_2_title": "172 verdicts, 86 pairs.",
        "read_2_body": "Every pair is judged twice, once without the skill and once with it, which is where the landing page&rsquo;s 172 comes from. The two empty cells are qwen3.8-27b on the two longest cases; it timed out in both arms, so there is nothing to subtract.",
        "read_3_title": "These deltas are subtraction, not new judging.",
        "read_3_body": "The v1.7.0 report deliberately stopped short of case-level deltas. This page takes them by subtracting the two arms of each already-judged pair. No output was re-judged and no model was refitted.",
        "read_4_title": "Cases are not interchangeable.",
        "read_4_body": "Each mode is tested on the jobs it exists for: write on drafting and reworking, audit on finding defects, digest on reporting what was read, viz on showing an existing structure. A single pooled score would average these into a number that describes none of them.",
        "methodology": "Read the full methodology and limitations",
        "back": "Back to the Minto home page",
        "footer_note": "The skill settles the argument before it rewrites the prose. Barbara Minto&rsquo;s source material remains the property of its rights holders; the plugin code is MIT-licensed.",
        "footer_changelog": "Changelog",
        "footer_switch": "Русский",
    },
    "ru": {
        "lang": "ru",
        "dir_assets": "../../assets",
        "dir_home": "../",
        "dir_self": "./",
        "dir_other": "../../eval-map/",
        "canonical": "https://welltraum.github.io/minto/ru/eval-map/",
        "title": "Карта оценки&nbsp;&mdash; Minto по кейсам",
        "description": "Одиннадцать рабочих задач на восьми моделях, с навыком и без него. Один и тот же навык даёт плюс четыре балла на одном кейсе аудита и минус четыре на другом.",
        "og_title": "Карта оценки: Minto по кейсам",
        "skip": "К&nbsp;основному содержимому",
        "nav_examples": "Примеры",
        "nav_evidence": "Данные",
        "nav_modes": "Возможности",
        "nav_install": "Установка",
        "nav_sections": "Разделы",
        "nav_language": "Язык",
        "nav_links": "Ссылки",
        "brand_alt": "Пирамида из трёх рядов",
        "h1": "Одна общая оценка не отвечает, помогает ли Minto",
        "lede": "В&nbsp;этом прогоне Claude Haiku 4.5 отработал два кейса режима audit. На наборе заголовков структура выросла с&nbsp;2 до 6&nbsp;баллов из 8. На наборе ежемесячных отчётов&nbsp;— упала с&nbsp;6 до 2. Одна модель, один режим, один навык&nbsp;— противоположный результат. Поэтому оценка устроена как карта кейсов, а&nbsp;не как одно число.",
        "provenance": "Прогон v1.7.0-final &middot; 11&nbsp;кейсов в&nbsp;4&nbsp;режимах &middot; 8&nbsp;моделей &middot; 172&nbsp;слепых вердикта по 86&nbsp;парам",
        "measure_label": "Шкала",
        "tab_structure": "Структура (из 8)",
        "tab_quality": "Качество (из 10)",
        "heading_structure": "Изменение структуры: с&nbsp;Minto и&nbsp;без него",
        "heading_quality": "Изменение качества текста: с&nbsp;Minto и&nbsp;без него",
        "name_structure": "Изменение структуры по кейсам и моделям, прогон v1.7.0-final",
        "caption_structure": "Каждая клетка&nbsp;— один судейский документ: оценка структуры с&nbsp;Minto минус оценка той же модели без него. Максимум за структуру&nbsp;— 8&nbsp;баллов.",
        "name_quality": "Изменение качества текста по кейсам и моделям, прогон v1.7.0-final",
        "caption_quality": "Каждая клетка&nbsp;— один судейский документ: оценка качества текста с&nbsp;Minto минус оценка той же модели без него. Максимум за качество&nbsp;— 10&nbsp;баллов.",
        "col_case": "Кейс",
        "col_avg": "Среднее",
        "na": "нет данных",
        "legend_label": "Как читать заливку",
        "legend_down": "С&nbsp;Minto хуже",
        "legend_zero": "Без изменений",
        "legend_up": "С&nbsp;Minto лучше",
        "read_heading": "Как читать эту карту",
        "read_1_title": "В&nbsp;клетке один документ.",
        "read_1_body": "Каждая клетка&nbsp;— одна судейская пара, а&nbsp;не среднее. Клетка в&nbsp;плюс-минус один балл&nbsp;— шум; средние по строке, взятые по восьми моделям, надёжнее, а&nbsp;средние по режимам ещё надёжнее.",
        "read_2_title": "172&nbsp;вердикта, 86&nbsp;пар.",
        "read_2_body": "Каждую пару судят дважды: без навыка и&nbsp;с&nbsp;навыком. Отсюда и&nbsp;берётся число 172 на главной странице. Две пустые клетки&nbsp;— это qwen3.8-27b на двух самых длинных кейсах: он не уложился в&nbsp;лимит ни с&nbsp;навыком, ни без него, и&nbsp;вычитать нечего.",
        "read_3_title": "Эти дельты&nbsp;— вычитание, а&nbsp;не новая судейская работа.",
        "read_3_body": "Отчёт v1.7.0 сознательно не считал дельты на уровне кейсов. Эта страница берёт их вычитанием: оценка с&nbsp;навыком минус оценка без него в&nbsp;уже оценённой паре. Ничего не пересуживали и&nbsp;ничего не перенастраивали.",
        "read_4_title": "Кейсы не взаимозаменяемы.",
        "read_4_body": "Каждый режим проверяем на тех задачах, для которых он сделан: write&nbsp;— на создании и&nbsp;переработке текста, audit&nbsp;— на поиске дефектов, digest&nbsp;— на отчёте о&nbsp;прочитанном, viz&nbsp;— на показе готовой структуры. Общая оценка свела бы их в&nbsp;одно число, которое не описывает ни один из них.",
        "methodology": "Полная методология и ограничения",
        "back": "На главную страницу Minto",
        "footer_note": "Навык приводит в&nbsp;порядок аргумент, прежде чем править слова. Материал книги Барбары Минто принадлежит правообладателям; код навыка&nbsp;&mdash; под лицензией MIT.",
        "footer_changelog": "Изменения",
        "footer_switch": "English",
    },
}


def asset_versions() -> dict[str, str]:
    """Read the cache-busting versions off the landing page instead of keeping a sixth copy."""
    source = (SITE / "index.html").read_text(encoding="utf-8")
    versions = {}
    for asset in ("mirai.css", "styles.css", "app.js"):
        match = re.search(rf"{re.escape(asset)}\?v=(\d+)", source)
        if not match:
            raise SystemExit(f"ERROR: site/index.html carries no ?v= for {asset}; cannot version the map pages")
        versions[asset] = match.group(1)
    return versions


def render(lang: str, scores: dict, pairs: dict, versions: dict[str, str]) -> str:
    copy = COPY[lang]
    template = TEMPLATE.read_text(encoding="utf-8")
    values = dict(copy)
    values["run"] = scores["run"]
    values["cells"] = str(scores["cells_used"])
    values["v_mirai"] = versions["mirai.css"]
    values["v_styles"] = versions["styles.css"]
    values["v_app"] = versions["app.js"]
    # eval/report-v1.7.0.md is named for the release, not the run directory.
    values["run_short"] = re.sub(r"-(final|baseline|r\d+)$", "", scores["run"])
    values["href_en"] = copy["dir_self"] if lang == "en" else copy["dir_other"]
    values["href_ru"] = copy["dir_other"] if lang == "en" else copy["dir_self"]
    values["current_en"] = ' aria-current="page"' if lang == "en" else ""
    values["current_ru"] = "" if lang == "en" else ' aria-current="page"'
    for name, source, maximum in MEASURES:
        values[f"table_{name}"] = "\n".join(render_table(lang, name, source, maximum, pairs, copy))

    def substitute(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise SystemExit(f"ERROR: the template asks for {{{{{key}}}}}, which no copy entry defines")
        return values[key]

    page = re.sub(r"\{\{(\w+)\}\}", substitute, template)
    if "{{" in page:
        raise SystemExit("ERROR: the rendered page still contains an unresolved placeholder")
    return page


def target(lang: str) -> Path:
    return SITE / "eval-map" / "index.html" if lang == "en" else SITE / "ru" / "eval-map" / "index.html"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", default=DEFAULT_RUN, help="run directory name under eval/runs/")
    parser.add_argument("--check", action="store_true", help="diff against the committed pages instead of writing")
    args = parser.parse_args()

    scores = load_scores(args.run)
    pairs = index_cells(scores)
    assert_shape(scores, pairs)
    versions = asset_versions()

    # The pages under the map: one per case, one per judged pair, one for the skill.
    # Imported here because that module reads this one's constants.
    import build_eval_detail

    pages = {target(lang): render(lang, scores, pairs, versions) for lang in ("en", "ru")}
    pages.update(build_eval_detail.render_all(args.run, versions))

    drifted = 0
    written = 0
    # A page this run no longer renders must not linger on the site under a stale URL.
    for folder in build_eval_detail.managed_dirs():
        for stray in sorted(folder.rglob("index.html")):
            if stray not in pages:
                drifted += 1
                print(f"ERROR: {stray.relative_to(ROOT)} is not rendered by {args.run}; delete it")

    for path, page in pages.items():
        label = path.relative_to(ROOT)
        if args.check:
            current = path.read_text(encoding="utf-8") if path.is_file() else ""
            if current != page:
                drifted += 1
                if drifted > 3:
                    print(f"ERROR: {label} is not what {args.run} renders")
                    continue
                diff = difflib.unified_diff(
                    current.splitlines(), page.splitlines(),
                    fromfile=f"{label} (committed)", tofile=f"{label} (from {args.run})", lineterm="", n=1,
                )
                print("\n".join(list(diff)[:60]))
                print(f"ERROR: {label} is not what {args.run} renders; run scripts/build_eval_map.py")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            if not path.is_file() or path.read_text(encoding="utf-8") != page:
                path.write_text(page, encoding="utf-8")
                written += 1

    if drifted:
        return 1
    if args.check:
        complete = sum(1 for arms in pairs.values() if len(arms) == 2)
        print(f"All {len(pages)} Eval Map pages match eval/runs/{args.run}/scores.json ({complete} judged pairs).")
    else:
        print(f"{len(pages)} Eval Map pages rendered from {args.run}; {written} changed on disk.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
