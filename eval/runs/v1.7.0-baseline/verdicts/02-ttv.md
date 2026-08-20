## 1. Score table

Structural sub-scores are `(top, key line, levels, order/kind)`; quality sub-scores are `(top, grouping, order, MECE, display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (1, 1, 1, 1) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-02 | 7 (2, 1, 2, 2) | 9 (2, 2, 2, 1, 2) | `invented_facts` |
| out-03 | 3 (1, 1, 0, 1) | 6 (2, 2, 1, 0, 1) | `invented_facts`, `unacknowledged_source_loss` |
| out-04 | 3 (1, 1, 0, 1) | 7 (2, 2, 1, 0, 2) | `invented_facts`, `unacknowledged_source_loss` |
| out-05 | 4 (1, 1, 1, 1) | 6 (1, 2, 1, 0, 2) | `invented_facts`, `unacknowledged_source_loss` |
| out-06 | 3 (1, 1, 0, 1) | 7 (2, 2, 1, 0, 2) | `unacknowledged_source_loss` |
| out-07 | 1 (1, 0, 0, 0) | 6 (2, 2, 1, 0, 1) | `invented_facts` |
| out-08 | 4 (1, 1, 1, 1) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-09 | 4 (1, 1, 1, 1) | 6 (1, 2, 1, 0, 2) | `invented_facts` |
| out-10 | 2 (1, 0, 0, 1) | 7 (2, 2, 1, 0, 2) | `invented_facts` |
| out-11 | 1 (1, 0, 0, 0) | 6 (2, 2, 1, 0, 1) | `invented_facts`, `unacknowledged_source_loss` |
| out-12 | 5 (1, 1, 2, 1) | 7 (2, 2, 1, 0, 2) | None |
| out-13 | 6 (1, 1, 2, 2) | 9 (2, 2, 2, 1, 2) | `invented_facts` |
| out-14 | 3 (1, 1, 0, 1) | 7 (2, 2, 1, 0, 2) | `invented_facts` |

## 2. Decisive questions

| output | Process and method merged? | Wages promoted? | First-level actions | Observations below actions? | Irrelevant material explicitly omitted? | Literal reader question? |
|---|---|---|---:|---|---|---|
| out-01 | No | No | 2 | Yes | Yes | No |
| out-02 | No | Yes | 3 | Yes | Yes | No |
| out-03 | No | No | 2 | No | No | No |
| out-04 | No | No | 2 | No | Yes | No |
| out-05 | No | No | 2 | Yes | Yes | No |
| out-06 | No | No | 2 | No | No | No |
| out-07 | No | No | 0 | No | Yes | Yes |
| out-08 | No | No | 2 | No | No | No |
| out-09 | No | No | 2 | Yes | Yes | No |
| out-10 | No | No | 3 | No | No | No |
| out-11 | No | No | 0 | No | Yes | No |
| out-12 | No | No | 3 | Yes | No | No |
| out-13 | No | No | 3 | Yes | Yes | No |
| out-14 | No | No | 2 | No | No | No |

## 3. Output notes

- **out-01:** The recommendation is highly visible, but the methods study duplicates process simplification while staffing evidence is used to support an invented “root cause.”
- **out-02:** This is the only output to promote pay to the first level, though it leaves the two overlapping process interventions separate and adds unsupported causal claims.
- **out-03:** The clean prose loses the actual pay-and-capacity branch and incorrectly attributes support for investigation to all three named interviewees.
- **out-04:** The two-action display is clear, but staffing evidence sits above the actions and the memo invents owners, test durations, and replacement scope.
- **out-05:** Relevant observations sit under visible actions, but the pay mechanism disappears and method change is asserted to resolve capacity constraints.
- **out-06:** It opens directly with an actionable answer, but its “root cause” section promotes evidence above the actions and the omitted-material note misses management disagreement.
- **out-07:** The literal SCQ is present, but the displayed first level consists of reasons rather than actions and the operational plan introduces unsupported timings, roles, and savings claims.
- **out-08:** The two levers are easy to follow, but capacity pressure is treated only as urgency and the memo asserts unsupported necessity and causal effects.
- **out-09:** Evidence is largely subordinated to actions, but the answer is delayed and the memo adds a fabricated date and unsupported management causality.
- **out-10:** External benchmarking becomes an unnecessary third branch while the wage-and-staffing lever is explicitly removed.
- **out-11:** The visible first level is a list of reasons rather than recommendations, and several claimed benchmarks, outcomes, and implementation details are fabricated.
- **out-12:** Evidence is consistently placed under visible action-like branches, but the third branch merely measures labour pressure instead of acting on below-market wages.
- **out-13:** The action hierarchy and payoff order are unusually clear, but “address capacity” never becomes the specific wage action and the top overstates the attainable saving.
- **out-14:** The memo is readable and answer-led, but it removes the hidden wage branch while retaining irrelevant comparison and opinion material as supporting information.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Process simplification and method change remain duplicate branches | Core loop §6, “MECE” and “Duplicate branches in disguise” | ignored | out-01–out-14 |
| Below-market wages are not promoted as the real second action | Core loop §6, “promote the real branch from the observations” | ignored | out-01, out-03–out-14 |
| Reader question is not written literally | Core loop §§1 and 3, “write it down as one literal question” | ignored | out-01–out-06, out-08–out-14 |
| Ordering principle is not named | Core loop §5, “Name it” | ignored | out-01, out-03–out-12, out-14 |
| Unsupported certainty, evidence, dates, roles, or causal claims are introduced | Mode 3, “Invent nothing” | ignored | out-01–out-05, out-07–out-11, out-13–out-14 |
| Useful source material disappears without being identified in the omission note | Mode 3, source-preservation rule | missing | out-03–out-06, out-11 |

## 5. Observation

The stronger outputs expose a concise action hierarchy, keep operational observations beneath those actions, and make the ordering legible; the weaker outputs either promote reasons and background to the first level or remove the staffing chain entirely. Even the strongest outputs preserve the source’s overlapping process/method split, and only one elevates pay as a separate action.

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
        "total": 4,
        "top": 1,
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
      "hard_failures": ["invented_facts"],
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
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": true,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
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
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
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
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
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
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": false,
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
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
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
      "hard_failures": ["unacknowledged_source_loss"],
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
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
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
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
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
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
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
      "hard_failures": ["invented_facts"],
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
      "output": "out-11",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
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
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
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
        "top": 1,
        "key_line_composition": 1,
        "levels": 2,
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
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
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
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 1,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": true,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
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
      "hard_failures": ["invented_facts"],
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
    }
  ]
}
```