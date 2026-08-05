## 1. Score table

Structural sub-scores are shown as `(top/key line/levels/order-kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 8 (2/2/2/2) | 9 | — |
| out-02 | 5 (1/2/0/2) | 6 | `unacknowledged_source_loss` |
| out-03 | 7 (2/2/1/2) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-04 | 8 (2/2/2/2) | 9 | — |
| out-05 | 6 (2/2/1/1) | 8 | — |
| out-06 | 5 (2/1/1/1) | 7 | — |
| out-07 | 8 (2/2/2/2) | 9 | `invented_facts` |
| out-08 | 7 (2/2/1/2) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-09 | 8 (2/2/2/2) | 9 | `invented_facts` |
| out-10 | 7 (2/2/1/2) | 8 | `unacknowledged_source_loss` |
| out-11 | 6 (2/2/1/1) | 7 | — |
| out-12 | 8 (2/2/2/2) | 9 | `invented_facts` |
| out-13 | 6 (2/2/0/2) | 7 | `invented_facts`, `unacknowledged_source_loss` |
| out-14 | 8 (2/2/2/2) | 9 | — |

## 2. Decisive questions

| output | Diagram? | Exactly two first-level actions? | First-level kind | Observations under correct action? | Unrequested file/HTML? | Memo rewritten? | Unsupported nodes added |
|---|---|---|---|---|---|---|---|
| out-01 | Yes | Yes | Actions | Yes | No | No | None |
| out-02 | Yes, text diagram | Yes | Actions | Yes, for the material retained | No | No | None |
| out-03 | Yes | Yes | Actions | Yes | No | No | “Simple jobs can use fewer checks” and the competitive-pay result are stated with unsupported certainty |
| out-04 | Yes | Yes | Actions | Yes | No | No | None |
| out-05 | Yes | Yes | Actions | Partly; wage evidence is incorrectly chained instead of grouped as siblings | No | No | None, though the wage-branch relationships are unsupported |
| out-06 | Yes, text diagram | No; it has three branches | Mixed: one context branch and two actions | No; context is promoted to the first level | No | No | None |
| out-07 | Yes, text diagram | Yes | Actions | Yes | No | No | Competitive pay is presented as certainly enabling hiring and removing the premium |
| out-08 | Yes | Yes | Actions | Yes, for the material retained | No | No | Competitive pay is presented as a certain result; the ranking rationale is also unsupported |
| out-09 | Yes | Yes | Actions | Yes | No | No; it reproduces the memo for annotation | Competitive pay is presented as certainly producing the stated results |
| out-10 | Yes | Yes | Actions | Yes, for the material retained | No | No | None |
| out-11 | Yes, text diagram | Yes | Actions | Partly; alignment misattaches the methods study and potential saving | No | No | None |
| out-12 | Yes, text diagram | Yes | Actions | Yes | No | No | It attributes the benchmark gap to uniform checks and turns the wage outcome into certainty |
| out-13 | Yes, text diagram | Yes | Actions | Partly; the 10% saving is attached to the methods study | No | No | The competitive-pay outcome is presented as certain |
| out-14 | Yes, text diagram | Yes | Actions | Yes | No | No | None |

## 3. Output notes

- **out-01:** Complete source-grounded hierarchy with both a readable outline and an accurate Mermaid pyramid.
- **out-02:** The two actions are clear, but much of the methods-study and wage-branch evidence disappears.
- **out-03:** The hierarchy is clean, but it omits material support and hardens experimental or expected outcomes into facts.
- **out-04:** Closely matches the gold structure and preserves the memo’s qualifications and supporting details.
- **out-05:** The key line is correct, but the wage evidence is rendered as a causal chain rather than parallel support.
- **out-06:** A source-supported context block is incorrectly promoted beside the two actions.
- **out-07:** The diagram is comprehensive, but the competitive-pay outcome loses the source’s tentative modality.
- **out-08:** The pyramid is concise, but it drops several supports and supplies a weak ranking interpretation.
- **out-09:** It preserves the source, though the violation markers are unnecessary and the diagram overstates the wage outcome.
- **out-10:** The main branches are right, but the methods study, union pressure, and exact uniform-check observation are lost.
- **out-11:** The two-action skeleton is correct, while the crowded lower layout obscures which evidence supports which claim.
- **out-12:** It is concise and nearly complete, but adds an unsupported causal link and converts “should” into “will.”
- **out-13:** Several required observations disappear, and the 10% saving is incorrectly grouped with the methods study.
- **out-14:** A clear and proportionate text pyramid preserves the two actions and the material gold support.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Material supporting observations omitted | Core loop §8, source-grounding check | ignored | 5: out-02, out-03, out-08, out-10, out-13 |
| Tentative or conditional claims converted into certainty | Core loop §8 and “Invent nothing” | ignored | 6: out-03, out-07, out-08, out-09, out-12, out-13 |
| Supporting evidence chained or attached to the wrong parent | Core loop §2 and §6 | ignored | 3: out-05, out-11, out-13 |
| Ordering principle absent, weak, or incorrectly diagnosed | Core loop §5 | ignored | 14: out-01–out-14 |

## 5. Observation

Stronger outputs retain exactly two action branches, keep the observations as parallel support under the correct action, and preserve tentative language; weaker outputs promote context, serially chain evidence, omit material observations, or turn expected outcomes into certainties.

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
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 2,
        "levels": 0,
        "order_and_kind": 2
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
      "output": "out-03",
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
      "output": "out-04",
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
      "output": "out-05",
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
      "output": "out-09",
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
    },
    {
      "output": "out-10",
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
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
        "order_type_named": "na"
      }
    },
    {
      "output": "out-12",
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
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 0,
        "order_and_kind": 2
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
      "output": "out-14",
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
    }
  ]
}
```