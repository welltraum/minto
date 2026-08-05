## 1. Score table

Structural sub-scores are `(top, key-line composition, levels, order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 2 (1, 0, 0, 1) | 7 | — |
| out-02 | 2 (1, 0, 0, 1) | 5 | — |
| out-03 | 2 (1, 0, 0, 1) | 7 | — |
| out-04 | 2 (1, 0, 0, 1) | 7 | — |
| out-05 | 2 (1, 0, 0, 1) | 7 | — |
| out-06 | 3 (2, 0, 0, 1) | 8 | `invented_facts` |
| out-07 | 2 (1, 0, 0, 1) | 7 | `invented_facts` |
| out-08 | 3 (2, 0, 0, 1) | 8 | — |
| out-09 | 7 (2, 2, 2, 1) | 9 | — |
| out-10 | 4 (1, 1, 1, 1) | 8 | `invented_facts` |
| out-11 | 6 (2, 2, 1, 1) | 9 | `unacknowledged_source_loss` |
| out-12 | 2 (1, 0, 0, 1) | 7 | — |
| out-13 | 6 (2, 2, 1, 1) | 8 | `invented_facts`, `unacknowledged_source_loss` |
| out-14 | 2 (1, 0, 0, 1) | 7 | `invented_facts` |

## 2. Decisive questions

| output | First-level kind | Grounded elements | Top answers acceptance? | Invented facts or benefits | Details below key line? | Literal reader question? |
|---|---|---:|---|---|---|---|
| out-01 | mechanics | 3 | No—only feasibility | None | No; they constitute the key line | No |
| out-02 | mechanics | 3 | No—only feasibility | None | No; the three paragraphs are process stages | No |
| out-03 | mechanics | 3 | No—only workability | None | No; requirements are promoted | No |
| out-04 | mechanics | 3 | No—only feasibility | None | No; implementation stages are the key line | No |
| out-05 | mechanics | 3 | No—only accommodation | None | No; specifications and processing are first-level | No |
| out-06 | mechanics | 3 | Yes | Identifiers being populated “before processing” and implementation without additional operational changes | No; mechanics remain the key findings | No |
| out-07 | mechanics | 3 | No; the conditional “proceed” statement is buried | An unsupported confirmation prerequisite | No; the three-part process is the key line | No |
| out-08 | mechanics | 3 | Yes | None | No; the recommendation is supported directly by stages | No |
| out-09 | benefits | 3 | Yes | None; the limits of the evidence are expressly acknowledged | Yes | No |
| out-10 | mixed | 2 | No—only accommodation | Certainty that Big Chief can supply all required data despite the stated identifier contingency | Yes, beneath the capability-style headings | No |
| out-11 | benefits | 3 | Yes | None | Mostly; retained details are subordinate, but the extraction-program and accepted-format facts disappear | No |
| out-12 | mechanics | 3 | No; it explicitly stops at feasibility | None; cost and timeline are marked as data gaps | No; requirements remain first-level | No |
| out-13 | benefits | 3 | Yes | Separate payments for every outlet-date combination, pre-submission balancing, automatic matching, and correctness claims | No; mechanics enter the SCQ and key line, while lockbox routing is lost | Yes |
| out-14 | mechanics | 3 | No—only operational feasibility | Mailing the cheque and automatic routing | No; the requirements are the key line | No |

## 3. Output notes

- **out-01:** Faithfully preserves the procedure, but merely relabels the original mechanics and leaves the acceptance decision unanswered.
- **out-02:** Concise and coherent chronologically, though its paragraph-only presentation obscures the hierarchy and never rises above feasibility.
- **out-03:** Opens with workability and visibly groups three requirements, but those requirements are still the wrong first-level kind.
- **out-04:** Presents a clean implementation sequence while omitting the managerial recommendation and benefit layer.
- **out-05:** Retains the source well, but the opening situation delays an incomplete feasibility top and the bullets remain mechanics.
- **out-06:** Gives an explicit approval recommendation, yet its supporting line is still a requirements list and its conclusion overstates the absence of operational change.
- **out-07:** A strong subject line and compact sequence do not cure the can-do versus should-do gap; the closing confirmation condition is unsupported.
- **out-08:** Recommends acceptance clearly, but both memo and diagram support that recommendation with stages rather than managerial reasons.
- **out-09:** Best separates the decision, grounded reasons, and subordinate mechanics, while candidly distinguishing feasibility from the unproven commercial case.
- **out-10:** Moves toward reason-based headings, but mixes benefits with system capabilities and overstates Big Chief’s ability to supply every identifier.
- **out-11:** Uses three grounded acceptance reasons effectively, but loses the extraction-program and accepted-file-format requirements.
- **out-12:** Correctly flags the missing commercial evidence instead of inventing it, but consequently delivers a feasibility conclusion rather than an acceptance answer.
- **out-13:** States the literal question and answers it, but the overbuilt SCQ treatment introduces unsupported details and loses the lockbox route.
- **out-14:** Cleanly displays the process stages, but it remains an operational-feasibility memo and adds unsupported transmission behavior.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Feasibility substituted for the acceptance decision | Core loop §1, Topic → reader question | ignored | out-01–out-05, out-07, out-10, out-12, out-14 |
| Mechanics promoted into or mixed with the key line | Core loop §4, Groups | ignored | out-01–out-08, out-10, out-12, out-14 |
| Reader’s question not written literally | Core loop §§1 and 3 | ignored | out-01–out-12, out-14 |
| Ordering principle absent or incorrectly named | Core loop §5, Order | ignored | out-01–out-14 |
| Unsupported operational claims added | Mode 3, “Invent nothing” | ignored | out-06, out-07, out-10, out-13, out-14 |
| Required source mechanics lost | Mode 3, “Keep every fact” | ignored | out-11, out-13 |

## 5. Observation

The stronger outputs explicitly recommend acceptance and make grounded managerial reasons the first-level branches, with fields, routing, balancing, and processing beneath them. The weaker outputs preserve and organize the procedure but mistake chronological mechanics for reasons management should approve the proposal.

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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": false
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
        "total": 5,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 0
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
        "order_type_named": false
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": false
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": false
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": false
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
        "total": 8,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": false
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
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
        "total": 8,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": false
      }
    },
    {
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
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
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": true
      }
    },
    {
      "output": "out-10",
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
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    },
    {
      "output": "out-11",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
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
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": false
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
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
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false
      }
    }
  ]
}
```