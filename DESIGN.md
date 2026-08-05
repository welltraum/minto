# Minto visual system

## Direction

The site uses a live-argument register: a true white field, dark olive structural ink, a restrained terracotta annotation color, strong typographic scale, and diagrams that make hierarchy physical. The composition behaves like a working argument rather than a static report. Answers move to the top, supporting ideas collect beneath them, and a single structural line connects the page.

The physical scene is a bright project room before a decision meeting: a precise plan is pinned to a white wall, the answer is written largest, and a few terracotta corrections reveal how the logic was assembled. It avoids the usual developer-tool shorthand of dark terminals, glass panels, decorative grids, and endless feature cards.

## Color strategy

Committed. Olive carries the identity across roughly one third of the visual surface; terracotta appears only where an annotation, action, or measured change needs emphasis.

```css
--color-bg: oklch(1 0 0);
--color-surface: oklch(0.965 0.008 110);
--color-ink: oklch(0.18 0.025 110);
--color-primary: oklch(0.35 0.075 110);
--color-primary-deep: oklch(0.25 0.06 110);
--color-accent: oklch(0.50 0.16 35);
--color-muted: oklch(0.43 0.025 110);
--color-line: oklch(0.84 0.014 110);
```

All foreground/background combinations are verified in the finished page. White is used on saturated olive or terracotta fills.

## Typography

Use the Onest variable family, self-hosted under the SIL Open Font License. It is a geometric/humanist grotesque with strong small-size legibility and full Cyrillic support. A single family keeps English and Russian visually equivalent; hierarchy comes from weight, size, width, and composition rather than a decorative font pairing.

- Display: 760–850 weight, `clamp()` capped below 6rem, tracking no tighter than `-0.035em`.
- Section headings: 680–760 weight with balanced wrapping.
- Body: 400–500 weight, 1.55–1.7 line-height, maximum 70ch.
- Labels and code: Onest with tabular numbers; monospace is not used as a generic “technical” costume.

## Layout

- A 12-column desktop system collapses into a single reading column on small screens.
- A one-pixel argument spine connects the major white sections on desktop and disappears when it no longer helps the reading order.
- Sections use different visual forms: an asymmetric argument map, a dense installation plane, a document transformation, a mode explorer, an SCQ sequence, and a benchmark plot.
- Cards are reserved for real artifacts and controls. Other information uses rules, alignment, hierarchy, and whitespace.
- The header stays visible during the long page and indicates the section currently in view.
- Corners top out at 14px. Borders and wide shadows are never combined.
- The page must not overflow horizontally at 320px or above.

## Components

- Wordmark: text “Minto” plus a geometric three-level pyramid mark.
- Language switch: two ordinary links with the active language exposed through `aria-current`.
- Installation block: Codex and Claude Code steps are both visible; copy buttons enhance the static code.
- Pyramid diagram: one answer over three same-kind supports, implemented with semantic HTML and CSS. The answer arrives first, connectors draw, and supports settle in sequence.
- Document transformation: two real benchmark artifacts side by side — a source document and a model output produced from it. Static, with no switcher: the two texts have different shapes, and that contrast is the argument, so asking the reader to hold one shape in memory while looking at the other defeats the point. Quoted texts carry `lang` when it differs from the page.
- Mode explorer: `intent`, `audit`, `write`, and `viz` operate on one example so their differences are visible. Links remain useful without JavaScript and become keyboard-operated tabs when enhanced.
- SCQ ribbon: a four-part ordered flow whose final answer receives the strongest color.
- Benchmark: percentage rows on a shared 0–100% track, control against skill, backed by a native disclosure containing the exact scores. Bar geometry is an inline `--bar` custom property, never a per-value CSS class, so a new benchmark run touches markup only. A regression renders as a shorter skill bar with no special-casing.
- Copy feedback: an `aria-live` status message, not a visual-only toast.

## Motion

The first-load choreography brings in the answer, draws the pyramid connectors, and settles the three supports. Mode changes are immediate so the explorer feels like a tool rather than a carousel. The example section does not animate: it is evidence, and evidence should not perform.

Content is visible without JavaScript and before animation starts. Hover and focus transitions use an ease-out-quint curve and affect only color, opacity, and transforms. `prefers-reduced-motion: reduce` disables drawing and movement.

## Content rules

- English is canonical; Russian is a complete localized route. The two pages are line-for-line mirrors with identical tag skeletons and identical `data-*` values; only text nodes differ.
- Lead with the outcome, then explain mechanics.
- Benchmark figures come from `eval/runs/<run>/scores.json`, which `eval/aggregate.py` computes from the published verdicts. `scripts/check_benchmark_numbers.py` enforces the match in CI, against both the `data-*` attributes and the visible copy, in both locales. Never hand-edit a figure.
- Every measure that moved against the skill appears as its own row, at the same prominence as the ones that moved for it. Choosing rows by which direction they point is how a benchmark becomes marketing.
- Examples are real, cited artifacts from a committed run, quoted verbatim and linked to their source. Where a fixture's scenario is derived from a published example, the page does not imply the scenario is ours.
- No marketing superlatives, fake customer logos, invented testimonials, or unsupported efficiency claims.
