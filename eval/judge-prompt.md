# Judge instructions

Evaluate all blinded outputs for one fixture. Every engine produced two arms:
one with the skill and one control. Do not infer engine or arm identities.

Read the supplied fixture, gold structure, rubric, decisive questions, frozen
skill, rules, and outputs. They are the complete evidence. Do not use outside
knowledge to reconstruct hidden source text.

Return one Markdown report with:

## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|

Show the four structural sub-scores in parentheses after each total.

Report the axes as you judge them. Do not deduct for hard failures — list them in
the last column and leave the totals alone. The penalty is applied downstream from
a fixed map, so that it lands identically in every cell.

## 2. Decisive questions

Answer every supplied decisive question for every output, concisely.

## 3. Output notes

One sentence per output, two at most, covering whichever of top, key line, levels,
invented or lost material, and mode compliance actually separates it from the
others. The numbers belong in section 6, so this section does not need to restate
them.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|

Use only `vague`, `buried`, `missing`, or `ignored` as causes.

## 5. Observation

State what structurally separates stronger from weaker outputs, without
guessing engines or arms.

## 6. Machine-readable scores

End the report with exactly one fenced `json` block, matching the schema below.
Nothing may follow it. It repeats decisions already made in sections 1 and 2; if
the two disagree, this block is authoritative and section 1 is wrong.

Include one entry per supplied output, in ascending `out-NN` order — no more, no
fewer. Use `"na"` for a check the supplied applicability matrix marks not
applicable for this fixture. Never `null`, `"n/a"`, `"unknown"`, or an omitted key.

```json
{
  "schema_version": 1,
  "fixture": "04-meeting-note",
  "mode": "write",
  "outputs": [
    {
      "output": "out-01",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    }
  ]
}
```

Rules the block must satisfy:

- every axis is the integer 0, 1, or 2;
- `structure.total` equals the sum of its four axes; `quality.total` equals the sum
  of its five;
- `hard_failures` uses only the tokens from the rubric's hard-failure table, with
  no duplicates;
- `checks.invented_facts` is true if and only if `invented_facts` is in
  `hard_failures`, and the same holds for `unacknowledged_source_loss`;
- `checks.first_level_count` exceeds 4 if and only if `more_than_four_first_level`
  is in `hard_failures`;
- when `completed` is false, `structure` and `quality` are `null` and `checks` is
  an empty object.

These restatements are deliberate. They are the only available cross-check against
a judge that drifts, and they cost nothing, because every one of them repeats a
decision already made.

An empty or truncated output is `not completed` and receives no score. Do not
reward verbosity. If an output improves on a disputable gold assumption, note
the improvement and do not penalize it.
