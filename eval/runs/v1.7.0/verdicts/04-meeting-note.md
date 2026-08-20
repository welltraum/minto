## 1. Score table

Parentheses show `(top, key-line composition, levels, order and kind)` for Structure and `(top, same-kind grouping, order, MECE, visible structure)` for Quality.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 5 (2,1,1,1) | 9 (2,1,2,2,2) | `invented_facts` |
| out-02 | 3 (2,0,0,1) | 9 (2,2,2,2,1) | — |
| out-03 | 3 (2,0,0,1) | 9 (2,2,2,2,1) | `invented_facts` |
| out-04 | 5 (2,1,1,1) | 9 (2,2,2,2,1) | `invented_facts` |
| out-05 | 3 (2,0,0,1) | 6 (2,1,1,1,1) | `invented_facts` |
| out-06 | 3 (2,0,0,1) | 10 (2,2,2,2,2) | `invented_facts` |
| out-07 | 3 (2,0,0,1) | 9 (2,2,2,1,2) | `unacknowledged_source_loss` |
| out-08 | 4 (2,0,1,1) | 3 (2,0,1,0,0) | `invented_facts` |
| out-09 | 3 (2,0,0,1) | 10 (2,2,2,2,2) | — |
| out-10 | 5 (2,1,1,1) | 8 (2,2,2,1,1) | `invented_facts` |
| out-11 | 4 (2,1,0,1) | 9 (2,2,2,2,1) | `invented_facts` |
| out-12 | 4 (2,1,0,1) | 10 (2,2,2,2,2) | `invented_facts` |
| out-13 | 3 (2,0,0,1) | 8 (2,2,2,1,1) | `invented_facts`, `unacknowledged_source_loss` |
| out-14 | 5 (2,1,1,1) | 7 (2,1,2,1,1) | `invented_facts` |
| out-15 | 3 (2,0,0,1) | 9 (2,2,2,1,2) | `unacknowledged_source_loss` |
| out-16 | 3 (2,0,0,1) | 9 (2,2,2,2,1) | `invented_facts` |

## 2. Decisive questions

“Benefits” counts benefit branches specifically; parenthetical text identifies additional first-level constraints counted in section 6.

| output | Benefits | Room promoted? | Request first? | No longer than source? | Excessive devices | Attendee constraints | Invented material |
|---|---:|---|---|---|---|---|---|
| out-01 | 1 (plus room) | Yes | Yes | Yes | None | Demoted under one attendee branch | All attendees available; all conflicts resolved |
| out-02 | 0 (four constraints) | Yes | Yes | No | None | Promoted as three peer constraints | No |
| out-03 | 0 (four constraints) | Yes | Yes | No | None | Promoted; Johnson’s window is misstated | Johnson unavailable until tomorrow at 10:30 |
| out-04 | 3 (plus room) | Yes | Yes | Yes | Separate bold key line | Converted into four peer availability claims | Collins and Johnson can attend Thursday; definite feasibility |
| out-05 | 1 (plus room) | Yes | Yes | No | None | Promoted but collapsed and distorted | Everyone unavailable today or tomorrow; first feasible slot |
| out-06 | 0 (four constraints) | Yes | Yes | Yes | None | Promoted as peer requirements | Thursday meets all requirements |
| out-07 | 0 (four constraints) | Yes | Yes | Yes | None | Promoted; availability details are partly omitted | No |
| out-08 | 2, but the wrong two (plus room) | Yes | Yes | No | Headings and separate marked key line | Demoted under attendee availability | Earliest/only slot, avoided delay, full attendance and productivity |
| out-09 | 0 (four constraints) | Yes | Yes | Yes | None | Promoted as peer constraints | No |
| out-10 | 1 (plus room) | Yes | Yes | No | None | Demoted under a combined availability claim | Only slot; works for everyone |
| out-11 | 1 combined benefit | Yes | Yes | No | None | Promoted, with the conclusion buried afterward | Thursday works for everyone |
| out-12 | 2 attendee claims among four items | Yes | Yes | Yes | None | Promoted and partly converted into benefits | Johnson is available Thursday |
| out-13 | 0 (four constraints) | Yes | Yes | Yes | None | Promoted as peer constraints | Thursday satisfies all constraints |
| out-14 | 0 explicit benefit branches | No | Yes | Yes | Headings and separate key line | Demoted under two mixed reason groups | Thursday works; implied Johnson availability Thursday |
| out-15 | 0 (four constraints) | Yes | Yes | Yes | None | Promoted as peer constraints | No |
| out-16 | 1 combined benefit (plus room) | Yes | Yes | No | Headings and separate key line | Promoted as bullets, then summarized | Thursday meets every participant’s availability |

## 3. Output notes

- **out-01:** The explicit attendee/room split is readable, but it promotes the room and turns incomplete availability evidence into certainty.
- **out-02:** It faithfully preserves the source’s tentative wording—an improvement over the gold’s disputable Johnson assumption—but leaves all four constraints at the key-line level.
- **out-03:** The request is immediate, but Johnson’s availability is materially changed and the note grows beyond the source.
- **out-04:** It exposes a clear hierarchy, though it over-splits attendee benefits, promotes the room, and asserts unsupported availability.
- **out-05:** Its compact argument depends on multiple false availability claims and an unsupported “first slot” conclusion.
- **out-06:** The one-sentence presentation is exceptionally economical, but “meets all requirements” converts a merely possible slot into a certain one.
- **out-07:** It is concise and cautious, but loses the crucial fact that the room is available Thursday.
- **out-08:** The marked, numbered apparatus is disproportionate, mixes feasibility and impact, and contains the most invented material.
- **out-09:** This is the strongest faithful note and avoids the gold’s unsupported Thursday-attendance assumption, although it presents constraints rather than the two benefit branches.
- **out-10:** It groups participant and room feasibility clearly, but “only slot that works for everyone” is unsupported.
- **out-11:** The combined attendance conclusion appears after its evidence and asserts availability the source does not establish.
- **out-12:** It is concise and benefit-oriented, but invents Johnson’s Thursday availability and promotes four peer items.
- **out-13:** The constraint list is orderly, yet it omits Thursday room availability while claiming that every constraint is satisfied.
- **out-14:** Its need-versus-feasibility grouping is intelligible, but the headings are excessive and the feasibility conclusion is unsupported.
- **out-15:** It stays short and factual but omits the source’s affirmative evidence that the room is available Thursday.
- **out-16:** The constraints are cleanly ordered, though the headings are excessive and the final availability conclusion is invented.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| The exact two reader-benefit branches are replaced by constraints, combined feasibility, or over-split attendee claims | Core loop §4, Groups | ignored | out-01–out-16 |
| Room availability is promoted to the first level instead of supporting the recommendation | Core loop §4, Groups | ignored | out-01–out-13, out-15, out-16 |
| Tentative or incomplete availability evidence becomes certain feasibility | Mode 3, “Invent nothing”; self-check §8.4 | ignored | out-01, out-03–out-06, out-08, out-10–out-14, out-16 |
| The affirmative Thursday room-availability fact disappears | Mode 3, “Keep every fact from the source” | ignored | out-07, out-13, out-15 |
| Headings or a separate key-line block overwhelm the short-note format | Core loop §7; Mode 3 clean-text rule | ignored | out-04, out-08, out-14, out-16 |
| The literal approval question is absent | Core loop §1 and §3 | ignored | out-01, out-06, out-08, out-09, out-13, out-15, out-16 |
| The rewrite exceeds the source’s proportional length | Mode 3 rendering rules | ignored | out-02, out-03, out-05, out-08, out-10, out-11, out-16 |

## 5. Observation

The stronger outputs put a precise rescheduling request first, remain compact, preserve the source’s tentative evidence, and subordinate scheduling facts. The weaker outputs either expose four peer constraints instead of two reader benefits, elevate the room into a key-line branch, or manufacture certainty that Thursday works for everyone.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "04-meeting-note",
  "mode": "write",
  "outputs": [
    {
      "output": "out-01",
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
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
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
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
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
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 10,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 0,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 3,
        "top": 2,
        "same_kind_grouping": 0,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 0
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
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 10,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
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
        "order_type_named": "na",
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
        "levels": 1,
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-11",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
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
        "total": 10,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-13",
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
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-14",
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
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-15",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-16",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    }
  ]
}
```