# Minto visual system

## Direction

The site uses an architectural-poster register: a true white field, dark olive structural ink, a restrained terracotta annotation color, strong typographic scale, and diagrams that make hierarchy physical. It avoids the usual developer-tool shorthand of dark terminals, glass panels, decorative grids, and endless feature cards.

The physical scene is a bright project room before a decision meeting: a precise plan is pinned to a white wall, the answer is written largest, and a few terracotta corrections reveal how the logic was assembled.

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
- Sections alternate between dense answer/support groupings and wide structural diagrams.
- Cards are reserved for installation commands; other information uses rules, alignment, hierarchy, and whitespace.
- Corners top out at 14px. Borders and wide shadows are never combined.
- The page must not overflow horizontally at 320px or above.

## Components

- Wordmark: text “Minto” plus a geometric three-level pyramid mark.
- Language switch: two ordinary links with the active language exposed through `aria-current`.
- Installation block: Codex and Claude Code steps are both visible; copy buttons enhance the static code.
- Pyramid diagram: one answer over three same-kind supports, implemented with semantic HTML and CSS.
- SCQ ribbon: a four-part ordered flow whose final answer receives the strongest color.
- Benchmark: a compact comparison table with one honest headline delta and an explicit caveat.
- Copy feedback: an `aria-live` status message, not a visual-only toast.

## Motion

One first-load choreography draws the pyramid connectors and brings the answer into focus. Content is visible before animation starts. Hover and focus transitions use an ease-out-quint curve and affect only color, opacity, and transforms. `prefers-reduced-motion: reduce` disables drawing and movement.

## Content rules

- English is canonical; Russian is a complete localized route.
- Lead with the outcome, then explain mechanics.
- Benchmark figures must match `eval/report-v1.5.0.md`.
- Examples are original and clearly illustrative.
- No marketing superlatives, fake customer logos, invented testimonials, or unsupported efficiency claims.
