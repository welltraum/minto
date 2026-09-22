"""Render the pages under the Eval Map: one per case, one per judged pair, one for the skill.

The map says how far a score moved. These pages say why: both outputs side by side,
the judge's own words about each, the axis scores, and the exact prompts. They are
rendered by `build_eval_map.py`, so one command writes every eval page and one
`--check` diffs all of them.

The same rules as the map hold. Every number comes from `scores.json` through
`eval_detail.py`; nothing is typed. Both locales are rendered from one function per
page, and every line carries one structural element, so the Russian copy cannot
change the line count or the tag sequence that `check_parity` compares. The model
outputs and the judge's prose are English originals on both locales and are marked
`lang="en"`.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import eval_detail as ed
from build_eval_map import COPY as MAP_COPY
from build_eval_map import ENGINES, FIXTURES, MINUS, MODE_GLOSS, SITE, esc, signed

TEMPLATE = Path(__file__).resolve().parent / "eval-detail.template.html"
BASE_URL = "https://welltraum.github.io/minto/"

ENGINE_LABEL = dict(ENGINES)
ENGINE_ORDER = [engine for engine, _ in ENGINES]
FIXTURE_ORDER = [fixture for fixture, *_ in FIXTURES]
FIXTURE_NAME = {"en": {f: en for f, _, en, _ in FIXTURES}, "ru": {f: ru for f, _, _, ru in FIXTURES}}
FIXTURE_MODE = {f: mode for f, mode, *_ in FIXTURES}
MODE_TEXT = {"en": {m: en for m, en, _ in MODE_GLOSS}, "ru": {m: ru for m, _, ru in MODE_GLOSS}}

MEASURES = (("structure", "structure", 8), ("quality", "quality_raw", 10))
AXES = {
    "structure": ed.STRUCTURE_AXES,
    "quality": ed.QUALITY_AXES,
}

# Why a slot on the map is empty. Asserted against the run below, so a new hole
# cannot appear without a reason being written for it. Source:
# eval/runs/v1.7.0-final/raw-excluded/README.md.
EXCLUDED = {
    ("02-ttv", "qwen3.8-27b"): {
        "en": "Excluded. The baseline run never completed this model’s skill arm, so the pair was dropped from both runs to keep them comparable cell for cell.",
        "ru": "Исключена. В&nbsp;базовом прогоне модель так и&nbsp;не&nbsp;закончила ответ с&nbsp;навыком, поэтому пару убрали из&nbsp;обоих прогонов, чтобы их&nbsp;можно было сравнивать клетка в&nbsp;клетку.",
    },
    ("10-rollout-review", "qwen3.8-27b"): {
        "en": "Not judged. The model hub closed the connection on both arms after about twenty minutes.",
        "ru": "Не&nbsp;оценена. Хаб моделей закрывал соединение на&nbsp;обоих ответах примерно через двадцать минут.",
    },
}


def plural_ru(n: int, one: str, few: str, many: str) -> str:
    if n % 10 == 1 and n % 100 != 11:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


# Every value is one line and carries no markup of its own, so the two locales
# cannot differ in structure.
COPY = {
    "en": {
        "crumbs": "Breadcrumb",
        "map": "Eval Map",
        "measure": {"structure": "Structure", "quality": "Quality"},
        "of": "of",
        "per_axis": "2 points per axis",
        "without": "Without Minto",
        "with": "With Minto",
        "without_short": "without",
        "with_short": "with Minto",
        "delta": "Change",
        "axis": {
            "structure": {"top": "Top", "key_line_composition": "Key-line composition", "levels": "Levels", "order_and_kind": "Order and kind"},
            "quality": {"top": "Top", "same_kind_grouping": "Same-kind grouping", "explainable_order": "Explainable order", "mece": "MECE", "visible_structure": "Visible, proportionate structure"},
        },
        "judge_on_skill": "The judge on the output with Minto",
        "mode": "Mode",
        "case": "case",
        "run": "run",
        "control_sub": "control prompt",
        "skill_sub": "prompt with the skill",
        "blind": "blind label",
        "no_hard": "No hard failures",
        "hard": "Hard failures",
        "penalized": "quality after the rubric’s penalty",
        "judge": "The judge",
        "originals": "Outputs and the judge’s words are quoted as written, in English.",
        "defect": "Recurring defect",
        "present": "present",
        "absent": "absent",
        "no_defects": "The judge attributed no recurring defect to either output.",
        "decisive": "Decisive questions",
        "checks": "Judge’s check",
        "yes": "yes",
        "no": "no",
        "na": "not applicable",
        "check": {
            "answer_first": "Answer first",
            "first_level_count": "First-level elements",
            "first_level_kind_matches": "First-level kind matches the gold",
            "invented_facts": "Invented facts",
            "unacknowledged_source_loss": "Source lost without a note",
            "mode_respected": "Mode respected",
            "readers_question_literal": "Reader’s question stated literally",
            "order_type_named": "Order type named",
            "scq_intro_present": "SCQ introduction present",
        },
        "cause": {
            "ignored": "the skill has the rule; the model did not follow it",
            "missing": "the skill has no such rule",
            "buried": "the rule is there but buried",
            "vague": "the rule is too vague to follow",
        },
        "test": "How the test was built",
        "control_prompt": "Prompt without Minto",
        "skill_prompt": "Prompt with Minto",
        "five_parts": "five parts, in order",
        "task_whole": "the whole case input",
        "input": "Case input",
        "gold": "The judge’s gold",
        "bytes": "B",
        "at": "at",
        "judge_prov": "Judge",
        "effort": "effort",
        "skill_from": "skill from commit",
        "prev_model": "Previous model",
        "next_model": "Next model",
        "prev_case": "Previous case",
        "next_case": "Next case",
        "steps": "Neighbouring pairs",
        "case_models": "Eight models on this case",
        "case_col_model": "Model",
        "no_pair": "no pair",
        "questions": "What the judge asked of every output",
        "observation": "What the judge saw across all outputs",
        "attribution": "Where the outputs fell short",
        "attr_section": "Skill section",
        "attr_cause": "Cause",
        "attr_where": "Where it appeared",
        "skill_title": "The skill as the models saw it",
        "skill_head": "Minto skill at commit",
        "back_map": "Back to the map",
    },
    "ru": {
        "crumbs": "Путь",
        "map": "Карта оценки",
        "measure": {"structure": "Структура", "quality": "Качество"},
        "of": "из",
        "per_axis": "по&nbsp;2&nbsp;балла на&nbsp;ось",
        "without": "Без Minto",
        "with": "С&nbsp;Minto",
        "without_short": "без",
        "with_short": "с&nbsp;Minto",
        "delta": "Изменение",
        "axis": {
            "structure": {"top": "Вершина", "key_line_composition": "Состав ключевой линии", "levels": "Уровни", "order_and_kind": "Порядок и&nbsp;род"},
            "quality": {"top": "Вершина", "same_kind_grouping": "Однородные группы", "explainable_order": "Объяснимый порядок", "mece": "MECE", "visible_structure": "Видимая соразмерная структура"},
        },
        "judge_on_skill": "Судья об&nbsp;ответе с&nbsp;Minto",
        "mode": "Режим",
        "case": "кейс",
        "run": "прогон",
        "control_sub": "контрольный промпт",
        "skill_sub": "промпт с&nbsp;навыком",
        "blind": "слепая метка",
        "no_hard": "Жёстких провалов нет",
        "hard": "Жёсткие провалы",
        "penalized": "качество со&nbsp;штрафом рубрики",
        "judge": "Судья",
        "originals": "Ответы моделей и&nbsp;слова судьи приведены в&nbsp;оригинале, по-английски.",
        "defect": "Повторяющийся дефект",
        "present": "есть",
        "absent": "нет",
        "no_defects": "Судья не&nbsp;приписал ни&nbsp;одному из&nbsp;двух ответов повторяющихся дефектов.",
        "decisive": "Решающие вопросы",
        "checks": "Проверка судьи",
        "yes": "да",
        "no": "нет",
        "na": "не&nbsp;применяется",
        "check": {
            "answer_first": "Ответ в&nbsp;начале",
            "first_level_count": "Элементов первого уровня",
            "first_level_kind_matches": "Род первого уровня как в&nbsp;эталоне",
            "invented_facts": "Выдуманные факты",
            "unacknowledged_source_loss": "Потеря материала без пометки",
            "mode_respected": "Режим соблюдён",
            "readers_question_literal": "Вопрос читателя назван дословно",
            "order_type_named": "Тип порядка назван",
            "scq_intro_present": "Есть вступление SCQ",
        },
        "cause": {
            "ignored": "правило в&nbsp;навыке есть, модель его не&nbsp;выполнила",
            "missing": "такого правила в&nbsp;навыке нет",
            "buried": "правило есть, но&nbsp;спрятано глубоко",
            "vague": "правило сформулировано слишком размыто",
        },
        "test": "Как устроен тест",
        "control_prompt": "Промпт без Minto",
        "skill_prompt": "Промпт с&nbsp;Minto",
        "five_parts": "пять частей по&nbsp;порядку",
        "task_whole": "вход кейса целиком",
        "input": "Вход кейса",
        "gold": "Эталон судьи",
        "bytes": "Б",
        "at": "на",
        "judge_prov": "Судья",
        "effort": "effort",
        "skill_from": "навык с&nbsp;коммита",
        "prev_model": "Предыдущая модель",
        "next_model": "Следующая модель",
        "prev_case": "Предыдущий кейс",
        "next_case": "Следующий кейс",
        "steps": "Соседние пары",
        "case_models": "Восемь моделей на&nbsp;этом кейсе",
        "case_col_model": "Модель",
        "no_pair": "нет пары",
        "questions": "О&nbsp;чём судья спрашивал каждый ответ",
        "observation": "Что судья увидел во&nbsp;всех ответах",
        "attribution": "Где ответы не&nbsp;дотянули",
        "attr_section": "Раздел навыка",
        "attr_cause": "Причина",
        "attr_where": "У&nbsp;кого",
        "skill_title": "Навык в&nbsp;том виде, в&nbsp;каком его видели модели",
        "skill_head": "Навык Minto на&nbsp;коммите",
        "back_map": "Вернуться к&nbsp;карте",
    },
}


def text(lang: str, en: str, ru: str) -> str:
    return en if lang == "en" else ru


# ---------------------------------------------------------------- paths


class Place:
    """Where one page sits, and every relative link it needs."""

    def __init__(self, lang: str, rel: str) -> None:
        self.lang = lang
        self.rel = rel  # e.g. "eval-map/03-period-graph-books/haiku45/"
        depth = rel.count("/")
        self.up = "../" * depth
        self.assets = self.up + ("assets" if lang == "en" else "../assets")
        self.home = self.up if self.up else "./"
        self.other = self.up + ("ru/" if lang == "en" else "../") + rel
        self.url = BASE_URL + ("" if lang == "en" else "ru/") + rel
        self.url_en = BASE_URL + rel
        self.url_ru = BASE_URL + "ru/" + rel

    def to(self, rel: str) -> str:
        """A link to another page of the same locale, given its path from the locale root."""
        return self.up + rel

    def file(self) -> Path:
        return SITE / ("" if self.lang == "en" else "ru") / self.rel / "index.html"


def pair_rel(fixture: str, engine: str) -> str:
    return f"eval-map/{fixture}/{engine}/"


def case_rel(fixture: str) -> str:
    return f"eval-map/{fixture}/"


SKILL_REL = "eval-map/skill/"


# ---------------------------------------------------------------- page shell


def shell(place: Place, versions: dict, title: str, description: str, main: list[str], wide: bool) -> str:
    chrome = MAP_COPY[place.lang]
    values = {
        "lang": place.lang,
        "description": description,
        "canonical": place.url,
        "url_en": place.url_en,
        "url_ru": place.url_ru,
        "dir_assets": place.assets,
        "dir_home": place.home,
        "dir_other": place.other,
        "href_en": "./" if place.lang == "en" else place.other,
        "href_ru": place.other if place.lang == "en" else "./",
        "current_en": ' aria-current="page"' if place.lang == "en" else "",
        "current_ru": "" if place.lang == "en" else ' aria-current="page"',
        "v_mirai": versions["mirai.css"],
        "v_styles": versions["styles.css"],
        "v_app": versions["app.js"],
        "og_title": title,
        "title": title,
        "body_attrs": ' data-layout="wide"' if wide else "",
        "main": "\n".join(main),
    }
    for key in ("skip", "brand_alt", "nav_sections", "nav_examples", "nav_evidence", "nav_modes",
                "nav_install", "nav_language", "footer_note", "nav_links", "footer_changelog", "footer_switch"):
        values[key] = chrome[key]

    def substitute(match: re.Match) -> str:
        key = match.group(1)
        if key not in values:
            raise SystemExit(f"ERROR: eval-detail.template.html asks for {{{{{key}}}}}, which is not defined")
        return values[key]

    page = re.sub(r"\{\{(\w+)\}\}", substitute, TEMPLATE.read_text(encoding="utf-8"))
    if "{{" in page:
        raise SystemExit("ERROR: a detail page still contains an unresolved placeholder")
    return page


def crumbs(place: Place, trail: list[tuple[str, str | None]]) -> list[str]:
    c = COPY[place.lang]
    out = [f'        <nav class="crumbs" aria-label="{c["crumbs"]}">']
    for i, (label, href) in enumerate(trail):
        if i:
            out.append('          <span class="crumbs__sep" aria-hidden="true">/</span>')
        if href is None:
            out.append(f'          <span aria-current="page">{label}</span>')
        else:
            out.append(f'          <a class="link" href="{href}">{label}</a>')
    out.append("        </nav>")
    return out


def md_block(indent: str, source: str, cls: str = "md") -> list[str]:
    """Rendered markdown, one block per line, identical on both locales."""
    body = ed.markdown(source)
    return [f'{indent}<div class="{cls}" lang="en">'] + [f"{indent}  {line}" for line in body.split("\n")] + [f"{indent}</div>"]


def size_label(lang: str, n: int) -> str:
    return f"{n:,}".replace(",", "&nbsp;") + "&nbsp;" + COPY[lang]["bytes"]


# ---------------------------------------------------------------- shared pieces


def units(score: int, other: int | None = None) -> str:
    """Two squares per axis. Earned is ink; a point the control earned and this arm
    lost is hatched; a point neither earned is an outline."""
    cells = []
    for k in range(2):
        if k < score:
            cells.append('<span class="unit"></span>')
        elif other is not None and k < other:
            cells.append('<span class="unit" data-state="flaw"></span>')
        else:
            cells.append('<span class="unit" data-state="gap"></span>')
    return f'<span class="axis-units" aria-hidden="true">{"".join(cells)}</span>'


def tone(value: int) -> str:
    return "up" if value > 0 else "down" if value < 0 else "flat"


def totals(pair: dict) -> dict[str, tuple[int, int, int]]:
    out = {}
    for name, source, _ in MEASURES:
        control = pair["arms"]["control"]["cell"][source]["total"]
        skill = pair["arms"]["skill"]["cell"][source]["total"]
        out[name] = (control, skill, skill - control)
    return out


def verdict_phrase(lang: str, pair: dict) -> str:
    t = totals(pair)
    ds, dq = t["structure"][2], t["quality"][2]
    m = {"en": {"structure": "structure", "quality": "quality"}, "ru": {"structure": "структуре", "quality": "качеству"}}[lang]
    n = {"en": {"structure": "structure", "quality": "quality"}, "ru": {"structure": "структура", "quality": "качество"}}[lang]
    if ds > 0 and dq > 0:
        return text(lang, "better with Minto on both measures", "с&nbsp;Minto лучше по&nbsp;обеим мерам")
    if ds < 0 and dq < 0:
        return text(lang, "worse with Minto on both measures", "с&nbsp;Minto хуже по&nbsp;обеим мерам")
    if ds == 0 and dq == 0:
        return text(lang, "no change with Minto", "с&nbsp;Minto без изменений")
    if ds * dq < 0:
        up, down = ("structure", "quality") if ds > 0 else ("quality", "structure")
        return text(lang, f"with Minto, better on {m[up]} and worse on {m[down]}",
                    f"с&nbsp;Minto лучше по&nbsp;{m[up]} и&nbsp;хуже по&nbsp;{m[down]}")
    moved, still = ("structure", "quality") if ds else ("quality", "structure")
    delta = ds or dq
    if lang == "en":
        return f"with Minto, {'better' if delta > 0 else 'worse'} on {m[moved]}, {n[still]} unchanged"
    same = "та&nbsp;же" if still == "structure" else "то&nbsp;же"
    return f"с&nbsp;Minto {'лучше' if delta > 0 else 'хуже'} по&nbsp;{m[moved]}, {n[still]} {same}"


def figures(lang: str, pair: dict, indent: str) -> list[str]:
    c = COPY[lang]
    out = [f'{indent}<p class="pair-top__figs">']
    for name, (control, skill, delta) in totals(pair).items():
        maximum = dict((m, x) for m, _, x in MEASURES)[name]
        out.append(
            f'{indent}  <span class="pair-fig pair-fig--{tone(delta)}" data-pair-measure="{name}" '
            f'data-pair-control="{control}" data-pair-skill="{skill}" data-pair-delta="{delta}">'
            f'<span class="pair-fig__name">{c["measure"][name]}</span> '
            f'<span class="num">{control}&nbsp;→&nbsp;{skill}</span> '
            f'<span class="pair-fig__max">{c["of"]}&nbsp;{maximum}</span> '
            f'<span class="num pair-fig__delta">{signed(delta)}</span></span>'
        )
    out.append(f"{indent}</p>")
    return out


def axis_tables(lang: str, pair: dict, indent: str) -> list[str]:
    c = COPY[lang]
    out = [f'{indent}<div class="axes">']
    for name, source, maximum in MEASURES:
        control_cell = pair["arms"]["control"]["cell"][source]
        skill_cell = pair["arms"]["skill"]["cell"][source]
        out.append(f'{indent}  <table class="axis-table" id="{name}">')
        out.append(f'{indent}    <caption class="axis-table__cap"><span class="axis-table__capin"><span class="subtitle">{c["measure"][name]}</span> '
                   f'<span class="label">{c["of"]}&nbsp;{maximum}, {c["per_axis"]}</span></span></caption>')
        out.append(f"{indent}    <thead>")
        out.append(f'{indent}      <tr><th scope="col"><span class="visually-hidden">{c["measure"][name]}</span></th>'
                   f'<th scope="col" class="label">{c["without"]} <span class="num">{control_cell["total"]}</span></th>'
                   f'<th scope="col" class="label">{c["with"]} <span class="num">{skill_cell["total"]}</span></th>'
                   f'<th scope="col" class="label axis-table__d">{c["delta"]}</th></tr>')
        out.append(f"{indent}    </thead>")
        out.append(f"{indent}    <tbody>")
        for axis in AXES[name]:
            control, skill = control_cell[axis], skill_cell[axis]
            delta = skill - control
            out.append(
                f'{indent}      <tr class="axis-row axis-row--{tone(delta)}" data-axis-measure="{name}" data-axis="{axis}" '
                f'data-axis-control="{control}" data-axis-skill="{skill}">'
                f'<th scope="row" class="axis-row__name">{c["axis"][name][axis]}</th>'
                f'<td>{units(control)}<span class="visually-hidden">{control}</span></td>'
                f'<td>{units(skill, control)}<span class="visually-hidden">{skill}</span></td>'
                f'<td class="num axis-row__delta">{signed(delta) if delta else ""}</td></tr>'
            )
        out.append(f"{indent}    </tbody>")
        out.append(f"{indent}  </table>")
    out.append(f"{indent}</div>")
    return out


def score_strip(lang: str, pair: dict, arm: str, indent: str) -> list[str]:
    c = COPY[lang]
    out = [f'{indent}<div class="strips" aria-hidden="true">']
    for name, source, maximum in MEASURES:
        cell = pair["arms"][arm]["cell"][source]
        other = pair["arms"]["control"]["cell"][source] if arm == "skill" else None
        axes = "".join(
            f'<span class="strip__axis">{units(cell[axis], other[axis] if other else None)}</span>' for axis in AXES[name]
        )
        out.append(f'{indent}  <div class="strip"><span class="label strip__name">{c["measure"][name]}</span>'
                   f'<span class="strip__units">{axes}</span>'
                   f'<span class="num strip__total">{cell["total"]}<span class="label">/{maximum}</span></span></div>')
    out.append(f"{indent}</div>")
    return out


def hard_failures(lang: str, cell: dict, indent: str) -> str:
    c = COPY[lang]
    tokens = cell["hard_failures"]
    if not tokens:
        return f'{indent}<p class="label arm-hf arm-hf--none">{c["no_hard"]}</p>'
    items = "".join(f'<li><span class="unit" data-state="flaw" aria-hidden="true"></span><code class="mono">{esc(t)}</code></li>' for t in tokens)
    raw, penalized = cell["quality_raw"]["total"], cell["quality_penalized"]["total"]
    if penalized != raw:
        # The map and this page mean quality_raw; the rubric's penalty is shown
        # where it bites, so the lower figure is never hidden.
        items += (f'<li class="arm-hf__pen" data-pair-penalized="{penalized}" data-pair-raw="{raw}">'
                  f'<span class="label">{c["penalized"]}</span> <span class="num">{penalized}</span><span class="label">/10</span></li>')
    return f'{indent}<ul class="arm-hf" aria-label="{c["hard"]}">{items}</ul>'


def checks_table(lang: str, pair: dict, indent: str) -> list[str]:
    c = COPY[lang]
    control = pair["arms"]["control"]["cell"]["checks"]
    skill = pair["arms"]["skill"]["cell"]["checks"]

    def show(key: str, value) -> str:
        if value == "na":
            return f'<span class="check check--na">{c["na"]}</span>'
        if isinstance(value, bool):
            good = (not value) if key in ("invented_facts", "unacknowledged_source_loss") else value
            return f'<span class="check check--{"ok" if good else "bad"}">{c["yes"] if value else c["no"]}</span>'
        return f'<span class="num">{esc(str(value))}</span>'

    rows, skipped = [], 0
    for key in c["check"]:
        if key not in control:
            continue
        if control[key] == "na" and skill[key] == "na":
            skipped += 1
            continue
        diff = " check-row--diff" if control[key] != skill[key] else ""
        rows.append(f'{indent}    <tr class="check-row{diff}"><th scope="row">{c["check"][key]}</th>'
                    f'<td>{show(key, control[key])}</td><td>{show(key, skill[key])}</td></tr>')
    out = [f'{indent}<table class="checks">',
           f'{indent}  <thead><tr><th scope="col" class="label">{c["checks"]}</th><th scope="col" class="label">{c["without_short"]}</th><th scope="col" class="label">{c["with_short"]}</th></tr></thead>',
           f"{indent}  <tbody>", *rows, f"{indent}  </tbody>", f"{indent}</table>"]
    if skipped:
        mode = pair["mode"]
        if lang == "en":
            note = f"{skipped} more judge {'check does' if skipped == 1 else 'checks do'} not apply to mode"
        else:
            note = (f"Ещё {skipped}&nbsp;{plural_ru(skipped, 'проверка', 'проверки', 'проверок')} судьи "
                    f"{plural_ru(skipped, 'не&nbsp;применяется', 'не&nbsp;применяются', 'не&nbsp;применяются')} к&nbsp;режиму")
        out.append(f'{indent}<p class="label checks__na">{note} <code class="mono">{mode}</code></p>')
    return out


def defect_matrix(lang: str, run: ed.Run, pair: dict, indent: str) -> list[str]:
    c = COPY[lang]
    verdict = run.verdicts[pair["fixture"]]
    control_out = pair["arms"]["control"]["output"]
    skill_out = pair["arms"]["skill"]["output"]
    rows = []
    for item in verdict.attribution:
        in_control, in_skill = control_out in item["outputs"], skill_out in item["outputs"]
        if not (in_control or in_skill):
            continue

        def mark(present: bool) -> str:
            state, word = ("flaw", c["present"]) if present else ("gap", c["absent"])
            return f'<span class="unit" data-state="{state}" aria-hidden="true"></span><span class="visually-hidden">{word}</span>'

        rows.append(
            f'{indent}    <tr><th scope="row"><span class="doc-item" lang="en">{ed.inline(item["defect"])}</span>'
            f'<span class="label defect__cause">{c["cause"][item["cause"]]} · <span lang="en">{ed.inline(item["section"])}</span></span></th>'
            f"<td>{mark(in_control)}</td><td>{mark(in_skill)}</td></tr>"
        )
    if not rows:
        return [f'{indent}<p class="small">{c["no_defects"]}</p>']
    return [f'{indent}<table class="dmatrix">',
            f'{indent}  <thead><tr><th scope="col" class="label">{c["defect"]}</th><th scope="col" class="label">{c["without_short"]}</th><th scope="col" class="label">{c["with_short"]}</th></tr></thead>',
            f"{indent}  <tbody>", *rows, f"{indent}  </tbody>", f"{indent}</table>"]


def decisive_compare(lang: str, run: ed.Run, pair: dict, indent: str) -> list[str]:
    c = COPY[lang]
    fixture = pair["fixture"]
    questions = ed.decisive_questions(fixture)
    verdict = run.verdicts[fixture]
    control = ed.decisive_rows(verdict, questions, pair["arms"]["control"]["output"])
    skill = ed.decisive_rows(verdict, questions, pair["arms"]["skill"]["output"])
    out = [f'{indent}<ol class="cmp-list">']
    for head, control_answer, skill_answer in align_answers(questions, control, skill):
        out.append(f'{indent}  <li class="cmp"><p class="small cmp__q" lang="en">{head}</p>'
                   f'<p class="cmp__a"><span class="label">{c["without_short"]}</span> <span lang="en">{ed.inline(control_answer)}</span></p>'
                   f'<p class="cmp__a"><span class="label">{c["with_short"]}</span> <span lang="en">{ed.inline(skill_answer)}</span></p></li>')
    out.append(f"{indent}</ol>")
    return out


def align_answers(questions: list[str], control: list, skill: list) -> list[tuple[str, str, str]]:
    """Pair the judge's answers for two outputs row by row.

    A table gives both outputs the same labels, so they pair as they stand. A list
    line can bundle questions ("Q4, Q5 and Q6 each …") for one output and not the
    other; those pair by question number, the bundled answer standing for each.
    A line the judge never split by question stays one row per output.
    """
    if [r[0] for r in control] == [r[0] for r in skill]:
        return [(esc(q) if q else esc(label or ""), a, b) for (label, q, a), (_, _, b) in zip(control, skill)]

    def by_number(rows: list) -> dict[int, str] | None:
        found: dict[int, str] = {}
        for label, _, answer in rows:
            numbers = ed.question_numbers(label)
            if not numbers:
                return None
            for n in numbers:
                found[n] = answer if len(numbers) == 1 else f"({label}) {answer}"
        return found

    left, right = by_number(control), by_number(skill)
    if left is None or right is None:
        whole = lambda rows: " ".join(f"{label or ''} {answer}".strip() for label, _, answer in rows)
        return [("", whole(control), whole(skill))]
    numbers = sorted(set(left) | set(right))
    return [(esc(questions[n - 1]) if 1 <= n <= len(questions) else f"Q{n}", left.get(n, "—"), right.get(n, "—")) for n in numbers]


def prompts(lang: str, place: Place, run: ed.Run, fixture: str, indent: str) -> list[str]:
    """The exact prompts, reassembled the way eval/build-prompts.sh writes them."""
    c = COPY[lang]
    commit = run.scores["commits"][0][:7]
    control = ed.control_prompt(fixture)
    skill_bytes = len(ed.skill_prompt(run, fixture).encode("utf-8"))
    parts = []
    for label, filename in ed.SKILL_PARTS:
        anchor = filename.replace(".", "-").lower()
        size = size_label(lang, len(run.skill_files[label].encode("utf-8")))
        parts.append(f'{indent}      <li><code class="mono">===== {label} =====</code> '
                     f'<a class="link small" href="{place.to(SKILL_REL)}#{anchor}">{label} {c["at"]} {commit}</a> <span class="label">{size}</span></li>')
    return [
        f'{indent}<details class="test__part">',
        f'{indent}  <summary><span class="subtitle">{c["control_prompt"]}</span> <span class="label">{size_label(lang, len(control.encode("utf-8")))}</span></summary>',
        f'{indent}  <pre class="prompt-src" lang="en"><code>{esc(control)}</code></pre>',
        f"{indent}</details>",
        f'{indent}<details class="test__part">',
        f'{indent}  <summary><span class="subtitle">{c["skill_prompt"]}</span> <span class="label">{c["five_parts"]} · {size_label(lang, skill_bytes)}</span></summary>',
        f'{indent}  <ol class="assembly">',
        f'{indent}      <li><code class="mono" lang="en">{esc(ed.SKILL_PREAMBLE)}</code></li>',
        *parts,
        f'{indent}      <li><code class="mono">===== TASK =====</code> <span class="small">{c["task_whole"]}</span></li>',
        f'{indent}      <li><code class="mono" lang="en">{esc(ed.CLOSING)}</code></li>',
        f"{indent}  </ol>",
        f"{indent}</details>",
    ]


def source_parts(lang: str, fixture: str, indent: str) -> list[str]:
    c = COPY[lang]
    out = []
    for title, source, name in ((c["input"], ed.fixture_input(fixture), "before.md"), (c["gold"], ed.fixture_gold(fixture), "gold.md")):
        out += [f'{indent}<details class="test__part">',
                f'{indent}  <summary><span class="subtitle">{title}</span> <code class="label">{name}</code></summary>',
                *md_block(indent + "  ", source, "md md--src"),
                f"{indent}</details>"]
    return out


def provenance(lang: str, run: ed.Run, engine: str | None) -> str:
    c = COPY[lang]
    judge = run.scores["judge"]
    bits = [f'{c["judge_prov"]} {esc(judge["model"])}, {c["effort"]} {esc(judge["effort"])}']
    if engine:
        settings = run.scores["engines"].get(engine, {})
        effort = settings.get("effort") or settings.get("reasoning_effort")
        if effort:
            bits.append(f'{ENGINE_LABEL[engine]}, {c["effort"]} {esc(effort)}')
    bits.append(f'{c["skill_from"]} {run.scores["commits"][0][:7]}')
    bits.append(f'{c["run"]} {run.name}')
    return " · ".join(bits)


# ---------------------------------------------------------------- pages


def pair_page(lang: str, run: ed.Run, fixture: str, engine: str, versions: dict) -> tuple[Path, str]:
    c = COPY[lang]
    place = Place(lang, pair_rel(fixture, engine))
    pair = ed.pair(run, fixture, engine)
    case_name = FIXTURE_NAME[lang][fixture]
    engine_name = ENGINE_LABEL[engine]
    mode = pair["mode"]
    t = totals(pair)
    n_outputs = len(run.mapping[fixture])

    main = [f'      <article class="pair" data-pair-fixture="{fixture}" data-pair-engine="{engine}">']
    main += ['        <header class="pair-top">']
    main += ["  " + line for line in crumbs(place, [(c["map"], place.to("eval-map/")), (case_name, place.to(case_rel(fixture))), (esc(engine_name), None)])]
    quote_open, quote_close = ("“", "”") if lang == "en" else ("«", "»")
    connector = "on" if lang == "en" else "на&nbsp;кейсе"
    main.append(f'          <h1 class="display pair-top__h">{esc(engine_name)} {connector} {quote_open}{case_name}{quote_close}: {verdict_phrase(lang, pair)}</h1>')
    main += figures(lang, pair, "          ")
    main.append('          <div class="pair-top__why">')
    main.append(f'            <p class="label">{c["judge_on_skill"]}</p>')
    main.append(f'            <blockquote class="judge-note" lang="en"><p>{ed.inline(pair["arms"]["skill"]["note"])}</p></blockquote>')
    main.append("          </div>")
    main.append(f'          <p class="label pair-top__meta">{c["mode"]} <code class="mono">{mode}</code> · {c["case"]} <code class="mono">{fixture}</code> · {c["run"]} {run.name}</p>')
    main.append("        </header>")

    main.append(f'        <section class="section pair-axes" aria-label="{c["measure"]["structure"]}, {c["measure"]["quality"]}">')
    main += axis_tables(lang, pair, "          ")
    main.append("        </section>")

    main.append(f'        <section class="section margins" aria-labelledby="rail-h">')
    main.append(f'          <p class="label margins__note">{c["originals"]}</p>')
    main.append(f'          <div class="case-tabs arm-tabs" data-arm-tablist aria-label="{c["judge"]}">')
    main.append(f'            <a class="case-tab" href="#arm-control" data-arm-tab="control">{c["without"]}</a>')
    main.append(f'            <a class="case-tab" href="#arm-skill" data-arm-tab="skill">{c["with"]}</a>')
    main.append("          </div>")
    main.append('          <div class="margins__docs">')
    for arm in ed.ARMS:
        a = pair["arms"][arm]
        title = c["without"] if arm == "control" else c["with"]
        sub = c["control_sub"] if arm == "control" else c["skill_sub"]
        main.append(f'            <article class="arm arm--{arm}" id="arm-{arm}" data-arm-panel="{arm}" aria-labelledby="arm-{arm}-h">')
        main.append(f'              <header class="arm__head"><h2 class="subtitle" id="arm-{arm}-h">{title}</h2>'
                    f'<span class="label">{sub} · {c["blind"]} <code class="mono">{a["output"]}</code></span></header>')
        main += score_strip(lang, pair, arm, "              ")
        main.append(hard_failures(lang, a["cell"], "              "))
        main.append(f'              <blockquote class="judge-note" lang="en"><p>{ed.inline(a["note"])}</p></blockquote>')
        main += md_block("              ", a["text"], "md arm__doc")
        main.append("            </article>")
    main.append("          </div>")
    main.append('          <aside class="margins__rail" aria-labelledby="rail-h">')
    main.append(f'            <h2 class="subtitle" id="rail-h">{c["judge"]}</h2>')
    main += defect_matrix(lang, run, pair, "            ")
    main.append(f'            <h3 class="label rail__sub">{c["decisive"]}</h3>')
    main += decisive_compare(lang, run, pair, "            ")
    main += checks_table(lang, pair, "            ")
    main.append("          </aside>")
    main.append("        </section>")

    main.append('        <section class="section test" aria-labelledby="test-h">')
    main.append(f'          <h2 class="title" id="test-h">{c["test"]}</h2>')
    if lang == "en":
        lede = (f"{esc(engine_name)} received the same task twice. The control prompt is one framing line and the task. "
                f"The prompt with Minto is the same task preceded by the full text of the skill. The judge read both outputs "
                f"among {n_outputs} under blind labels and did not know which one had the skill.")
    else:
        lede = (f"{esc(engine_name)} получила одну и&nbsp;ту&nbsp;же задачу дважды. Контрольный промпт&nbsp;— одна вводная строка и&nbsp;задача. "
                f"Промпт с&nbsp;Minto&nbsp;— та&nbsp;же задача, перед которой стоит полный текст навыка. Судья читал оба ответа среди "
                f"{n_outputs}&nbsp;{plural_ru(n_outputs, 'ответа', 'ответов', 'ответов')} под слепыми метками и&nbsp;не&nbsp;знал, в&nbsp;каком из&nbsp;них был навык.")
    main.append(f'          <p class="body test__lede">{lede}</p>')
    main.append('          <div class="test__grid">')
    main += prompts(lang, place, run, fixture, "            ")
    main += source_parts(lang, fixture, "            ")
    main.append("          </div>")
    main.append(f'          <p class="label test__prov">{provenance(lang, run, engine)}</p>')
    main.append("        </section>")

    main += neighbours(lang, place, run, fixture, engine)
    main.append("      </article>")

    title = (f"{engine_name} on {FIXTURE_NAME['en'][fixture]} — Minto Eval Map" if lang == "en"
             else f"{esc(engine_name)} на&nbsp;кейсе «{case_name}» — карта оценки Minto")
    ds, dq = t["structure"], t["quality"]
    if lang == "en":
        description = (f"{engine_name}, case {fixture}: structure {ds[0]} to {ds[1]} of 8, quality {dq[0]} to {dq[1]} of 10 with Minto. "
                       "Both outputs, the judge’s notes and the exact prompts.")
    else:
        description = (f"{engine_name}, кейс {fixture}: с&nbsp;Minto структура {ds[0]}&nbsp;→&nbsp;{ds[1]} из&nbsp;8, качество {dq[0]}&nbsp;→&nbsp;{dq[1]} из&nbsp;10. "
                       "Оба ответа, заметки судьи и&nbsp;точные промпты.")
    return place.file(), shell(place, versions, title, description, main, wide=True)


def neighbours(lang: str, place: Place, run: ed.Run, fixture: str, engine: str) -> list[str]:
    c = COPY[lang]

    def judged(f: str, e: str) -> bool:
        return ed.pair(run, f, e) is not None

    engines = [e for e in ENGINE_ORDER if judged(fixture, e)]
    fixtures = [f for f in FIXTURE_ORDER if judged(f, engine)]
    ei, fi = engines.index(engine), fixtures.index(fixture)
    steps = [
        ("prev", c["prev_model"], engines[ei - 1] if ei else None, None),
        ("next", c["next_model"], engines[ei + 1] if ei + 1 < len(engines) else None, None),
        ("prev", c["prev_case"], None, fixtures[fi - 1] if fi else None),
        ("next", c["next_case"], None, fixtures[fi + 1] if fi + 1 < len(fixtures) else None),
    ]
    out = [f'        <nav class="pair-steps" aria-label="{c["steps"]}">']
    for i, (rel, label, other_engine, other_fixture) in enumerate(steps):
        key = ("model", "case")[i // 2]
        if other_engine:
            out.append(f'          <a class="nav-step" href="{place.to(pair_rel(fixture, other_engine))}" rel="{rel}" data-step="{rel}-{key}">'
                       f'<span class="label">{label}</span><span class="small">{esc(ENGINE_LABEL[other_engine])}</span></a>')
        elif other_fixture:
            out.append(f'          <a class="nav-step" href="{place.to(pair_rel(other_fixture, engine))}" rel="{rel}" data-step="{rel}-{key}">'
                       f'<span class="label">{label}</span><span class="small">{FIXTURE_NAME[lang][other_fixture]}</span></a>')
        else:
            out.append(f'          <span class="nav-step nav-step--none" aria-hidden="true"><span class="label">{label}</span><span class="small">—</span></span>')
    out.append("        </nav>")
    return out


def case_page(lang: str, run: ed.Run, fixture: str, versions: dict) -> tuple[Path, str]:
    c = COPY[lang]
    place = Place(lang, case_rel(fixture))
    case_name = FIXTURE_NAME[lang][fixture]
    mode = FIXTURE_MODE[fixture]
    verdict = run.verdicts[fixture]
    out_to = {info_out.removesuffix(".md"): (info["engine"], info["arm"]) for info_out, info in run.mapping[fixture].items()}

    main = [f'      <article class="case-page" data-case-fixture="{fixture}">']
    main += ['        <header class="pair-top">']
    main += ["  " + line for line in crumbs(place, [(c["map"], place.to("eval-map/")), (case_name, None)])]
    main.append(f'          <h1 class="display pair-top__h">{case_name}</h1>')
    main.append(f'          <p class="lead case-page__mode">{c["mode"]} <code class="mono">{mode}</code> · {MODE_TEXT[lang][mode]}</p>')
    main.append("        </header>")

    main.append('        <section class="section" aria-labelledby="models-h">')
    main.append(f'          <h2 class="title" id="models-h">{c["case_models"]}</h2>')
    main.append('          <table class="case-models">')
    main.append(f'            <thead><tr><th scope="col" class="label">{c["case_col_model"]}</th>'
                f'<th scope="col" class="label">{c["measure"]["structure"]}, {c["of"]}&nbsp;8</th>'
                f'<th scope="col" class="label">{c["measure"]["quality"]}, {c["of"]}&nbsp;10</th></tr></thead>')
    main.append("            <tbody>")
    for engine in ENGINE_ORDER:
        pair = ed.pair(run, fixture, engine)
        if pair is None:
            reason = EXCLUDED[(fixture, engine)][lang]
            main.append(f'              <tr class="case-models__row case-models__row--none" data-case-missing="{engine}"><th scope="row">{esc(ENGINE_LABEL[engine])}</th>'
                        f'<td colspan="2"><span class="label">{c["no_pair"]}.</span> <span class="small">{reason}</span></td></tr>')
            continue
        cells = []
        attrs = []
        for name, (control, skill, delta) in totals(pair).items():
            attrs.append(f'data-case-{name}-control="{control}" data-case-{name}-skill="{skill}" data-case-{name}-delta="{delta}"')
            cells.append(f'<td><span class="num">{control}&nbsp;→&nbsp;{skill}</span> <span class="num case-models__d case-models__d--{tone(delta)}">{signed(delta)}</span></td>')
        main.append(f'              <tr class="case-models__row" data-case-engine="{engine}" {" ".join(attrs)}>'
                    f'<th scope="row"><a class="link" href="{place.to(pair_rel(fixture, engine))}">{esc(ENGINE_LABEL[engine])}</a></th>{"".join(cells)}</tr>')
    main.append("            </tbody>")
    main.append("          </table>")
    main.append("        </section>")

    main.append('        <section class="section case-page__judge" aria-labelledby="obs-h">')
    main.append(f'          <h2 class="title" id="obs-h">{c["observation"]}</h2>')
    main.append(f'          <blockquote class="judge-note judge-note--lead" lang="en"><p>{ed.inline(verdict.observation)}</p></blockquote>')
    main.append(f'          <h3 class="subtitle case-page__sub">{c["questions"]}</h3>')
    main.append('          <ol class="case-questions" lang="en">')
    for question in ed.decisive_questions(fixture):
        main.append(f"            <li>{ed.inline(question)}</li>")
    main.append("          </ol>")
    main.append(f'          <h3 class="subtitle case-page__sub">{c["attribution"]}</h3>')
    main.append('          <div class="md-table">')
    main.append('          <table class="case-attr">')
    main.append(f'            <thead><tr><th scope="col" class="label">{c["defect"]}</th><th scope="col" class="label">{c["attr_section"]}</th>'
                f'<th scope="col" class="label">{c["attr_cause"]}</th><th scope="col" class="label">{c["attr_where"]}</th></tr></thead>')
    main.append("            <tbody>")
    for item in verdict.attribution:
        by_arm = {"control": [], "skill": []}
        for out in sorted(item["outputs"]):
            engine, arm = out_to[out]
            by_arm[arm].append(engine)
        where = []
        for arm, label in (("control", c["without"]), ("skill", c["with"])):
            names = sorted(by_arm[arm], key=ENGINE_ORDER.index)
            listed = ", ".join(esc(ENGINE_LABEL[e]) for e in names) or "—"
            where.append(f'<span class="case-attr__arm"><span class="label">{label} · <span class="num">{len(names)}</span></span> <span class="small">{listed}</span></span>')
        main.append(f'              <tr><th scope="row"><span class="doc-item" lang="en">{ed.inline(item["defect"])}</span></th>'
                    f'<td><span class="small" lang="en">{ed.inline(item["section"])}</span></td>'
                    f'<td><span class="small">{c["cause"][item["cause"]]}</span></td><td>{"".join(where)}</td></tr>')
    main.append("            </tbody>")
    main.append("          </table>")
    main.append("          </div>")
    main.append("        </section>")

    main.append('        <section class="section test" aria-labelledby="test-h">')
    main.append(f'          <h2 class="title" id="test-h">{c["test"]}</h2>')
    main.append('          <div class="test__grid">')
    main += prompts(lang, place, run, fixture, "            ")
    main += source_parts(lang, fixture, "            ")
    main.append("          </div>")
    main.append(f'          <p class="label test__prov">{provenance(lang, run, None)}</p>')
    main.append(f'          <p><a class="link small" href="{place.to("eval-map/")}">{c["back_map"]}</a></p>')
    main.append("        </section>")
    main.append("      </article>")

    title = (f"{FIXTURE_NAME['en'][fixture]} — Minto Eval Map" if lang == "en" else f"{case_name} — карта оценки Minto")
    description = (f"Case {fixture}, mode {mode}: eight models with and without Minto, the judge’s questions and findings, the exact prompts."
                   if lang == "en" else
                   f"Кейс {fixture}, режим {mode}: восемь моделей с&nbsp;Minto и&nbsp;без него, вопросы и&nbsp;выводы судьи, точные промпты.")
    return place.file(), shell(place, versions, title, description, main, wide=False)


def skill_page(lang: str, run: ed.Run, versions: dict) -> tuple[Path, str]:
    c = COPY[lang]
    place = Place(lang, SKILL_REL)
    commit = run.scores["commits"][0]
    main = ['      <article class="skill-page">']
    main += ['        <header class="pair-top">']
    main += ["  " + line for line in crumbs(place, [(c["map"], place.to("eval-map/")), (c["skill_title"], None)])]
    main.append(f'          <h1 class="display pair-top__h">{c["skill_title"]}</h1>')
    if lang == "en":
        lede = (f"Every prompt with Minto in run {run.name} carried these three files, in this order, between the preamble and the task. "
                f"They are the skill at commit {commit[:7]}, not the current one.")
    else:
        lede = (f"Каждый промпт с&nbsp;Minto в&nbsp;прогоне {run.name} содержал эти три файла в&nbsp;таком порядке, между вводной строкой и&nbsp;задачей. "
                f"Это навык на&nbsp;коммите {commit[:7]}, а&nbsp;не&nbsp;текущий.")
    main.append(f'          <p class="lead">{lede}</p>')
    main.append("        </header>")
    for label, filename in ed.SKILL_PARTS:
        body = run.skill_files[label]
        anchor = filename.replace(".", "-").lower()
        digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
        main.append(f'        <section class="section skill-file" id="{anchor}" aria-labelledby="{anchor}-h">')
        main.append(f'          <h2 class="subtitle" id="{anchor}-h"><code class="mono">===== {label} =====</code></h2>')
        main.append(f'          <p class="label">{size_label(lang, len(body.encode("utf-8")))} · sha256 <code class="mono">{digest[:16]}</code> · '
                    f'<a class="link" href="https://github.com/welltraum/minto/blob/{commit}/plugins/minto/skills/minto/{label}">GitHub, {commit[:7]}</a></p>')
        main.append(f'          <pre class="prompt-src prompt-src--tall" lang="en"><code>{esc(body)}</code></pre>')
        main.append("        </section>")
    main.append(f'        <p class="section"><a class="link small" href="{place.to("eval-map/")}">{c["back_map"]}</a></p>')
    main.append("      </article>")
    title = "The Minto skill as the models saw it — Minto Eval Map" if lang == "en" else "Навык Minto в&nbsp;прогоне оценки — карта оценки Minto"
    description = (f"SKILL.md, rules.md and templates.md at commit {commit[:7]}, exactly as run {run.name} sent them."
                   if lang == "en" else
                   f"SKILL.md, rules.md и&nbsp;templates.md на&nbsp;коммите {commit[:7]}, ровно в&nbsp;том виде, в&nbsp;каком их&nbsp;получил прогон {run.name}.")
    return place.file(), shell(place, versions, title, description, main, wide=False)


# ---------------------------------------------------------------- all pages


def expected_pages(run: ed.Run) -> list[tuple[str, ...]]:
    """(kind, *keys) for every page one locale must carry, in a fixed order."""
    pages: list[tuple[str, ...]] = [("skill",)]
    for fixture in FIXTURE_ORDER:
        pages.append(("case", fixture))
        for engine in ENGINE_ORDER:
            if ed.pair(run, fixture, engine) is not None:
                pages.append(("pair", fixture, engine))
    return pages


def render_all(run_name: str, versions: dict) -> dict[Path, str]:
    run = ed.load_run(run_name)
    missing = {(f, e) for f in FIXTURE_ORDER for e in ENGINE_ORDER if ed.pair(run, f, e) is None}
    if missing != set(EXCLUDED):
        raise SystemExit(f"ERROR: the run leaves {sorted(missing)} unjudged but EXCLUDED explains {sorted(EXCLUDED)}")
    pages: dict[Path, str] = {}
    for lang in ("en", "ru"):
        for kind, *keys in expected_pages(run):
            if kind == "skill":
                path, page = skill_page(lang, run, versions)
            elif kind == "case":
                path, page = case_page(lang, run, keys[0], versions)
            else:
                path, page = pair_page(lang, run, keys[0], keys[1], versions)
            pages[path] = page
    return pages


def managed_dirs() -> list[Path]:
    """Directories whose index.html files this module owns, for orphan detection."""
    return [SITE / "eval-map", SITE / "ru" / "eval-map"]
