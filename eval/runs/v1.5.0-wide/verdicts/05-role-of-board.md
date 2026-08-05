## 1. Score table

Structural axes: top / key-line composition / levels / order and kind.  
Quality axes: top / same-kind grouping / explainable order / MECE / visible structure.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (2/1/0/1) | 8 (2/2/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-02 | 2 (2/0/0/0) | 6 (1/1/1/1/2) | `more_than_four_first_level` |
| out-03 | 0 (0/0/0/0) | 5 (0/1/1/1/2) | `invented_facts`, `more_than_four_first_level` |
| out-04 | 5 (2/1/1/1) | 7 (1/2/1/1/2) | None |
| out-05 | 1 (0/0/1/0) | 3 (0/0/0/1/2) | `invented_facts` |
| out-06 | 1 (1/0/0/0) | 6 (1/1/1/1/2) | `more_than_four_first_level` |
| out-07 | 5 (2/1/1/1) | 8 (2/2/1/1/2) | None |
| out-08 | 3 (2/0/1/0) | 7 (2/1/1/1/2) | None |

## 2. Decisive questions

| output | First-level kind | Unchanged source topics | Alternative branch? | Purpose gone? | Top answers required changes? | SCQ contradicts context? | All topics retained or noted? | Invented facts |
|---|---|---:|---|---|---|---|---|---|
| out-01 | Actions | 4 | No | Yes | Yes | No; the later assignment of “operational duties” to the Executive Committee is unsupported | No; transition alternatives disappear | Role ambiguity, impaired outside-director impact, undefined arrangements, and Executive Committee operational duties |
| out-02 | Topics/reasons | 5 | Yes | Yes | Partly; it gives the desired state rather than the redesign | No | Yes | None |
| out-03 | Topics/reasons | 5 | Yes | No | No | No | Yes | The Board spending “most of its time” on operational problems |
| out-04 | Actions | 3 | Yes | Yes | Partly; “restructuring” is not specified in the top | No | Yes | None |
| out-05 | Mixed topics | 2 | Yes | Yes | No; it names subjects to settle | No | Yes | The policy-and-planning role having “never” been defined or staffed |
| out-06 | Topics/reasons | 5 | Yes | No | Partly; only redefining the role is named | No SCQ is supplied | Yes | None |
| out-07 | Actions | 2 | Yes | Yes | Yes | No | Yes | None |
| out-08 | Topics/reasons | 3 | Yes | No | Yes | No | Yes | None |

## 3. Output notes

- **out-01:** It converts four source topics into actions, but leaves them at the first level, drops transition material, and adds unsupported complications.
- **out-02:** Its answer-first opening is followed by the original five-topic inventory, including transition as a separate branch.
- **out-03:** It preserves the purpose statement and original list without supplying a controlling answer.
- **out-04:** It is answer-first and sensibly nests tenure under composition, but still organizes the memorandum as issues rather than the gold changes.
- **out-05:** Its hierarchy is highly visible, but “job, membership, transition” is a mixed topical decomposition and includes unsupported claims.
- **out-06:** A vague recommendation precedes an essentially unchanged five-topic list and another purpose statement.
- **out-07:** It has the strongest action-oriented key line, although transition remains incorrectly promoted and the answer follows the SCQ.
- **out-08:** Its first sentence answers directly, but the supporting line reverts to overlapping governance topics and preserves purpose language.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| First-level elements are topics or mixed categories rather than changes | Core loop §4, Groups | ignored | out-02, out-03, out-05, out-06, out-08 |
| The answer is not encountered first | Mode 3, write/rewrite | buried | out-01, out-03, out-05, out-07 |
| Transition mechanics survive as a peer branch | Core loop §6, MECE | ignored | out-02, out-03, out-04, out-05, out-06, out-07, out-08 |
| The ordering principle is never named | Core loop §5, Order | ignored | out-01, out-02, out-03, out-04, out-05, out-06, out-07, out-08 |
| Purpose language survives instead of disappearing | Core loop §3, SCQ anti-patterns | ignored | out-03, out-06, out-08 |
| Unsupported assertions are added to the source | Mode 3, “Invent nothing” | ignored | out-01, out-03, out-05 |
| The original five-item level is retained | Mode 3, three-to-four-group rule | ignored | out-02, out-03, out-06 |

## 5. Observation

The stronger outputs state a strategic recommendation and recast the support as actions, while the weaker outputs reproduce or lightly relabel the five source discussion topics. Even the stronger drafts stop short of the gold structure because they retain transition as a peer branch or leave composition, outside participation, and governance procedures at too high a level.

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
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
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
      "output": "out-02",
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
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "more_than_four_first_level"
      ],
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
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 0,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 5,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts",
        "more_than_four_first_level"
      ],
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
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": false,
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
        "top": 0,
        "key_line_composition": 0,
        "levels": 1,
        "order_and_kind": 0
      },
      "quality": {
        "total": 3,
        "top": 0,
        "same_kind_grouping": 0,
        "explainable_order": 0,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
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
        "total": 6,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "more_than_four_first_level"
      ],
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
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
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
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 1,
        "order_and_kind": 0
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
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false
      }
    }
  ]
}
```