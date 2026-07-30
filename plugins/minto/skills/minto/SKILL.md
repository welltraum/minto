---
name: minto
description: |
  Apply the Minto Pyramid Principle to business writing and thinking. Four modes:
  (1) intent — interview the user and turn a vague goal into reader question +
  one-sentence answer; (2) audit — check an existing text for pyramid logic and
  report the gaps; (3) write — draft or rewrite answer-first with SCQ intro and
  ordered, same-kind groups; (4) viz — annotate problems inline and build the
  pyramid (mermaid, optional HTML page). Use for memos, emails, decision notes,
  board papers, executive summaries, deck storylines, Slack updates. Triggers:
  pyramid principle, Minto, SCQ, MECE, answer-first, structure this text, check
  the logic, executive memo, and equivalent requests in Russian or other
  languages.
---

# Minto Pyramid Principle

You structure thinking before writing. One controlling idea on top, answering the
question the reader already has; below it, groups that are same-kind, ordered, and
free of overlaps and gaps; below those, the details.

**Output language.** These instructions are English; your output is not. Produce
pyramids, audits, drafts and diagrams in the language of the input text. With no
input text, use the language of the user's request. Never translate the user's
material unless asked.

## Router

Explicit argument wins: `intent` | `audit` | `write` | `viz`. Otherwise:

| Signal | Mode |
|---|---|
| No text yet, goal is vague ("we need to do something about X", "write something about Y") | `intent` |
| Text supplied + "check / what's wrong / is the logic sound / review" | `audit` |
| Text, notes or bullets + "write / rewrite / restructure / make a memo" | `write` |
| Structure exists (or was just produced) + "show / diagram / pyramid / picture" | `viz` |

Chaining: after `audit`, offer `write` in one line — do not rewrite unasked. After
`write`, append the compact mermaid pyramid by default. If the request mixes signals,
say which mode you picked in one sentence and go.

## Core loop (all modes)

1. **Topic → reader question.** Not "what is this about" but "what question must it
   close for this specific reader". Name the reader. When the source never states the
   question, build it from the complication — what changed or blocks for that reader — and
   write it down as one literal question before you draft anything. Everything below answers
   that written question, not the topic of the source.

   Then read that question back: does answering it settle whether the reader should act, or
   only whether the thing can be done? "Can we implement this without breaking our procedures"
   can be answered yes while the reader still has no reason to spend money, time or authority.
   A reader who is deciding asks what the thing is worth, not whether it fits.
2. **Provisional answer** in one sentence, no "and also". Test it by objection: if
   refuting it takes two separate objections, it is two tops, not one.
3. **SCQ intro, in story form.** Situation (what the reader already agrees with) →
   Complication (what changed, what blocks, what forces a choice) → Question → Answer.
   Tell it, do not label it: the reader recognizes the Situation, feels the turn, and
   reaches the Question already asking it. Nothing in the intro may need proving — a
   sentence the reader could argue with belongs in the body. The Question stays on the
   page: §8 hides your process, not the reader's question.

   **Dose the Situation by what the reader already holds**, with breadth of readership as
   the proxy — the wider the circle, the less is shared, the further back you start:

   | Reader | Situation |
   |---|---|
   | One person who asked for this, or was in the room | the request itself — one clause, or nothing |
   | A small group already briefed | one or two sentences of the fact they all hold |
   | A body or circulation list that was not in the room | the full story, pitched at the least-informed reader who must act |

   Then cut back: cover any Situation sentence — if the Complication still bites without
   it, it was a run-up, not a Situation. Anti-patterns: `references/rules.md`.
4. **Groups** — 3–4 first-level groups. Before filling them, name out loud the kind the
   question demands:

   | Reader's question | Kind of the elements |
   |---|---|
   | Why? Is this a good idea? | reasons — what the reader gains or loses, never how the thing works |
   | How? What do we do? | actions or changes — never the current state |
   | Of what? What is it made of? | parts of one whole |
   | Which one? | options, and separately the criteria for choosing |

   Write every element as the reader's payoff ("we will get X", "X will fall") or as an
   instruction ("do X"). Then the same-kind test: all elements fit one plural noun. A tidy
   list of the wrong kind passes that test and still fails the reader — the kind comes first.

   The commonest miss: writing mechanics while believing you wrote reasons. Test every
   element of a *reasons* group by rephrasing it as **"the system can X"** — if that
   reads naturally, it is mechanics, and the reason is what the reader gets out of it.
   "The file format is compatible" is mechanics; "we will finally have the data we lack"
   is a reason. In an *actions* group, an element that only states how things currently
   are is an observation, not an action.

   When the source describes only mechanics, the reasons are still there to be derived: for
   each mechanic ask what the reader ends up with once it works, put that on the first level,
   and hang the mechanic under it as its support. Stay inside the material — a mechanic whose
   payoff you cannot name from the source is a support, not a branch.
5. **Order** — pick one and be able to justify it: time, structure, ranking,
   deduction, induction. Name it, so the reader can see it.
6. **MECE** — no overlaps, no gaps, no false grouping. Duplication test: cover one
   first-level branch with your hand. If its supports still fit under the branches that
   remain, and the question is still answered without it, it was a duplicate — merge it.
   Then find the real second branch: it is usually sitting among the observations, demoted
   by the author.
7. **Show the structure** — headings, key line, numbering, indentation.
8. **Self-check, then deliver.** Run this pass over your own draft and fix what it catches.
   Do it silently: the fixes go into the text, the pass itself never appears in the output.
   1. Write out the reader's question and the kind it demands. If the reader is deciding
      whether to act, the question asks what the thing is worth. Every first-level element
      that is not of that kind — recast it as a payoff or an instruction.
   2. Cover each first-level branch in turn. If the rest still answer the question, that
      branch is a duplicate: merge it and promote the real branch from the observations.
   3. Check the top: one sentence, answers the written question, contains no gap marker.
   4. Check that each element rests on material from the source, and name the order type
      in one word.

Read `references/rules.md` when you need the exact test, the order-type table, the
failure catalogue, or the scoring rubric. Read `references/templates.md` when
rendering a concrete format.

## Mode 1 — intent

Turn a badly formed intention into a pyramid top.

Ask once using the host's structured user-input mechanism when one is available,
with up to four slots: who the reader is and what they will ask; the situation they
already accept; the complication; what decision or action you need from them. If
structured input is unavailable, ask the same questions together in one compact chat
message. Two rounds maximum. After that, stop asking — state assumptions explicitly
instead.

Deliver an intent card:

```
Reader:          <who, and why this person decides>
Reader question: <one question>
Answer (top):    <one sentence, without "and also">
Supports:        <3–4 same-kind groups, with the kind named>
Order:           <type + why this type>
Gaps:            [data needed: …]
Assumptions:     <what you assumed about the reader>
```

Never invent facts to fill the card. A missing branch is `[data needed: …]`, not a
plausible guess. End with one line: what the user should do next (`write` or supply
the missing data).

## Mode 2 — audit

Diagnose only. Do not deliver a rewritten text in this mode.

Run these six checks:

1. **Top** — does the first line answer the reader's question, or is it a topic label?
   Separate two diagnoses and never soften the first into the second: *there is no answer
   anywhere in the document* is heavier than *the answer exists but sits at the end*. When the
   answer is missing, name the kind of answer that belongs there — the reader's question
   decides it (see the table in the core loop): a reader asking what to change needs the
   changes, not the reasons change is needed.
2. **Vertical** — does each parent actually summarize its children, or is it a new
   theme dropped in from nowhere?
3. **Horizontal** — is each group same-kind (one plural noun)? Is the order explicable?
4. **MECE** — overlapping categories, missing category, false grouping. When the document
   describes a process or an object, check the description for completeness too: every
   stage present, every part named.
5. **Buried logic** — a conclusion sitting lower than it should; a jump from fact
   straight to recommendation with the intermediate conclusion missing; a deduction
   whose middle premise is never proven.
6. **Display** — can the skeleton be read at a glance, or is a good idea drowned in
   prose?

A finding is a structural defect, not a wish for more content. "Add the churn numbers" is
not a finding; a branch with no evidence under it is — mark it as a gap with `⊕`.

Deliver, in this order:

- the text with inline markers (legend once, above it — see **Markers**). Above
  roughly 1500 words, annotate only the passages that carry findings, quote each
  with enough context to locate it, and say that you annotated selectively;
- a findings table `location → violation → fix`, most severe first,
  **max 7 rows**; if more were found, state the number left out;
- the score: five axes × 0–2 with the band from `references/rules.md`;
- the three fixes that buy the most, each one line.

## Mode 3 — write / rewrite

Run the core loop, then render in the format the request implies — email, decision
memo, deck storyline, one-pager, chat message — using `references/templates.md`.

Rules that do not bend:

- Keep every fact from the source — keeping is not promoting. A fact that supports a
  first-level element sits under it; a fact that supports nothing above it goes to an
  appendix, or into the one line about what you dropped and why. The first level holds only
  elements that answer the reader's question. Restructuring is not summarizing.
- Invent nothing. No fabricated numbers, quotes, dates or evidence. Gaps are
  `[data needed: …]` — but never the top. The top always states the answer the material
  supports; if the material genuinely does not settle it, say so in one line under the
  top, and keep the answer above.
- 3–4 first-level groups. Not seven.
- Close with one line on what changed structurally — not a list of edits.

## Mode 4 — viz

Default output is markdown + mermaid, in chat, nothing written to disk:

- pyramid: `flowchart TD`, top → 3–4 groups → supports (see `references/templates.md`);
- SCQ ribbon: `flowchart LR`, Situation → Complication → Question → Answer;
- the annotated text with markers, when problems exist;
- a gap table for what is missing or overlapping.

Build an HTML page **only** when the user asks for something interactive, shareable,
or a page. Create a self-contained HTML file in the current workspace. Publish it
only when the current host exposes an appropriate site or artifact publishing
capability; otherwise return the local file. Use a stable favicon, support light and
dark themes, avoid external CDNs and remote images, and keep wide diagrams scrolling
inside their own container. Show the pyramid levels, highlight violations, and put
the findings in a side panel.

## Markers

Print the legend once, immediately above annotated text. Symbols are fixed; labels
follow the output language.

| Marker | Meaning |
|---|---|
| `▲` | top / answer |
| `●` | first-level group |
| `○` | supporting detail |
| `⚠` | violation (mixed kinds, unexplainable order, false grouping) |
| `↑` | conclusion buried lower than it belongs — promote it |
| `⇄` | wrong order type here |
| `⊗` | overlap (ME broken) |
| `⊕` | gap (CE broken) |
| `✂` | cut, or move to an appendix |

Markers go at the start of the line or inline in brackets after the offending
phrase. Keep the original wording intact — annotate, never silently edit.

## Limits — do not turn this into dogma

- **Discovery first, MECE later.** For research, product discovery, innovation or an
  ill-defined problem, diverge before converging. A premature perfect structure cuts
  off strong hypotheses. Offer a hypothesis map instead of a pyramid, and say why.
- **Three or four, not seven.** Working memory holds roughly four chunks — the "magic
  number seven" justification is outdated. Four honest groups beat three forced ones, and
  a false grouping is a worse defect than an uneven count.
- **Genre and culture adapt the directness.** A board paper, an academic note and a
  letter to an external partner can share the same top and differ in how bluntly it
  is stated, how much context comes first, and how fast you get to the ask.
