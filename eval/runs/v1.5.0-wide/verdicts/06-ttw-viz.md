## 1. Score table

Sub-score order: Structure `(top/key line/levels/order and kind)`; Quality `(top/grouping/order/MECE/display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 7 (2/2/1/2) | 7 (2/2/1/1/1) | `invented_facts`, `unacknowledged_source_loss` |
| out-02 | 8 (2/2/2/2) | 8 (2/2/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-03 | 8 (2/2/2/2) | 8 (2/2/1/2/1) | `invented_facts` |
| out-04 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | None |
| out-05 | 8 (2/2/2/2) | 9 (2/2/1/2/2) | None |
| out-06 | 6 (2/2/1/1) | 7 (2/2/0/1/2) | `unacknowledged_source_loss` |
| out-07 | 7 (2/2/1/2) | 8 (2/2/1/1/2) | `unacknowledged_source_loss` |
| out-08 | 8 (2/2/2/2) | 9 (2/2/1/2/2) | `invented_facts` |

## 2. Decisive questions

| output | Diagram? | Exactly two first-level actions? | First-level kind | Observations under correct action? | Unrequested file/HTML? | Memo rewritten? | Unsupported additions or assertions |
|---|---|---|---|---|---|---|---|
| out-01 | Yes | Yes | Actions | Yes, though lower attachments are visually ambiguous | No | No | Competitive-pay outcome is stated as certain rather than tentative |
| out-02 | Yes | Yes | Actions | Yes | No | No | Adds a causal “because” to the benchmark gap and makes the pay outcome certain |
| out-03 | Yes | Yes | Actions | Yes | No | No; it is reproduced and annotated | Changes “more than 50%” to exactly 50% and states the pay outcome as certain |
| out-04 | Yes | No; three first-level nodes | Mixed context observation and actions | No; context is promoted | No | No | None |
| out-05 | Yes | Yes | Actions | Yes | No | No | None |
| out-06 | Yes | Yes | Actions | No; wage evidence is presented as a serial chain | No | No | None |
| out-07 | Yes | Yes | Actions | Yes, for the observations retained | No | No | None |
| out-08 | Yes | Yes | Actions | Yes | No | No | Competitive-pay outcome is stated as certain rather than tentative |

## 3. Output notes

- **out-01:** It has the right top and two actions, but the crowded ASCII attachments obscure levels, generalize the two departures, and overstate the pay outcome.
- **out-02:** The tree is clean and correctly branched, but it drops the two departures while adding unsupported causal and certainty language.
- **out-03:** Its pyramid is structurally strong, but the full annotation apparatus is disproportionate and the diagram alters both the overtime threshold and the pay claim’s certainty.
- **out-04:** It promotes contextual evidence into a third first-level branch, mixing an observation with the two required actions.
- **out-05:** It gives the most complete, direct action pyramid and a useful SCQ ribbon without changing the source’s claims.
- **out-06:** The two main actions are correct, but the wage evidence becomes a misleading serial chain and the late-work fact disappears.
- **out-07:** It preserves the action split but omits the methods study and union pressure and weakens the uniform-check observation.
- **out-08:** It is complete and readable, but changes the conditional competitive-pay benefit into a certain outcome.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Tentative evidence is converted into certainty | Core loop §8, evidence-grounding self-check | ignored | out-01, out-02, out-03, out-08 |
| Supporting source material is omitted or materially weakened | Core loop §7–8, show and verify the structure | ignored | out-01, out-02, out-06, out-07 |
| The ordering principle is displayed but not explicitly explained | Core loop §5, Order | ignored | out-01 through out-08 |

## 5. Observation

Stronger outputs place one clear claim above exactly two action branches and retain the observations as sibling support under the appropriate action. Weaker outputs promote context, turn sibling evidence into a false chain, lose source details, or strengthen tentative claims.

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
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na"
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
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
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
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na"
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 8,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
        "readers_question_literal": "na",
        "order_type_named": "na"
      }
    },
    {
      "output": "out-04",
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
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na"
      }
    },
    {
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 8,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 2
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
        "order_type_named": "na"
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 0,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na"
      }
    },
    {
      "output": "out-07",
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
        "explainable_order": 1,
        "mece": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na"
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 8,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
        "readers_question_literal": "na",
        "order_type_named": "na"
      }
    }
  ]
}
```