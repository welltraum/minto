## 1. Score table

Structural sub-scores are `(top, key-line composition, levels, order and kind)`; quality sub-scores are `(top, same-kind grouping, explainable order, MECE, visible structure)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 5 (2, 1, 0, 2) | 8 (2, 2, 2, 0, 2) | `unacknowledged_source_loss` |
| out-02 | 5 (2, 1, 0, 2) | 7 (2, 2, 2, 0, 1) | `unacknowledged_source_loss` |
| out-03 | 4 (2, 1, 0, 1) | 6 (2, 1, 1, 0, 2) | `invented_facts` |
| out-04 | 6 (2, 1, 1, 2) | 7 (2, 2, 1, 0, 2) | — |
| out-05 | 6 (2, 1, 1, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-06 | 5 (2, 1, 0, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-07 | 6 (2, 1, 1, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-08 | 6 (2, 1, 1, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-09 | 5 (2, 1, 0, 2) | 8 (2, 2, 2, 0, 2) | `invented_facts` |
| out-10 | 5 (2, 1, 0, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts`, `unacknowledged_source_loss` |
| out-11 | 4 (2, 1, 0, 1) | 4 (2, 0, 1, 0, 1) | `invented_facts`, `unacknowledged_source_loss` |
| out-12 | 5 (2, 1, 0, 2) | 8 (2, 2, 2, 0, 2) | `unacknowledged_source_loss` |
| out-13 | 5 (2, 1, 0, 2) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-14 | 7 (2, 1, 2, 2) | 8 (2, 2, 1, 1, 2) | — |

## 2. Decisive questions

| output | Q1: merged? | Q2: wages first-level? | Q3: first-level actions | Q4: observations below actions? | Q5: comparison/opinion omitted and noted? | Q6: literal question? |
|---|---|---|---:|---|---|---|
| out-01 | No | No | 3 | Yes, but staffing is unattached context | No | No |
| out-02 | No | No | 3 | No; staffing is omitted | No | Yes |
| out-03 | No | No | 2 | No; staffing becomes a separate reason branch | No | No |
| out-04 | No | No | 2 | Yes, but staffing is only urgency context | Yes | No |
| out-05 | No | No | 2 | Yes, though staffing is attached to the methods study | Yes | No |
| out-06 | No | No | 2 | No; staffing appears before the actions | Yes | No |
| out-07 | No | No | 2 | Yes, though staffing supports the wrong action | Yes | No |
| out-08 | No | No | 2 | Yes, as undifferentiated supporting context | Yes | No |
| out-09 | No | No | 3 | Yes, though staffing is attached to productivity | No | No |
| out-10 | No | No | 2 | No; staffing is in the complication | No | No |
| out-11 | No | No | 0 | No; observations are promoted as first-level arguments | Yes | No |
| out-12 | No | No | 2 | No; the staffing chain is omitted | No | No |
| out-13 | No | No | 2 | No; the staffing chain is omitted | Yes | No |
| out-14 | No | Yes, as a capacity-and-pay action | 3 | Yes | No; managerial disagreement remains in the text | No |

## 3. Output notes

- **out-01:** Clear and visibly ordered, but it promotes external comparison while losing the low-pay and hiring evidence that should reveal the missing wage action.
- **out-02:** It is the only output to state the reader’s question literally, but it retains benchmarking as an action and omits the staffing branch.
- **out-03:** Staffing is promoted as a separate “why now” section, and the printer-mix rationale for rejecting comparison is invented.
- **out-04:** The two workstreams are concise and well supported, but the wage chain remains urgency context rather than becoming an action.
- **out-05:** Staffing evidence is buried under the methods study, while identical checks are asserted to waste capacity without source support.
- **out-06:** The wage evidence is placed in the complication, and the text turns the untested possibility of fewer checks into a requirement.
- **out-07:** The two branches are easy to scan, but the wage lever disappears and tentative benefits are expressed too certainly.
- **out-08:** Useful staffing facts survive only as context explicitly denied the status of a solution, while “at least 10%” reverses the source’s upper-bound estimate.
- **out-09:** A third validation branch duplicates the pilot and promotes weak peer comparison, alongside an invented outdated-workflow diagnosis.
- **out-10:** The compact SCQ-style opening is effective, but the literal question is absent and the claim of minimal risk is unsupported.
- **out-11:** Extensive invented estimates, timing, owners, automation examples, and rollout mechanics overwhelm a mixed first level and still miss the wage action.
- **out-12:** The concise parallel initiatives are visibly presented, but the labor evidence and managerial disagreement are removed without a complete acknowledgment.
- **out-13:** The answer follows a contextual opening, while the memo incorrectly separates staffing from composing-cost reduction.
- **out-14:** This is the only output to promote pay and capacity to an action with its causal evidence beneath it, although it still leaves simplification and method change as overlapping branches.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Process simplification and method/productivity change remain duplicate branches | Core loop §6, MECE duplication test | ignored | out-01–out-14 |
| The wage action remains buried in observations or disappears | Core loop §§4 and 6, promotion of the real branch from observations | ignored | out-01–out-13 |
| Staffing evidence is placed in context, attached to the methods branch, or omitted | Core loop, vertical support and levels | buried | out-01–out-13 |
| The literal reader question is absent | Core loop §§1 and 3 | ignored | out-01, out-03–out-14 |
| Unsupported certainty, causal claims, or implementation details are introduced | Mode 3, “Invent nothing” | ignored | out-03, out-05–out-11, out-13 |
| Omitted source material is not fully acknowledged | Mode 3, preservation and dropped-fact rule | ignored | out-01, out-02, out-10–out-12 |
| No output names one of the prescribed order types | Core loop §5, obscured by Mode 3’s clean-text guidance | buried | out-01–out-14 |

## 5. Observation

The strongest output is distinguished by promoting the low-pay → staffing shortage → delay and overtime chain into a first-level action and nesting the evidence beneath it. The weaker outputs consistently preserve the source’s overlapping simplification and methods-study branches, leaving the genuine wage lever buried, misplaced, or omitted.

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
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
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
        "total": 4,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
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
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
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
    },
    {
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
    },
    {
      "output": "out-07",
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
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
        "answer_first": true,
        "first_level_count": 3,
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
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-11",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 4,
        "top": 2,
        "same_kind_grouping": 0,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
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
      "output": "out-12",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
    },
    {
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
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