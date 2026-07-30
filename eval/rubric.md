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

Record each separately and set the corresponding quality axis to zero:

- invented facts, numbers, names, dates, quotations, or evidence;
- loss of source material without an explicit note, except where a fixture's
  gold permits proportional omission;
- more than four first-level elements;
- output in the wrong language;
- `audit` returns a rewritten document instead of diagnosis;
- `write` returns analysis without a finished text;
- `viz` returns no diagram;
- `viz` writes a file or returns HTML without an explicit request.

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
