## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 1 (1, 0, 0, 0) | 7 | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-02 | 5 (2, 1, 1, 1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-03 | 2 (1, 0, 1, 0) | 7 | — |
| out-04 | 0 (0, 0, 0, 0) | 6 | `unacknowledged_source_loss` |
| out-05 | 1 (1, 0, 0, 0) | 7 | `invented_facts`, `more_than_four_first_level` |
| out-06 | 1 (1, 0, 0, 0) | 6 | `unacknowledged_source_loss` |
| out-07 | 4 (1, 1, 1, 1) | 7 | — |
| out-08 | 5 (2, 1, 1, 1) | 8 | `unacknowledged_source_loss` |
| out-09 | 0 (0, 0, 0, 0) | 6 | — |
| out-10 | 1 (1, 0, 0, 0) | 7 | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-11 | 3 (1, 1, 0, 1) | 7 | `more_than_four_first_level` |
| out-12 | 0 (0, 0, 0, 0) | 5 | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-13 | 4 (1, 1, 1, 1) | 8 | `invented_facts` |
| out-14 | 0 (0, 0, 0, 0) | 6 | `invented_facts` |
| out-15 | 1 (1, 0, 0, 0) | 7 | `unacknowledged_source_loss` |
| out-16 | 1 (1, 0, 0, 0) | 7 | `unacknowledged_source_loss` |

## 2. Decisive questions

| output | First-level kind | Source topics unchanged at first level | Transition branch? | Purpose gone? | Top answers required change? | SCQ contradicts context? | All source topics retained? | Invented facts |
|---|---|---:|---|---|---|---|---|---|
| out-01 | topics/reasons | 5 | Yes | Yes | No | No | Yes | None |
| out-02 | actions | 4 | Yes | Yes | Yes | No | No—outside participation is lost | “Considerable time” is an unsupported quantification |
| out-03 | topics/reasons | 5 | Yes | Yes | Yes, but vaguely | No | Yes | None |
| out-04 | topics/reasons | 5 | Yes | No | No | No | Yes | None |
| out-05 | topics/reasons | 5 | Yes | Yes | No | No | Yes | “Most of its time” |
| out-06 | mixed | 4 | No; it is a trailing consequence | Yes | Yes, incompletely | No | Yes | None |
| out-07 | actions | 4 | Yes | Yes | Yes, but vaguely | No | Yes | None |
| out-08 | actions | 5 | Yes | Yes | Yes | No | Yes | None |
| out-09 | topics/reasons | 5 | Yes, merged into item 4 | Yes | No | No | Yes | None |
| out-10 | topics/reasons | 5 | Yes | Yes | No | No | Yes | None |
| out-11 | actions | 5 | Yes | Yes | Yes, through the list rather than a single top | No | Yes | None |
| out-12 | topics/reasons | 5 | Yes | Yes | No | No | Yes | None |
| out-13 | actions | 1 | Yes | Yes | Yes, but incompletely | No | Yes | “Spend its meetings” and the claimed reorganization intention |
| out-14 | topics/reasons | 4 | No; it remains document-wide | No | No | No | Yes | “Much of its time” |
| out-15 | topics/reasons | 5 | Yes | Yes | Yes, but incompletely | No | Yes | None |
| out-16 | topics/reasons | 1 | Yes | No | No | No | Yes | None |

## 3. Output notes

- **out-01:** It opens with a useful conclusion but immediately reproduces all five agenda topics and loses the short-term-operational complication.
- **out-02:** It supplies a strong action-oriented top and three visible branches, but omits outside-director participation and treats transition as a substantive action.
- **out-03:** The SCQ is well grounded, yet the key line remains three governance topics rather than the changes required by the gold.
- **out-04:** The purpose-led opening and topic hierarchy preserve the original agenda logic while dropping most of the supplied context.
- **out-05:** It presents the source faithfully as five questions, but neither converts them into actions nor avoids unsupported quantification.
- **out-06:** The answer-first opening is useful, but its first level mixes topics with an action and omits the Board’s longstanding operational preoccupation.
- **out-07:** It has a complete SCQ and nests several source details, though composition and transition still occupy the key line instead of supporting the required changes.
- **out-08:** This is concise and answer-first, but it largely converts the original topics into imperative wording without deriving the gold action structure.
- **out-09:** Its explicit reader question and full context are strengths, but the answer is only a list of design topics.
- **out-10:** It states the desired shift promptly, then reproduces the five-question agenda without the reorganization context.
- **out-11:** It visibly presents actions, but uses five first-level items, exposes SCQ labels, and lacks a single controlling answer above the list.
- **out-12:** It is compact and source-faithful at the topic level, but drops the longstanding operational complication and leaves all five topics unchanged.
- **out-13:** It provides the strongest supporting hierarchy and action phrasing, but wrongly promotes transition and introduces unsupported claims about meetings and intent.
- **out-14:** It offers a sound SCQ frame, yet stops at four questions and retains a purpose-style closing sentence.
- **out-15:** Its opening gives direction, but the key line remains four agenda topics and the operational complication disappears.
- **out-16:** It groups the source material cleanly beneath three headings, but those headings remain topics, transition stays a branch, and the historical complication is weakened.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Original agenda topics remain at the first level instead of becoming support for actions | Core loop §4, Groups | ignored | 11: out-01, out-03, out-04, out-05, out-06, out-09, out-10, out-12, out-14, out-15, out-16 |
| “Alternative ways to get there” remains a substantive branch | Core loop §6, MECE | ignored | 14: out-01, out-02, out-03, out-04, out-05, out-07, out-08, out-09, out-10, out-11, out-12, out-13, out-15, out-16 |
| The required action to formalize Board operation through policies and procedures is absent | Core loop §4, deriving actions from source mechanics | missing | 16: all outputs |
| The answer does not appear in the first sentence | Core loop §3 and Mode 3 answer-first rendering | buried | 11: out-02, out-03, out-04, out-05, out-07, out-09, out-11, out-12, out-13, out-14, out-15 |
| The ordering principle is never named | Core loop §5 versus Mode 3 delivery guidance | buried | 16: all outputs |
| Supplied context or a source topic disappears without acknowledgement | Mode 3, “Keep every fact from the source” | ignored | 8: out-01, out-02, out-04, out-06, out-08, out-10, out-12, out-15, out-16 |

## 5. Observation

Stronger outputs derive a small set of visible actions from the agenda and place composition, tenure, role boundaries, and outside participation underneath them. Weaker outputs merely shorten, merge, or rephrase the five original topics, usually leaving transition as another branch rather than treating it as a document-wide implementation concern.

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
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "unacknowledged_source_loss",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-02",
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
        "answer_first": false,
        "first_level_count": 3,
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
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 1,
        "order_and_kind": 0
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
        "answer_first": false,
        "first_level_count": 3,
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
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 0,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 6,
        "top": 0,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
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
        "order_type_named": false,
        "scq_intro_present": false
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 2,
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
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
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
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
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
        "total": 4,
        "top": 1,
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
        "answer_first": false,
        "first_level_count": 3,
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
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 0,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 6,
        "top": 0,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": false,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "unacknowledged_source_loss",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": false
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 5,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-12",
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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [
        "unacknowledged_source_loss",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
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
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 0,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 6,
        "top": 0,
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
      "output": "out-15",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-16",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 7,
        "top": 1,
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
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    }
  ]
}
```