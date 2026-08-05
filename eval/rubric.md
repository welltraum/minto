# Evaluation rubric

## Structural match: 0-8

Score four axes from 0 to 2:

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| Top | absent, topic, or wrong answer | answer present but buried or incomplete | one clear answer to the reader's question at the top |
| Key-line composition | wrong kind or unsupported | mixed kind or one major miss | grounded same-kind elements matching the gold |
| Levels | evidence promoted or major evidence lost | mostly correct with one material level error | details consistently support the right parent |
| Order and kind | neither coherent nor identifiable | kind or order is implicit but workable | kind is correct and order is clear or explained |

Judge semantic equivalence, not literal wording.

## Writing quality: 0-10

Score the five skill axes from 0 to 2:

1. Top.
2. Same-kind grouping.
3. Explainable order.
4. MECE.
5. Visible, proportionate structure.

## Hard failures

Record each one that applies, using the machine token in the first column. Score
the quality axes as you actually judge them and **do not apply the penalty
yourself** — `eval/aggregate.py` applies the map below, so the deduction is
identical in every cell instead of depending on which failures a judge happened
to weigh:

| Token | Failure | Zeroes quality axis |
|---|---|---|
| `invented_facts` | invented facts, numbers, names, dates, quotations, or evidence | 4. MECE |
| `unacknowledged_source_loss` | loss of source material without an explicit note, except where a fixture's gold permits proportional omission | 4. MECE |
| `more_than_four_first_level` | more than four first-level elements | 5. Visible, proportionate structure |
| `wrong_language` | output in the wrong language | 5. Visible, proportionate structure |
| `audit_returned_rewrite` | `audit` returns a rewritten document instead of diagnosis | 1. Top |
| `write_returned_analysis` | `write` returns analysis without a finished text | 1. Top |
| `viz_no_diagram` | `viz` returns no diagram | 1. Top |
| `viz_unrequested_file` | `viz` writes a file or returns HTML without an explicit request | 5. Visible, proportionate structure |

Two failures mapping to the same axis zero it once; the penalty is not cumulative.

The map is a judgement call, not a derivation — the five quality axes were not
designed to absorb these eight failures. It is pinned here so that every run
applies the same one, and `scores.json` records `rubric_penalty_version`. Changing
the map invalidates comparison with earlier runs.

Reports carry both `quality_raw` (the axes as judged) and `quality_penalized`
(after the map), because the two answer different questions: how well the output is
structured, and how much of that survives its factual defects.

## Audit-specific checks

- Count gold defects found, distinguishing critical defects.
- Count false positives.
- Check the seven-finding limit, five-axis score, and three highest-value fixes.

## Attribution

For every recurring miss, identify:

- the relevant skill section;
- one cause: `vague`, `buried`, `missing`, or `ignored`;
- the number of affected outputs.

Do not include an unattributed complaint. Do not reward length.
