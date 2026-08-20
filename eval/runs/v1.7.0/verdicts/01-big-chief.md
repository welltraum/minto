## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2, 1, 2, 1) | 9 (2, 2, 1, 2, 2) | `invented_facts` |
| out-02 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-03 | 2 (1, 0, 0, 1) | 8 (1, 2, 2, 2, 1) | — |
| out-04 | 3 (2, 0, 0, 1) | 8 (2, 2, 2, 1, 1) | `invented_facts`, `unacknowledged_source_loss` |
| out-05 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-06 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-07 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-08 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-09 | 1 (0, 0, 0, 1) | 8 (0, 2, 2, 2, 2) | — |
| out-10 | 3 (2, 0, 0, 1) | 8 (2, 2, 2, 1, 1) | `invented_facts`, `unacknowledged_source_loss` |
| out-11 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-12 | 1 (0, 0, 0, 1) | 8 (0, 2, 2, 2, 2) | — |
| out-13 | 1 (0, 0, 0, 1) | 8 (0, 2, 2, 2, 2) | — |
| out-14 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-15 | 1 (0, 0, 0, 1) | 8 (0, 2, 2, 2, 2) | — |
| out-16 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |

## 2. Decisive questions

| output | First-level kind | Grounded elements | Acceptance answered? | Invented facts or benefits | Details below key line? | Literal reader question? |
|---|---|---:|---|---|---|---|
| out-01 | benefits | 2 | Yes | The categorical claim that nothing changes on the company’s side; the control claim is supportable from pre-processing balancing. | Yes | No |
| out-02 | mechanics | 3 | No—only feasibility is answered. | None | No | No |
| out-03 | mechanics | 3 | No—only ability to process is answered. | None | No | No |
| out-04 | mechanics | 3 | Yes | “Labor-intensive,” a separate payment for every ticket, mailing to the lockbox, and immediate insertion of missing identifiers; the coordination call is also unsupported new operational material. | No | Yes |
| out-05 | mechanics | 3 | No—only ability to accommodate is answered. | None | No | No |
| out-06 | mechanics | 3 | No—only implementability is answered. | None | No | No |
| out-07 | mechanics | 3 | No—only ability to accommodate is answered. | None | No | No |
| out-08 | mechanics | 3 | No—only processability is answered. | None | No | No |
| out-09 | mechanics | 3 | No recommendation or acceptance answer appears. | None | No | No |
| out-10 | mechanics | 3 | Yes | Adding identifiers before processing, mailing the cheque and listing, and the new checklist/action apparatus. | No | No |
| out-11 | mechanics | 3 | No—only implementability is answered. | None | No | No |
| out-12 | mechanics | 3 | No recommendation or acceptance answer appears. | None | No | No |
| out-13 | mechanics | 3 | No recommendation or acceptance answer appears. | None | No | No |
| out-14 | mechanics | 3 | No—only ability to handle the process is answered. | None | No | No |
| out-15 | mechanics | 3 | No recommendation or acceptance answer appears. | None | No | No |
| out-16 | mechanics | 3 | No—only ability to accommodate is answered. | None | No | No |

## 3. Output notes

- out-01 is the only output that consistently elevates reader outcomes above the mechanics, but its broad no-change assertion exceeds the evidence.
- out-02 is a concise and complete process summary whose conditional-feasibility top stops short of recommending acceptance.
- out-03 preserves the process but leaves its hierarchy largely implicit and answers whether processing is possible rather than whether approval is warranted.
- out-04 states the decision and the reader’s literal question, but SCQ labels over-structure the note and unsupported operational claims weaken it.
- out-05 is visibly organized around implementation steps, leaving the management rationale unstated.
- out-06 has a clear chronological workflow beneath an implementability statement, but no acceptance case.
- out-07 cleanly divides work by setup and organizational responsibility, yet remains a process description.
- out-08 is compact and complete, but its bullets promote conditions and workflow to the key line.
- out-09 never reaches a management answer, opening with scope and proceeding directly into mechanics.
- out-10 recommends acceptance, but repeats the conditions as new actions and alters the timing of identifier supplementation.
- out-11 presents coherent conditions and processing detail, though “can implement” does not settle whether management should approve.
- out-12 is a faithful operating specification without a controlling decision.
- out-13 explicitly exposes the chronological order, but that order answers how the process works rather than why it should be accepted.
- out-14 turns the workflow into clear imperatives, which improves actionability without supplying acceptance reasons.
- out-15 clearly names a sequential process while omitting the management conclusion.
- out-16 comes closest to turning mechanics into reasons, but its “can” formulations remain system capabilities rather than reader benefits.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Feasibility replaces or omits the acceptance decision | Core loop §§1–2; self-check 1 | ignored | out-02, out-03, out-05–out-09, out-11–out-16 |
| Mechanics occupy the first level instead of grounded reasons for acceptance | Core loop §4; self-check 1 | ignored | out-02–out-16 |
| The reader’s question is not written literally | Core loop §§1 and 3 | missing | out-01–out-03, out-05–out-16 |
| The ordering principle is not named | Core loop §5 | missing | out-01–out-12, out-14, out-16 |
| Situation and complication are not both visible before support | Core loop §3 | missing | out-05, out-10 |
| Unsupported facts or operational claims are introduced | Mode 3, “Invent nothing” | ignored | out-01, out-04, out-10 |
| The source’s later-submission timing for supplied identifiers is changed or lost | Mode 3, “Keep every fact” | ignored | out-04, out-10 |

## 5. Observation

The stronger output separates the acceptance rationale from its evidence: reader outcomes form the key line, while fields, routing, balancing, and system processing sit underneath. The weaker outputs often preserve and organize the source mechanics very well, but merely turn the original operating sequence into a tidy list without closing management’s decision question.

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
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
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
      "hard_failures": ["invented_facts"],
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
      "output": "out-02",
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
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
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
        "order_type_named": false,
        "scq_intro_present": false
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
        "order_type_named": false,
        "scq_intro_present": true
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
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 0,
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
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
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
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-12",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 0,
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
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 0,
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
        "order_type_named": true,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-14",
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
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-15",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 0,
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
        "order_type_named": true,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-16",
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
        "order_type_named": false,
        "scq_intro_present": true
      }
    }
  ]
}
```