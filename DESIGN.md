---
name: Minto
description: Mustard and charcoal on warm paper; one square unit builds every picture on the page.
colors:
  paper: "#f8f1e3"
  sand: "#eee0c4"
  card: "#fffaf0"
  mustard: "#e9b100"
  mustard-hover: "#f2c22a"
  ink: "#0e0a06"
  coal: "#1f1915"
  coal-soft: "#332c27"
  ash: "#726759"
  field: "#8f8272"
  line: "#c6bcac"
  stone: "#d8d0c3"
  ok: "#5f6b2e"
  hot: "#cc572a"
  hot-text: "#943419"
typography:
  display:
    fontFamily: "Play, system-ui, sans-serif"
    fontSize: "clamp(38px, 6.2vw, 72px)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Play, system-ui, sans-serif"
    fontSize: "clamp(23px, 3.5vw, 38px)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Play, system-ui, sans-serif"
    fontSize: "clamp(17px, 1.4vw, 20px)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  lead:
    fontFamily: "Golos Text, system-ui, sans-serif"
    fontSize: "clamp(15px, 1.15vw, 17.5px)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Golos Text, system-ui, sans-serif"
    fontSize: "15.5px"
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: "Golos Text, system-ui, sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Golos Text, system-ui, sans-serif"
    fontSize: "12.5px"
    fontWeight: 500
    lineHeight: 1.55
  mono:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "12.5px"
    fontWeight: 400
    lineHeight: 1.55
  figure-xl:
    fontFamily: "Play, system-ui, sans-serif"
    fontSize: "clamp(38px, 6.4vw, 88px)"
    fontWeight: 700
    lineHeight: 0.92
    letterSpacing: "-0.03em"
    fontFeature: "tabular-nums"
  figure-lg:
    fontFamily: "Play, system-ui, sans-serif"
    fontSize: "34px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.02em"
    fontFeature: "tabular-nums"
  figure-md:
    fontFamily: "Play, system-ui, sans-serif"
    fontSize: "23px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.02em"
    fontFeature: "tabular-nums"
  figure-sm:
    fontFamily: "Play, system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.02em"
    fontFeature: "tabular-nums"
rounded:
  base: "4px"
spacing:
  unit: "11px"
  unit-gap: "4px"
  gap: "14px"
  pad: "18px"
  pad-lg: "22px"
  page-pad: "20px"
  section: "56px"
components:
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.base}"
    padding: "12px 20px"
    height: "44px"
  button-dark-hover:
    backgroundColor: "{colors.coal-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.base}"
    padding: "12px 20px"
    height: "44px"
  button-ghost-hover:
    backgroundColor: "{colors.sand}"
  button-primary:
    backgroundColor: "{colors.mustard}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.base}"
    padding: "12px 20px"
    height: "44px"
  button-primary-hover:
    backgroundColor: "{colors.mustard-hover}"
  card:
    backgroundColor: "{colors.card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.base}"
    padding: "22px"
  plate-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.base}"
    padding: "22px"
  panel-sand:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.coal-soft}"
    rounded: "{rounded.base}"
    padding: "22px"
  tag:
    backgroundColor: "transparent"
    textColor: "{colors.coal-soft}"
    typography: "{typography.label}"
    rounded: "{rounded.base}"
    padding: "3px 8px"
  tab-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.base}"
    padding: "6px 12px"
    height: "44px"
  unit:
    backgroundColor: "{colors.ink}"
    size: "13px"
  unit-answer:
    backgroundColor: "{colors.mustard}"
    size: "13px"
  unit-weak:
    backgroundColor: "{colors.line}"
    size: "13px"
---

# Design System: Minto

## Overview

**Creative North Star: "The Isotype Ledger"**

Minto is a printed-looking argument on warm paper. Everything on the page is made of one
material: a small solid square. Scattered, the squares are raw material; stacked into a
pyramid they are a settled argument; graduated into twenty ticks they are a benchmark rail.
The system never draws a picture of a product; it draws the thing the product does, in the
same ink the text is set in. Its density is editorial rather than marketing: long measures,
hairline rules instead of boxes, sections separated by air rather than by colour.

The world is Mirai at `data-tone="vivid"`, vendored whole. The page layer composes; it never
redecorates. Every surface on the site is one of four grounds — paper, card, sand, ink —
and the page never leaves paper as its base. There is no gradient field, no glass, no
shadow, and no second accent. One mustard exists, and the discipline around it is the
single loudest rule in this system.

The page carries exactly one authored animation and nothing that enters on scroll. The
material is meant to read as already there, the way a diagram in a book is already there.

**Key Characteristics:**
- One pictorial atom (the square unit) in five states carries every illustration.
- Warm paper ground throughout; the page never goes full-bleed and never inverts a section.
- One accent (mustard), spent on an answer and nothing else.
- Flat by construction: hairlines and tonal grounds, no shadows anywhere.
- Play 700 for headings and figures, Golos Text for prose, JetBrains Mono for commands and named data.
- One radius (4px) and one square form; circles belong to Mirai, not to the page.

## Colors

A warm, slightly yellowed paper palette with a charcoal near-black, one saturated mustard,
and a burnt orange reserved for measured loss.

### Primary
- **Mustard** (#e9b100): the answer, and only the answer. It appears on the apex unit of the
  hero pyramid, on the apex of case 03's result pyramid, and on the unit that opens the ink
  install plate. Mirai also spends it on `mr-button[data-variant="primary"]` and on the
  4px top edge of a stat card; the page layer itself never introduces a fourth mustard.

### Secondary
- **Burnt Orange / Hot** (#cc572a, text tone #943419): the loss channel. It carries the one
  measure that got worse — the `−10` figure, its rail band, its delta — and the `flaw` tag.
  It is a report, never a decoration or a call to action.

### Neutral
- **Paper** (#f8f1e3): the page ground, top to bottom, both locales and 404.
- **Card** (#fffaf0): lifted-by-tone surfaces — hero picture card, method stages, caveats, install cards.
- **Sand** (#eee0c4): the "before" ground — case source panels, source chips, inline `code` in prose, the unfilled part of a benchmark rail, and nav/ghost hover.
- **Ink** (#0e0a06): body text, the solid unit, the dark button, the fourth method stage, and the install prompt plate.
- **Coal Soft** (#332c27): running prose, and the mandatory tint for quiet text on sand.
- **Ash** (#726759): labels and captions on paper; on sand it is allowed for graphics only.
- **Field** (#8f8272): the control arm of every benchmark rail and its legend swatch.
- **Line** (#c6bcac): every hairline, and the `weak` unit.
- **Stone** (#d8d0c3): quiet text on ink grounds.
- **Olive / OK** (#5f6b2e): Mirai's positive delta tone; available, sparsely used.

### Named Rules
**The Two-Mustard Rule.** The markup carries three mustard units — the hero apex, case 03's
result apex, and the install prompt plate. Case 03 lives in a tab panel that JavaScript
hides by default, so a reader with JavaScript on sees two; a reader with it off sees three
down a very long scroll. Either way no viewport ever holds two. Mustard means "this is the
answer"; a second one in view would mean there are two answers.

**The Sand Contrast Rule.** `--mr-ash` clears 4.5:1 on paper but only 4.2:1 on sand. Text on
a sand ground steps to `--mr-coal-soft`; a *graphic* on sand may use ash, which clears the
3:1 bar — that is exactly why the case glyph's weak units repaint from line to ash inside
`.case__source`. Ash text on sand is banned.

**The Loss-Has-A-Colour Rule.** Hot is the page's honesty channel. If a number went the wrong
way it wears hot in the figure band, in the rail, and in the delta, and its element carries
`figure--down` / `metric--down`. Hot never appears where nothing was lost.

## Typography

**Display Font:** Play 700 (with system-ui, sans-serif)
**Body Font:** Golos Text (with system-ui, sans-serif)
**Label/Mono Font:** JetBrains Mono (with ui-monospace, monospace)

**Character:** Play's squared-off geometry is the letterform of the square unit; set at 700
with tight tracking it makes headings read as built rather than written. Golos Text keeps
the prose plain and highly legible in both Cyrillic and Latin, so the two locales set
identically. Mono appears only where the reader is meant to type or to trust a measurement.

### Hierarchy
- **Display** (Play 700, `clamp(38px, 6.2vw, 72px)`, 1.02): one per page — the hero H1 and the 404 H1.
- **Headline** (Play 700, `clamp(23px, 3.5vw, 38px)`, 1.02): section titles.
- **Title** (Play 700, `clamp(17px, 1.4vw, 20px)`, 1.1): card, stage and case headings.
- **Lead** (Golos Text 400, `clamp(15px, 1.15vw, 17.5px)`): the hero lede and section intros; also the lead metric name on a rail row.
- **Body** (Golos Text, 15.5px): running prose, capped at a 44em measure.
- **Small** (Golos Text, 13.5px): captions, case documents, caveats.
- **Label** (Golos Text 500, 12.5px, ash): figure captions, legends, tabs, provenance.
- **Mono** (JetBrains Mono, 12.5–15.5px): install commands, mode names, metric slugs.
- **Figures** — four Play 700 tabular steps, largest to smallest: headline band
  `clamp(38px, 6.4vw, 88px)`, rail delta and case score 34px, inline delta 23px, stage and
  brand numerals 19px.

### Named Rules
**The Broken-Word-Over-Hyphen Rule.** The display face never auto-hyphenates
(`hyphens: manual`); it may only break on `overflow-wrap: break-word` when a word genuinely
cannot fit. A headline that reads as three clean lines beats one that reads as prose with a
hyphen in it — and the RU locale's longer words are the reason the escape hatch exists.

**The Numbers-Are-Display Rule.** Every number a reader is meant to remember is set in Play
700 with tabular figures, not in body text. Prose states, figures count.

**The Figure Is Derived Rule.** No headline number is transcribed. `check_figures()` in
`scripts/check_benchmark_numbers.py` derives each one from `scores.json` (`cells_used`,
`len(engines)`, `site_metrics[...]["delta"]`) and fails the check if the visible text drifts
or if a negative delta is missing `figure--down`. A new large number needs a
`data-figure` source before it needs a size.

## Layout

One centred column, 1180px maximum, with page padding stepping 20 → 32 → 40px at 700px and
1080px. Sections are separated by a `--section` rhythm of 56 → 76 → 96px and, where a border
is needed, by a 1px `--mr-line` hairline rather than a container.

The page is single-column below 700px and pairs above it: the hero splits 0.86 / 1.14, cases
split evenly (or 0.85/1.15, 0.8/1.2 where the result needs room), install splits in two,
method stages go 1 → 2 → 4 across 700 and 1000px, and the figure band goes 2 → 4. Three
breakpoints do all the work: 700px (pairs), 900px (hero picture turns), 1080px (largest
type and padding).

The unit scale is itself a layout token: `--u` steps 11 → 12 → 13px with the viewport, and
`--u-step` (`--u` + `--u-gap`) is what scatter offsets are counted in, so a diagram stays in
proportion at every width.

### Named Rules
**The Solve-For-The-Column Rule.** A diagram is scaled for the column it sits in, not by a
generic size token. The hero picture is eight units wide at its widest, so it sets its own
`--u: clamp(13px, 1.7vw, 24px)` inside `.hero__card` instead of taking `data-size="lg"`.

**The Turn-When-It-Fits Rule.** The hero picture only becomes a row — scatter, arrow,
pyramid — once the column can hold eight units across, at 900px. Below that it stacks and
the arrow rotates 90°. A picture is never allowed to clip to stay horizontal.

**The One-Vertical Rule.** Repeated diagrams align on a track, not by eye. Each of the five
mode rows uses the same three-track grid (`7 units | auto | 4 units`), so every arrow and
every output edge sits on one vertical down the list.

## Elevation & Depth

There are no shadows in this system, anywhere, in any state. Depth is tonal and linear only:
four grounds (paper → sand → card → ink), 1px `--mr-line` hairlines, and a 1.5px ink border
that marks the one surface in a pair that carries the result. A card is distinguished from
the page by being lighter (`--mr-card` on paper) and outlined, never by being lifted.
Focus is the single exception to flatness and it belongs to Mirai: a two-ring
`0 0 0 2px paper, 0 0 0 4px ink` offset outline.

### Named Rules
**The Flat-Ground Rule.** If a surface needs to feel more important, change its ground or its
border weight. Never add a shadow, a glow, or a blur.

**The Border Says Which One Won Rule.** In a before/after pair the source half is sand with no
border and the result half is card with a 1.5px ink border. Weight, not colour, marks the
authored side.

## Shapes

One radius: 4px (`--mr-radius`), on every button, card, panel, tab, tag and code chip. There
is no second radius and no pill.

The square is the page's only drawn form. Units are hard squares with no radius at all, and
every illustration — scatter, pyramid, SCQ ladder, mode glyph, case glyph, brand mark,
benchmark rail tick, legend swatch — is an arrangement of them. The five states are the whole
vocabulary: solid ink (a stated idea), `--mr-line` (weak material), a 1.5px inset outline
(a named gap), a 45° 2px hatch (a defect the audit found), mustard (the answer). Rails and
legend swatches are the same square logic stretched: a 5%-pitch repeating stripe graduated in
twenty ticks, 13px for the control track and 26px for the skill track, with 7 / 13 / 13px
legend swatches echoing those heights.

Circles are not a page form. The only round object on the site is Mirai's `mr-sunmark` on
404, which is vendored.

### Named Rules
**The One Atom Rule.** A new illustration is built from `.unit` in its five states or it is
not built. No new glyph vocabulary, no icon set, no illustration style.

**The Arrow Is Not A Unit Rule.** The only non-square marks the page draws are the two inline
flow arrows (26×16 in the hero, 30×14 in the modes), stroked in `currentColor` at ash. They
are connectives, not decoration, and no other bespoke SVG exists in the page layer.

## Components

### Buttons
- **Shape:** 4px radius, 44px minimum control height (40px at `data-size="sm"`).
- **Dark (primary CTA):** ink ground, paper text; hover to coal-soft. Used for "Install the skill".
- **Ghost:** transparent with a line border, ink text; hover fills sand. Used for the secondary hero action, every copy button, and the 404 return.
- **Primary (mustard):** vendored by Mirai, available, currently unused on the page — mustard is spent on the answer unit instead.
- **Focus:** Mirai's two-ring offset outline; never a colour-only change.

### Chips and Tags
- **Style:** 12.5px label, coal-soft on transparent inside a line hairline, 4px radius.
- **Tones:** `hot` fills the burnt orange for a named defect; `flaw`/`stone` for neutral marks. Tags label evidence; they are never navigation.

### Cards and Panels
- **Card** (`--mr-card` + 1px line, 4px, 18–22px padding): hero picture, method stage, caveat, install column.
- **Sand panel** (no border): the "before" half of a case, source chips, the inline `code` chip.
- **Ink plate** (ink ground, paper text, stone for quiet text): the fourth method stage, and the install prompt at the foot of the page.
- **Shadow strategy:** none; see Elevation & Depth.

### Navigation
- Header is a masthead that scrolls away: brand mark (a three-row unit pyramid) plus wordmark, section links, and an EN / RU pair.
- Links are 13px 500 coal-soft, 44px tall, hover fills sand; the current section takes ink text and a 2px inset ink underline, set by an IntersectionObserver.
- **Case tabs:** ghost-shaped anchors that are real in-page links with JavaScript off (all five cases render as one page); JavaScript upgrades them to a tablist and the selected tab inverts to ink.

### The Unit and Its Compositions (signature)
- **Unit:** a `--u` square (11/12/13px) in five states. `data-shape="scatter"` offsets each row by `--x` steps of `--u-step`; `data-shape="pyramid"` centres rows.
- **Mode row:** mono command, a three-track turn (input glyph → arrow → output glyph), a 15.5px 600 result sentence. Five rows, one anatomy, hairline-separated.
- **Case glyph:** a 9px-unit miniature of the mode a case demonstrates, sitting above each half over a hairline, so the shape of the change reads before the text does.
- **Benchmark rail:** control track 13px in field, skill track 26px, the difference band in ink (or hot when the measure fell), all three as the same graduated stripe; the delta is set in Play at 23px, 34px from 700px.
- **Figure band:** four derived numbers at the top of Evidence, on the largest type step on the page, over and under a hairline; a negative figure takes `figure--down` and turns hot.

## Do's and Don'ts

### Do:
- **Do** build every new illustration from `.unit` in its five states, and scale it for its own column.
- **Do** keep mustard on the answer only: no viewport may show two mustard elements.
- **Do** consume `var(--mr-*)` for every colour, family, radius and stroke width; a literal in `styles.css` is a defect.
- **Do** re-vendor `mirai.css` when the design system changes — it is read-only, and no page rule may restyle an `mr-*` class or invent one.
- **Do** keep both locales line-for-line mirrors (867 lines, identical tag sequence per line); `check_benchmark_numbers.py` enforces it.
- **Do** step quiet text on sand to `--mr-coal-soft`, and let graphics on sand use `--mr-ash` for the 3:1 bar.
- **Do** derive every visible benchmark number from `scores.json` and let the check fail the build when it drifts.
- **Do** keep content and both install commands working with JavaScript off, and keep the page buildless — two stylesheets, one script, no toolchain.
- **Do** set every remembered number in Play 700 with tabular figures.

### Don't:
- **Don't** add a shadow, glow, or blur to anything, in any state.
- **Don't** introduce a second radius, a pill, or a page-drawn circle; 4px and the square are the whole form language.
- **Don't** animate anything in on scroll, and don't fade anything in. The page's one authored animation is `hero-gather`: the pyramid's rows start visible and merely displaced (an inline `--from` at 5px a step, staggered by an inline `--i` at 90ms), declared only inside `@media (prefers-reduced-motion: no-preference)`. Anything beyond that needs the same three properties: already visible, inside the reduced-motion guard, and bounded by the container's own padding.
- **Don't** put a second accent colour on the page, and don't spend hot on anything but a measured loss.
- **Don't** let a section go full-bleed or invert the page ground; paper runs top to bottom.
- **Don't** hide information the page exists to carry behind hover or a pointer.
- **Don't** add a bespoke icon or glyph set; the two flow arrows are the only non-square marks.
