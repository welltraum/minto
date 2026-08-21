## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 5 (2, 1, 1, 1) | 7 | `invented_facts`, `unacknowledged_source_loss` |
| out-02 | 2 (1, 0, 0, 1) | 9 | — |
| out-03 | 7 (2, 1, 2, 2) | 10 | `invented_facts` |
| out-04 | 2 (1, 0, 0, 1) | 9 | — |
| out-05 | 1 (0, 0, 0, 1) | 8 | — |
| out-06 | 2 (1, 0, 0, 1) | 8 | — |
| out-07 | 3 (2, 0, 0, 1) | 8 | `unacknowledged_source_loss` |
| out-08 | 2 (1, 0, 0, 1) | 8 | — |
| out-09 | 2 (1, 0, 0, 1) | 9 | — |
| out-10 | 2 (1, 0, 0, 1) | 8 | — |
| out-11 | 1 (0, 0, 0, 1) | 8 | — |
| out-12 | 2 (1, 0, 0, 1) | 9 | — |
| out-13 | 1 (0, 0, 0, 1) | 8 | — |
| out-14 | 3 (2, 0, 0, 1) | 5 | `invented_facts` |
| out-15 | 3 (2, 0, 0, 1) | 10 | `invented_facts` |
| out-16 | 1 (0, 0, 0, 1) | 7 | `unacknowledged_source_loss` |

## 2. Decisive questions

1. **out-01:** Kind: mixed; grounded elements: 1 of 3 fully; top recommends approval; inventions: automatic processing without manual intervention, no system modifications, accuracy/control, and simplified extraction; details are not all properly retained beneath the key line; reader question absent.
2. **out-02:** Kind: mechanics; grounded elements: 3; top establishes feasibility but not acceptance; no inventions; field, format, routing, and balancing form the key line rather than supporting reasons; reader question absent.
3. **out-03:** Kind: benefits; grounded elements: 2 of 3 fully; top recommends acceptance; invention: no change to existing systems/as-is operation; mechanics sit beneath payoff-oriented headings; reader question absent.
4. **out-04:** Kind: mechanics; grounded elements: 3; top answers whether implementation is possible, not whether to accept; no inventions; operational stages form the key line; reader question absent.
5. **out-05:** Kind: mechanics; grounded elements: 3; no acceptance answer; no inventions; operational requirements form the key line; reader question absent.
6. **out-06:** Kind: mechanics; grounded elements: 3; top answers processability rather than acceptance; no inventions; mechanics remain first-level requirements and are repeated in the skeleton; reader question absent.
7. **out-07:** Kind: mechanics; grounded elements: 3; top explicitly supports acceptance; no inventions; mechanics form the key line and the accepted file-format fact is lost; reader question is literal.
8. **out-08:** Kind: mechanics; grounded elements: 3; top says the request is implementable but does not recommend accepting it; no inventions; operational requirements form the key line; reader question absent.
9. **out-09:** Kind: mechanics; grounded elements: 3; top establishes accommodation, not acceptance; no inventions; mechanics form the key line; reader question absent.
10. **out-10:** Kind: mechanics; grounded elements: 3; top establishes accommodation, not acceptance; no inventions; the three process paragraphs remain the key line; reader question absent.
11. **out-11:** Kind: mechanics; grounded elements: 3; top answers the narrower feasibility question rather than whether to accept; no inventions; mechanics form the key line; a literal but incorrectly framed reader question is present.
12. **out-12:** Kind: mechanics; grounded elements: 3; top establishes accommodation, not acceptance; no inventions; workflow stages form the key line; reader question absent.
13. **out-13:** Kind: mechanics; grounded elements: 3; no acceptance answer; no material inventions; implementation stages form the key line; reader question absent.
14. **out-14:** Kind: mechanics; grounded elements: 3; top clearly recommends approval; invention: the cheque is said to be mailed; conditions remain the key line and are then redundantly restated as steps; reader question absent.
15. **out-15:** Kind: mechanics; grounded elements: 3; top clearly recommends approval; inventions: claims that the requirements ensure or enable accurate payment processing, reconciliation, and billing; mechanics form the key line; reader question absent.
16. **out-16:** Kind: mechanics; grounded elements: 3; no acceptance answer; no inventions; mechanics form the key line, while the monthly prepaid-payment proposal and other request context are lost; reader question absent.

## 3. Output notes

- **out-01:** It reaches the right decision but mixes benefits with system capabilities and adds several unsupported operational assurances.
- **out-02:** It is a clean and complete process summary whose controlling idea remains feasibility rather than approval.
- **out-03:** It is the only output to sustain payoff-oriented first-level branches, though its assertion that existing systems require no change is stronger than the source.
- **out-04:** Its concise chronological workflow is easy to follow but merely reorganizes the original mechanics.
- **out-05:** The memo has visible grouping and complete mechanics but never supplies a management conclusion.
- **out-06:** The answer and appended skeleton both organize the same feasibility mechanics, making the delivery more repetitive than necessary.
- **out-07:** It states the approval question and answer explicitly, but SCQ labels are disproportionate and the file-format requirement disappears.
- **out-08:** It preserves the operative facts efficiently but treats three implementation conditions as the reasons for management action.
- **out-09:** Its requirements are particularly clear and complete, yet they support only “can be accommodated.”
- **out-10:** The concise prose preserves the main workflow but leaves the hierarchy only partly visible and does not cross from feasibility to recommendation.
- **out-11:** It gives the fullest context and a literal question, but deliberately frames that question as “can it operate?” rather than “should we accept it?”
- **out-12:** It is a polished workflow memo with no reason-level key line.
- **out-13:** Its action sequence is coherent, but the text assumes implementation without stating the approval conclusion.
- **out-14:** It gives the correct recommendation but duplicates the same mechanics as both conditions and implementation steps.
- **out-15:** It opens with approval and presents a strong sequence, but the sequence remains mechanical and adds unsupported accuracy benefits.
- **out-16:** It is compact and visibly grouped, but it supplies neither the management answer nor enough context to preserve the proposal fully.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Feasibility or implementation replaces the acceptance decision | Core loop §1–2, reader question and provisional answer | ignored | out-02, out-04, out-05, out-06, out-08, out-09, out-10, out-11, out-12, out-13, out-16 |
| Mechanics occupy the first level instead of grounded reasons | Core loop §4, Groups | ignored | out-01, out-02, out-04–out-16 |
| Literal reader question is absent | Core loop §1 and §3 | ignored | out-01–out-06, out-08–out-10, out-12–out-16 |
| Situation and complication are not both visible before support | Core loop §3, SCQ intro | missing | out-02, out-05, out-10, out-14, out-16 |
| Unsupported operational assurances or benefits are asserted | Mode 3, “Invent nothing” | ignored | out-01, out-03, out-14, out-15 |
| Operational source material disappears without acknowledgement | Mode 3, “Keep every fact” | ignored | out-01, out-07, out-16 |

## 5. Observation

The stronger outputs state an approval decision and translate mechanics into reader-level reasons before presenting evidence. The weaker outputs are often tidy, complete, and chronological, but their first-level branches remain file requirements and processing stages, so they answer whether the proposal can work rather than whether management should accept it.

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
        "answer_first": true,
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
      "hard_failures": [
        "invented_facts"
      ],
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
        "total": 8,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
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
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
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
        "total": 8,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
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
        "readers_question_literal": true,
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
        "total": 8,
        "top": 1,
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
      "output": "out-10",
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
        "answer_first": true,
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
      "output": "out-11",
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
        "answer_first": true,
        "first_level_count": 3,
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
        "total": 9,
        "top": 1,
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
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 2,
        "same_kind_grouping": 1,
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
        "order_type_named": false,
        "scq_intro_present": false
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
      "output": "out-16",
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
        "same_kind_grouping": 2,
        "explainable_order": 2,
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
    }
  ]
}
```