# Universal checks

The rubric scores how good an output is. These checks record what an output
actually did, as booleans and counts, so pass rates can be computed across every
fixture, mode, and engine without a language model doing arithmetic.

Four checks apply in all three modes. Four apply only where the mode makes them
meaningful, and are reported with their own smaller denominators.

Every check needs a mode-specific operational definition, or the same name means
different things in a `write` cell and a `viz` cell and the pass rate is
meaningless. The definitions below are the contract. Judge the output in front of
you against the definition, not against your sense of what the skill wanted.

## The four universal checks

### `first_level_kind_matches` — boolean

Are the first-level elements the kind of thing the reader's question demands —
reasons for a `Why?`, actions for a `How?`, parts for an `Of what?`, options for a
`Which one?` — and are they all the same kind as each other?

False when the elements are topics, mechanics, constraints, transition steps, or a
mix of kinds. In `audit`, false when findings mix structural defects with wishes
for more content. In `viz`, false when the first level mixes claims with topic
labels.

### `invented_facts` — boolean

Does the output assert any fact, number, name, date, quotation, causal claim, or
piece of evidence that the source material does not support? Converting tentative
evidence into certainty counts. `true` means the defect is present.

### `unacknowledged_source_loss` — boolean

Did material from the source disappear without an explicit note, beyond what the
fixture's gold permits as proportional omission? `true` means the defect is
present.

### `mode_respected` — boolean

Did the output deliver the artifact the mode requires?

- `write`: a finished text, not an analysis of how one might be written.
- `audit`: a diagnosis, not a rewritten document.
- `viz`: a diagram, with no file written and no HTML unless the task asked for one.

## The four conditional checks

These are recorded only where they apply. Each is reported against its own
denominator and never pooled with a check that means something different.

### `answer_first` — boolean, `write` and `viz`

Does the reader meet the answer before the support?

- `write`: the recommendation, decision, or answer appears in the first sentence
  of the delivered text. A subject line carrying it counts. A first sentence that
  states a topic, a situation, or what the document is about does not.
- `viz`: the top node of the diagram is a claim that answers the reader's
  question. A topic word, a document title, or a category label does not count.

Not applicable to `audit`. An audit delivers a diagnosis in a prescribed order that
begins with the annotated source text, so there is no first sentence in which an
answer could appear.

### `first_level_count` — integer, `write` and `viz`

How many elements sit at the first level below the top? In `write`, the elements of
the key line; in `viz`, the first-level nodes below the top node.

Count what the output presents as one level, not what you think it should have
grouped. If the output has no discernible level structure, record `0`.

Never report whether the count is within the limit. The aggregator derives that
from the integer, so the two can never disagree.

Not applicable to `audit`, where the first-level elements are findings and the
governing limit is a different number. Pooling the two would average counts that
are not the same quantity.

### `readers_question_literal` — boolean, `write` only

Is the reader's question written out somewhere in the delivered text?

Not applicable to `viz`, which delivers no prose to write it in, and not required
by `audit`, whose job is to diagnose someone else's text rather than to frame a
question of its own.

### `order_type_named` — boolean, `write` and `audit`

Does the output name its ordering principle — time, structure, ranking,
deduction, or induction — in so many words?

Not applicable where the fixture's gold calls for an output too short to carry a
stated ordering principle without over-structuring it. The applicability matrix
records that decision; do not re-derive it.

## Applicability matrix

One fenced block, read by `run-judge.sh` when it builds a judge prompt and by
`aggregate.py` when it computes rates. Both read the same bytes, so the two cannot
drift apart.

```json
{
  "schema_version": 1,
  "checks": {
    "first_level_kind_matches":   {"type": "bool", "modes": ["write", "audit", "viz"], "good": true},
    "invented_facts":             {"type": "bool", "modes": ["write", "audit", "viz"], "good": false},
    "unacknowledged_source_loss": {"type": "bool", "modes": ["write", "audit", "viz"], "good": false},
    "mode_respected":             {"type": "bool", "modes": ["write", "audit", "viz"], "good": true},
    "answer_first":               {"type": "bool", "modes": ["write", "viz"],          "good": true},
    "first_level_count":          {"type": "int",  "modes": ["write", "viz"], "limit": 4},
    "readers_question_literal":   {"type": "bool", "modes": ["write"],                 "good": true},
    "order_type_named":           {"type": "bool", "modes": ["write", "audit"],        "good": true}
  },
  "overrides": {
    "04-meeting-note": {"order_type_named": "na"}
  },
  "headline": [
    "answer_first",
    "first_level_count_within_limit",
    "first_level_kind_matches",
    "no_invented_facts",
    "no_unacknowledged_source_loss",
    "mode_respected"
  ]
}
```

`"good": false` tells the aggregator to report the inverted form, so every rate reads
higher-is-better. `first_level_count_within_limit` is derived from
`first_level_count <= 4` and is never asked of the judge.

The `headline` list names the rates fit to publish. It includes two conditional
checks, which is allowed as long as each is published with its own denominator and
never pooled with the others into one figure.

Expected denominators, per arm, for a run of E engines: 8E for the four universal
checks; 6E for `answer_first` and `first_level_count` (five `write` plus one `viz`);
5E for `readers_question_literal`; 6E for `order_type_named` (five `write` plus two
`audit`, minus the `04-meeting-note` override). If a conditional check ever reports
8E, the matrix is not being applied.

## What these checks are not

They do not replace the per-fixture decisive questions in `decisive-questions.md`.
Those are differently typed per fixture, deliberately not aggregable, and remain
the primary signal for a human reader. These checks are the aggregable subset, and
a good pass rate here is not evidence that a fixture's decisive questions were
answered well.

## Maintainer notes

Not sent to any judge. `eval/slice-checks.py` emits only the `### check` sections
and the resolved matrix, so anything under a `##` heading stays here — which is
what lets the notes below name fixtures freely while the judge-facing prose cannot.

The `04-meeting-note` override on `order_type_named` exists because that fixture's
gold requires an output no longer than its two-sentence source. Naming an order
type there is over-structuring, which the writing-quality rubric penalizes on its
fifth axis. A check that a correct output has to fail is not a measurement.

`answer_first` and `first_level_count` were universal in the first draft of this
file, and the v1.5.0-contract run showed why they cannot be. `SKILL.md`'s audit mode
prescribes a fixed delivery order that opens with the annotated source text and
caps findings at seven rows. So a fully compliant audit output has no answer in its
first sentence, and its first-level count is measured against seven rather than
four. Pooled across modes, both checks were quietly scoring skill-arm audit cells as
failures for obeying the skill — `answer_first` came out 18.8 points *against* the
skill, most of it from the two audit fixtures. Same principle as the override above,
found by running the pipeline rather than by reading it.

The lesson generalizes: before promoting a check to universal, read what `SKILL.md`
requires in each of the three modes, not just in `write`.

Adding an override is cheap; adding a check is not. A new check has to be defined
for all three modes before it can be called universal, and anything that cannot be
is a conditional check with its own denominator, permanently excluded from the
headline.

