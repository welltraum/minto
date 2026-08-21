## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 3 (0, 1, 1, 1) | 5 (0, 2, 1, 1, 1) | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-02 | 4 (1, 1, 1, 1) | 7 (1, 2, 1, 2, 1) | `invented_facts`, `unacknowledged_source_loss` |
| out-03 | 6 (1, 2, 1, 2) | 7 (1, 2, 2, 1, 1) | `unacknowledged_source_loss` |
| out-04 | 5 (1, 1, 2, 1) | 8 (2, 1, 2, 2, 1) | `more_than_four_first_level` |
| out-05 | 3 (0, 1, 1, 1) | 5 (0, 2, 1, 1, 1) | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-06 | 4 (1, 1, 1, 1) | 5 (1, 1, 1, 1, 1) | `invented_facts`, `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-07 | 4 (1, 1, 1, 1) | 5 (1, 1, 1, 1, 1) | `unacknowledged_source_loss` |
| out-08 | 4 (1, 1, 1, 1) | 5 (1, 2, 1, 0, 1) | `unacknowledged_source_loss` |
| out-09 | 4 (1, 1, 1, 1) | 6 (1, 2, 1, 1, 1) | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-10 | 4 (1, 1, 1, 1) | 6 (1, 2, 1, 1, 1) | `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-11 | 8 (2, 2, 2, 2) | 9 (2, 2, 2, 2, 1) | `invented_facts` |
| out-12 | 3 (0, 1, 1, 1) | 5 (0, 1, 1, 2, 1) | — |
| out-13 | 8 (2, 2, 2, 2) | 10 (2, 2, 2, 2, 2) | — |
| out-14 | 4 (1, 1, 1, 1) | 6 (1, 2, 1, 1, 1) | `invented_facts`, `unacknowledged_source_loss` |
| out-15 | 4 (1, 1, 1, 1) | 7 (1, 2, 1, 1, 2) | `unacknowledged_source_loss` |
| out-16 | 4 (1, 1, 1, 1) | 7 (1, 2, 1, 1, 2) | `unacknowledged_source_loss` |

## 2. Decisive questions

1. **out-01:** Plain chat text; no listed apparatus. The top has neither count nor optional-staging nuance. Additions are implicitly clustered but production is split; the removals are contiguous but individually promoted. Covered layers are not padded. No invented facts.
2. **out-02:** Carries layer numbers in parentheses. The top gives no counts, though staging remains optional. Additions follow layer order rather than the three clusters; removals form one group. Covered layers are not padded. “Recommended” is invented.
3. **out-03:** Carries layer numbers in parentheses. The top states only the removal count and loses staging’s optional status. Additions use the three clusters and removals form one group. No covered-layer padding or invented facts.
4. **out-04:** Plain text without the listed apparatus, but it adds a fifth covered-layers branch. The top states eight and three; the ninth optional block appears only later. Additions use the correct clusters and removals form one group. No invented facts.
5. **out-05:** Plain text with no apparatus. It gives no counts or optional-staging nuance. Additions are only implicitly clustered and split the production path; removals form one line. No padding or invented facts.
6. **out-06:** Plain text with no listed apparatus. The top fixes the count at nine and omits staging’s optional status. Additions use three workable clusters, but the removals are three separate first-level lines. “Out of scope” is invented, and “distributed tracing” changes the supplied terminology.
7. **out-07:** Plain text with a padded closing statement about the covered core. It gives no counts and loses staging’s optional status. The additions are flat but ordered roughly by cluster; removals form one group. No invented facts.
8. **out-08:** Uses layer-number prefixes as apparatus. It gives no counts but preserves staging’s optional status. Additions follow layers, and the retention DB is incorrectly placed in both add and remove groups. Covered layers are not padded; no facts are invented.
9. **out-09:** Plain prose with no listed apparatus. The top states nine and three but loses staging’s optional status. Additions are organized by four layers rather than three clusters; removals form one group. No covered-layer padding or invented facts.
10. **out-10:** Plain chat text with no apparatus. The top states only that three blocks should be removed and loses staging’s optional status. Additions are implicitly grouped but split the production path; removals form one group. No padding or invented facts.
11. **out-11:** Uses layer numbers in parentheses. The top has both counts and preserves optional staging; additions use the right clusters and removals form one group. Covered layers are acknowledged in the top, not padded. “No owner” and the laptop-to-production claim are invented.
12. **out-12:** Plain text with no listed apparatus, but it lacks a controlling top and ends with a covered-core padding line. The optional status survives; additions are partly clustered but staging is detached from the production path. Removals form one group. No invented facts.
13. **out-13:** Plain, pasteable text with no listed apparatus. The top has both counts and optional staging; additions use the three clusters and removals form one group. Covered components are acknowledged in the top, not padded. No invented facts.
14. **out-14:** Includes a closing line about what the updates structurally resolve. The top says nine required and three removed, erasing optional staging. Additions are divided into four functional groups rather than the three requested clusters; removals form one group. “Critical” and “required” are invented.
15. **out-15:** Plain, pasteable text with no listed apparatus. The top states nine and three but loses optional staging. Additions use four subgroups, splitting delivery from observability; removals form one group. No padding or invented facts.
16. **out-16:** Plain, pasteable text with no listed apparatus. The top states nine and three but loses optional staging. Additions use four subgroups, splitting deployment from observability; removals form one group. No padding or invented facts.

## 3. Output notes

- **out-01:** It supplies every requested block but replaces the pyramid with seven flat action lines and drops the count, optionality, and supporting reasons.
- **out-02:** Its clean add/remove split is undermined by layer-by-layer audit notation and the unsupported recommendation for staging.
- **out-03:** It has the right cluster skeleton, but its incomplete top and layer labels prevent a fully pasteable result.
- **out-04:** It preserves nearly all source reasoning, but the covered-layers paragraph creates a fifth, wrong-kind branch.
- **out-05:** It is concise and complete at item level, but has no controlling answer or explicit cluster hierarchy.
- **out-06:** Its three addition clusters are useful, but the fixed nine-block claim, ungrouped removals, and unsupported terminology weaken it.
- **out-07:** It retains several valuable causal details, yet presents them in a flat add paragraph and loses staging’s optional status.
- **out-08:** It preserves optional staging but creates a direct overlap by treating retention-DB consolidation as both an addition and a removal.
- **out-09:** Its opening counts are useful, but layer-based organization creates five branches and silently makes staging mandatory.
- **out-10:** The bullets are easy to scan, but the production path is split and the top omits the missing-block count and optionality.
- **out-11:** Its pyramid and evidence are strong, but layer annotations overshoot the requested mode and two unsupported details contaminate it.
- **out-12:** It preserves the important evidence and optionality, but never supplies a controlling top and leaves staging structurally detached.
- **out-13:** It best combines a complete top, three addition clusters, one removal group, grounded evidence, and proportionate presentation.
- **out-14:** Its two-section hierarchy is readable, but it converts optional staging into a critical required component and adds an unnecessary closing synthesis.
- **out-15:** It is clean and compact, but fixes the count at nine and buries the intended three-cluster key line beneath generic add/remove headings.
- **out-16:** It has readable add/remove sections, but loses optionality and splits the single production-path cluster into deployment and observability.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Both counts and staging optionality are not all carried by the top | Core loop §2; Mode 3 plain-list rule | missing | out-01, out-02, out-03, out-04, out-05, out-06, out-07, out-08, out-09, out-10, out-12, out-14, out-15, out-16 |
| The three addition clusters are flattened, split, or buried below generic add/remove buckets | Core loop §4 Groups | buried | out-01, out-02, out-05, out-07, out-08, out-09, out-10, out-12, out-14, out-15, out-16 |
| Supporting causes from the assessment disappear | Mode 3 “Keep every fact from the source” | ignored | out-01, out-02, out-03, out-05, out-06, out-08, out-10, out-14, out-15, out-16 |
| Layer notation or closing/padding material overshoots the requested plain-list format | Mode 3 plain-list presentation rule | ignored | out-02, out-03, out-04, out-07, out-08, out-11, out-12, out-14 |
| Unsupported recommendations, scope claims, severities, or operational details are introduced | Mode 3 “Invent nothing” | ignored | out-02, out-06, out-11, out-14 |
| More than four elements are promoted to the first level | Core loop §4 first-level limit | ignored | out-01, out-04, out-05, out-06, out-09, out-10 |

## 5. Observation

Stronger outputs put both counts and the staging caveat in a controlling first sentence, then expose exactly four branches: three cluster-based addition groups and one removal group. Weaker outputs flatten individual blocks, organize by reference-model layer, bury clusters beneath generic add/remove headings, or add covered-state commentary that does not answer what should change.

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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [
        "unacknowledged_source_loss",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 7,
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
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts",
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": false,
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
    },
    {
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 1,
        "levels": 2,
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
      "output": "out-05",
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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
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
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
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
        "total": 5,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
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
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 0,
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
      "output": "out-09",
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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
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
        "total": 6,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
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
      "output": "out-11",
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
      "output": "out-12",
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
      "hard_failures": [],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
        "total": 7,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
      "output": "out-16",
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
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
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
    }
  ]
}
```