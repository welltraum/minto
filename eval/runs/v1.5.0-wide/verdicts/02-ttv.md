## 1. Score table

Structural sub-scores are shown as `(top/key line/levels/order)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (2/1/0/1) | 7 | `unacknowledged_source_loss` |
| out-02 | 4 (2/1/0/1) | 7 | — |
| out-03 | 4 (2/1/0/1) | 6 | `invented_facts` |
| out-04 | 5 (2/1/1/1) | 6 | `invented_facts` |
| out-05 | 4 (2/1/0/1) | 6 | `invented_facts` |
| out-06 | 4 (1/1/1/1) | 7 | `invented_facts`, `unacknowledged_source_loss` |
| out-07 | 5 (2/1/1/1) | 7 | `invented_facts`, `unacknowledged_source_loss` |
| out-08 | 4 (2/1/0/1) | 6 | `invented_facts` |
| out-09 | 3 (1/1/0/1) | 6 | — |
| out-10 | 6 (1/1/2/2) | 8 | `invented_facts` |
| out-11 | 3 (1/1/0/1) | 6 | `invented_facts`, `unacknowledged_source_loss` |
| out-12 | 4 (2/1/0/1) | 7 | — |
| out-13 | 4 (2/1/0/1) | 6 | `invented_facts` |
| out-14 | 5 (1/1/2/1) | 7 | `unacknowledged_source_loss` |

## 2. Decisive questions

`Q1` merged simplification and method/productivity; `Q2` promoted higher wages; `Q3` number of first-level actions; `Q4` placed the specified observations below actions; `Q5` explicitly noted omission of both comparison and opinion material; `Q6` stated the reader’s question literally.

| output | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
|---|---|---|---:|---|---|---|
| out-01 | No | No | 2 | No | No | No |
| out-02 | No | No | 2 | No | Yes | No |
| out-03 | No | No | 2 | No | Yes | No |
| out-04 | No | No | 2 | Yes | No | No |
| out-05 | No | No | 2 | No | No | Yes |
| out-06 | No | No | 2 | Yes | No | No |
| out-07 | No | No | 2 | No | No | No |
| out-08 | No | No | 2 | No | Yes | No |
| out-09 | No | No | 2 | No | Yes | No |
| out-10 | No | Yes | 3 | Yes | No | No |
| out-11 | No | No | 3 | No | No | Yes |
| out-12 | No | No | 2 | No | Yes | No |
| out-13 | No | No | 2 | No | Yes | No |
| out-14 | No | No | 3 | Yes | No | No |

## 3. Output notes

- **out-01:** Clear answer-first presentation, but it preserves the duplicate process/productivity split and discards the wage argument while failing to acknowledge the omitted management disagreement.
- **out-02:** The concise two-action study is well displayed, but its omission note explicitly misclassifies the evidence for the missing wage branch as a separate staffing issue.
- **out-03:** A non-action investigation branch disrupts the level structure, while “almost certainly” unnecessary stages and savings of “10% or more” exceed the source.
- **out-04:** Evidence is consistently placed beneath visible branches, but pay is subordinated to a methods study and unsupported printer differences and opportunity sizing are added.
- **out-05:** The literal question and named ranking are strengths, but urgency becomes a mixed-kind branch and several claims about lost work, cheap tests, and accumulating delay are unsupported.
- **out-06:** Staffing evidence remains beneath an action, but the recommendation is delayed and the claim that streamlining will restore competitiveness is stronger than the source.
- **out-07:** The two action headings are readable, but unsupported owners, early wins, and nonexistent production-run data accompany an incomplete omission note.
- **out-08:** Strong visual organization is outweighed by a fabricated benchmark interpretation, technologies, owners, timelines, metrics, and implementation plan.
- **out-09:** The memo is compact and factually restrained, but labeled setup precedes an incomplete answer and the wage evidence is deliberately kept outside the recommendation.
- **out-10:** This is the only output to elevate the pay/capacity issue into an action and it explicitly ranks the branches, but it retains the overlapping method branch and asserts certainty, magnitude, and causal conclusions absent from the source.
- **out-11:** The literal question and temporal pilot logic are visible, but benchmarking becomes an action while invented metrics, experimental details, and rollout claims replace the missing wage intervention.
- **out-12:** This is the cleanest restrained rewrite, though it explicitly removes the evidence needed to discover the wage branch and retains the duplicate two-study structure.
- **out-13:** The answer is immediate, but an urgency argument sits alongside actions and tentative savings and management willingness are overstated.
- **out-14:** Staffing, delay, and overtime evidence are visibly grouped, but “address capacity pressure” stops short of recommending competitive wages and the two-track top does not fully summarize its displayed branches.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Process simplification and method change remain duplicate branches | Core loop §6, MECE duplication test | ignored | out-01–out-14 |
| The wage action remains buried in staffing observations | Core loop §6, “promote the real branch from the observations” | ignored | all except out-10 |
| The reader’s question is not written literally | Core loop §§1 and 3 | ignored | all except out-05 and out-11 |
| The ordering principle is not named | Core loop §5, Order | ignored | all except out-05 and out-10 |
| Assertions exceed the supplied evidence | Mode 3, “Invent nothing” | ignored | out-03, out-04, out-05, out-06, out-07, out-08, out-10, out-11, out-13 |
| The omission statement fails to cover material actually lost | Mode 3, fact-retention rule | ignored | out-01, out-06, out-07, out-11, out-14 |

## 5. Observation

The stronger outputs keep a clear answer at the top, use action-shaped branches, and nest operational evidence visibly beneath them. The weaker outputs either promote context and urgency beside the actions or add unsupported implementation detail; across the set, the decisive shared structural miss is failure to recognize that process simplification and method change overlap and that competitive wages are the independent second action.

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
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
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
      "output": "out-03",
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
      "hard_failures": ["invented_facts"],
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
      "hard_failures": ["invented_facts"],
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
      "output": "out-05",
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
      "hard_failures": ["invented_facts"],
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
      "output": "out-06",
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
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
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
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-08",
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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-09",
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
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 1,
        "key_line_composition": 1,
        "levels": 2,
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
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": true
      }
    },
    {
      "output": "out-11",
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
        "explainable_order": 2,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
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
      "output": "out-12",
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
      "output": "out-13",
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
      "hard_failures": ["invented_facts"],
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
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 1,
        "levels": 2,
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
      "hard_failures": ["unacknowledged_source_loss"],
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