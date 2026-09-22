# Canon: tests, orders, failures, rubric

Read this when you need the exact test rather than the general idea.

## The seven rules and how to test each

| Rule | Substance | Practical test |
|---|---|---|
| Single top | One controlling idea answering the reader's question | Can it be said in one sentence with no "and also" |
| Top summarizes below | Each level is a generalization of its children, not a new theme | Remove the children — the parent loses its ground |
| Group is same-kind | Elements are one kind: reasons, steps, criteria, parts, options, risks | All branches fit under one plural noun |
| Group is ordered | An explicit ordering principle inside the group | You can say why this order and not another |
| MECE for analysis | No overlaps, no gaps in a decomposition | No duplicates, no obviously missing category |
| Intro is SCQ, in story form | Situation → Complication → Question → Answer, told as a story and dosed by what the reader already holds | After the intro it is clear which question the document closes, and no sentence in it needs proving |
| Structure is visible | Headings, numbering, key line, indentation mirror the hierarchy | One glance at the page shows the skeleton |

## The introduction: story form and its dose

The intro reminds, it does not inform. Everything in it the reader already knows or accepts
on sight; nothing in it is proved. The shape is a fairy tale: once upon a time (Situation),
then one day (Complication), so what do we do (Question), here is what (Answer).

Dose follows common ground, not habit. A reader who commissioned the document holds the
whole Situation — restating it spends their attention and reads as padding. A circulation
list that was not in the room holds none of it, and the Situation has to be supplied at the
level of the least-informed reader who must act.

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| Heading "Introduction", "Background", "Context" | the point it makes is not on the same level of abstraction as the key line | run the story as prose, no heading |
| Statement of purpose ("the purpose of this memo is to…") | names the topic, answers nothing, and is not a Situation either | delete; open with the Situation or the Answer |
| Long run-up ("as you know, last quarter we worked hard…") | Situation-shaped padding that never reaches a Complication | cover the sentence: if the Complication still bites, cut it |
| Situation the reader would argue with | it needs proof, so it is an argument, not common ground | move it below, as a support under the key line |
| SCQ labels or subheadings on a four-sentence note | apparatus wider than the document | answer first, the reasons in the same sentence |
| The Question never reaches the page | S and C delivered, the reader left to guess what is answered | one literal question, or a first line it is visibly the answer to |

## Order types

| Type | Use when | Key question |
|---|---|---|
| Time | Process, change, causal chain, stages | What comes first, second, third |
| Structure | The whole splits into parts: functions, regions, units, layers | What parts make up the whole |
| Ranking | Elements rank by size, risk, benefit, importance | What matters most, and why |
| Deduction | A chain of premises leading to a conclusion | If A and B hold, what follows |
| Induction | Independent observations rolling up into one conclusion | What do these facts have in common |

Time / structure / ranking govern how you group and present. Deduction / induction
govern how the argument unfolds. Both questions need an answer; they are not
alternatives to each other.

## MECE

- **ME — no overlaps.** Two branches must not claim the same content. If a fact fits
  two branches equally, the split is wrong.
- **CE — no gaps.** The branches together cover the relevant field. Name the field
  first, then check coverage against it.
- **No false grouping.** A tidy-looking list can reflect the author's association
  chain rather than the structure of the subject. Ask: is this how the subject is
  built, or how I happened to recall it?

## Failure catalogue

| Failure | What it looks like | Fix |
|---|---|---|
| Top does not answer | "A memo about project X" instead of "we recommend X because…" | Turn the topic into a question, then answer it |
| Mixed kinds | One group holds reasons, steps, numbers and risks | Split into same-kind classes |
| No order | Arguments sit in recall order | Assign time / structure / ranking / deduction / induction |
| Non-MECE split | Categories overlap or leave a hole | Reformulate branches, check the boundary |
| False deduction | Sounds like logic, but the middle premise is never proven | Recast as induction or comparison |
| Hidden structure | A good idea drowned in paragraphs | Headings, key line, numbering, slides |
| Missing intermediate conclusion | A fact jumps straight to a recommendation | Insert the conclusion the fact actually supports |
| Duplicate branches in disguise | Two elements that say the same thing are presented as different lines of action | Cover one branch: if the rest still answer the question, merge it. The real second branch is usually demoted among the observations |
| Right kind, wrong kind | The group is internally uniform but answers a different question than the reader's | Re-derive the kind from the question, then refill the group |

## Scoring rubric

Five axes, 0–2 each, maximum 10.

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| Top | No answer | Answer is vague | Precise and actionable |
| Same-kind groups | Full mix | Partly mixed | One kind per group |
| Order | Unexplainable | Formally present | Explicable and useful to the reader |
| MECE | Clear gaps and overlaps | Some doubtful spots | Overlaps and gaps minimal |
| Display | Solid prose | Partly visible | Hierarchy readable in seconds |

Bands: `0–3` not structured yet · `4–6` baseline workable · `7–8` good working level ·
`9–10` executive level.

Note: the source report's interpretation bands run to 12 points while its own five
axes cap at 10. This file uses the 10-point maximum and the bands above.

## Reviewer checklist

- Which question does this document answer?
- Can the top be challenged without challenging any single support?
- Is there a conclusion hiding below where it belongs?
- Does the text jump from fact to recommendation with nothing in between?
- Would a different order type serve the reader better?
