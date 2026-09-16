## 1. Score table

Structural sub-scores are shown as `(top, key-line composition, levels, order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 5 (2, 1, 1, 1) | 6 | `invented_facts` |
| out-02 | 7 (1, 2, 2, 2) | 8 | `invented_facts` |
| out-03 | 6 (2, 1, 2, 1) | 7 | `more_than_four_first_level` |
| out-04 | 3 (2, 0, 0, 1) | 4 | `invented_facts`, `more_than_four_first_level` |
| out-05 | 7 (2, 1, 2, 2) | 9 | `invented_facts` |
| out-06 | 8 (2, 2, 2, 2) | 9 | — |

## 2. Decisive questions

### out-01

1. The top is one contestable claim: the missing 10× gain is caused by human and operating-model bottlenecks.
2. It effectively shows only top → four flat bullets; evidence is embedded inside each bullet rather than displayed as a third level.
3. Four first-level elements appear, but they are mixed thematic bundles rather than a clean set of conclusions.
4. Surviving specifics: default “auto,” three to six months, contracts/APIs/databases, and GPS. The two-hour/half-hour comparison, month/couple-of-days contrast, two or three people, 100 tools, ten features plus ten hypotheses, and 20 degrees are lost.
5. Each bullet has a broad minute range, although some ranges cover several claims imprecisely.
6. Feedback is split between the control/CI branch and the GPS branch; unit tests disappear.
7. Attribution is generally to the speaker, but the marketplace is incorrectly described as having tried and failed, and “one person cannot reliably cover both” contradicts the speaker’s stated one-person possibility.
8. No legend, mermaid, findings table, order commentary, chronological retelling, or file is present.

### out-02

1. The answer is a contestable recommendation, but it comes after situation, complication, and a literal question rather than in the first sentence.
2. It shows three levels: answer → three changes → supporting examples.
3. There are three first-level actions, organized around process adaptation rather than talk chronology.
4. Of the specified examples, GPS survives; “an app in days” survives only partially. The remaining named figures and comparisons are omitted or generalized.
5. Every support has a marker, though several are coarse or inaccurate—for example, agent-facing service security is assigned to `[00:20]`.
6. CI review and GPS are gathered under the direct-feedback branch; unit tests are omitted.
7. The output turns several observations into direct prescriptions and invents that classical teams “stall for months”; the source says a team could go one month without writing code.
8. None of the listed unwanted apparatus or chronology appears, and no file is written.

### out-03

1. The top is one clear, falsifiable claim about the operating model limiting speed.
2. It shows top → conclusions → supporting prose, although the supports lack locators.
3. Five first-level conclusions appear; they broadly follow the talk’s thematic progression, and the business-function branch should have remained support under the engineering-and-research branch.
4. Surviving specifics: three to six months, month versus days, API/database controls, and about 100 tools. Default use survives without the word “auto”; the other named figures and analogies are absent.
5. No minute markers or other locators are supplied.
6. Feedback is divided between delegated review in the first branch and automated execution feedback in the second.
7. Estimates and anecdotes are consistently identified as the speaker’s account; no invented facts are apparent.
8. No legend, mermaid, findings table, order commentary, chronological retelling, or file appears.

### out-04

1. The top is a clear contestable claim about human organization blocking acceleration.
2. It has three visible levels inside many sections, but evidence and subsidiary conclusions are repeatedly promoted to first level.
3. There are 12 first-level points, ordered largely by the chronology of the talk rather than by a reader-oriented argument.
4. Many examples survive: “auto,” three to six months, month versus days, two or three people, APIs/databases, 100 tools, and GPS/temperature analogies. However, two hours versus half an hour becomes an invented “2–3×,” while ten-plus-ten and the exact 20-degree detail are lost.
5. No minute markers or equivalent locators are provided.
6. CI review, external correction, and tests are spread across separate points 4 and 5 rather than gathered under one conclusion.
7. Anecdotes are frequently labeled “Fact” or “Data.” Unsupported additions include tying no 10× uplift to a year of “auto” use, the 2–3× figure, agents breaking the control points, “most organisations” shrinking teams, retraining, and agent-specific authentication.
8. It is a chronological retelling. It contains no marker legend, mermaid, findings table, group-order commentary, or written file.

### out-05

1. The top is a single contestable causal claim.
2. It clearly shows answer → three conclusions → separately labeled claims and evidence.
3. Three first-level conclusions follow the answer in a defensible causal grouping rather than chronology.
4. Surviving specifics: two hours versus 30 minutes and waiting, two or three people, API/database controls, and GPS. Features/experiments/hypotheses survive without the ten-plus-ten figure; the remaining named examples are absent.
5. No support has a minute marker or other locator.
6. CI review and GPS are gathered under the oversight-and-feedback branch; unit tests are omitted.
7. The material is broadly framed as the speaker’s evidence, but calling the ML System Design Doc “essential” strengthens the source’s “very useful” assessment into an unsupported necessity.
8. None of the listed unwanted apparatus or chronology appears, and no file is written.

### out-06

1. The top is one clear, falsifiable claim about tool adoption being insufficient.
2. It consistently shows claim → four conclusions → concrete, located supports.
3. Four first-level conclusions follow the answer in a coherent operating-model decomposition.
4. Surviving specifics: default “auto,” three to six months, month versus days, contracts/APIs/databases, and about 100 tools. The two-hour/half-hour comparison, exact team size, ten-plus-ten, and 20 degrees/GPS are omitted.
5. Every load-bearing paragraph carries a minute range.
6. Feedback is split: review and changing context sit under the first branch, while unit tests and runtime feedback sit under the second.
7. Estimates, cases, and speculation are explicitly attributed and qualified; no invented facts are apparent.
8. No legend, mermaid, findings table, order commentary, chronological retelling, or file appears.

## 3. Output notes

- **out-01:** It reaches the right top quickly, but compresses the talk into four mixed, overlapping bullets and misstates the marketplace example.
- **out-02:** It has a strong three-level action structure, but delays the answer and preserves very little of the talk’s numerical evidence.
- **out-03:** Its skeptical attribution is excellent, but a fifth branch promotes the business-function technique and breaks the four-group limit; all locators are missing.
- **out-04:** It preserves the most raw material but reproduces the speaker’s sequence as 12 overlapping points, introduces unsupported details, and does not behave like a digest.
- **out-05:** It is concise and visibly hierarchical, but omits the adoption-and-learning conclusion, supplies no locators, and overstates the documentation tool as essential.
- **out-06:** It best combines a precise top, four defensible conclusions, concrete support, qualification, and locators; its main structural blemish is splitting feedback across two branches.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| More than four first-level conclusions | Core loop §4, “Groups — 3–4 first-level groups” | ignored | 2 (out-03, out-04) |
| Load-bearing supports lack source locators | Mode 4, “a source reference on every load-bearing claim” | ignored | 3 (out-03, out-04, out-05) |
| Concrete figures and comparisons are abstracted away | Core loop §4, “Supports keep the source’s concreteness” | missing | 5 (out-01, out-02, out-03, out-05, out-06) |
| Feedback evidence is distributed across branches | Core loop §6, “MECE — no overlaps” | ignored | 4 (out-01, out-03, out-04, out-06) |
| Speaker observations are strengthened beyond the source | Core loop §4, attribution and invention rules | ignored | 4 (out-01, out-02, out-04, out-05) |

## 5. Observation

The stronger outputs turn the talk into three or four distinct conclusions, subordinate concrete anecdotes to the right conclusion, preserve the speaker’s uncertainty, and attach locators. The weaker ones either flatten evidence into broad bullets or promote the talk’s chronological sequence into too many overlapping first-level points.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "12-talk-digest",
  "mode": "digest",
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
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": "na",
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": true
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
        "total": 8,
        "top": 1,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": "na",
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": true
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 7,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": "na",
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
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
        "total": 4,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
        "visible_structure": 0
      },
      "hard_failures": [
        "invented_facts",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 12,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": "na",
        "mode_respected": false,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": true
      }
    },
    {
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
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
        "invented_facts"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": "na",
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": true
      }
    },
    {
      "output": "out-06",
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
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": "na",
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": true
      }
    }
  ]
}
```