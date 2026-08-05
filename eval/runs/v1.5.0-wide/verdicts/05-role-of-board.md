## 1. Score table

Structural sub-scores are `(top, key line, levels, order/kind)`; quality sub-scores are `(top, grouping, order, MECE, display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (1, 1, 1, 1) | 6 (1, 1, 1, 1, 2) | `invented_facts` |
| out-02 | 3 (1, 1, 0, 1) | 6 (1, 2, 0, 1, 2) | `invented_facts`, `unacknowledged_source_loss` |
| out-03 | 1 (1, 0, 0, 0) | 4 (1, 1, 0, 0, 2) | `more_than_four_first_level` |
| out-04 | 4 (1, 1, 1, 1) | 7 (1, 2, 1, 1, 2) | `invented_facts` |
| out-05 | 1 (1, 0, 0, 0) | 4 (1, 1, 0, 0, 2) | `more_than_four_first_level` |
| out-06 | 2 (1, 0, 0, 1) | 6 (1, 1, 1, 1, 2) | `invented_facts` |
| out-07 | 0 (0, 0, 0, 0) | 3 (0, 1, 0, 0, 2) | `more_than_four_first_level` |
| out-08 | 4 (1, 1, 1, 1) | 7 (1, 2, 1, 1, 2) | — |
| out-09 | 5 (1, 1, 1, 2) | 8 (1, 2, 2, 1, 2) | `invented_facts` |
| out-10 | 4 (1, 1, 1, 1) | 6 (1, 1, 1, 1, 2) | — |
| out-11 | 2 (1, 0, 0, 1) | 6 (1, 1, 1, 1, 2) | — |
| out-12 | 1 (0, 0, 0, 1) | 5 (0, 1, 1, 1, 2) | `invented_facts` |
| out-13 | 0 (0, 0, 0, 0) | 3 (0, 1, 0, 0, 2) | `invented_facts`, `more_than_four_first_level` |
| out-14 | 2 (1, 0, 0, 1) | 5 (1, 1, 1, 0, 2) | `invented_facts`, `more_than_four_first_level` |

## 2. Decisive questions

| output | 1. First-level kind | 2. Source topics unchanged | 3. Transition branch? | 4. Purpose gone? | 5. Top answers change? | 6. SCQ contradiction? | 7. All topics retained? | 8. Invented facts |
|---|---|---:|---|---|---|---|---|---|
| out-01 | Mixed topics and transition | 2 | Yes | Yes | Partly | No | Yes | The policy role was “never defined or staffed for.” |
| out-02 | Actions | 4 | No; omitted | Yes | Yes | Yes; it assigns operational duties to the Executive Committee | No | The mismatch limits outside directors, leaves rules undefined, and gives the Executive Committee operational duties. |
| out-03 | Mixed topics and transition | 5 | Yes | Yes | Partly | No | Yes | None. |
| out-04 | Actions | 3 | Yes | Yes | Yes | No | Yes | An Executive Committee “arbitrating role,” special value from outside-director independence, and a disruption-free transition. |
| out-05 | Mixed topics and transition | 5 | Yes | No | Partly | No | Yes | None. |
| out-06 | Topics/questions | 4 | No | Yes | Partly | No | Yes | The Board still spends “much” of its time operationally and outside directors are passive attendees. |
| out-07 | Mixed topics and transition | 5 | Yes | Yes | No | No | Yes | None. |
| out-08 | Actions | 2 | Yes | Yes | Yes | No | Yes | None. |
| out-09 | Actions | 1 | Yes | Yes | Yes | No | Yes | Existing arrangements were built for the former Board; policy work especially needs outside members; appointment-by-appointment drift occurs. |
| out-10 | Mixed topics and transition | 3 | Yes | Yes | Partly | No | Yes | None. |
| out-11 | Mixed topics and transition | 3 | Yes | Yes | Partly | No | Yes | None. |
| out-12 | Topics/questions | 4 | No | No | No | No | Yes | The Board is free to focus “exclusively” on policy and planning. |
| out-13 | Mixed topics and transition | 5 | Yes | No | No | No | Yes | The Board spent “most” of its time on operational problems. |
| out-14 | Mixed topics and transition | 5 | Yes | Yes | Partly | No | Yes | The Board continues to spend “most” of its time on operational problems. |

## 3. Output notes

- **out-01:** It consolidates membership details well, but its top remains a set of subjects to settle and incorrectly elevates transition.
- **out-02:** Its imperatives form a same-kind action group, but the labeled SCQ invents consequences and drops the transition material entirely.
- **out-03:** It opens with a recommendation, then reproduces all five source topics as first-level areas.
- **out-04:** It provides a visible action hierarchy and useful consolidation, but adds unsupported governance mechanisms and preserves transition as a branch.
- **out-05:** The answer-first opening is too general to overcome the nearly verbatim five-topic list and surviving purpose formulation.
- **out-06:** It correctly treats transition as subsequent work, but the key line consists of four questions rather than the required changes.
- **out-07:** It supplies context followed by the original five issues, without a controlling answer.
- **out-08:** It offers the cleanest concise three-action grouping without invented facts, although the answer follows the SCQ and transition remains first-level.
- **out-09:** It has the strongest visible hierarchy and clearest ordering rationale, but promotes transition and adds several unsupported causal claims.
- **out-10:** It is answer-first and consolidates selection with composition, but its branches remain issues for resolution rather than substantive changes.
- **out-11:** The opening frames the complication clearly, while the four branches retain the source’s topical organization and elevate transition.
- **out-12:** It appropriately treats transition as applying across the proposal, but never supplies the promised answer and retains a purpose statement.
- **out-13:** It improves the contextual setup but preserves both the original purpose statement and all five discussion topics.
- **out-14:** It adds a vague recommendation before recasting all five original topics as questions, leaving the transition at the wrong level.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Source topics remain first-level instead of becoming supporting evidence beneath changes | Core loop §4, “Groups” | ignored | out-01, out-03, out-05, out-06, out-07, out-10, out-11, out-12, out-13, out-14 |
| Transition is promoted as a separate branch | Core loop §6, “MECE” | ignored | out-01, out-03, out-04, out-05, out-07, out-08, out-09, out-10, out-11, out-13, out-14 |
| The answer appears after contextual material | Core loop §§2–3, “Provisional answer” and “SCQ intro” | buried | out-01, out-02, out-04, out-08, out-09, out-14 |
| No controlling answer is supplied | Mode 3, “write / rewrite” | missing | out-07, out-12, out-13 |
| More than four first-level elements are used | Core loop §4 and Mode 3 limits | ignored | out-03, out-05, out-07, out-13, out-14 |
| The canonical ordering principle is not named | Core loop §5, “Order” | missing | out-01–out-14 |
| Unsupported factual or causal material is added | Mode 3, “Invent nothing” | ignored | out-01, out-02, out-04, out-06, out-09, out-12, out-13, out-14 |

## 5. Observation

The stronger outputs synthesize the source into three or four visible actions and place composition, tenure, and outside-director details beneath broader changes. The weaker outputs preserve the five-item discussion agenda, treat transition as a peer topic, and offer either a vague “address these issues” top or no answer at all.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "05-role-of-board",
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
        "total": 6,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false
      }
    },
    {
      "output": "out-02",
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
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 0,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": false,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false
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
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 0,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["more_than_four_first_level"],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-04",
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
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": false,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-05",
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
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 0,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["more_than_four_first_level"],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-06",
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
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 0,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 3,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 0,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["more_than_four_first_level"],
      "checks": {
        "answer_first": false,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
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
        "top": 1,
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
        "readers_question_literal": true,
        "order_type_named": false
      }
    },
    {
      "output": "out-09",
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
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false
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
        "total": 6,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-11",
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
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false
      }
    },
    {
      "output": "out-12",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": false,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 0,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 3,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 0,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts", "more_than_four_first_level"],
      "checks": {
        "answer_first": false,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts", "more_than_four_first_level"],
      "checks": {
        "answer_first": false,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    }
  ]
}
```