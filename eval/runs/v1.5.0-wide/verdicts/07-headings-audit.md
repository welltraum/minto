## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 3 (1/1/1/0) | 4 | — |
| out-02 | 6 (2/1/1/2) | 9 | — |
| out-03 | 2 (1/0/0/1) | 6 | `invented_facts` |
| out-04 | 5 (2/1/1/1) | 7 | — |
| out-05 | 6 (2/1/1/2) | 8 | — |
| out-06 | 6 (2/1/1/2) | 7 | — |
| out-07 | 4 (2/1/0/1) | 6 | — |
| out-08 | 6 (2/1/1/2) | 8 | — |

Structural sub-scores are shown as top/key-line composition/levels/order and kind.

## 2. Decisive questions

| output | Q1: topics, hence no key line | Q2: first sentence is a topic | Q3: `Background` abstraction | Q4: both nesting errors | Q5: six first-level topics | Q6: body-dependent or content-seeking findings | Q7: invented quotations, locations, or contents | Q8: diagnosis-only with apparatus |
|---|---|---|---|---|---|---|---|---|
| out-01 | No | Yes | No | No | No | None; the body limitation is appropriately acknowledged. | No | Diagnosis-only, but apparatus missing |
| out-02 | Yes | Yes | Yes | No | Yes | The proposed `Definition` demotion, Principles/Organization overlap, and benefit-size ranking exceed the visible evidence; the overlap is qualified. | No | Yes |
| out-03 | No | Yes | No | No | No | The exact “decision question” and demand for additional SCQ content are not grounded in the excerpt. | Yes—invented line numbers | Yes |
| out-04 | No | Yes | Yes | No | No | The claimed dependency between benefits and success prerequisites is speculative. | No | Diagnosis-only, but apparatus missing |
| out-05 | No | Yes | No | No | Yes | The score’s assertion of clear gaps and overlaps is unsupported by a visible example. | No | Yes |
| out-06 | Yes | Yes | Yes | No | No | None; uncertainty about the unavailable body is handled correctly. | No | Diagnosis-only, but apparatus missing |
| out-07 | No | Yes | Yes | No | No | The asserted Background/Principles overlap, scattered related content, and unjustified scope shift depend on unseen section content. | No | Diagnosis-only, but apparatus missing |
| out-08 | Yes | Yes | No | No | Yes | The possible Organization/Conditions overlap depends on the body, but is explicitly marked unverified. | No | Yes |

## 3. Output notes

- **out-01:** Concise and appropriately scoped, but it buries the missing governing point and overlooks the count, `Background`, and nesting defects.
- **out-02:** The most complete audit apparatus and strongest prioritization, though several proposed relationships and the benefit-ranking fix overreach the visible evidence.
- **out-03:** It concentrates almost entirely on the introduction, wrongly treats the headings as same-kind, and invents line locations.
- **out-04:** It recognizes the weak opening and uneven abstraction, but substitutes grammatical parallelism and speculative narrative sequencing for the key-line and nesting diagnoses.
- **out-05:** It clearly flags the weak top, mixed group, excessive count, and absent order, but its unsupported MECE verdict and omission of the specific nesting problems weaken it.
- **out-06:** It gives the clearest explanation that topic headings cannot communicate a key line and handles the missing body cautiously, but omits the count and likely nesting errors as well as the required apparatus.
- **out-07:** It identifies the weak opening, abstraction mismatch, and absent ordering, but its MECE claims infer relationships inside unavailable sections.
- **out-08:** It is disciplined, visibly structured, and cautious about uncertainty, but misses `Background` and both likely nesting relationships.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Failure to state that topic headings cannot constitute a key line | Core loop §4 and Mode 2 — Horizontal | ignored | out-01, out-03, out-04, out-05, out-07 |
| Failure to isolate `Background` as a wrong-level introduction element | Canon — Introduction anti-patterns; Mode 2 — Vertical | ignored | out-01, out-03, out-05, out-08 |
| Failure to identify both likely parent-child relationships | Mode 2 — Vertical and MECE | vague | out-01–out-08 |
| Failure to flag the excessive first-level count | Core loop §4; Limits — Three or four | ignored | out-01, out-03, out-04, out-06, out-07 |
| Missing annotated text, findings table, score, or highest-value fixes | Mode 2 — Deliver, in this order | ignored | out-01, out-04, out-06, out-07 |
| Claims about relationships that require the unavailable body | Core loop §8; Mode 2 — findings must be structural defects | ignored | out-02, out-03, out-04, out-05, out-07, out-08 |

## 5. Observation

Stronger outputs distinguish the two critical defects—the topic-only opening and topic-only setout—then assess abstraction, group count, and order with explicit scope limits and visible audit apparatus. Weaker outputs either reduce the problem to generic parallelism and SCQ advice or infer overlaps and section relationships that the unavailable body cannot establish.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "07-headings-audit",
  "mode": "audit",
  "outputs": [
    {
      "output": "out-01",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 0
      },
      "quality": {
        "total": 4,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 0,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    },
    {
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    },
    {
      "output": "out-03",
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
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
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
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": false
      }
    },
    {
      "output": "out-05",
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
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    },
    {
      "output": "out-07",
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
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    },
    {
      "output": "out-08",
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
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    }
  ]
}
```