## 1. Score table

Structural sub-scores are shown as `(top, key line, levels, order/kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 3 (1, 1, 0, 1) | 7 | — |
| out-02 | 1 (1, 0, 0, 0) | 8 | — |
| out-03 | 3 (1, 1, 0, 1) | 6 | `invented_facts`, `unacknowledged_source_loss` |
| out-04 | 1 (1, 0, 0, 0) | 6 | `invented_facts`, `more_than_four_first_level` |
| out-05 | 4 (1, 1, 1, 1) | 8 | — |
| out-06 | 4 (1, 1, 1, 1) | 8 | — |
| out-07 | 0 (0, 0, 0, 0) | 5 | `unacknowledged_source_loss` |
| out-08 | 0 (0, 0, 0, 0) | 5 | `more_than_four_first_level` |
| out-09 | 6 (2, 1, 1, 2) | 10 | `invented_facts` |
| out-10 | 5 (2, 1, 1, 1) | 9 | — |
| out-11 | 2 (1, 0, 0, 1) | 8 | `invented_facts`, `more_than_four_first_level` |
| out-12 | 1 (1, 0, 0, 0) | 7 | `more_than_four_first_level` |
| out-13 | 0 (0, 0, 0, 0) | 6 | — |
| out-14 | 2 (2, 0, 0, 0) | 8 | `invented_facts`, `more_than_four_first_level` |
| out-15 | 1 (1, 0, 0, 0) | 7 | `more_than_four_first_level` |
| out-16 | 1 (1, 0, 0, 0) | 7 | — |

## 2. Decisive questions

Columns correspond to the eight supplied questions.

| output | 1. Kind | 2. Unchanged | 3. Transition branch | 4. Purpose gone | 5. Top answers change | 6. SCQ contradicts | 7. Source retained | 8. Invented facts |
|---|---|---:|---|---|---|---|---|---|
| out-01 | actions | 3 | yes, merged | yes | partly | no | yes | none |
| out-02 | topics/reasons | 3 | yes | no | no | no | yes | none |
| out-03 | actions | 4 | no | yes | partly | no | no; transition lost | “considerable time,” blurred boundaries, and diversity benefits |
| out-04 | topics/reasons | 5 | yes | yes | partly | no | yes | Executive Committee freed for policy/planning; outside directors characterized as passive |
| out-05 | actions | 2 | yes | no | partly | no | yes | none |
| out-06 | actions | 2 | yes | yes | yes | no | yes | none |
| out-07 | topics/reasons | 4 | no | yes | no | no | no; transition lost | none |
| out-08 | mixed | 5 | yes | yes | no | no | yes | none |
| out-09 | actions | 2 | yes | yes | yes | no | yes | Board meetings as the venue; unsupported claims about outside-director judgement |
| out-10 | actions | 2 | yes | yes | yes | no | yes | none |
| out-11 | topics/reasons | 5 | yes | yes | partly | no | yes | “most of its time,” outside-director benefits and prerequisites, and an asserted effect on transition speed |
| out-12 | topics/reasons | 5 | yes | no | partly | no | yes | none |
| out-13 | topics/reasons | 4 | no; document-level | no | no | no | yes | none |
| out-14 | topics/reasons | 5 | yes | no | yes | no | yes | Executive Committee assigned day-to-day operational duties |
| out-15 | topics/reasons | 5 | yes | yes | partly | no | yes | none |
| out-16 | topics/reasons | 3 | yes | yes | partly | no | yes | none |

## 3. Output notes

- **out-01:** It converts the topics into imperatives, but retains the old hierarchy and falsely combines tenure with transition.
- **out-02:** The SCQ is grounded and the membership details are consolidated, but the governing question is weakened to what the Board should discuss.
- **out-03:** Its visible action list is undermined by losing transition and by adding unsupported governance benefits.
- **out-04:** Four stated aspects plus a separate “remaining question” recreate all five source branches instead of subordinating them.
- **out-05:** Three compact action headings improve grouping, though the transition remains a first-level action and the memorandum-purpose frame survives.
- **out-06:** Role, membership, and transition form a coherent three-part action list, but they do not recover the gold actions.
- **out-07:** This is essentially the first four source topics with a stronger lead-in; transition disappears.
- **out-08:** The four numbered topics and appended transition still amount to the original five-part topic list.
- **out-09:** It provides the clearest controlling answer and the only explicitly justified sequence, while promoting transition and adding unsupported claims.
- **out-10:** The three actions are concise, mutually distinct, and sensibly sequenced, but membership substitutes for the required outside-director and internal-operation changes.
- **out-11:** Dependency explanations make the order unusually intelligible, but five questions preserve the source hierarchy and several supporting assertions are invented.
- **out-12:** The recommendation is answer-first, yet the support is an unchanged five-topic agenda with no SCQ grounding.
- **out-13:** It correctly treats transition as applying to the document rather than as a numbered branch, but the key line remains four questions rather than changes.
- **out-14:** The key message is explicit, but both it and the list preserve five topic-level elements and introduce an unsupported Executive Committee role.
- **out-15:** The desired Board focus appears immediately, but the five original questions remain first-level support.
- **out-16:** Combining composition with selection and tenure reduces the list to four, but it remains a topic agenda and still promotes transition.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Source topics remain first-level instead of becoming supporting evidence under actions | Core loop §4, “Groups” | ignored | out-02, out-04, out-07, out-08, out-11, out-12, out-13, out-14, out-15, out-16 |
| Transition is promoted as an independent branch | Core loop §6, “MECE” | ignored | out-01, out-02, out-04, out-05, out-06, out-08, out-09, out-10, out-11, out-12, out-14, out-15, out-16 |
| The governing reader question is not written literally | Core loop §1, “Topic → reader question” | ignored | out-04 through out-16 |
| Purpose or discussion framing survives | Introduction anti-patterns, “Statement of purpose” | ignored | out-02, out-05, out-12, out-13, out-14 |
| Unsupported facts or causal claims are added | Mode 3, “Invent nothing” | ignored | out-03, out-04, out-09, out-11, out-14 |
| A source topic disappears without acknowledgement | Mode 3, “Keep every fact from the source” | ignored | out-03, out-07 |

## 5. Observation

The stronger outputs replace the source agenda with a small set of verbs, group related membership evidence beneath one parent, and provide a defensible sequence. The weaker outputs mainly improve the introduction while leaving the original five topics—especially transition—at the first level.

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
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 8,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-04",
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
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-05",
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
        "explainable_order": 1,
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
        "order_type_named": false,
        "scq_intro_present": false
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
        "total": 8,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
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
      "output": "out-07",
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
        "mece": 0,
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
        "scq_intro_present": true
      }
    },
    {
      "output": "out-08",
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
        "same_kind_grouping": 1,
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
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
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
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
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
      "output": "out-11",
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
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-12",
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
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
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
      "output": "out-13",
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
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
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
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
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
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
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
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 2,
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
    }
  ]
}
```