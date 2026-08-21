## 1. Score table

Structural sub-scores are shown as `(top/key line/levels/order)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 5 (2/2/0/1) | 7 | `unacknowledged_source_loss` |
| out-02 | 6 (2/2/1/1) | 8 | `unacknowledged_source_loss` |
| out-03 | 7 (2/2/2/1) | 9 | None |
| out-04 | 7 (2/2/2/1) | 9 | None |
| out-05 | 7 (2/2/2/1) | 7 | None |
| out-06 | 6 (2/2/1/1) | 8 | `unacknowledged_source_loss` |
| out-07 | 7 (2/2/2/1) | 9 | None |
| out-08 | 6 (2/2/1/1) | 8 | `unacknowledged_source_loss` |
| out-09 | 7 (2/2/2/1) | 9 | None |
| out-10 | 6 (2/2/1/1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-11 | 6 (2/2/1/1) | 8 | `unacknowledged_source_loss` |
| out-12 | 6 (2/2/1/1) | 8 | `unacknowledged_source_loss` |
| out-13 | 6 (2/2/1/1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-14 | 7 (2/2/2/1) | 9 | None |
| out-15 | 6 (2/2/1/1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-16 | 7 (2/2/1/2) | 8 | None |

## 2. Decisive questions

| output | Diagram? | Exactly two actions? | First-level kind | Observations correctly placed? | File/HTML? | Rewritten? | Unsupported nodes added |
|---|---|---|---|---|---|---|---|
| out-01 | Yes | Yes | Actions | Yes | No | No | None |
| out-02 | Yes | Yes | Actions | Yes, although some supports are nested too deeply | No | No | None |
| out-03 | Yes | Yes | Actions | Yes | No | No | None |
| out-04 | Yes | Yes | Actions | Yes | No | No | None |
| out-05 | Yes | Yes | Actions | Yes | No | No; annotated in addition | None in the diagrams |
| out-06 | Yes | Yes | Actions | Yes | No | No | None |
| out-07 | Yes | Yes | Actions | Yes | No | No | None |
| out-08 | Yes | Yes | Actions | Yes | No | No | None |
| out-09 | Yes | Yes | Actions | Yes | No | No | None |
| out-10 | Yes | Yes | Actions | Yes | No | No | “Competitive pay will solve recruitment and overtime issues” overstates the tentative source |
| out-11 | Yes | Yes | Actions | Yes | No | No | None |
| out-12 | Yes | Yes | Actions | Yes | No | No | None |
| out-13 | Yes, as a text hierarchy | Yes | Actions | Yes | No | No | The certain claim that competitive pay “will” deliver both outcomes |
| out-14 | Yes | Yes | Actions | Yes | No | No | None |
| out-15 | Yes | Yes | Actions | Yes | No | No | A completed test showing savings; the source describes a future test and only a possible saving |
| out-16 | Yes | Yes | Actions | Yes; a meta-gap is also placed beneath the wage action | No | No; annotated in addition | “Saving not quantified” is an analytical gap node, not part of the memo’s pyramid |

## 3. Output notes

- **out-01:** The correct skeleton is visible, but most of the factual support and quantitative evidence has disappeared.
- **out-02:** It retains much of the evidence, though the identical-checks observation and union pressure are lost and some sibling supports appear as descendants.
- **out-03:** This is a faithful, complete pyramid with every observation attached to the correct action.
- **out-04:** The complete hierarchy is preserved, with the SCQ context added separately rather than disturbing the pyramid.
- **out-05:** The pyramid itself is complete, but the annotation, ribbon, and speculative gap table make the response substantially less proportionate than the task requires.
- **out-06:** The compact text tree is clear and faithful apart from losing the late-work consequence.
- **out-07:** It closely matches the expected structure and preserves the controlled-test and wage-pressure details.
- **out-08:** The two branches are correct, but monitoring, complexity, and delay details are lost or weakened.
- **out-09:** It compresses the evidence effectively while retaining the material logic of both branches.
- **out-10:** The layout is clear, but it drops monitoring and union pressure and turns a tentative wage outcome into certainty.
- **out-11:** The pyramid is clean but over-compressed, losing the methods study, departures, union pressure, and parts of the controlled-test design.
- **out-12:** The correct actions and much evidence remain, but the identical-checks argument and the wage branch’s proposed resolution are missing.
- **out-13:** The bullet hierarchy is a valid visible diagram, though it omits controlled-test and departure details and overstates the wage outcome.
- **out-14:** It is complete and accurately separates the main pyramid from the contextual SCQ ribbon.
- **out-15:** It preserves the main branches but falsely presents the planned test as completed and drops monitoring and union pressure.
- **out-16:** It preserves the source thoroughly and uniquely explains the order, but the added gap node and extensive diagnostic apparatus contaminate an otherwise strong visualization.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Source observations or qualifiers disappear from the pyramid | Core loop §8, evidence-grounding self-check | ignored | out-01, out-02, out-06, out-08, out-10, out-11, out-12, out-13, out-15 |
| The order of the two actions is left implicit rather than explained | Core loop §5, Order | ignored | out-01 through out-15 |
| Tentative source claims are converted into certain outcomes | Core loop §8, source-grounding check | ignored | out-10, out-13, out-15 |
| Unneeded annotation or analytical apparatus dilutes the requested visualization | Mode 4 — viz | ignored | out-05, out-16 |

## 5. Observation

The stronger outputs preserve one answer at the top, exactly two action branches, and the full set of observations beneath their proper parent; weaker outputs keep the same outer skeleton but compress away material evidence, distort tentative claims, or add analysis that is not part of the memorandum’s existing pyramid.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "06-ttw-viz",
  "mode": "viz",
  "outputs": [
    {
      "output": "out-01",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 2,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 0,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-11",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-12",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-15",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-16",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    }
  ]
}
```