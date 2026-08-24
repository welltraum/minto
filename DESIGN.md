# Minto visual system

Ported from the **AiCtoEditorial** design system: milky paper, graphite typography, one
terracotta. Depth comes from lines, underlays and layer order — never from shadows or
gradients. There is no blue anywhere.

## Direction

The page reads like an editorial working document rather than a product brochure. A single
warm paper field carries graphite text; terracotta appears only where the design marks a
direction, a chosen outcome, or a negative verdict. Every illustration on the page — the
before/after card, the five mode demos, the pyramid, the benchmark bars — is built from rules,
underlays and text. There are no photographs and no raster illustrations.

The physical scene is a desk with a printed memo and a red editing pencil: the answer moved to
the top, like items collected under it, and a few terracotta marks showing where the argument
was rebuilt.

## Color

Two tiers. The raw palette is the system's ink; the role tier is what every rule reads. Never
consume a raw token outside `:root`.

```css
--ac-paper: #fcf9f4;             --ac-surface
--ac-paper-light: #fffcf6;       --ac-surface-raised
--ac-ink: #27231f;               --ac-text
--ac-ink-soft: #6c625a;          --ac-text-soft
--ac-line: #8c8078;              --ac-border, --ac-rule
--ac-sand: #f2e7da;              --ac-surface-underlay
--ac-sand-light: #f6efe4;        --ac-surface-underlay-soft
--ac-terracotta: #b85e43;        --ac-accent          (fills, rules, borders — never text)
--ac-terracotta-text: #a04e36;   --ac-accent-text, --ac-accent-solid
--ac-terracotta-light: #f2e2d5;  --ac-accent-underlay
```

Measured contrast on paper: ink 14.85:1, ink-soft 5.66:1, terracotta-text 5.50:1, paper-light
on terracotta-solid 5.64:1, borders 3.65:1. All pass WCAG 2.2 AA for their role.

Rules the system enforces:

- Terracotta marks direction, a selected outcome, or a failed measure. It is not a second text
  color, and `--ac-terracotta` is never used for type — `--ac-terracotta-text` is.
- No shadows, no gradients, no blue.
- At most three levels of text inside one block.
- Corners top out at `--ac-radius-md` (10px). Borders are `--ac-stroke` (1.5px) or
  `--ac-stroke-strong` (2px), never combined with a shadow.

## Typography

Three self-hosted families under the SIL Open Font License, in `site/assets/fonts/`, each
shipped as `cyrillic` and `latin` subsets so both locales load the same weight of assets.

| Role | Family | Class |
|---|---|---|
| Display | Tektur 700 | `.ac-display` |
| Titles and body | Golos Text 400–700 | `.ac-title-text`, `.ac-body`, `doc-*` |
| Labels, table headers, code | JetBrains Mono 500–600 | `.ac-label`, `.install__cmd` |

Sizes derive from the system's four raw sizes (51 / 27 / 21 / 15px) multiplied by `--ac-scale`.
Every step carries a `max()` floor, so on small screens the display keeps shrinking while body
and label stop:

```css
--ac-size-display: max(calc(var(--ac-display-size) * var(--ac-scale)), 28px);
--ac-size-body:    max(calc(var(--ac-body-size) * var(--ac-scale)), 16px);
--ac-size-label:   max(calc(var(--ac-label-size) * var(--ac-scale)), 13px);
```

`--ac-scale` ramps 0.58 → 0.66 → 0.74 → 0.95 at 0 / 480 / 700 / 1080px. The top value is the
design's own; the ramp exists because a fixed 0.95 overflows 320px on a long Cyrillic display
word. Derived body steps are `--lg` 0.9, `--md` 0.85 and `--sm` 0.8 of the body size; do not add
a fifth step, and do not write raw `calc()` chains in page rules.

Body measure stays under 46em. `.ac-display` carries `overflow-wrap: anywhere` and `hyphens`
as a backstop for compound Russian words.

## Layout

- One container: `.page`, max 1180px of content plus `--ac-page-pad` gutters.
- Sections in order: header, hero, `#modes`, `#cases`, `#evidence`, `#install`, footer.
  The header is not sticky — it scrolls away like a document masthead.
- Breakpoints are plain viewport media queries at 1180 / 1000 / 700px, not container queries:
  there is exactly one container, and `container-type` would make `.page` a containing block for
  fixed descendants.
- Every grid child carries `min-width: 0`. A long `<code>` command or table cell blows out a
  grid track long before a heading does; this is what holds the no-overflow promise.
- **The page must not overflow horizontally at 320px or above.** The per-model table is the one
  element allowed to scroll, inside its own `.models__scroll`.
- Two namespaces in `styles.css`: `ac-*` is a faithful port of the design system — never invent
  an `ac-` name — and unprefixed classes are page compositions. An unprefixed rule may not carry
  a literal color, family, radius or stroke width; it consumes `var(--ac-*)` or it is wrong.

## Components

- Wordmark: the existing three-level pyramid SVG plus “Minto”. Not redrawn.
- Language switch: two ordinary links, active one exposed through `aria-current="page"`. Both
  locales use the same element for both languages — see Content rules.
- Mode grid: five static tiles, each ending in a visual demonstration of that mode's output
  pinned to the bottom of the tile. `viz` spans two columns on desktop.
- Case explorer: five real benchmark artifacts. Tabs are anchors that JavaScript upgrades into a
  keyboard-operated tablist; with JavaScript off, all five cases render as one long page and the
  tabs work as in-page links.
- Benchmark chart: percentage rows on a shared 0–100% track, control against skill, backed by a
  native `<details>` with the exact per-model scores. Bar geometry is an inline `--bar` custom
  property — never a per-value CSS class — so a new run touches markup only, and a regression
  renders as a shorter skill bar with no special-casing.
- Glyphs: outline only, `viewBox 0 0 24 24`, stroke 1.6, from the system's own set
  (`check`, `cross`, `warn`, `doc`, `scales`). Never an icon font, never a filled icon.
- Arrows: drawn as SVG (`.ac-arrow`), never as a character. `U+2192` sits outside the Latin
  subset these three families ship, so a literal arrow would fall back to a system font.
- Copy feedback: an `aria-live` status message, not a visual-only toast.
- Hit areas are at least 44px in the nav, footer, language switch, case tabs and copy buttons,
  and each copy button is named by the command it copies.

## Motion

The design ratifies one motion register: state transitions. `.ac-motion` carries 120ms
`cubic-bezier(0.22, 1, 0.36, 1)` transitions on background, border, text and outline color for
buttons and links. There is no entrance choreography, no scroll-driven reveal, no bar growth and
no connector drawing — the page is evidence, and evidence should not perform.

Content is fully visible without JavaScript. `prefers-reduced-motion: reduce` disables every
transition and animation and turns off smooth scrolling.

## Content rules

- English is canonical; Russian is a complete localized route. The two pages are line-for-line
  mirrors with identical tag skeletons; only text nodes and attribute values differ.
  `scripts/check_benchmark_numbers.py` compares line counts and the full ancestor path of every
  element, so a structural edit on one page alone fails the build. Corollary: the language
  switch and the case tabs use the same element on both pages, with selection carried by
  `aria-current` / `aria-selected`.
- Write `13%` with no space before the percent sign, including on the Russian page. The checker
  looks for the literal `"<value>%"` in the rendered row text.
- Never write a self-closing void tag (`<br/>`). The benchmark parser treats the extra end tag as
  a real close and silently truncates the row's text.
- Lead with the outcome, then explain mechanics.
- Benchmark figures come from `eval/runs/<run>/scores.json`, which `eval/aggregate.py` computes
  from the published verdicts. `scripts/check_benchmark_numbers.py` enforces the match in CI,
  against both the `data-*` attributes and the visible copy, in both locales. Never hand-edit a
  figure.
- Every measure that moved against the skill appears as its own row, at the same prominence as
  the ones that moved for it. Choosing rows by which direction they point is how a benchmark
  becomes marketing.
- Examples are real, cited artifacts from a committed run. The Russian page shows translations
  and says so on the page. Where a fixture's scenario is derived from a published example, the
  page does not imply the scenario is ours.
- No marketing superlatives, fake customer logos, invented testimonials, or unsupported
  efficiency claims.

## Regenerating og.png

`site/assets/og.svg` is the source; `og.png` is what the meta tags point at. librsvg ignores
`@font-face`, so render through a browser engine:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --window-size=1200,630 --force-device-scale-factor=1 --virtual-time-budget=4000 \
  --screenshot=site/assets/og.png http://localhost:8000/assets/og.svg
```

(serve `site/` first, so the relative font URLs resolve).
