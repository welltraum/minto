## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 3 (0, 1, 1, 1) | 5 (0, 1, 1, 2, 1) | `unacknowledged_source_loss` |
| out-02 | 7 (1, 2, 2, 2) | 9 (1, 2, 2, 2, 2) | `unacknowledged_source_loss` |
| out-03 | 5 (2, 1, 1, 1) | 7 (2, 1, 1, 2, 1) | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-04 | 3 (0, 1, 1, 1) | 6 (0, 1, 1, 2, 2) | `unacknowledged_source_loss` |
| out-05 | 4 (1, 1, 1, 1) | 7 (1, 1, 1, 2, 2) | `unacknowledged_source_loss` |
| out-06 | 7 (1, 2, 2, 2) | 9 (1, 2, 2, 2, 2) | `invented_facts` |
| out-07 | 4 (1, 1, 1, 1) | 7 (1, 1, 1, 2, 2) | `unacknowledged_source_loss` |
| out-08 | 5 (1, 1, 1, 2) | 9 (1, 2, 2, 2, 2) | `invented_facts`, `unacknowledged_source_loss` |
| out-09 | 7 (1, 2, 2, 2) | 8 (1, 2, 2, 2, 1) | `invented_facts`, `unacknowledged_source_loss` |
| out-10 | 7 (1, 2, 2, 2) | 9 (1, 2, 2, 2, 2) | `invented_facts`, `unacknowledged_source_loss` |
| out-11 | 7 (1, 2, 2, 2) | 8 (1, 2, 2, 2, 1) | — |
| out-12 | 8 (2, 2, 2, 2) | 10 (2, 2, 2, 2, 2) | — |
| out-13 | 4 (1, 1, 1, 1) | 8 (1, 2, 1, 2, 2) | `unacknowledged_source_loss` |
| out-14 | 4 (1, 1, 1, 1) | 6 (1, 1, 1, 1, 2) | `invented_facts` |
| out-15 | 4 (1, 1, 1, 1) | 8 (1, 2, 1, 2, 2) | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-16 | 7 (1, 2, 2, 2) | 9 (1, 2, 2, 2, 2) | `invented_facts` |

## 2. Decisive questions

| output | Plain text / apparatus | Counts and optional staging | Addition grouping | Removals | Covered padding | Invented material |
|---|---|---|---|---|---|---|
| out-01 | Carries layer numbers in parentheses; no other listed apparatus | No counts; optional status lost | No—organized by layers | Yes, one group | No | None |
| out-02 | Plain; none of the listed apparatus | Nine and three stated; optional status lost | Yes | Yes | No | None |
| out-03 | Plain; none of the listed apparatus | Yes: eight required, one optional, three removals | Partly—cluster sequence is implicit, but production is fragmented | Yes | No | None |
| out-04 | Plain; none of the listed apparatus | No counts; optional status survives | No—flat addition list | Yes | No | None |
| out-05 | Plain; none of the listed apparatus | Nine and three stated; optional status lost | No—flat addition list | Yes | No | None |
| out-06 | Plain; none of the listed apparatus | No addition count; three removals; optional status survives | Yes | Yes | No | Unsupported “critical” severity |
| out-07 | Plain; none of the listed apparatus | No counts; optional status lost | No—flat addition list | Yes | No | None |
| out-08 | Plain; none of the listed apparatus | Nine and three stated, but staging is wrongly included among required components | Yes, though demoted beneath a generic Add branch | Yes | No | “Nine required components” |
| out-09 | Plain chat prose, but not list-form; no listed apparatus | No addition count; three removals; optional status lost | Yes | Yes | No | Unsupported claim that the deployment setup is “risky” |
| out-10 | Plain; none of the listed apparatus | Nine and three stated; optional status lost | Yes | Yes | No | “SSO provider” and “centralized” secrets store |
| out-11 | Light numbered-list apparatus; none of the specifically listed devices | Yes: eight, nine with optional staging, and three removals | Yes | Yes | No; covered elements are only acknowledged in the opening | None |
| out-12 | Plain; none of the listed apparatus | Yes: nine as eight required plus optional staging, and three removals | Yes | Yes | No; covered elements are confined to the top | None |
| out-13 | Plain; none of the listed apparatus | No counts; optional status lost | Partly—functional bundles are present, but production is split | Yes | No | None |
| out-14 | Plain; none of the listed apparatus | Eight and three stated; optional status survives separately, but nine is not stated | Partly—trust is grouped, while failure handling and production are fragmented | Yes | Yes, as “Solid as-is” | Unsupported claim that both SaaS connectors sit outside any trust boundary |
| out-15 | Plain; none of the listed apparatus | Nine and three stated; optional status lost | Partly—production is split across separate branches | Yes | No | None |
| out-16 | Plain chat text with acceptable bold labels; none of the listed apparatus | Top states eight and three; the optional ninth survives later | Yes | Yes | No | Unsupported “lowest-priority” ranking |

## 3. Output notes

- **out-01:** It preserves the add/remove inventory but substitutes layer-based hierarchy for the requested clusters and adds prohibited layer annotations.
- **out-02:** Its cluster structure is strong, but staging is silently treated like every other addition.
- **out-03:** The top handles staging correctly, while the supporting actions are over-fragmented and omit the source’s key rationales.
- **out-04:** It is clean and pasteable, but has no controlling sentence and leaves all additions in one flat list.
- **out-05:** The add/remove split is clear, but neither the optional qualification nor the cluster hierarchy survives.
- **out-06:** The cluster hierarchy and causal support are strong, but the answer lacks the addition count and introduces an unsupported severity.
- **out-07:** It delivers the requested inventory plainly, though without a substantive top, cluster grouping, rationales, or staging qualification.
- **out-08:** The clusters are readable, but they sit below an unnecessary generic branch and staging is incorrectly called required.
- **out-09:** The logic and supporting causes are strong, but list discipline is weaker and staging is unqualified.
- **out-10:** The hierarchy is effective, but it changes component specifications and loses staging’s optional status.
- **out-11:** It is structurally complete and well-supported, with only a delayed answer and unnecessary numbering reducing chat-mode discipline.
- **out-12:** It best combines a complete answer-first top, correct clusters, grounded support, and proportionate plain presentation.
- **out-13:** Its compact bundles are understandable, but the top, optional qualification, rationale, and production grouping are incomplete.
- **out-14:** Useful evidence survives, but the production branches are fragmented and the covered-elements padding mixes current state with requested actions.
- **out-15:** The compact action list covers every block, but production is split, staging is unqualified, and the key line exceeds the preferred width.
- **out-16:** It has a strong supported hierarchy, but the optional ninth arrives after an incomplete top and is given an invented priority.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Counts or optional-staging qualification absent from the controlling line | Core loop §2; Mode 3 plain-list rule | ignored | out-01, out-02, out-04, out-05, out-06, out-07, out-08, out-09, out-10, out-13, out-14, out-15, out-16 |
| Addition clusters flattened, split, or demoted beneath a generic Add branch | Core loop §4; Mode 3 first-level grouping | buried | out-01, out-03, out-04, out-05, out-07, out-08, out-13, out-14, out-15 |
| Material causal support or staging qualification lost | Mode 3 “Keep every fact from the source” | ignored | out-01, out-02, out-03, out-04, out-05, out-07, out-08, out-09, out-10, out-13, out-15 |
| Layer or numbering apparatus added to a plain chat list | Mode 3 plain-list presentation rule | ignored | out-01, out-11 |
| Unsupported severity, specification, or ranking introduced | Mode 3 “Invent nothing” | ignored | out-06, out-08, out-09, out-10, out-14, out-16 |

## 5. Observation

The stronger outputs place a complete count-qualified answer first, then expose trust, failure handling, production path, and removals as parallel action groups with relevant causes nested beneath them. Weaker outputs flatten everything under Add/Remove, split one cluster into several peer branches, lose staging’s optional status, or add presentation and factual detail that the pasteable-list request did not support.

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
        "total": 3,
        "top": 0,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": false,
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
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 1,
        "key_line_composition": 2,
        "levels": 2,
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
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
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
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["unacknowledged_source_loss", "more_than_four_first_level"],
      "checks": {
        "answer_first": true,
        "first_level_count": 6,
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
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 0,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 2
      },
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": false,
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
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
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
      "hard_failures": ["unacknowledged_source_loss"],
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
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 1,
        "key_line_composition": 2,
        "levels": 2,
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": false,
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
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
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
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": false,
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
        "total": 5,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
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
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
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
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 1,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 8,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
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
      "output": "out-10",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 1,
        "key_line_composition": 2,
        "levels": 2,
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
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
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
        "total": 7,
        "top": 1,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 2
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
        "answer_first": false,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
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
        "total": 8,
        "top": 2,
        "key_line_composition": 2,
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
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
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
      "hard_failures": ["unacknowledged_source_loss"],
      "checks": {
        "answer_first": false,
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
        "total": 6,
        "top": 1,
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-15",
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
      "hard_failures": ["unacknowledged_source_loss", "more_than_four_first_level"],
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
      "output": "out-16",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 1,
        "key_line_composition": 2,
        "levels": 2,
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
      "hard_failures": ["invented_facts"],
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
    }
  ]
}
```