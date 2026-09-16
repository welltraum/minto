## 1. Score table

Structural sub-scores are `(top, key-line composition, levels, order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 8 (2, 2, 2, 2) | 9 | `more_than_four_first_level` |
| out-02 | 5 (2, 1, 1, 1) | 8 | `invented_facts` |
| out-03 | 4 (2, 1, 0, 1) | 5 | `invented_facts`, `more_than_four_first_level` |
| out-04 | 6 (2, 1, 2, 1) | 8 | `more_than_four_first_level` |
| out-05 | 4 (2, 0, 1, 1) | 6 | — |
| out-06 | 4 (1, 1, 1, 1) | 8 | — |
| out-07 | 8 (2, 2, 2, 2) | 10 | `invented_facts` |
| out-08 | 7 (2, 2, 2, 1) | 8 | `invented_facts` |

## 2. Decisive questions

### out-01

1. One clear, falsifiable causal claim: code generation alone cannot deliver the acceleration because people and process remain the bottleneck.
2. Three levels: top → conclusions → located supports.
3. Five first-level conclusions, arranged as a conceptual progression that broadly follows the talk.
4. Survive: default “auto,” three to six months, two or three people, contracts/APIs/database, and about 100 tools. The month-versus-days, features-plus-hypotheses, and GPS examples survive without their full figures; the two-hours/half-hour comparison and 20 degrees do not.
5. Yes; load-bearing supports carry minute ranges.
6. Gathered under the conventional-delivery point: review-agent routing, external correction, tests, and runtime feedback are treated as one feedback model.
7. Estimates and anecdotes are consistently attributed to the speaker; no invented number, name, company, or citation.
8. None of the listed apparatus appears; no file was written.

### out-02

1. One causal claim rather than a theme list, although it improperly asserts that the reader’s own teams have stalled.
2. Three visible levels: top → four action headings → supports.
3. Four first-level elements, organized as proposed changes rather than the speaker’s conclusions; the order is thematic, not chronological.
4. Only the GPS analogy retains one of the listed concrete examples. The remaining figures and examples are omitted or abstracted.
5. Yes; the bullets have minute markers.
6. Feedback appears in one point, but only the GPS form survives; CI/CD feedback routing and unit tests are omitted.
7. The reader’s teams are said to have stalled without source support, and “MCP server vulnerabilities” are added although the talk discusses a compromised agent, not a vulnerable server.
8. None appears; no file was written.

### out-03

1. One clear claim at the top.
2. Nominally top → claims → evidence, but functionally it is a flat list of fourteen differently scaled claims with the intermediate grouping missing.
3. Fourteen first-level claims, largely following the talk’s chronology.
4. Survive exactly: default “auto,” three to six months, and APIs/database. Other examples are weakened or altered—hours instead of the two-hour/half-hour comparison, days versus weeks instead of a month versus a couple of days, and analogies without the 20-degree detail.
5. No minute markers or equivalent locators.
6. Spread between separate CI/CD-review and human-feedback rows; unit tests are lost.
7. “Measured output,” “training data,” “measured learning curves,” and a claimed accountability failure are unsupported; several anecdotes are presented as measurements.
8. It uses a formal claims/evidence table and chronological retelling, but no marker legend, mermaid, group-order commentary, findings table, or file.

### out-04

1. One clear, falsifiable central claim.
2. Three levels: top → numbered conclusions → supports.
3. Six first-level conclusions, following the talk’s chronology rather than a tighter decision-oriented grouping.
4. Survive: default “auto,” three to six months, two or three people, contracts/APIs/database, and roughly 100 tools. The month-versus-days, features-plus-hypotheses, and GPS examples survive without their full figures; the two-hour/half-hour and 20-degree details are lost.
5. No; none of the supports has a locator.
6. Spread across the tool-rollout and feedback-loop branches.
7. Estimates and anecdotes are generally identified as the speaker’s reports or estimates; no invented factual evidence.
8. Chronological organization appears; none of the other listed apparatus appears, and no file was written.

### out-05

1. A falsifiable causal claim, but overloaded with four bundled prescriptions.
2. Four displayed levels: top → topical buckets → claims → supports; the actual conclusions are therefore buried one level too low.
3. Four first-level topical categories in a thematic, non-chronological order.
4. Survive: default “auto,” three to six months, two hours versus half an hour and the waiting handoff, two or three people, contracts/APIs/database, 100 tools, and the 20-degree/GPS analogy. The month-versus-days and features-versus-hypotheses examples lose their exact paired figures.
5. No minute markers or other locators.
6. Gathered into one process claim combining CI/CD routing and the GPS/floor analogy; unit tests are omitted.
7. The material is presented assertively but contains no new number, name, company, or citation.
8. None appears; no file was written.

### out-06

1. One prescriptive claim, but it omits the talk’s central explanation that human and process constraints displaced code generation as the bottleneck.
2. Three levels: top → action groups → supports.
3. Three first-level actions in a thematic progression from teams to process to architecture.
4. Survive: two or three people and contracts/APIs/database. The month-versus-days, features-plus-experiments, and GPS examples survive only partially; the other listed specifics are omitted.
5. Yes; every supporting bullet has a minute marker.
6. Feedback occupies one research-cycle point, but the CI/CD-review and unit-test examples are absent.
7. Estimates and anecdotes are mostly stated without explicit speaker attribution, but no new number, name, company, or citation is introduced.
8. None appears; no file was written.

### out-07

1. One strong causal claim, immediately grounded by the required operating-model changes.
2. Three levels: top → four conclusions → supports.
3. Four first-level conclusions in a coherent thematic progression.
4. Survive: default “auto,” three to six months, two or three people, and contracts/APIs/database. The month-versus-days, over-equipped-agent, features-plus-hypotheses, and GPS/thermostat examples survive without their exact figures.
5. No minute markers or equivalent locators.
6. Gathered in the process-and-feedback branch; CI/CD and external correction appear together, while unit tests are omitted.
7. Unsupported strengthening includes “usage data,” the claim that agents work several times faster than humans, the marketplace having implemented rather than presented the CI/CD approach, calling the old-IDE proposal risky, and making the design document “essential.”
8. None appears; no file was written.

### out-08

1. One clear causal claim using the speaker’s own provocative conclusion.
2. Three levels: top → four conclusions → supports.
3. Four first-level conclusions, ordered broadly by the talk’s progression.
4. Survive exactly: default “auto,” three to six months, and contracts/APIs/database. The app-in-days and aircraft-feedback examples survive without their comparisons or exact details; the other listed examples are lost.
5. Yes; supporting bullets carry minute markers.
6. Gathered under architectural control and feedback, but the CI/CD-review and unit-test examples are omitted.
7. Unsupported strengthening says clean-architecture practices become impossible, denies the speaker’s explicit one-person dual-capability exception, and changes a compromised shopping agent into one compromising the retailer’s MCP server.
8. None appears; no file was written.

## 3. Output notes

- **out-01:** The strongest located evidence chain is weakened mainly by splitting engineering/research and experimentation into separate first-level conclusions and then adding the service-actor branch.
- **out-02:** The action-oriented presentation is readable, but it substitutes generic prescriptions for several of the talk’s concrete observations and invents a condition for the reader’s teams.
- **out-03:** A strong top is flattened into a chronological inventory whose rows mix conclusions, supporting details, and repetitions of the top.
- **out-04:** The hierarchy is clear and materially faithful, but six chronology-led branches, duplicated feedback material, and missing locators make it less selective than a digest.
- **out-05:** It preserves unusually strong concrete evidence, but topical bucket labels bury the actual conclusions one level below the key line.
- **out-06:** Its three action groups are compact and well located, but they omit the adoption evidence and business-function method that explain important parts of the speaker’s case.
- **out-07:** It most clearly preserves the intended three-level argument, though several careful anecdotes and proposals are strengthened into established facts.
- **out-08:** The four-part hierarchy is concise and located, but it loses much of the distinctive evidence and materially overstates several claims.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| More than four conclusions or a flat claim inventory | Mode 4 — digest: three or four conclusions and three levels | ignored | 3: out-01, out-03, out-04 |
| Actual conclusions hidden below action or topic headings | Core loop §4 — groups keyed to the reader’s question | buried | 3: out-02, out-05, out-06 |
| Load-bearing evidence lacks minute markers | Mode 4 — digest: source reference on every load-bearing claim | missing | 4: out-03, out-04, out-05, out-07 |
| Concrete comparisons and examples replaced by generic summaries | Core loop §4 — supports keep the source’s concreteness | vague | 6: out-02, out-03, out-04, out-06, out-07, out-08 |
| Anecdotes or proposals strengthened beyond the source | Core loop §4 — preserve the owner and status of every claim | ignored | 4: out-02, out-03, out-07, out-08 |

## 5. Observation

The stronger outputs place one challengeable claim over a small set of conclusion-level branches and attach the talk’s concrete, located examples directly beneath them. The weaker outputs either flatten the talk into chronology, insert topical or action labels above the real conclusions, omit locators and distinctive figures, or strengthen the speaker’s anecdotes into measured facts.

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
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
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
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 1,
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
        "invented_facts",
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 14,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": "na",
        "mode_respected": false,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": true
      }
    },
    {
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 6,
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
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 0,
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
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": false,
        "invented_facts": false,
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
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": "na",
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": true
      }
    },
    {
      "output": "out-07",
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
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
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
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 4,
        "first_level_kind_matches": true,
        "invented_facts": true,
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