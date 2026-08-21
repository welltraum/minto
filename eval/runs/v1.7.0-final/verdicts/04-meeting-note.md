## 1. Score table

Structural sub-scores are `(top/key line/levels/order)`; quality sub-scores are `(top/grouping/order/MECE/display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (2/1/0/1) | 7 (2/1/1/1/2) | — |
| out-02 | 4 (2/1/0/1) | 7 (2/1/1/1/2) | — |
| out-03 | 4 (2/1/0/1) | 7 (2/1/1/1/2) | `invented_facts` |
| out-04 | 6 (2/1/1/2) | 9 (2/2/2/1/2) | `invented_facts` |
| out-05 | 3 (1/0/1/1) | 3 (1/0/1/0/1) | `invented_facts` |
| out-06 | 4 (2/1/0/1) | 6 (2/1/1/1/1) | — |
| out-07 | 4 (2/1/0/1) | 6 (2/1/1/1/1) | `invented_facts` |
| out-08 | 4 (2/1/0/1) | 5 (2/1/1/1/0) | `invented_facts` |
| out-09 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | `invented_facts` |
| out-10 | 4 (2/1/0/1) | 6 (2/1/1/0/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-11 | 5 (2/1/1/1) | 7 (2/2/1/2/0) | `invented_facts` |
| out-12 | 6 (2/1/1/2) | 8 (2/1/2/1/2) | `invented_facts` |
| out-13 | 4 (2/1/0/1) | 6 (2/1/1/1/1) | — |
| out-14 | 6 (2/1/1/2) | 8 (2/1/2/1/2) | `invented_facts` |
| out-15 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | `invented_facts` |
| out-16 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | `invented_facts` |

## 2. Decisive questions

Question 1 counts reader-benefit branches; the machine-readable `first_level_count` counts every element presented at that level.

| output | 1. Benefits | 2. Room as extra benefit? | 3. Request first? | 4. No longer? | 5. Excessive devices | 6. Attendee constraints | 7. Invented material |
|---|---|---|---|---|---|---|---|
| out-01 | 0 explicit | Yes, as a fourth peer constraint | Yes | Yes | None | Promoted as peer evidence | None |
| out-02 | 0 explicit | Yes, as a fourth peer constraint | Yes | Yes | None | Promoted as peer evidence | None |
| out-03 | 0 explicit | Yes, as a fourth peer constraint | Yes, in subject | Yes | None | Promoted as peer evidence | “Thursday at 11:00 works” turns possibility into certainty |
| out-04 | 0; three time-slot claims | No, it supports the time-slot reasoning | Yes | Yes | None | Demoted beneath current/tomorrow/Thursday claims | Thursday feasibility and Johnson’s Thursday availability are asserted |
| out-05 | 1 genuine claimed benefit among three branches | Yes, as a peer branch | No; acceptability is asserted | No | Headings | Demoted under an attendee heading | Collins unavailable all day; “minimal disruption”; assured attendance |
| out-06 | 0 explicit | Yes, as a fourth peer constraint | Yes | No | None | Promoted as four bullets | None |
| out-07 | 1 aggregate benefit | Yes, as a fourth peer constraint | Yes | No | None | Promoted as four bullets | “Works for everyone” is certain rather than tentative |
| out-08 | 0 explicit | Yes, as a fourth rationale item | Yes | No | Headings and separate recommendation/conclusion blocks | Promoted as rationale bullets | “Earliest time” and complete satisfaction are unsupported |
| out-09 | 1 aggregate attendee benefit | Yes, as the other summary reason | Yes | Yes | None | Collins and Clifford promoted; Johnson detail omitted | Assured accommodation of all attendees |
| out-10 | 2 attendee-related reasons | Yes, as a third peer reason | Yes, as a proposal | Yes | None | Johnson and Clifford promoted; Collins omitted | Johnson’s Thursday availability is asserted |
| out-11 | 1 aggregate attendee benefit | Yes, as a separate key-line branch | Yes, in subject | No | Headings and separate key-line block | Repeated in the lead, then demoted under a heading | “Earliest slot” and specific Thursday availability claims |
| out-12 | 1 aggregate attendee benefit | Yes, as a coequal condition | Yes | No | None | Kept flat before the aggregate conclusion; Johnson altered | Johnson made available only tomorrow; Thursday assured for all three |
| out-13 | 2 attendee-related branches | Yes, as the third bullet | Yes | Yes | None | Promoted as bullets | None |
| out-14 | 1 aggregate attendee benefit | Yes, as a coequal condition | Yes, in subject | No | None | Demoted beneath the schedule conclusion | Thursday is asserted to work for everyone |
| out-15 | 1 aggregate attendee benefit | Yes, as a coequal venue condition | Yes | Yes | None | Demoted after the aggregate claim | Assured accommodation of all attendees |
| out-16 | 1 aggregate attendee benefit | Yes, as a coequal condition | Yes | Yes | None | Collins and Clifford retained; Johnson detail omitted under an aggregate claim | Thursday is asserted to work for all attendees |

## 3. Output notes

- **out-01:** The request is immediate and compact, but four scheduling constraints replace the two benefit-level reasons.
- **out-02:** This is the most faithful compact constraint summary, though it still promotes evidence rather than synthesizing the benefits.
- **out-03:** The subject is answer-first, but the body repeats the conclusion and upgrades a possible slot to one that “works.”
- **out-04:** Clear chronological elimination makes the logic unusually easy to follow, but the first level consists of time options rather than reader benefits.
- **out-05:** It forces three labeled branches, promotes the room, and invents “minimal disruption.”
- **out-06:** It is factually faithful but turns a two-sentence note into a four-item evidence list.
- **out-07:** The aggregate benefit is clearer than a bare constraint list, but the four bullets and unsupported certainty weaken it.
- **out-08:** Heavy recommendation/rationale/conclusion apparatus culminates in the unsupported claim that this is the earliest feasible time.
- **out-09:** Compact prose collapses the attendee benefits together and elevates room availability as the other main reason.
- **out-10:** It is concise, but Collins disappears and Johnson’s availability is extended to Thursday.
- **out-11:** The attendee/room split is visually explicit but disproportionate, repetitive, and supported with several invented availability claims.
- **out-12:** The today–tomorrow–Thursday progression is coherent, but Johnson’s constraint is altered and tentative feasibility becomes certainty.
- **out-13:** It stays compact, yet the bullets expose raw constraints and make the room a third peer branch.
- **out-14:** The chronological prose is clear, but it groups all attendees together, promotes the room, and overstates schedule certainty.
- **out-15:** It is proportionate and answer-first, though “attendees and venue” is the wrong key-line split and overstates feasibility.
- **out-16:** It is concise and keeps both aggregate attendee and room claims visible, but omits Johnson’s detail and asserts that the slot works.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Constraints or time slots replace the two benefit-level reasons | Core loop §4, “Groups” | ignored | out-01, out-02, out-03, out-04, out-06, out-07, out-08, out-13 |
| Room availability is promoted to a peer branch instead of remaining support | Core loop §4 and §6, “Groups” and “MECE” | ignored | out-01, out-02, out-03, out-05–out-16 |
| A numerical grouping norm encourages unnecessary extra branches | Mode 3 “3–4 first-level groups” versus Limits “four honest groups beat three forced ones” | buried | out-01, out-02, out-03, out-05, out-06, out-07, out-08, out-13 |
| Tentative or bounded evidence becomes certain availability, feasibility, or priority | Mode 3, “Invent nothing” | ignored | out-03, out-04, out-05, out-07–out-12, out-14–out-16 |
| Structural apparatus is disproportionate to a short meeting note | Mode 3, “clean text” and plain-format rules | ignored | out-05, out-08, out-11 |
| Collins and the reason the original slot fails disappear | Mode 3, “Keep every fact from the source” | ignored | out-10 |

## 5. Observation

Stronger outputs put the reschedule proposal first, remain close to the source’s length, and subordinate scheduling facts to a compact rationale. Weaker outputs leave constraints flat, promote room availability beside attendee benefits, force extra branches, or turn the source’s tentative possibility into certainty.

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
        "total": 4,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
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
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
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
        "readers_question_literal": true,
        "order_type_named": "na",
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
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 0,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 3,
        "top": 1,
        "same_kind_grouping": 0,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 1
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
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-06",
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
        "mece": 1,
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
        "readers_question_literal": false,
        "order_type_named": "na",
        "scq_intro_present": "na"
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
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
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
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 0
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
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-09",
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
        "invented_facts"
      ],
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
      "output": "out-10",
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
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
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
      "output": "out-11",
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
        "mece": 2,
        "visible_structure": 0
      },
      "hard_failures": [
        "invented_facts"
      ],
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
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
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
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
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
      "output": "out-14",
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
      "hard_failures": [
        "invented_facts"
      ],
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
        "invented_facts"
      ],
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
      "output": "out-16",
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
        "invented_facts"
      ],
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
    }
  ]
}
```