## 1. Score table

Sub-scores are ordered as `(top, key-line composition, levels, order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2, 2, 1, 1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-02 | 8 (2, 2, 2, 2) | 10 | None |
| out-03 | 6 (2, 2, 0, 2) | 9 | `invented_facts`, `unacknowledged_source_loss` |
| out-04 | 7 (2, 2, 2, 1) | 9 | `invented_facts` |
| out-05 | 7 (2, 2, 2, 1) | 9 | None |
| out-06 | 4 (2, 1, 0, 1) | 7 | `invented_facts`, `unacknowledged_source_loss` |
| out-07 | 6 (2, 2, 1, 1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-08 | 7 (2, 2, 2, 1) | 8 | None |

## 2. Decisive questions

| output | 1. Recommendation | 2. First-level kind | 3. Count | 4. All evidence correctly placed? | 5. Backlog as SCQ complication? | 6. Format | 7. Invented material | 8. Reader question literal? |
|---|---|---|---:|---|---|---|---|---|
| out-01 | First, in subject | Mixed | 3 | No; CX evidence disappears | No; it remains a reason as well | Colleague message | Threshold crossed, rising churn, formal complaint, direct correlation, unmanageable backlog, interview-confirmed dissatisfaction | No |
| out-02 | First, in subject | Business losses | 3 | Yes; backlog evidence is appropriately held in the complication | Yes; this is stronger | Colleague message | None | No |
| out-03 | First, in subject | Business losses | 3 | No; CX and interview evidence are lost | Yes; structurally stronger, though weakened by inventions | Compact but over-labeled colleague note | Backlog doubling, defects as the primary churn driver, churn spikes, prospects citing defect concerns | No |
| out-04 | First, in subject | Mixed | 3 | Yes | No | Colleague message | Feature delivery every sprint, backlog roughly doubling, deals falling through | No |
| out-05 | First sentence | Mixed | 3 | Yes | No | Colleague message | None | No |
| out-06 | First sentence | Mixed | 3 | No; CX is lost, while the interview and account complaint sit under the wrong parents | No | Compact memo-style message | Accelerating backlog growth and significant frustration revealed by the interview/posts | No |
| out-07 | First sentence | Mixed | 3 | No; CX is lost and evidence is repeated in a detached attachment list | No | Compact memo-style message, not oversized | Backlog doubling, a recent interview, a formal complaint, threatened future deals, and unsupported claims that interview excerpts/reports are attached | No |
| out-08 | First sentence | Mixed | 3 | Yes | No | Concise colleague message | None | No |

## 3. Output notes

- **out-01:** The recommendation is visible immediately, but the reverse-ordered key line loses CX evidence and adds several unsupported degrees of certainty.
- **out-02:** The cleanest output uses backlog growth as the complication and keeps the key line entirely at the level of business losses.
- **out-03:** Its business-loss key line is strong, but conspicuous SCQ labels, missing evidence, and fabricated magnitudes make the execution less reliable.
- **out-04:** It closely follows the gold hierarchy and preserves the evidence, but invents feature-delivery history, a doubling forecast, and completed deal losses.
- **out-05:** This is the strongest gold-shaped version: complete evidence, clear hierarchy, and no unsupported additions.
- **out-06:** The middle branches overlap, CX disappears, and the interview and complaint are assigned to weaker parents.
- **out-07:** The main branches are readable, but the detached evidence inventory repeats the structure while introducing missing and fabricated attachment details.
- **out-08:** It preserves the source cleanly and concisely, although the hierarchy is less visible and mixes backlog status with external business losses.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Unsupported facts, magnitudes, or certainty | Mode 3 — “Invent nothing” | ignored | out-01, out-03, out-04, out-06, out-07 |
| Source evidence omitted or assigned to the wrong parent | Mode 3 — “Keep every fact”; Core loop §2–4 | missing | out-01, out-03, out-06, out-07 |
| Backlog condition mixed with external business-loss branches | Core loop §4 — Groups and same-kind test | ignored | out-01, out-04, out-05, out-06, out-07, out-08 |
| No visible SCQ grounding before support | Core loop §3 — SCQ intro | missing | out-06, out-07, out-08 |
| Reader’s question never written literally | Core loop §1 and §3 | ignored | out-01, out-02, out-03, out-04, out-05, out-06, out-07, out-08 |

## 5. Observation

The stronger outputs combine an immediate recommendation with complete evidence under clean business-loss branches; the weaker ones lose or detach evidence, mix operational backlog data with external losses, or manufacture specificity that the source never supplied.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "08-techdebt",
  "mode": "write",
  "outputs": [
    {
      "output": "out-01",
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
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
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
        "total": 8,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 10,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
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
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 0,
        "order_and_kind": 2
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
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
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
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
        "total": 9,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": false,
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
        "total": 4,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
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
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
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
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": false,
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