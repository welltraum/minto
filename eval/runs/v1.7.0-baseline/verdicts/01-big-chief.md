## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 1 (0, 0, 0, 1) | 7 (0, 1, 2, 2, 2) | `invented_facts` |
| out-02 | 3 (2, 0, 0, 1) | 9 (2, 1, 2, 2, 2) | — |
| out-03 | 1 (0, 0, 0, 1) | 7 (0, 1, 2, 2, 2) | — |
| out-04 | 3 (2, 0, 0, 1) | 10 (2, 2, 2, 2, 2) | — |
| out-05 | 3 (2, 0, 0, 1) | 8 (2, 1, 2, 2, 1) | `invented_facts` |
| out-06 | 3 (2, 0, 0, 1) | 10 (2, 2, 2, 2, 2) | — |
| out-07 | 2 (1, 0, 0, 1) | 8 (1, 2, 2, 2, 1) | `unacknowledged_source_loss` |
| out-08 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-09 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | `invented_facts` |
| out-10 | 3 (2, 0, 0, 1) | 9 (2, 1, 2, 2, 2) | `invented_facts` |
| out-11 | 2 (1, 0, 0, 1) | 8 (1, 1, 2, 2, 2) | — |
| out-12 | 2 (1, 0, 0, 1) | 8 (1, 1, 2, 2, 2) | — |
| out-13 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-14 | 4 (1, 1, 1, 1) | 8 (1, 1, 2, 2, 2) | `invented_facts` |
| out-15 | 2 (1, 0, 0, 1) | 9 (1, 2, 2, 2, 2) | — |
| out-16 | 7 (2, 1, 2, 2) | 10 (2, 2, 2, 2, 2) | `invented_facts` |

The structural parentheses show `(top, key-line composition, levels, order and kind)`; the quality parentheses show `(top, same-kind grouping, explainable order, MECE, visible structure)`.

## 2. Decisive questions

| output | First-level kind | Grounded first-level elements | Top answers acceptance? | Invented facts or benefits | Mechanics below key line? | Reader question literal? |
|---|---|---:|---|---|---|---|
| out-01 | mechanics | 3 | No | Finance inserting identifiers into later submissions | No | No |
| out-02 | mechanics | 3 | Yes | None | No | No |
| out-03 | mechanics | 3 | No | None | No | No |
| out-04 | mechanics | 3 | Yes | None | No | No |
| out-05 | mechanics | 3 | Yes | Finance adding the missing identifiers, rather than supplying them for later inclusion | No | Yes |
| out-06 | mechanics | 3 | Yes | None | No | No |
| out-07 | mechanics | 3 | No; it establishes feasibility only | None; the extraction-program responsibility is lost | No | No |
| out-08 | mechanics | 3 | No; it answers an implementation question | None | No | No |
| out-09 | mechanics | 3 | No; approval is deferred to the closing ask | Missing identifiers being added before the file is used | No | No |
| out-10 | mechanics | 3 | Yes | Mailing the cheque, populating identifiers internally, and implementation without system changes | No | No |
| out-11 | mechanics | 3 | No; it establishes feasibility only | None | No | No |
| out-12 | mechanics | 3 | No; it describes conditional processing | None | No | No |
| out-13 | mechanics | 3 | No; it establishes implementability only | None | No | No |
| out-14 | mixed | 3 | No; “Proceed” is at the end | Guaranteed identifier completeness and integration without modification | Yes | No |
| out-15 | mechanics | 3 | No; it establishes feasibility only | None | No | No |
| out-16 | benefits | 1 | Yes | Preservation of the same cash control and billing output as today | Yes | No |

## 3. Output notes

- **out-01:** It faithfully sequences the workflow but never reaches a management conclusion, and it changes identifier inclusion from Big Chief’s responsibility to Finance’s.
- **out-02:** The recommendation is immediate and conditional, but its first level remains a list of implementation topics.
- **out-03:** Clear headings expose the mechanics well, yet there is no acceptance decision anywhere.
- **out-04:** Strong action-oriented presentation makes the conditions easy to follow, but those conditions replace the required reasons at the key line.
- **out-05:** The explicit SCQ supplies the only literal reader question, although the labels over-structure this short note and one operational responsibility is altered.
- **out-06:** This is a crisp conditional recommendation with a coherent process sequence, but every first-level branch still explains how.
- **out-07:** The prose is concise and sequential, but the top stops at feasibility and silently drops Big Chief’s extraction-program obligation.
- **out-08:** It is the only output to explain its process order, but it explicitly substitutes “what must happen” for management’s acceptance question.
- **out-09:** The three steps are readable, while the actual approval ask is buried at the end and the identifier timing is changed.
- **out-10:** The opening recommendation is strong, but the implementation considerations remain at the first level and the conclusion adds unsupported no-change assurance.
- **out-11:** It gives an answer-first feasibility statement and complete mechanics, without saying whether management should accept.
- **out-12:** The source is preserved in a clean sequence, but the opening is a processing description rather than a decision.
- **out-13:** Its three requirements are coherent and visible, though “can implement” answers possibility rather than desirability.
- **out-14:** It begins to turn mechanics into reasons and subordinates most detail, but the recommendation is buried and two claimed operational benefits exceed the evidence.
- **out-15:** The process stages are especially clear, but the benefit or acceptance-reason layer is absent.
- **out-16:** It is the only output with a consistently benefit-shaped key line and properly subordinate mechanics, but two of its preservation benefits are not established by the fixture.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Mechanics or implementation conditions occupy the key line instead of acceptance reasons | Core loop §4, “Groups” | ignored | out-01–out-15 |
| The top answers feasibility or procedure rather than whether management should accept | Core loop §§1–2, “Topic → reader question” and “Provisional answer” | ignored | out-01, out-03, out-07–out-09, out-11–out-15 |
| The acceptance decision appears only after the support | Core loop §8, “Self-check, then deliver” | buried | out-09, out-14 |
| The reader’s question is not left literally on the page | Core loop §§1 and 3 | ignored | all except out-05 |
| The ordering principle is not named | Core loop §5, “Order” | ignored | all except out-08 |
| Operational responsibilities or benefits exceed the supplied evidence | Mode 3, “Invent nothing” | ignored | out-01, out-05, out-09, out-10, out-14, out-16 |

## 5. Observation

The stronger outputs state an acceptance decision immediately, recast the first level as management reasons or preserved outcomes, and subordinate fields, routing, balancing, and system processing as evidence. The weaker outputs often have excellent chronological workflow structure, but that structure answers how the proposal works rather than why management should accept it.

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
        "total": 1,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 7,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
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
        "same_kind_grouping": 1,
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
        "total": 1,
        "top": 0,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 7,
        "top": 0,
        "same_kind_grouping": 1,
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
        "total": 8,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
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
        "order_type_named": false,
        "scq_intro_present": true
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
        "total": 8,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["unacknowledged_source_loss"],
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
        "order_type_named": true,
        "scq_intro_present": true
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
        "total": 9,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
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
        "first_level_count": 3,
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
        "same_kind_grouping": 1,
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
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 1,
        "same_kind_grouping": 1,
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
        "total": 8,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
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
      "output": "out-16",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
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
    }
  ]
}
```