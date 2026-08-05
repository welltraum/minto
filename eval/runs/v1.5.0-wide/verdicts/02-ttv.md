## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 2 (2/0/0/0) | 3 (2/0/0/0/1) | `invented_facts` |
| out-02 | 4 (2/1/0/1) | 6 (2/1/1/0/2) | `invented_facts` |
| out-03 | 5 (2/1/1/1) | 6 (2/1/1/0/2) | `invented_facts` |
| out-04 | 4 (2/1/0/1) | 7 (2/2/1/0/2) | — |
| out-05 | 3 (1/1/0/1) | 6 (2/2/1/0/1) | `invented_facts`, `unacknowledged_source_loss` |
| out-06 | 3 (2/1/0/0) | 6 (2/1/1/0/2) | `invented_facts` |
| out-07 | 4 (1/1/1/1) | 6 (2/2/0/0/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-08 | 5 (2/1/1/1) | 7 (2/2/1/0/2) | `unacknowledged_source_loss` |

## 2. Decisive questions

| output | 1. Process and method merged? | 2. Wages first-level? | 3. First-level actions | 4. Observations below actions? | 5. Irrelevant material omitted with note? | 6. Reader question literal? |
|---|---|---|---:|---|---|---|
| out-01 | No | No | 2 | No; benchmarking and staffing become peer arguments. | No; comparison is promoted. | No |
| out-02 | No | No | 2 | No; staffing, delay, and overtime form an urgency branch. | No; comparison and opinion remain. | Yes |
| out-03 | No | No | 2 | Yes, although staffing evidence supports the wrong action. | Yes | No |
| out-04 | No | No | 2 | No; the staffing, delay, and overtime chain is discarded. | Yes | No |
| out-05 | No | No | 3 | No; evidence is split into separate reason and mechanics groups, with material missing. | No; comparison and disagreement remain. | Yes |
| out-06 | No | No | 2 | No; staffing evidence is removed and benchmark evidence is partly promoted. | Yes | No |
| out-07 | No | No | 2 | Yes, but the wage evidence is misparented under method change. | No; managerial opinion disappears without a note. | No |
| out-08 | No | No | 3 | Yes; the observations sit beneath action headings. | No; managerial disagreement remains. | No |

## 3. Output notes

- **out-01:** The recommendation is answer-first, but the four supporting branches mix actions, benchmarking, and feasibility, while the detailed implementation plan introduces extensive unsupported material.
- **out-02:** It uniquely names an ordering principle and states the question, but preserves the duplicate process branches and elevates urgency instead of wages.
- **out-03:** Its evidence is visibly nested, but urgency becomes a third peer branch and willingness to investigate is overstated as implementation support.
- **out-04:** This is concise and visibly organized around two actions, but it explicitly removes the entire evidence chain that should lead to raising wages.
- **out-05:** It writes out a question but reframes the decision as how to validate two predetermined process changes, adding unsupported measures while losing wage-related evidence.
- **out-06:** The answer appears at the top, but an evidence heading becomes a peer of the actions and the wage branch is dismissed as a separate capacity discussion.
- **out-07:** It retains much of the wage evidence but incorrectly hangs it beneath method change, and its actual recommendation arrives only after contextual claims.
- **out-08:** The observations are well subordinated, but “address capacity pressure” remains too broad to recover the specific raise-wages action and the union evidence disappears silently.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Duplicate simplification and method-change branches survive, while the wage action is not promoted | Core loop §6, MECE duplication test | ignored | 8 (out-01–out-08) |
| Staffing, delay, and overtime evidence is omitted, promoted, or placed under method change rather than a wage action | Core loop §4, Groups; §7, Show the structure | ignored | 8 (out-01–out-08) |
| Reader’s question is not written literally | Core loop §1 and §3 | ignored | 6 (out-01, out-03, out-04, out-06, out-07, out-08) |
| Ordering principle is not named | Core loop §5, Order | ignored | 7 (out-01, out-03–out-08) |
| Unsupported facts, certainty, implementation details, or causal claims are added | Mode 3, “Invent nothing” | ignored | 6 (out-01, out-02, out-03, out-05, out-06, out-07) |
| Useful source evidence disappears without a sufficient omission note | Mode 3, fact-retention rule | ignored | 3 (out-05, out-07, out-08) |

## 5. Observation

The stronger outputs provide a concise answer and visibly subordinate process, benchmark, and operating evidence beneath action-like branches. None completes the decisive structural move: merging the two overlapping process interventions and promoting competitive wages from the staffing evidence; weaker outputs further dilute the pyramid with urgency, benchmarking, invented implementation detail, or discarded evidence.

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
        "total": 2,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 3,
        "top": 2,
        "same_kind_grouping": 0,
        "explainable_order": 0,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts"
      ],
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
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 1,
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
        "invented_facts"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": true
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
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
        "total": 4,
        "top": 2,
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
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
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
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": false,
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
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 0
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
        "explainable_order": 0,
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
        "order_type_named": false
      }
    },
    {
      "output": "out-08",
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
        "same_kind_grouping": 2,
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
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    }
  ]
}
```