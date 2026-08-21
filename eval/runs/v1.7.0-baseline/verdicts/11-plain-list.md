## 1. Score table

Sub-scores are shown as `(top / key line / levels / order)` for Structure and `(top / grouping / order / MECE / display)` for Quality.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (1/1/1/1) | 6 (1/1/2/1/1) | `more_than_four_first_level` |
| out-02 | 4 (1/1/1/1) | 8 (1/2/1/2/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-03 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | `invented_facts` |
| out-04 | 3 (1/1/0/1) | 6 (1/1/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-05 | 3 (1/1/0/1) | 6 (1/1/1/2/1) | `invented_facts`, `unacknowledged_source_loss` |
| out-06 | 3 (1/1/0/1) | 7 (1/1/1/2/2) | `unacknowledged_source_loss` |
| out-07 | 4 (1/1/0/2) | 7 (1/1/2/2/1) | `unacknowledged_source_loss` |
| out-08 | 3 (1/1/0/1) | 7 (1/1/1/2/2) | `unacknowledged_source_loss` |
| out-09 | 5 (1/1/1/2) | 7 (1/1/2/2/1) | `invented_facts`, `unacknowledged_source_loss` |
| out-10 | 6 (1/2/1/2) | 7 (1/2/2/1/1) | `invented_facts`, `unacknowledged_source_loss` |
| out-11 | 6 (2/1/1/2) | 9 (2/2/2/1/2) | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-12 | 3 (1/1/0/1) | 7 (1/1/1/2/2) | `unacknowledged_source_loss` |
| out-13 | 8 (2/2/2/2) | 9 (2/2/2/2/1) | `invented_facts` |
| out-14 | 5 (1/2/0/2) | 9 (1/2/2/2/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-15 | 3 (1/1/0/1) | 6 (1/1/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-16 | 4 (1/1/0/2) | 7 (1/1/2/2/1) | `unacknowledged_source_loss` |

## 2. Decisive questions

| output | 1. Plain or apparatus? | 2. Listed apparatus | 3. Counts and optional staging | 4. Cluster grouping | 5. Removals together | 6. Covered-layer padding | 7. Invented material |
|---|---|---|---|---|---|---|---|
| out-01 | Light document apparatus | Layer numbers in parentheses | Top gives only the addition count; optional status survives later | Yes | Yes | Yes | None |
| out-02 | Plain pasteable text | None | Says nine and three, but loses the required/optional distinction | Mostly; delivery and observability are split | Yes | No | Treats staging as required; adds “obsolete,” “out of scope,” and “full observability” claims |
| out-03 | Plain pasteable text | None | Yes | No; additions are flat | Yes | Yes | Adds a credentials claim and says the ML block is not planned work |
| out-04 | Plain pasteable text | None | No counts; staging is absent | No; flat list | Yes | No | Claims the architecture is not ready |
| out-05 | Light document apparatus | Layer numbers in parentheses | No counts; staging is not marked optional | No; organized by layer | Yes | No | Assigns the two excess blocks to layer 6 and treats staging as required |
| out-06 | Plain pasteable text | None | No counts; staging is not marked optional | Implicit clusters, but the production path is split | Yes | No | None |
| out-07 | Light document apparatus | Layer numbers in parentheses | No counts; optional status survives | No; organized by layer | Yes | No | None |
| out-08 | Plain pasteable text | None | No counts; optional status survives | Only implicitly, with the production path fragmented | Yes | No | None |
| out-09 | Light layer scaffold | None of the specifically listed devices | Top gives only the removal count; optional status is lost | No; organized by layer | Yes | No | Invents “critical” severity and calls the items obsolete |
| out-10 | Light document apparatus | Layer numbers in parentheses | Top says eight and three, but the body adds nine and omits staging’s optional status | Yes | Yes | No | Treats staging as required |
| out-11 | Plain pasteable text | None | Yes | Yes, though staging is promoted to a separate branch | Yes | No | None |
| out-12 | Plain pasteable text | None | No counts; optional status survives | No; flat list | Yes | No | None |
| out-13 | Light document apparatus | Layer numbers in parentheses | Yes | Yes | Yes | No; covered layers appear only in the top | Says the connectors are live and labels the ML block “not architecture” |
| out-14 | Plain pasteable text | None | Says nine and three, but loses the optional distinction | Yes | Yes | No | Treats staging as required and substitutes “no consumers” for the stated lack of inbound writes |
| out-15 | Plain pasteable text | None | Says nine and three, but loses the optional distinction | No; failure handling and deployment are mixed | Yes | No | Treats staging as required and labels all removals obsolete |
| out-16 | Disproportionate heading/layer apparatus | None of the specifically listed devices | Says eight and three, but omits optional staging entirely | No; organized by layer | Yes | No | None |

No output uses pyramid markers or a legend, `##` headings, ordering meta-commentary, SCQ labels, mermaid, or a closing line describing its structural rewrite.

## 3. Output notes

- **out-01:** The useful cluster logic is diluted by a separate staging aside, layer annotations, and an unnecessary covered-layers branch.
- **out-02:** It groups additions clearly but silently turns optional staging into a required component and splits the production path.
- **out-03:** The answer-first opening is strong, but the additions remain a flat inventory and the covered-layer coda pads the response.
- **out-04:** It supplies the essential required block names but omits staging, supporting reasons, and an answer-first synthesis.
- **out-05:** Layer-by-layer presentation preserves the inventory while missing the requested cluster logic and optional-status nuance.
- **out-06:** It is concise and pasteable, but its unlabeled bundles erase the reasons and the distinction between required and optional additions.
- **out-07:** Optional staging survives, but layer annotations replace the more useful trust/failure/production grouping.
- **out-08:** The format is proportionate, though the production-path items are fragmented and the causal support is lost.
- **out-09:** The layer scaffold is readable but does not follow the requested cluster structure, and it adds unsupported severity language.
- **out-10:** The cluster structure is strong, but the top count conflicts with the body because staging is presented as required.
- **out-11:** This is the strongest plain-chat rendering, although staging becomes a separate first-level action and the source’s causal support disappears.
- **out-12:** It is clean and pasteable but functions as an undifferentiated inventory rather than a pyramid.
- **out-13:** It most closely matches the intended pyramid and preserves the causal logic, with only unnecessary layer apparatus and small unsupported embellishments.
- **out-14:** Its compact cluster structure is effective, but optional staging is converted into a required addition and one removal rationale reverses the source’s arrow logic.
- **out-15:** It is concise, but the middle group mixes failure handling with deployment while observability is separated from the rest of the production path.
- **out-16:** The layer headings make the hierarchy easy to scan but overshoot the chat format, omit optional staging, and discard the supporting reasons.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Counts or optional-staging status absent, incomplete, or inconsistent | Core loop §2 and §8.3 — provisional answer and top self-check | ignored | out-01, out-02, out-04, out-05, out-06, out-07, out-08, out-09, out-10, out-12, out-14, out-15, out-16 |
| Additions left flat, organized by layer, or split across the wrong clusters | Core loop §4 — Groups | ignored | out-02, out-03, out-04, out-05, out-06, out-07, out-08, out-09, out-12, out-15, out-16 |
| Material causal support removed without acknowledgement | Mode 3 — keep every fact from the source | ignored | out-02, out-04, out-05, out-06, out-07, out-08, out-09, out-10, out-11, out-12, out-14, out-15, out-16 |
| Tentative or source-bounded claims converted into certainty or embellished | Mode 3 — invent nothing | ignored | out-02, out-03, out-04, out-05, out-09, out-10, out-13, out-14, out-15 |
| Layer labels and formal scaffolding overshoot the requested chat format | Mode 3 — render in the format the request implies | buried | out-01, out-05, out-07, out-09, out-10, out-13, out-16 |

## 5. Observation

The stronger outputs open with the complete answer, preserve the required-versus-optional staging distinction, organize additions into trust, failure handling, and path-to-production clusters, then place all removals together. Weaker outputs flatten the inventory or revert to layer order, omit causal support, misstate staging, or add audit-like layer apparatus to what should be plain chat text.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "11-plain-list",
  "mode": "write",
  "outputs": [
    {
      "output": "out-01",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-02",
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
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
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
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 1,
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
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
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
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
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
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
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
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 1,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 1,
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
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-11",
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
        "unacknowledged_source_loss",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-12",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
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
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 8,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-14",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 2,
        "levels": 0,
        "order_and_kind": 2
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
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-15",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 1,
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
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-16",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 2,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    }
  ]
}
```