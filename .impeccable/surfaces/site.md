---
version: 1
slug: "site"
primary_target: "site"
related_targets: []
---

## Scope

The Minto landing page: English canonical at `site/index.html`, the complete Russian route at
`site/ru/index.html`, and `site/404.html`. Page composition lives in `site/assets/styles.css`;
`site/assets/mirai.css` is the vendored world and `site/assets/app.js` is progressive
enhancement only. Visitor mode: Persuade.

## Audience and job

Knowledge workers who already use Claude Code or Codex and arrive with a draft whose argument
is weak. They must understand in one screen that Minto reorders the thinking rather than
polishing the prose, and install it in two commands.

## Constraints

Built on the Mirai design system (`welltraum/mirai`), vendored as CSS and fonts. `mirai.css` is
read-only: it is changed only by re-vendoring, never edited in place, and no page rule restyles
an `mr-*` class or invents a new one. `styles.css` carries no literal colour, family, radius or
stroke width; it consumes `var(--mr-*)` or it is wrong. No build step. Content and both install
commands work with JavaScript off, and all five cases render as one long page without it. The
two locales stay line-for-line mirrors — 867 lines each, identical tag sequence per line —
enforced by `scripts/check_benchmark_numbers.py`. Every benchmark number on the page, including
the four in the headline band, is derived from `eval/runs/v1.7.0-final/scores.json` by the same
script; the measure that moved against the skill keeps equal prominence.

## Direction contract, as shipped

THESIS: one unit is one idea, and the page shows the same units rearranged rather than two
different texts. It refuses the category arrangement of a product screenshot over three
feature columns.

OWN-WORLD: Mirai at `data-tone="vivid"` — paper `#f8f1e3`, ink `#0e0a06`, one mustard
`#e9b100`, hairlines `#c6bcac`, radius 4 everywhere, Play 700 for headings and figures, Golos
Text for prose, JetBrains Mono for commands and measured data. The unit is a square in five
states, not four: ink idea, `--mr-line` weak material, outlined named gap, hatched defect,
mustard answer. Every illustration on the page is built from it.

STORY: the visitor sees disorder turn into a pyramid made of identical material, reads five
modes in one anatomy, sees five before/after cases, reads one benchmark that also reports its
loss, and installs in two commands.

FIRST VIEWPORT: paper. Left column carries the Play headline, one lede paragraph, an ink
primary button and a ghost second. Right column carries a card that stretches to the copy
column's height and holds the whole transformation in one row — scatter, arrow, pyramid, and
nothing else — with the case provenance beneath it. Below 900px the card stacks and the arrow
rotates. Three promises sit in a full-width band under both columns. Header scrolls away like
a masthead.

FORM: isotype, chosen by the owner from live-rendered variants rather than from a comp — every
direction was judged in the browser at real widths, and the shipped page is the one that was
picked, not an approximation of a picture of it.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the
verdict, DESIGN.md and its sidecar, and every shipping raster carrying its provenance.

## Signature device

The unit is the shared atom, and it now does four distinct jobs.

**The hero picture.** One row, no words: a scatter of weak units with one ink unit still in it,
an arrow, and a pyramid whose apex is mustard and whose last base unit is an outlined gap. The
card holds nothing else — no captions, no quotes, no bullets. Its scale is solved for the
column (`--u: clamp(13px, 1.7vw, 24px)`), not borrowed from a generic size token, because the
picture is eight units wide at its widest.

**The mode list.** Five rows of one anatomy: mono command, the turn, the result sentence. The
turn is a three-track grid (`7 units | auto | 4 units`), so every arrow and every output edge
sits on one vertical down the whole list. The SCQ ladder keeps a row of its own beneath them,
because it is the one thing the old mode cards carried that appears nowhere else.

**The case glyph.** Each half of each case opens with a miniature of the mode that case
demonstrates, over a hairline, so the shape of the change reads before a word of either text.
On the sand half the weak units step from `--mr-line` to `--mr-ash`: line reads at 1.4:1 on
sand, ash at 4.2:1, clear of the 3:1 bar for non-text graphics. Ash stays banned for text on
sand.

**The benchmark rail.** The same square logic stretched: twenty ticks of five points, control
track 13px in `--mr-field`, skill track 26px, the difference permanently drawn as a band in
`--mr-ink` (or `--mr-hot` where the measure fell), legend swatches at 7/13/13 echoing those
heights. Above the rails, a band of four large derived numbers answers before the rails
explain. This replaces the hover-revealed delta bracket the contract first named: that version
hid the page's central number behind a pointer, so no touch reader ever saw it, and information
a chart exists to carry should not be an interaction.

## Motion

Exactly one authored animation ships: `hero-gather`, declared only inside
`@media (prefers-reduced-motion: no-preference)`. The pyramid's rows start visible and merely
displaced — an inline `--from` at 5px a step, so the widest travel (three steps, 15px) stays
inside the card's narrowest inline padding and no row is ever clipped — and they gather,
staggered by an inline `--i` at 90ms. This is not a scroll animation: nothing on the page fades
in, nothing enters on scroll, everything is visible without JavaScript, and
`prefers-reduced-motion: reduce` stills every transition and the smooth scroll with it.

## Mustard budget

The markup carries three `data-state="answer"` units: the hero apex, case 03's result apex, and
the install prompt plate. Case 03 sits in a tab panel that `app.js` hides by default, so a
reader with JavaScript on sees two; a reader with it off sees three, spread down a very long
scroll. Both numbers are correct, and neither produces two mustards in one viewport — which is
the rule the count exists to protect.

## Recorded decisions, not oversights

- **The owner chose this build from live-rendered variants**, at real widths in a browser,
  rather than from a comp. Where the shipped page and an earlier drawing disagree, the shipped
  page is the decision.
- **The install section stays light.** No ink band behind it. The one inverted surface there is
  the prompt plate at the very foot; a dark install section would have made the page read as two
  documents.
- **The hero does not go full-bleed.** It sits inside the same 1180px column as everything else,
  so the page keeps one ground from masthead to footer.

## Accepted findings

Three findings are accepted and stay in the build: `cream-palette` (the warm paper ground is the
world, not a default), `repeating-stripes-gradient` (the rail's graduation is the measurement,
drawn from the unit), and `em-dash-overuse`. The detector returns those three and nothing else.

## Unresolved

None open. The benchmark stays pinned to `v1.7.0-final`; `check_benchmark_numbers.py` —
including `check_figures()` for the headline band — is what keeps the page honest when it moves.
