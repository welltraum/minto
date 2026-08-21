## 1. Score table

Structural subscores are `(top, key-line composition, levels, order and kind)`; quality subscores are `(top, grouping, order, MECE, visible structure)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2, 1, 1, 2) | 7 (2, 2, 1, 0, 2) | `unacknowledged_source_loss` |
| out-02 | 6 (2, 1, 1, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts`, `unacknowledged_source_loss` |
| out-03 | 5 (2, 1, 1, 1) | 7 (2, 2, 1, 0, 2) | `invented_facts`, `unacknowledged_source_loss` |
| out-04 | 6 (2, 1, 1, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-05 | 6 (2, 1, 1, 2) | 8 (2, 2, 2, 0, 2) | `invented_facts` |
| out-06 | 1 (1, 0, 0, 0) | 5 (1, 2, 1, 0, 1) | `invented_facts`, `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-07 | 2 (2, 0, 0, 0) | 6 (2, 2, 1, 0, 1) | `unacknowledged_source_loss` |
| out-08 | 6 (2, 1, 1, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts` |

## 2. Decisive questions

| output | Q1: merged? | Q2: wages promoted? | Q3: first-level actions | Q4: observations below actions? | Q5: comparison/opinion omitted with note? | Q6: literal question? |
|---|---|---|---:|---|---|---|
| out-01 | No | No | 3 | Partly; staffing evidence is detached | Yes | No |
| out-02 | No | No | 3 | Partly; staffing and delay evidence is incomplete | Yes | Yes |
| out-03 | No | No | 2 | Yes, though under the wrong second action | Yes | No |
| out-04 | No | No | 2 | Yes, though wage evidence supports the wrong parent | Yes | No |
| out-05 | No | No | 3 | Partly; staffing evidence is in the introduction or omitted | Partly; opinion is omitted, comparison is promoted | No |
| out-06 | No | No | 0 | No; observations sit below reason headings | Yes | No |
| out-07 | No | No | 0 | No; the observations themselves form the first level | Yes | No |
| out-08 | No | No | 2 | Partly; staffing, delay, and overtime sit in a separate urgency section | Yes | No |

## 3. Output notes

- **out-01:** The program is clear and actionable, but it preserves three overlapping diagnostic/process branches while losing the below-market-pay cause and union pressure without noting them.
- **out-02:** The literal SCQ and hierarchy are strong, but the answer retains the duplicate method branch, omits the wage action, and turns an upside estimate into a guaranteed minimum.
- **out-03:** The two action sections carry their evidence cleanly, but below-market pay remains subordinate to method change and Kennedy’s role is strengthened beyond the source.
- **out-04:** The memo is crisp and visibly organized, but it assigns wage-related evidence to productivity improvement and invents a timetable.
- **out-05:** The action sequence is especially easy to follow, but automation and the necessity of peer benchmarking are invented while the actual wage lever is discarded.
- **out-06:** The output builds five evidence/reason branches rather than an action key line and introduces unsupported benchmark, case-study, automation, and savings claims.
- **out-07:** It opens with an answer, but the numbered level consists of observations while the actual actions are buried beneath them, and the pay cause disappears.
- **out-08:** The separate-test presentation is clean, but it explicitly preserves the overlap the fixture requires merging and overstates the potential saving.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Process simplification and method/productivity change survive as duplicate branches | Core loop §6, MECE hand-cover test | ignored | out-01–out-08 |
| Competitive wages are not promoted from the staffing observations | Core loop §6, “promote the real branch from the observations” | buried | out-01–out-08 |
| Evidence or reasons occupy the action level | Core loop §4, question-to-kind test | ignored | out-06, out-07 |
| Reader’s question is not written literally | Core loop §§1 and 3 | ignored | out-01, out-03–out-08 |
| Unsupported facts, certainty, roles, methods, or timings are introduced | Mode 3, “Invent nothing” | ignored | out-02–out-06, out-08 |
| Material source evidence disappears without an explicit omission note | Mode 3, source-preservation rule | ignored | out-01–out-03, out-06, out-07 |

## 5. Observation

The stronger outputs expose a concise action-led skeleton and place most evidence beneath visible parents; the weaker outputs either promote observations to the first level or overbuild a repeated evidence structure. None makes the decisive structural correction: merging the two process interventions and promoting competitive wages as the independent second action.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "02-ttv",
  "mode": "write",
  "outputs": [
    {
      "output": "out-01",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 5,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 6,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    }
  ]
}
```