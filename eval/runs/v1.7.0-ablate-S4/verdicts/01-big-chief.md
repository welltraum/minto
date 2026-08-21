## 1. Score table

Structural sub-scores are shown as `(top/key line/levels/order)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 2 (1/0/0/1) | 9 | `invented_facts`, `unacknowledged_source_loss` |
| out-02 | 3 (2/0/0/1) | 10 | None |
| out-03 | 3 (2/0/0/1) | 6 | `invented_facts`, `unacknowledged_source_loss` |
| out-04 | 2 (1/0/0/1) | 9 | None |
| out-05 | 2 (1/0/0/1) | 9 | None |
| out-06 | 1 (0/0/0/1) | 8 | None |
| out-07 | 2 (1/0/0/1) | 9 | None |
| out-08 | 3 (2/0/0/1) | 10 | `invented_facts`, `unacknowledged_source_loss` |

## 2. Decisive questions

| output | First-level kind | Grounded first-level elements | Top answers acceptance? | Invented material | Mechanics below key line? | Reader question literal? |
|---|---|---:|---|---|---|---|
| out-01 | mechanics | 3 | No; it establishes feasibility and asks for approval only at the end | Identifiers added before use; notifying Big Chief | No | No |
| out-02 | mechanics | 3 | Yes | None | No | No |
| out-03 | mechanics | 3 | Yes | Readiness for the next billing cycle and the associated confirmation step | No | Yes |
| out-04 | mechanics | 3 | No; it establishes processability | None | No | No |
| out-05 | mechanics | 3 | No; it establishes implementability | None | No | No |
| out-06 | mechanics | 3 | No | None | No | No |
| out-07 | mechanics | 3 | No; it answers how implementation can occur | None | No | No |
| out-08 | mechanics | 3 | Yes | Mailing the cheque, format review, and a new balancing checklist | No | No |

## 3. Output notes

- **out-01:** The approval request is buried after a mechanically organized key line, and the identifier workaround is moved from later submissions to before file use.
- **out-02:** The subject supplies the clearest answer-first recommendation, but both the memo and appended pyramid promote settlement mechanics rather than reasons for acceptance.
- **out-03:** It alone states the reader’s question explicitly and gives a clear approval answer, but its file/actor split overlaps and adds an unsupported next-cycle condition.
- **out-04:** This is concise and operationally coherent, but its top says only that the proposal can be processed.
- **out-05:** The time-ordered mechanics are clear, while the management conclusion remains limited to implementability.
- **out-06:** It is the tidiest reproduction of the source’s procedural structure but never answers the decision question.
- **out-07:** The visible pyramid reinforces a coherent implementation sequence, yet it repeats the wrong, mechanics-based key line.
- **out-08:** It gives an explicit acceptance recommendation and strong display, but adds unsupported implementation actions and changes the timing of missing identifiers.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Mechanics promoted as the key line instead of reasons for acceptance | Core loop §4, Groups | ignored | out-01–out-08 |
| Reader’s question not written in the delivered memo | Core loop §§1 and 3 | missing | out-01, out-02, out-04–out-08 |
| Top stops at feasibility or implementation rather than the acceptance decision | Core loop §1, Topic → reader question | ignored | out-01, out-04–out-07 |
| Ordering principle is never named | Core loop §5, Order | ignored | out-01–out-08 |
| Unsupported operational additions | Mode 3, “Invent nothing” | ignored | out-01, out-03, out-08 |
| Later-submission timing is removed or replaced | Mode 3, “Keep every fact” | ignored | out-01, out-03, out-08 |

## 5. Observation

The stronger outputs state an approval decision before the supporting material; the weaker ones state only feasibility or omit the decision entirely. None makes the required structural shift from field, routing, balancing, and processing mechanics to grounded reasons for accepting the proposal.

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
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
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
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
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
      "output": "out-04",
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
        "scq_intro_present": true
      }
    },
    {
      "output": "out-06",
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
        "scq_intro_present": false
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
        "order_type_named": false,
        "scq_intro_present": true
      }
    }
  ]
}
```