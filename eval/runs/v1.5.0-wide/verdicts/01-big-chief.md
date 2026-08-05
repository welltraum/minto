## 1. Score table

Structural sub-scores are shown as `(top/key line/levels/order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 7 (2/2/2/1) | 9 | `invented_facts`, `unacknowledged_source_loss` |
| out-02 | 8 (2/2/2/2) | 10 | None |
| out-03 | 3 (2/0/0/1) | 10 | `invented_facts` |
| out-04 | 3 (2/0/0/1) | 10 | None |
| out-05 | 2 (1/0/0/1) | 9 | None |
| out-06 | 2 (1/0/0/1) | 9 | `invented_facts` |
| out-07 | 2 (1/0/0/1) | 8 | `unacknowledged_source_loss` |
| out-08 | 2 (1/0/0/1) | 9 | None |

## 2. Decisive questions

| output | First-level kind | Grounded elements | Top answers acceptance? | Invented material | Details below key line? | Literal reader question? |
|---|---|---:|---|---|---|---|
| out-01 | Benefits | 3 | Yes | Separate payments by outlet-date; combined Data Processing routing; automatic matching; unsupported deadline | Partly; mechanics also appear in the answer and balancing branch | Yes |
| out-02 | Benefits | 3 | Yes | None | Yes | No |
| out-03 | Mechanics | 3 | Yes | Identifier population before processing; implementation without operational changes | No | No |
| out-04 | Mechanics | 3 | Yes | None | No | No |
| out-05 | Mechanics | 3 | No; it answers feasibility only | None | No | No |
| out-06 | Mechanics | 3 | No; it answers feasibility only | Direct transmission, mailing the cheque, automatic routing, and “all” subsequent submissions | No | No |
| out-07 | Mechanics | 3 | No; it answers feasibility only | None | No | No |
| out-08 | Mechanics | 3 | No; it answers feasibility only | None | No | No |

## 3. Output notes

- **out-01:** It derives a benefit-oriented key line and states the reader’s question, but introduces unsupported operating details and loses the lockbox routing.
- **out-02:** It most cleanly turns the mechanics into grounded acceptance reasons, with the operational evidence correctly subordinated.
- **out-03:** The recommendation is clear, but the “Key Findings” revert immediately to process mechanics and the conclusion overclaims operational impact.
- **out-04:** The acceptance recommendation is prominent, yet the entire supporting pyramid remains a chronological process description.
- **out-05:** Its process structure is clean and complete, but “can accommodate” stops short of advising management to accept.
- **out-06:** It presents requirements rather than reasons and embellishes several transmission and processing details.
- **out-07:** The prose is concise but visually weak, answers feasibility instead of acceptance, and drops the prepaid and program-building details.
- **out-08:** It faithfully preserves the mechanics, but largely reproduces the source’s central defect: accommodation is asserted without an acceptance recommendation.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Mechanics occupy the first level instead of acceptance reasons | Core loop §4, Groups | ignored | out-03, out-04, out-05, out-06, out-07, out-08 |
| The top answers feasibility rather than whether management should accept | Core loop §1–2, Reader question and provisional answer | missing | out-05, out-06, out-07, out-08 |
| The reader’s question is not written literally | Core loop §1 and §3, Question and SCQ | ignored | out-02, out-03, out-04, out-05, out-06, out-07, out-08 |
| The ordering principle is not named | Core loop §5, Order | missing | out-01, out-02, out-03, out-05, out-06, out-07, out-08 |
| Unsupported operational claims are introduced | Mode 3, “Invent nothing” | ignored | out-01, out-03, out-06 |
| Material source details disappear | Mode 3, “Keep every fact” | ignored | out-01, out-07 |

## 5. Observation

The stronger outputs convert the source mechanics into grounded reasons to accept the proposal and subordinate fields, routing, balancing, and processing beneath those reasons. The weaker outputs may be orderly and polished, but their first level still explains how the process works—or merely that it is feasible—rather than why management should accept it.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "01-big-chief",
  "mode": "write",
  "outputs": [
    {
      "output": "out-01",
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
        "readers_question_literal": true,
        "order_type_named": false
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
        "order_type_named": false
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 10,
        "top": 2,
        "same_kind_grouping": 2,
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
        "order_type_named": false
      }
    },
    {
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
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
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": true
      }
    },
    {
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
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
        "total": 9,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
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
        "readers_question_literal": false,
        "order_type_named": false
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
        "total": 8,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    }
  ]
}
```