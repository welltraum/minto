## 1. Score table

Sub-scores are shown as `(Top, Key-line composition, Levels, Order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 1 (0, 0, 0, 1) | 3 | `more_than_four_first_level` |
| out-02 | 3 (1, 1, 0, 1) | 6 | `more_than_four_first_level` |
| out-03 | 3 (1, 1, 0, 1) | 6 | — |
| out-04 | 2 (1, 0, 0, 1) | 6 | `invented_facts` |
| out-05 | 1 (1, 0, 0, 0) | 4 | `invented_facts` |
| out-06 | 5 (2, 1, 1, 1) | 8 | `invented_facts` |
| out-07 | 2 (1, 0, 0, 1) | 6 | — |
| out-08 | 4 (2, 0, 1, 1) | 6 | — |

## 2. Decisive questions

| output | 1. First-level kind | 2. Unchanged topics | 3. Transition branch? | 4. Purpose gone? | 5. Top answers? | 6. SCQ contradicts? | 7. Topics retained? | 8. Invented facts |
|---|---|---:|---|---|---|---|---|---|
| out-01 | topics/reasons | 5 | Yes | No | No | No | Yes | None |
| out-02 | actions | 5 | Yes | No | Yes, broadly | No | Yes | None |
| out-03 | actions | 3 | Yes | No | Yes, incompletely | No | Yes | None |
| out-04 | topics/reasons | 4 | No | No | Yes, vaguely | Yes | Yes | “Last October”; operational matters staying with the Executive Committee; outside directors being merely nominal |
| out-05 | topics/reasons | 3 | Yes, combined with tenure | Yes | Yes, broadly | No | Yes | Orientation, information access and decision authority for outsiders; renewal processes and succession planning |
| out-06 | actions | 2 | Yes | Yes | Yes | No | Yes | A specifically phased transition; the asserted causal impairment of the Board’s ability |
| out-07 | topics/reasons | 3 | Yes | No | Yes, vaguely | No SCQ is supplied | Yes | None |
| out-08 | mixed | 1 | Yes | No | Yes, broadly | No SCQ is supplied | Yes | None |

## 3. Output notes

- **out-01:** It largely reproduces all five source topics, including transition as an extra fifth branch, without supplying a substantive answer.
- **out-02:** Action verbs improve the surface form, but the five original topics remain the governing architecture.
- **out-03:** It gives a genuine change-oriented top and action key line, but still promotes roles, outside participation, and transition instead of the gold actions.
- **out-04:** The SCQ is the fullest, but its four questions remain topical and it contradicts the stated allocation of day-to-day authority.
- **out-05:** It writes the reader’s question explicitly and shows a clear hierarchy, but adds several unsupported governance prescriptions and combines transition with tenure.
- **out-06:** It is the strongest action pyramid and usefully subordinates several composition details, though transition remains a branch and “phased” is unsupported.
- **out-07:** It is concise and answer-first, but offers a list of subject areas without the situation-complication grounding.
- **out-08:** It consolidates the source most effectively and opens with an answer, but mixes governance areas with transition steps and omits the SCQ.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Governance topics or transition mechanics replace the three controlling changes | Core loop §4, Groups | ignored | out-01–out-08 |
| Transition is promoted as an independent branch instead of describing implementation of the whole recommendation | Core loop §6, MECE | ignored | out-01, out-02, out-03, out-05, out-06, out-07, out-08 |
| A memorandum-purpose sentence remains in the introduction | Core loop §3, SCQ intro | ignored | out-01, out-02, out-03, out-04, out-07, out-08 |
| The overarching reader question is not written literally | Core loop §1, Topic → reader question | missing | out-01, out-02, out-03, out-04, out-06, out-07, out-08 |
| Unsupported governance or transition detail is added | Mode 3, Keep every fact / invent nothing | ignored | out-04, out-05, out-06 |
| Situation-complication grounding is absent | Core loop §3, SCQ intro | missing | out-07, out-08 |

## 5. Observation

Stronger outputs state a change-oriented answer and consolidate source details beneath a small action key line; weaker outputs preserve the original topic inventory, treat transition as a peer branch, or merely relabel topics with verbs.

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
        "total": 1,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 3,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": [
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 5,
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
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
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
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": false,
        "first_level_count": 4,
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
        "top": 1,
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
        "first_level_count": 4,
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
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 4,
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
      "output": "out-06",
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
      "output": "out-07",
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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
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
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 0,
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