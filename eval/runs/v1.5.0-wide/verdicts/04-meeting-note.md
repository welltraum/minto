## 1. Score table

Axis order: Structure = top/key line/levels/order; Quality = top/grouping/order/MECE/display.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2/1/2/1) | 6 (2/1/1/1/1) | `invented_facts` |
| out-02 | 3 (2/0/0/1) | 6 (2/1/2/1/0) | `invented_facts` |
| out-03 | 3 (2/0/0/1) | 7 (2/1/1/2/1) | `invented_facts` |
| out-04 | 3 (2/0/0/1) | 7 (2/1/1/2/1) | `invented_facts` |
| out-05 | 2 (1/0/0/1) | 5 (1/2/1/1/0) | `invented_facts` |
| out-06 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | `invented_facts` |
| out-07 | 3 (2/0/0/1) | 6 (2/1/1/0/2) | `unacknowledged_source_loss` |
| out-08 | 4 (2/0/1/1) | 6 (2/2/1/1/0) | `invented_facts` |

## 2. Decisive questions

- **out-01:** (1) One aggregate first-level benefit. (2) No; room availability is supporting evidence. (3) Yes. (4) No. (5) Heading and separate key-line block. (6) Attendee constraints are demoted beneath the aggregate claim. (7) “Resolves all scheduling conflicts” turns tentative feasibility into certainty.
- **out-02:** (1) No genuine first-level benefits; it presents three chronological slot assessments. (2) No standalone room branch. (3) Yes, in the subject. (4) No. (5) Headings, separate key line, and Mermaid. (6) Constraints are promoted into today/tomorrow branches. (7) “No one has raised a conflict,” definite Thursday feasibility, and the all-day room claim exceed the source.
- **out-03:** (1) No first-level benefits; four constraints are presented. (2) Yes, as a standalone first-level constraint. (3) Yes. (4) No. (5) None of the listed devices. (6) All attendee constraints are promoted. (7) “The first time everyone … [is] available” is unsupported.
- **out-04:** (1) No first-level benefits; four constraints are presented. (2) Yes, as a standalone first-level constraint. (3) Yes. (4) No. (5) None. (6) All attendee constraints are promoted. (7) The claim that Thursday at 11:00 satisfies every constraint is unsupported, particularly for Johnson.
- **out-05:** (1) Three purported benefits: participant availability, room availability, and avoiding delay. (2) Yes, as a standalone branch, although listed second. (3) Only incompletely in the subject; the explicit request comes last. (4) No. (5) Headings, SCQ labels, and a separate key-line block. (6) Constraints are moved into the labeled Situation. (7) It invents universal Thursday availability and avoidance of further delay.
- **out-06:** (1) Two attendee benefits appear among four coordinated first-level clauses. (2) Yes; the room is promoted to the same level. (3) Yes. (4) Yes. (5) None. (6) The Collins constraint is promoted; detailed Johnson and Frankfurt timing is omitted. (7) Johnson’s Thursday availability is invented.
- **out-07:** (1) One attendee benefit appears among three clauses. (2) Yes; the room is promoted to the same level. (3) Yes. (4) Yes. (5) None. (6) Collins and Clifford are promoted, while Johnson is omitted. (7) No fact is invented.
- **out-08:** (1) Two purported branches, but only one is an attendee benefit; the room is a constraint. (2) Yes, as a standalone branch. (3) Yes, in the subject. (4) No. (5) Headings, SCQ labels, and a separate key-line block. (6) Individual attendee constraints are omitted in favor of a generalization. (7) It invents availability for all attendees at Thursday 11:00.

## 3. Output notes

- **out-01:** It has the cleanest hierarchy of the expanded notes, but collapses the two intended benefits into one overconfident claim.
- **out-02:** Its chronological elimination is clear, but it answers with slot mechanics and adds a highly disproportionate diagram.
- **out-03:** The request leads, yet four source facts are promoted ahead of an unsupported conclusion.
- **out-04:** It is readable and answer-first, but its bullets remain constraints rather than the two reader benefits.
- **out-05:** Correctly labeled reasons are undermined by buried approval, invented support, and excessive SCQ apparatus.
- **out-06:** This is the most proportionate complete note, though its compressed key line mixes benefits with constraints and assumes Johnson can attend.
- **out-07:** It is concise and answer-first, but losing Johnson removes half of the intended attendee case.
- **out-08:** Its two availability branches are visually tidy but use the wrong split and rely on an unsupported attendee generalization.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Constraints or room availability promoted instead of the two reader benefits | Core loop §4, “Groups” | ignored | out-02, out-03, out-04, out-05, out-06, out-07, out-08 |
| Tentative feasibility converted into asserted availability or certainty | Mode 3, “Invent nothing”; Core loop §8.4 | ignored | out-01, out-02, out-03, out-04, out-05, out-06, out-08 |
| Structure disproportionate to a two-sentence scheduling note | Core loop §7, “Show the structure” and “Limits” | ignored | out-01, out-02, out-05, out-08 |
| The two attendee benefits collapsed or left unstated | Core loop §6, “MECE” | missing | out-01, out-02, out-03, out-04, out-05, out-07, out-08 |

## 5. Observation

Stronger outputs put the reschedule request first, remain brief, and subordinate constraints beneath the case for approval. Weaker outputs promote raw scheduling facts or room availability to the key line, replace tentative evidence with certainty, or add formatting apparatus larger than the note itself.

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
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
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
        "first_level_count": 1,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": "na"
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
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
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
        "readers_question_literal": true,
        "order_type_named": "na"
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": "na"
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": "na"
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
        "total": 5,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 0
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na"
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
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": "na"
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
        "total": 6,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 0
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
        "order_type_named": "na"
      }
    }
  ]
}
```