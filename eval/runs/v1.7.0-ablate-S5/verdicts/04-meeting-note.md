## 1. Score table

Structural sub-scores are `(top/key-line composition/levels/order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (2/1/0/1) | 8 | None |
| out-02 | 4 (2/1/0/1) | 7 | `unacknowledged_source_loss` |
| out-03 | 5 (2/1/1/1) | 7 | `invented_facts` |
| out-04 | 2 (2/0/0/0) | 3 | `invented_facts` |
| out-05 | 4 (2/1/0/1) | 8 | `invented_facts` |
| out-06 | 5 (2/1/1/1) | 6 | `invented_facts` |
| out-07 | 4 (2/1/0/1) | 8 | `invented_facts` |
| out-08 | 4 (2/1/0/1) | 7 | `invented_facts` |

## 2. Decisive questions

1. **out-01:** (1) No explicit benefits; four constraints appear first-level. (2) Yes, room availability is an extra coordinate rationale. (3) Yes. (4) Yes. (5) None. (6) Attendee constraints are promoted into the flat key line. (7) No invented fact.
2. **out-02:** (1) No explicit benefits; three constraints appear. (2) Yes, room availability is an extra rationale. (3) Yes. (4) Yes. (5) None. (6) Collins’s and Clifford’s constraints are promoted; Johnson’s is omitted. (7) No invented fact.
3. **out-03:** (1) One combined attendee benefit. (2) Not literally a third benefit, but room availability is wrongly elevated as the other first-level branch. (3) No; the request is the second sentence. (4) No. (5) None of the listed devices. (6) Attendee constraints are demoted under an “Attendees” branch. (7) Yes: Collins’s Thursday availability and the certainty that the slot works for everyone and clears every blocker.
4. **out-04:** (1) One combined attendee benefit. (2) Not literally third—it is numbered second—but it is wrongly independent. (3) Yes. (4) No. (5) Headings, SCQ labels, and a separate answer/key-line block. (6) Constraints are promoted into the labeled SCQ and then partly regrouped. (7) Yes: required attendance, today’s room booking, everyone’s Thursday availability, “earliest,” and the claim that no earlier slot works.
5. **out-05:** (1) No explicit benefits; four requirements or constraints appear. (2) Yes, room availability remains an extra coordinate rationale. (3) Yes. (4) Yes. (5) None. (6) Attendee constraints are promoted into the flat key line. (7) Yes: “meets all requirements” converts “appears possible” into certainty.
6. **out-06:** (1) One combined attendee benefit. (2) Not literally third, but room availability is wrongly made an independent first-level reason. (3) Yes. (4) No. (5) None. (6) Constraints are demoted beneath the combined claim that everyone can attend. (7) Yes: Johnson’s inability to attend at 3:00, universal Thursday attendance, and “the first slot” are unsupported.
7. **out-07:** (1) One combined attendee benefit. (2) Yes, room availability is an additional flat rationale. (3) Yes. (4) Yes. (5) None. (6) Attendee constraints remain promoted as flat support. (7) Yes: “works for everyone” turns a tentative possibility into certainty.
8. **out-08:** (1) One combined attendee benefit, stated after four constraint bullets. (2) Yes, room availability is an additional first-level rationale. (3) Yes. (4) No. (5) Headings. (6) Attendee constraints are promoted into separate rationale bullets. (7) Yes: the claim that Thursday at 11:00 meets every participant’s availability is unsupported certainty.

## 3. Output notes

- **out-01:** The concise request is answer-first, but the four scheduling facts replace the intended two-benefit key line.
- **out-02:** It retains the compact form but loses Johnson entirely, so one of the two intended attendee benefits cannot be recovered.
- **out-03:** It adds useful parent-child grouping, but bundles all attendees together, promotes the room, and invents confirmed availability.
- **out-04:** The request is visible immediately, but SCQ apparatus, three unsupported rationales, and duplicated answer material overwhelm the short note.
- **out-05:** This is compact and complete at the fact level, though its flat constraint list and unsupported certainty prevent the intended benefit hierarchy.
- **out-06:** Its opening exposes two reasons and demotes details, but one reason is the room constraint and several availability claims exceed the source.
- **out-07:** The note is concise and readable, but its constraints remain flat and “works for everyone” overstates the tentative source.
- **out-08:** The facts are easy to scan, but headings and four rationale bullets are disproportionate and substitute constraints for the two benefits.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Scheduling constraints replace the two reader-benefit branches | Core loop §4, Groups | ignored | out-01–out-08 |
| Room availability is elevated into an independent rationale | Core loop §§4 and 6, Groups and MECE | ignored | out-01–out-08 |
| Tentative feasibility is converted into confirmed availability or an unsupported superlative | Mode 3, “Invent nothing” | ignored | out-03–out-08 |
| Formatting apparatus is disproportionate to a two-sentence note | Mode 3, write/rewrite rendering rules | ignored | out-04, out-08 |

## 5. Observation

The stronger outputs put the rescheduling request first and remain compact; the weaker ones add apparatus or unsupported certainty. None cleanly reproduces the intended hierarchy of exactly two attendee benefits with room availability subordinate as a constraint.

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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
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
      "output": "out-04",
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
        "same_kind_grouping": 1,
        "explainable_order": 0,
        "mece": 0,
        "visible_structure": 0
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
        "order_type_named": "na",
        "scq_intro_present": "na"
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
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
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
        "readers_question_literal": false,
        "order_type_named": "na",
        "scq_intro_present": "na"
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
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
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
        "readers_question_literal": false,
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    }
  ]
}
```