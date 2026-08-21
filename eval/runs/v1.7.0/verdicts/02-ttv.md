## 1. Score table

Parentheses show structural axes as `(top, key line, levels, order/kind)` and quality axes as `(top, grouping, order, MECE, display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (1,1,1,1) | 5 (1,2,1,0,1) | `unacknowledged_source_loss` |
| out-02 | 5 (1,1,1,2) | 8 (2,2,2,0,2) | `invented_facts` |
| out-03 | 1 (1,0,0,0) | 4 (2,0,1,0,1) | `invented_facts`, `more_than_four_first_level` |
| out-04 | 2 (1,0,0,1) | 6 (2,1,1,0,2) | `unacknowledged_source_loss` |
| out-05 | 4 (1,1,1,1) | 6 (2,2,1,0,1) | `invented_facts`, `unacknowledged_source_loss` |
| out-06 | 3 (1,1,0,1) | 6 (2,2,1,0,1) | `invented_facts` |
| out-07 | 4 (1,1,1,1) | 6 (2,2,1,0,1) | `invented_facts` |
| out-08 | 4 (1,1,1,1) | 6 (1,2,1,0,2) | `invented_facts`, `unacknowledged_source_loss` |
| out-09 | 4 (1,1,1,1) | 7 (2,2,1,0,2) | `invented_facts`, `unacknowledged_source_loss` |
| out-10 | 4 (1,1,1,1) | 7 (2,2,1,0,2) | `invented_facts` |
| out-11 | 3 (1,1,0,1) | 7 (2,2,1,0,2) | `invented_facts` |
| out-12 | 2 (1,0,0,1) | 6 (2,0,2,0,2) | `invented_facts`, `unacknowledged_source_loss` |
| out-13 | 4 (1,1,1,1) | 7 (2,2,1,0,2) | `invented_facts`, `unacknowledged_source_loss` |
| out-14 | 5 (1,1,1,2) | 7 (2,2,1,0,2) | `invented_facts` |

## 2. Decisive questions

| output | Simplification and method merged? | Wages first-level? | First-level actions | Observations below actions? | Comparison/opinion explicitly omitted? | Literal reader question? |
|---|---|---|---:|---|---|---|
| out-01 | No | No | 2 | Partly; process evidence is lost | Yes | No |
| out-02 | No | No | 2 | Yes, though under the wrong second action | Yes | No |
| out-03 | No | No | 0 | No; observations are promoted and duplicated | Yes | No |
| out-04 | No | No | 0 | No; three observations form the numbered level | Yes | No |
| out-05 | No | No | 2 | Partly; staffing, delay, and overtime support is lost | Partly; management disagreement is unnoted | No |
| out-06 | No | No | 2 | Partly; staffing, delay, and overtime are explicitly discarded | Yes | No |
| out-07 | No | No | 2 | Partly; staffing evidence sits in the complication | Yes | Yes |
| out-08 | No | No | 2 | Partly; operating observations precede the actions | Yes | No |
| out-09 | No | No | 2 | Partly; staffing evidence is in the introduction | Yes | Yes |
| out-10 | No | No | 2 | Yes, but wage evidence supports productivity instead | Yes | No |
| out-11 | No | No | 3 | No; capacity becomes a third overlapping branch | No; both are retained as context | No |
| out-12 | No | No | 0 | No; observations occupy a “why” branch | Yes | No |
| out-13 | No | No | 2 | Yes, but staffing evidence supports method changes | Yes | No |
| out-14 | No | No | 2 | Partly; staffing evidence is a sibling urgency section | Yes | No |

## 3. Output notes

- **out-01:** The two-study hierarchy is readable, but it loses the wage evidence and treats staffing only as a methods-study constraint.
- **out-02:** It has the clearest ordering and display, but explicitly rules out higher pay and adds unsupported timing, authorization, and exclusivity claims.
- **out-03:** Five mixed first-level arguments promote evidence, duplicate it in a table, and introduce case studies, automation, and rollout conditions absent from the source.
- **out-04:** The recommendation is direct, but the numbered level consists of observations rather than the two required actions and omits material wage evidence.
- **out-05:** The two investigations are visible, but “fast,” “low-risk,” immediate relief, equipment, and scheduling are invented while key staffing facts disappear.
- **out-06:** The concise two-study answer explicitly discards the staffing causal chain and incorrectly declares that costs are genuinely excessive.
- **out-07:** The literal SCQ is visible but repetitive; the invented two-month test does not cure the missing wage action.
- **out-08:** The two branches are cleanly displayed, but the answer arrives after the setup and unsupported benefits are attributed to method changes.
- **out-09:** The question and two actions are explicit, but it reverses the staffing causality and leaves the pay remedy buried.
- **out-10:** It preserves nearly all wage evidence under a clear hierarchy, yet attaches it to productivity and invents a two-to-three-week schedule.
- **out-11:** A third capacity branch overlaps the first two, while claims about workload, delivery, and union exposure exceed the evidence.
- **out-12:** “Why” and “what” are mixed at one level, the uniform-check evidence is lost, and company-wide rollout is invented.
- **out-13:** The polished two-action structure preserves much of the evidence but places wage facts under method changes and overstates comparisons as confirmation.
- **out-14:** Its parallel-study presentation is coherent, but the 10–25% estimate, timing, comparative rationale, and delay effects are invented.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Process simplification and method/productivity change survive as duplicate branches | Core loop §6 — MECE duplication test | ignored | out-01–out-14 |
| The wage action remains buried in staffing observations | Core loop §§4 and 6 — promote the real action from observations | ignored | out-01–out-14 |
| Reader question is not written literally | Core loop §§1 and 3 | ignored | out-01–out-06, out-08, out-10–out-14 |
| Ordering principle is not named | Core loop §5 — Order | ignored | out-01–out-14 |
| Unsupported facts, certainty, timing, or causal claims are added | Mode 3 — “Invent nothing” | ignored | out-02, out-03, out-05–out-14 |
| Useful source facts disappear without a sufficient omission note | Mode 3 — “Keep every fact from the source” | ignored | out-01, out-04, out-05, out-08, out-09, out-12, out-13 |

## 5. Observation

Stronger outputs expose a concise answer and two action-shaped branches with evidence visibly nested beneath them; weaker outputs promote observations, mix “why” with “what,” or add sibling sections that obscure the key line. None makes the decisive structural correction: merging the two process interventions and promoting competitive wages as the independent second action.

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
        "total": 5,
        "top": 1,
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
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
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
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
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
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
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
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
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
        "top": 2,
        "same_kind_grouping": 2,
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
        "total": 6,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
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
        "scq_intro_present": true
      }
    },
    {
      "output": "out-07",
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
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
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
        "total": 6,
        "top": 1,
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
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-10",
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
      "output": "out-11",
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
      "output": "out-12",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 2,
        "same_kind_grouping": 0,
        "explainable_order": 2,
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
      "output": "out-13",
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
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
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
    }
  ]
}
```