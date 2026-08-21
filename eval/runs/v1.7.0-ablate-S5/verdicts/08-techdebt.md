## 1. Score table

Structural sub-scores are `(top/key line/levels/order and kind)`; quality sub-scores are `(top/grouping/order/MECE/display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2/2/1/1) | 9 (2/2/1/2/2) | `unacknowledged_source_loss` |
| out-02 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | `invented_facts` |
| out-03 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | `invented_facts` |
| out-04 | 7 (2/2/1/2) | 10 (2/2/2/2/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-05 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-06 | 6 (2/1/1/2) | 8 (2/2/2/1/1) | `invented_facts`, `unacknowledged_source_loss` |
| out-07 | 8 (2/2/2/2) | 9 (2/2/2/2/1) | None |
| out-08 | 8 (2/2/2/2) | 9 (2/2/2/2/1) | `invented_facts` |

## 2. Decisive questions

### out-01

1. First, through the subject line; repeated immediately afterward.
2. Business losses/payoffs.
3. Three.
4. No; the customer interview disappears.
5. No; backlog growth remains a reason and is repeated around the key line.
6. A concise colleague message.
7. None.
8. No.

### out-02

1. First; repeated near the end.
2. Business losses.
3. Three.
4. Yes.
5. No.
6. A concise colleague message.
7. The projected level being “unsustainable” and the claim that churn tracks defect volume “closely.”
8. No.

### out-03

1. First.
2. Business losses.
3. Three.
4. Yes.
5. No.
6. A concise colleague message.
7. The backlog being “unsustainable,” churn tracking “closely,” and the interview showing “exactly how.”
8. No.

### out-04

1. First through the subject line; the body repeats it after the introduction.
2. Business losses.
3. Four.
4. No; the interview is omitted, while unspecified CX data becomes “surveys.”
5. No.
6. A compact colleague email.
7. The backlog being already large, doubling within a year, a 100% increase, surveys, growing reputational concerns, and prospects citing quality issues.
8. No.

### out-05

1. First.
2. Business losses, though one branch improperly combines churn and sales.
3. Three.
4. No; CX/Research evidence is lost, the interview is moved under brand, and the account complaint is moved under churn/sales.
5. No.
6. A concise but somewhat formalized colleague message.
7. Accelerating backlog growth and “significant frustration” revealed by the posts and interview.
8. No.

### out-06

1. First.
2. Business losses.
3. Three.
4. No; CX/Research evidence is missing, and the remaining evidence is duplicated in a detached attachment list.
5. No.
6. A compact structured note, not an oversized memo.
7. An “exploding” backlog, consistent outpacing, doubling within a year, a recent interview, a formal complaint, and an interview excerpt specifically showing frustration.
8. No.

### out-07

1. First.
2. Business losses.
3. Three.
4. Yes.
5. No.
6. A concise colleague message.
7. None.
8. No.

### out-08

1. First through the subject line; repeated at the end of the opening paragraph.
2. Business losses.
3. Three.
4. Not literally: the backlog evidence is appropriately used in the SCQ complication, while the six external-loss units sit under the correct reasons.
5. Yes; this is structurally stronger because the key line contains only external business losses.
6. An over-structured colleague message with an unnecessary diagram, rather than a formal memo.
7. Active causation, direct correlation with backlog growth, a recent interview, rising posts, a formal grievance, accelerating reputational damage, and lengthening deal cycles.
8. No.

## 3. Output notes

- **out-01:** The subject is answer-first and the benefit branches are readable, but backlog growth is repeated and the interview is lost.
- **out-02:** It preserves the expected hierarchy and evidence unusually well, but adds unsupported certainty to the projection and churn relationship.
- **out-03:** The numbered reasons produce the clearest compact hierarchy, though several intensifiers go beyond the evidence.
- **out-04:** Its operational-to-commercial progression is coherent, but invented metrics and evidence types undermine an otherwise strong structure.
- **out-05:** The answer is prominent, but churn, sales, brand evidence, the interview, and the account complaint are grouped under inconsistent parents.
- **out-06:** Its three reasons are easy to scan, but the detached attachment list duplicates support while important CX/Research material disappears.
- **out-07:** This is the strongest factually disciplined colleague message, preserving the evidence under the expected reasons with only modestly visible hierarchy.
- **out-08:** Moving backlog growth into the complication creates the strongest key-line composition, but the diagram is disproportionate and the prose invents several trends and causal details.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Unsupported metrics, intensifiers, or strengthened causal claims | Mode 3 — “Invent nothing” | ignored | out-02, out-03, out-04, out-05, out-06, out-08 |
| Source evidence omitted without acknowledgment | Mode 3 — “Keep every fact from the source” | ignored | out-01, out-04, out-05, out-06 |
| Reader’s question never written literally | Core loop §1 and §3 | ignored | out-01 through out-08 |
| SCQ grounding absent before support | Core loop §3 | missing | out-05, out-06, out-07 |
| Ordering principle not named | Core loop §5 | missing | out-01 through out-08 |
| Evidence assigned to the wrong parent or detached from its reason | Core loop §4 and Mode 3 | ignored | out-05, out-06 |

## 5. Observation

The stronger outputs put the sprint recommendation in the subject or first sentence, use three or four parallel business-loss reasons, and keep each evidence type directly beneath its conclusion. The weaker outputs merge distinct losses, detach or omit evidence, or replace the supplied evidence with stronger metrics and causal claims; out-08 improves the key line by treating backlog growth as the complication, while out-07 is the cleanest fact-preserving execution.

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
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
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
        "scq_intro_present": true
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
        "levels": 1,
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
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-05",
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
        "scq_intro_present": false
      }
    },
    {
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
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
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-07",
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
        "scq_intro_present": false
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
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    }
  ]
}
```