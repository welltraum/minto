## 1. Score table

Axis order in parentheses: Structure = top/key line/levels/order; Quality = top/grouping/order/MECE/display.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 3 (2/0/0/1) | 7 (2/1/2/1/1) | `invented_facts`, `unacknowledged_source_loss` |
| out-02 | 2 (1/0/0/1) | 9 (1/2/2/2/2) | — |
| out-03 | 1 (0/0/0/1) | 8 (0/2/2/2/2) | `unacknowledged_source_loss` |
| out-04 | 2 (1/0/0/1) | 9 (1/2/2/2/2) | — |
| out-05 | 3 (2/0/0/1) | 7 (2/1/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-06 | 2 (1/0/0/1) | 9 (1/2/2/2/2) | — |
| out-07 | 1 (0/0/0/1) | 8 (0/2/2/2/2) | `unacknowledged_source_loss` |
| out-08 | 2 (1/0/0/1) | 6 (1/2/2/0/1) | — |

## 2. Decisive questions

| output | First-level kind | Grounded first-level elements | Top answers acceptance? | Invented facts or benefits | Details below key line? | Literal reader question? |
|---|---|---:|---|---|---|---|
| out-01 | mechanics | 3 | Yes | Per-outlet billing specificity and scheduling the first submission are unsupported additions | Partly: details are nested under mechanical headings, but not under reasons; cheque routing is lost | Yes |
| out-02 | mechanics | 3 | No; it establishes feasibility only | None | Partly; several details are nested, but field and processing mechanics remain key-line points | No |
| out-03 | mechanics | 3 | No | None | Formally yes, but beneath mechanical headings rather than reasons | No |
| out-04 | mechanics | 3 | No; it establishes feasibility only | None | No; the numbered key line is the mechanics | No |
| out-05 | mechanics | 3 | Yes | Identifier insertion “before processing” and added operational next steps are unsupported | Formally yes, but beneath mechanical condition headings rather than reasons | No |
| out-06 | mechanics | 3 | No; it establishes processability only | None | No; the bullets themselves are the mechanics | No |
| out-07 | mechanics | 3 | No | None | Formally yes, but beneath mechanical topic headings rather than reasons | No |
| out-08 | mechanics | 3 unique elements | No; it establishes processability only | None | Only in the appended skeleton; the memo repeats the same mechanics and supplies no reasons layer | No |

## 3. Output notes

- **out-01:** It gives the clearest approval answer and is the only output to state the reader’s question, but its key line remains procedural and its extra next step introduces unsupported material.
- **out-02:** It is concise and factually complete, but “we can implement” answers feasibility rather than whether management should accept the proposal.
- **out-03:** Its process hierarchy is clean, yet it never reaches an acceptance conclusion and drops the prepaid-payment condition.
- **out-04:** It preserves the operating sequence efficiently, but every numbered point is a mechanic supporting an incomplete feasibility top.
- **out-05:** It explicitly recommends acceptance, but adds a second action grouping and alters the timing of supplying missing identifiers.
- **out-06:** It is the most economical mechanical summary, though its top says only that existing procedures can process the proposal.
- **out-07:** Its headings make the workflow easy to scan, but the subject remains a process summary and the prepaid condition disappears.
- **out-08:** The appended skeleton exposes the hierarchy, but it duplicates the memo wholesale and still frames the answer as processability rather than acceptance.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Mechanics occupy the key line instead of grounded reasons for acceptance | Core loop §4, Groups | ignored | out-01–out-08 |
| Acceptance answer is missing or replaced by a feasibility claim | Core loop §§1–2, Reader question and provisional answer | ignored | out-02, out-03, out-04, out-06, out-07, out-08 |
| Reader’s question is not written literally | Core loop §§1 and 3 | missing | out-02–out-08 |
| Source details are lost or materially altered | Mode 3, “Keep every fact from the source” | ignored | out-01, out-03, out-05, out-07 |
| Unsupported operational additions appear outside the source | Mode 3, “Invent nothing” | ignored | out-01, out-05 |

## 5. Observation

The stronger outputs state an acceptance decision before the process explanation; the weaker ones stop at feasibility or provide no decision at all. None creates the required reasons-for-acceptance layer: all promote data, routing, balancing, and system processing into the key line, while the clearest presentations merely organize those mechanics more effectively.

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
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 1
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
        "readers_question_literal": true,
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
        "scq_intro_present": false
      }
    },
    {
      "output": "out-03",
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
        "mece": 1,
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
        "scq_intro_present": false
      }
    },
    {
      "output": "out-07",
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
        "total": 6,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 0,
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
    }
  ]
}
```