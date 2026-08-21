## 1. Score table

Structural sub-scores are shown as `(top, key-line composition, levels, order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 2 (1, 0, 0, 1) | 3 | — |
| out-02 | 4 (2, 1, 0, 1) | 6 | — |
| out-03 | 2 (1, 0, 0, 1) | 4 | — |
| out-04 | 6 (2, 1, 1, 2) | 9 | `invented_facts` |
| out-05 | 6 (2, 1, 1, 2) | 8 | — |
| out-06 | 4 (1, 1, 0, 2) | 8 | — |
| out-07 | 2 (1, 0, 0, 1) | 5 | — |
| out-08 | 5 (2, 1, 1, 1) | 7 | — |
| out-09 | 2 (1, 0, 0, 1) | 5 | — |
| out-10 | 5 (2, 1, 0, 2) | 8 | — |
| out-11 | 4 (1, 1, 0, 2) | 8 | — |
| out-12 | 6 (2, 1, 1, 2) | 8 | — |
| out-13 | 4 (1, 1, 0, 2) | 8 | — |
| out-14 | 4 (1, 1, 1, 1) | 6 | — |
| out-15 | 2 (1, 0, 0, 1) | 4 | — |
| out-16 | 5 (1, 1, 1, 2) | 7 | `invented_facts` |

## 2. Decisive questions

`Q8` reports diagnosis-only compliance first, then whether the full audit apparatus was supplied.

| output | Q1 Topics, hence no key line? | Q2 Opening is topic statement? | Q3 `Background` level? | Q4 Both nesting errors? | Q5 Six first-level topics? | Q6 Body-dependent findings or content wishes | Q7 Invented material? | Q8 Diagnosis / apparatus |
|---|---|---|---|---|---|---|---|---|
| out-01 | No | Yes | No | No | No | The grammatical-parallelism complaint is unsupported by the visible noun-phrase headings. | No | Yes / No |
| out-02 | Yes | Yes | No | No | No | None material. | No | Yes / No |
| out-03 | No | Yes | No | No | No | Adding SCQ material and claims that the setout is not headings are content/format wishes rather than grounded findings. | No | Yes / Yes |
| out-04 | No | Yes | Yes | No | No | The claimed implementation-how-to gap depends on unavailable content. | Yes—two unsupported illustrative answer quotations. | Yes / Yes |
| out-05 | Yes | Yes | Yes | No | Yes | The alleged Definition/Principles overlap and “six different questions” depend on assumed contents; SCQ and reader requests are content wishes. | No | Yes / Yes |
| out-06 | No | Yes | No | No | Yes | The Benefits/Conditions overlap is speculative and differs from the visible nesting issue. | No | Yes / Yes |
| out-07 | No | Yes | No | No | No | Both proposed overlap patterns and the prerequisite ordering are speculative. | No | Yes / No |
| out-08 | No | Yes | Yes | No | Yes | “No support” under every heading, adding claims, and several overlap assertions rely on the unavailable body. | No | Yes / Yes |
| out-09 | No | Yes | No | No | No | The claim that conditions must precede implementation and organization is inferred rather than established. | No | Yes / No |
| out-10 | Yes | Yes | No | No | No | None; it explicitly reserves conclusions about the unavailable body. | No | Yes / No |
| out-11 | No | Yes | No | No | Yes | The generic claim of gaps and overlaps is not demonstrated from the setout. | No | Yes / Yes |
| out-12 | Yes | Yes | Yes | No | Yes | The Definition/Principles overlap and exact subordination of Organization are inferred from unseen contents. | No | Yes / No |
| out-13 | No | Yes | No | No | Yes | The high-risk CE finding merely asks that unseen boundaries and coverage be verified. | No | Yes / Yes |
| out-14 | No | Yes | Yes | No | Yes | None material; the compound-heading criticism rests on visible wording. | No | Yes / No |
| out-15 | No | Yes | No | No | No | The grammatical inconsistency is weak, and the requested conceptual bridge is a content wish. | No | Yes / No |
| out-16 | No | Yes | Yes | No | No | It assumes an adoption decision, requests missing SCQ facts, and speculates about overlap among three sections. | Yes—an unsupported illustrative answer quotation. | Yes / Yes |

## 3. Output notes

- **out-01:** It recognizes the flat list and weak opening but substitutes a doubtful grammatical-parallelism complaint for the decisive topic-versus-idea diagnosis.
- **out-02:** It captures both critical defects succinctly, but misses the abstraction, nesting, and display-count problems and omits the audit apparatus.
- **out-03:** Its apparatus is complete, but the findings drift toward adding SCQ content and changing heading formatting while missing most of the gold structure.
- **out-04:** It presents a clear, well-ordered audit and notices `Background` as context, but invents candidate answer quotations and misses the named nesting relationships.
- **out-05:** It is the most comprehensive apparatus-led audit, with strong scope caution and count diagnosis, though several overlap and reader-question claims outrun the visible evidence.
- **out-06:** It is compact and structurally legible, but replaces the gold nesting analysis with a speculative Benefits/Conditions overlap.
- **out-07:** It identifies the missing governing message but devotes too much weight to speculative overlaps and grammatical parallelism.
- **out-08:** It has strong visible apparatus and catches the count and `Background`, but repeatedly treats the unavailable body as if support were absent.
- **out-09:** It is diagnosis-only but very incomplete, leading with an unsupported prerequisite-order claim and supplying none of the required apparatus.
- **out-10:** It states the core topic-versus-idea defect especially clearly and handles source limits well, but omits the level, count, nesting, and apparatus requirements.
- **out-11:** Its audit form is disciplined and it catches the count, mixed kinds, and order, but does not articulate why topic headings leave no key line.
- **out-12:** It offers the strongest stand-alone verdict and good source restraint, although its substitute nesting theories are not the two relationships named in the gold and it lacks apparatus.
- **out-13:** It is mode-compliant and complete in form, but remains generic on levels and nesting and overstates the visible MECE evidence.
- **out-14:** It notices `Background`, the excessive flat setout, and the source boundary, but does not explicitly make the decisive topics-to-no-key-line inference.
- **out-15:** It finds the weak opening and absent order, but the parallelism complaint is weak and the audit is structurally incomplete.
- **out-16:** It catches the opening, `Background`, mixed kinds, and order with full apparatus, but assumes a decision context and supplies an unsupported answer quotation.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Failure to state explicitly that topic headings cannot compose a key line | Mode 2 — Top; Core loop — Groups | ignored | out-01, out-03, out-04, out-06–out-09, out-11, out-13–out-16 |
| Failure to recover both likely parent-child relationships | Mode 2 — Vertical and MECE | vague | all outputs |
| Omission of markers, findings table, score, or highest-value fixes | Mode 2 — required delivery order | ignored | out-01, out-02, out-07, out-09, out-10, out-12, out-14, out-15 |
| Findings or fixes that demand unseen SCQ, support, gaps, or section contents | Mode 2 — “finding is a structural defect, not a wish for more content” | ignored | out-03–out-09, out-11–out-13, out-15, out-16 |
| Failure to flag the excessive first-level count | Core loop — Groups; Limits | buried | out-01–out-04, out-07, out-09, out-10, out-15, out-16 |

## 5. Observation

Stronger outputs explicitly connect topic-only headings to the absence of a key line, distinguish context from argument level, name an ordering principle, flag the excessive flat setout, and preserve uncertainty about the missing body. Weaker outputs give generic flat-list or parallelism criticism, infer unseen section contents, or omit the prescribed audit apparatus.

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
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 3,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 0
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 0
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
        "order_type_named": false,
        "scq_intro_present": "na"
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
        "total": 4,
        "top": 1,
        "same_kind_grouping": 0,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": false,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-04",
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
        "order_type_named": true,
        "scq_intro_present": "na"
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
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
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
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
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
        "total": 5,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": false,
        "scq_intro_present": "na"
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
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 1,
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
        "order_type_named": false,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-11",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
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
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-12",
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
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
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
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-14",
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
        "top": 1,
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
        "order_type_named": false,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-15",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 4,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-16",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    }
  ]
}
```