## 1. Score table

Structural sub-scores are shown as `(top, key-line composition, levels, order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 8 (2, 2, 2, 2) | 10 | `invented_facts` |
| out-02 | 8 (2, 2, 2, 2) | 10 | `invented_facts` |
| out-03 | 8 (2, 2, 2, 2) | 9 | `invented_facts` |
| out-04 | 4 (2, 1, 0, 1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-05 | 8 (2, 2, 2, 2) | 9 | `invented_facts` |
| out-06 | 5 (2, 1, 1, 1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-07 | 5 (2, 1, 1, 1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-08 | 7 (2, 2, 1, 2) | 8 | `invented_facts`, `unacknowledged_source_loss` |

## 2. Decisive questions

### out-01

1. First, through both the subject and opening recommendation.
2. `business losses`.
3. Three.
4. Yes; all nine units appear beneath the appropriate reason.
5. No; backlog growth remains a reason.
6. A compact, slightly formal colleague email.
7. “More than double,” “recent,” “key client,” the claim that the client left for this reason, and “formal” complaint.
8. No.

### out-02

1. First.
2. `business losses`.
3. Three; backlog growth functions as the complication before the three loss branches.
4. Not literally: all nine units are retained, but the backlog units sit in the complication rather than beneath a reason.
5. Yes; this produces a cleaner business-loss key line and is stronger than treating operational growth as a peer loss.
6. A concise colleague message.
7. “Customer interviews” invents multiple interviews where the source supplies one.
8. No.

### out-03

1. First.
2. `business losses`.
3. Three.
4. Yes.
5. No; backlog growth is the first reason.
6. A concise colleague message.
7. The interview is described as “recent,” which the source does not establish.
8. Yes, in the closing question.

### out-04

1. First in the subject, although the body delays the explicit answer until after labeled SCQ sections.
2. `business losses`.
3. Four.
4. No; incoming-defect evidence, Customer Experience evidence, and the interview are absent or distorted.
5. No; backlog growth is repeated as a reason.
6. A compact but over-formalized message, not an oversized memo.
7. Weekly cadence, roughly 50%, “proven,” prospects citing quality concerns, future engineering-capacity consumption, the 10%/5% relationship, a 30%+ reduction, restored confidence, prevented future costs, and the end-of-day deadline.
8. Yes.

### out-05

1. First in the subject; the recommendation is repeated in the middle of the opening paragraph.
2. `business losses`.
3. Three.
4. Yes.
5. No; backlog growth is both introductory context and the first reason.
6. A colleague message with an unnecessary appended diagram.
7. The conclusion that the pattern is “structural, not seasonal” is unsupported by the supplied material.
8. Yes.

### out-06

1. First.
2. `business losses`.
3. Three.
4. No; user posts disappear, and the account complaint is placed under revenue rather than brand damage.
5. No; escalating backlog is a reason.
6. A concise but formal colleague email.
7. “Formal” complaint and “recent” interview.
8. No.

### out-07

1. First in the subject; the body repeats it after the opening context.
2. `business losses`.
3. Three.
4. No; user posts disappear, and the account complaint is subordinated to close rates rather than brand harm.
5. No; backlog growth is the final reason.
6. A concise colleague message.
7. “Interviews” invents multiple interviews.
8. Yes.

### out-08

1. First in the subject.
2. `business losses`.
3. Three.
4. No; the interview and churn chart are lost inside an unspecific reference to customer feedback.
5. Yes; using backlog growth as the complication is structurally stronger, although the supporting evidence is over-compressed.
6. A very compact colleague message.
7. “Key accounts” pluralizes evidence concerning one major account.
8. No.

## 3. Output notes

- **out-01:** It has the clearest fully displayed gold hierarchy and preserves every evidence branch, but adds substantial quantitative and customer-specific claims.
- **out-02:** It cleanly converts backlog growth into the complication and keeps the key line focused on business losses, with only the invented plurality of interviews undermining fidelity.
- **out-03:** It is the strongest natural-sounding prose version, with every evidence unit under the correct parent, but adds unsupported recency.
- **out-04:** Its labeled SCQ apparatus is heavier than the message requires, while the unsupported fourth branch and extensive fabrication displace source evidence.
- **out-05:** Its hierarchy and evidence placement are sound, but the unsupported seasonal diagnosis and duplicated Mermaid rendering weaken proportionality.
- **out-06:** It remains answer-first and readable, but loses the user-post evidence and forces brand evidence into a revenue branch.
- **out-07:** Its impact-first ordering is workable, but brand damage becomes subordinate to sales and the user-post evidence disappears.
- **out-08:** Its complication-plus-business-loss structure is admirably compact, but that compression erases distinct churn evidence and overstates the account scope.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Unsupported specificity or factual inflation | Mode 3 — “Invent nothing” | ignored | out-01, out-02, out-03, out-04, out-05, out-06, out-07, out-08 |
| Evidence omitted or placed under the wrong parent | Mode 3 — “Keep every fact from the source” | ignored | out-04, out-06, out-07, out-08 |
| Reader’s question never appears literally | Core loop §1 and §3 | ignored | out-01, out-02, out-06, out-08 |
| Ordering principle is not named | Core loop §5 — Order | ignored | out-01, out-02, out-03, out-04, out-05, out-06, out-07, out-08 |

## 5. Observation

The stronger outputs place the sprint recommendation immediately, use a compact key line of grounded business reasons, and keep each chart, report, interview, and complaint under its proper parent. The weaker outputs add unsupported branches or precision, subordinate brand evidence to sales, or achieve brevity by erasing distinct evidence units.

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
        "order_type_named": false
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
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
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
        "readers_question_literal": true,
        "order_type_named": false
      }
    },
    {
      "output": "out-04",
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
        "answer_first": true,
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
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
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
        "readers_question_literal": true,
        "order_type_named": false
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
      "output": "out-08",
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
        "order_type_named": false
      }
    }
  ]
}
```