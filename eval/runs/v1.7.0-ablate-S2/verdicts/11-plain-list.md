## 1. Score table

Structural sub-scores are shown as `(top / key-line composition / levels / order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (1/1/2/2) | 8 | `unacknowledged_source_loss` |
| out-02 | 5 (1/1/1/2) | 9 | `invented_facts`, `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-03 | 4 (0/1/1/2) | 5 | `unacknowledged_source_loss` |
| out-04 | 6 (1/1/2/2) | 9 | `unacknowledged_source_loss` |
| out-05 | 4 (0/1/1/2) | 8 | `unacknowledged_source_loss` |
| out-06 | 5 (1/1/1/2) | 9 | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-07 | 6 (1/1/2/2) | 9 | `unacknowledged_source_loss` |
| out-08 | 6 (1/2/1/2) | 9 | `unacknowledged_source_loss` |

## 2. Decisive questions

| output | 1. Plain or apparatus? | 2. Listed apparatus | 3. Counts and optional staging | 4. Additions clustered? | 5. Removals one group? | 6. Covered-layer padding? | 7. Invented material |
|---|---|---|---|---|---|---|---|
| out-01 | Plain and pasteable | None | Counts absent; optional status survives | Partly; trust and failure are grouped, but production is split | Yes | No; the closing acknowledgement is brief | None |
| out-02 | Plain and pasteable | None | Says nine and three, but loses the base-eight count and staging’s optional status | Yes | No; three peer removal lines | No | “Out of scope,” mandatory nine-block alignment, and broader “distributed tracing” |
| out-03 | Carries light diagram-audit apparatus | Layer numbers in parentheses | Counts absent; optional status survives | No; organized by layers | Yes | No | None |
| out-04 | Plain and pasteable | None | Says nine and three, but loses the base-eight count and optional qualification | Partly; delivery and observability split the production cluster | Yes | No | None |
| out-05 | Plain and pasteable | None | Counts absent; optional status lost | No; additions are a flat layer-oriented list | Yes | No | None |
| out-06 | Plain and pasteable | None | Counts absent; optional status lost | Partly; delivery and observability remain separate | Yes | No | None |
| out-07 | Plain and pasteable | None | Counts absent; optional status survives | Partly; the production path is split into three bullets | Yes | No; the closing line is substantive | None |
| out-08 | Plain and pasteable | None | Counts absent; optional status lost | Yes | Yes | No | None |

## 3. Output notes

- **out-01:** It preserves the causal support and optional-staging qualification, but never supplies the required controlling count sentence and fragments the production cluster.
- **out-02:** It has a strong opening and useful clusters, but treats optional staging as required, promotes every removal to the key line, and introduces unsupported wording.
- **out-03:** Layer-by-layer presentation recreates the source organization, duplicates the retention-DB action across addition and removal, and adds the fixture’s prohibited layer tags.
- **out-04:** Its hierarchy is clean and readable, though it overstates the mandatory addition count and separates observability from the broader path-to-production cluster.
- **out-05:** It is complete at the block level but opens with a placeholder sentence, flattens the additions, and loses staging’s optional status.
- **out-06:** It is exceptionally concise and pasteable, but its flat sequence exceeds the first-level limit and omits the count nuance.
- **out-07:** It retains the strongest causal explanations and optional-staging language, but leaves the overall answer and counts until an incomplete closing summary.
- **out-08:** It most closely matches the intended four-part key line, but lacks a controlling summary and silently makes staging mandatory.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Required count nuance or optional-staging qualification is lost | Mode 3 — keep every fact; Core loop §2 — provisional answer | ignored | out-01, out-02, out-03, out-04, out-05, out-06, out-07, out-08 |
| No complete controlling summary sentence | Core loop §2; Self-check §8.3 | missing | out-01, out-03, out-05, out-06, out-07, out-08 |
| Path-to-production actions are split or flattened instead of gathered under one cluster | Core loop §4 — groups | ignored | out-01, out-03, out-04, out-05, out-06, out-07 |

## 5. Observation

The stronger outputs reduce the material to a few same-kind change clusters and keep removals together; the weaker ones reproduce layer-by-layer notes, flatten individual blocks onto the key line, or omit the count and optionality needed for a complete top answer.

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
        "total": 6,
        "top": 1,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 2
      },
      "quality": {
        "total": 8,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
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
      "output": "out-02",
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
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 6,
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
        "total": 4,
        "top": 0,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 5,
        "top": 0,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
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
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 1,
        "key_line_composition": 1,
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
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 0,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
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
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 1,
        "key_line_composition": 1,
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
        "total": 6,
        "top": 1,
        "key_line_composition": 2,
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
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
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
    }
  ]
}
```