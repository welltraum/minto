## 1. Score table

Structural sub-scores are `(top / key-line composition / levels / order and kind)`. Quality scores are raw; hard-failure penalties are not applied here.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2/1/1/2) | 4 | `invented_facts`, `more_than_four_first_level` |
| out-02 | 7 (2/2/2/1) | 9 | `invented_facts` |
| out-03 | 5 (1/1/2/1) | 7 | `invented_facts` |
| out-04 | 6 (2/1/2/1) | 7 | None |
| out-05 | 6 (2/1/2/1) | 7 | `invented_facts` |
| out-06 | 5 (1/1/2/1) | 7 | `invented_facts` |
| out-07 | 7 (2/1/2/2) | 7 | `more_than_four_first_level` |
| out-08 | 7 (2/1/2/2) | 5 | `more_than_four_first_level` |

## 2. Decisive questions

### out-01

1. The top is one contestable causal claim, although its second sentence enumerates several remedies.
2. It shows top → claims → evidence, but splits four conclusions into fourteen promoted claims.
3. There are 14 first-level claims, ordered almost entirely by transcript chronology.
4. Surviving specifics: default “auto,” three to six months, APIs/database, a hundred tools, and the GPS/floor analogy without 20 degrees. The exact handoff comparison, month-versus-couple-of-days comparison, two-or-three people, and ten-features-plus-ten-hypotheses figures are lost or blurred.
5. No minute markers or other locators are supplied.
6. Feedback is split between the CI/CD-review and external-feedback rows; unit tests are omitted.
7. It invents “measured output,” “modest productivity gains,” a control-point failure causing “loss of accountability,” and “measured learning curves”; several anecdotes are presented as measurements.
8. It uses a claims/evidence table and becomes a chronological retelling; there is no marker legend, mermaid, order commentary, or file.

### out-02

1. The top is one contestable causal claim, expressed through four causes.
2. It has the required top → conclusions → supports hierarchy.
3. Four first-level causes follow the answer in a broad people-to-architecture progression.
4. Surviving specifics: default “auto,” three to six months, and contracts/APIs/databases. The numerical handoff and product-engineer comparisons, two-or-three people, hundred tools, ten-plus-ten formulation, and 20-degrees/GPS example are absent.
5. Each branch has a minute locator.
6. The available feedback material is gathered in one branch, although unit tests and the floor-heating example are omitted.
7. “Even when forced to switch IDEs” converts a merely proposed experiment, which the speaker did not know had run, into fact; the three-to-six-month estimate is also left unqualified.
8. None of the listed apparatus or mode violations appears.

### out-03

1. A contestable answer appears, but only after a situation, complication, and literal question.
2. It shows top → three recommended changes → supporting examples.
3. Three action-oriented branches follow the eventual answer rather than merely retelling the talk.
4. Surviving specifics: two-or-three-person teams, the hundred-tool agent, and the floor-heating analogy. The month-versus-days comparison is distorted to “months”; most other listed figures and examples disappear.
5. Load-bearing paragraphs carry minute markers.
6. CI/CD review, the floor analogy, and unit-test feedback are gathered under one feedback branch.
7. “Classical teams take months” replaces the source’s “a month without writing code,” and saying the ML System Design Doc “solved” the problem strengthens “helped us a lot.”
8. None of the listed apparatus appears; it is not a chronological retelling.

### out-04

1. The top is a clear, contestable causal claim.
2. It has a full hierarchy: top → four topic groups → claims → evidence.
3. Four first-level groups use a synthesized process/roles/method/security order, though the labels are topic categories rather than parallel conclusions.
4. Surviving specifics include default “auto,” three to six months, two hours versus half an hour and waiting, two-or-three people, APIs/database, a hundred tools, and both 20 degrees and GPS. The complete month-versus-couple-of-days and ten-plus-ten comparisons are missing.
5. No minute markers or alternative locators appear.
6. CI/CD review and GPS/floor feedback are gathered in one claim; unit tests are omitted.
7. No clear factual invention appears, and uncertainty about the proposed IDE ban is preserved.
8. None of the listed apparatus or mode violations appears.

### out-05

1. The top is one contestable causal claim.
2. It shows top → four conclusions → supports.
3. Four branches follow the answer, but the first is a diagnosis while the other three are prescribed changes.
4. Surviving specifics: default “auto,” three to six months, month versus days, two-or-three people, APIs/database, and GPS/thermostat without 20 degrees. The exact handoff figures, hundred-tool count, and ten-plus-ten formulation are lost.
5. No locators are supplied.
6. CI/CD review and the two analogies are gathered under the process/feedback branch; unit tests are omitted.
7. It says the marketplace “implemented” the CI/CD reviewer where the source says it presented the idea, adds that an IDE ban is “risky,” and upgrades the ML System Design Doc from useful to “essential.”
8. None of the listed apparatus appears.

### out-06

1. The first sentence is situation and complication; the answer begins in the second sentence.
2. It shows top → three actions → supporting examples.
3. Three same-kind actions follow the delayed answer in a workable team/process/control order.
4. Surviving specifics: two-or-three people and APIs/database. Month versus days is distorted to “months,” while the other listed examples and figures are absent.
5. Every bullet has a minute marker.
6. Only the external-human-feedback point survives; CI/CD review and unit-test feedback are omitted rather than dispersed.
7. It invents that the reader’s teams have failed to obtain acceleration, changes “a month without code” to “months,” and adds outage prevention as an outcome of the disk anecdote.
8. None of the listed apparatus appears.

### out-07

1. The top is a clear, contestable claim.
2. It shows top → four numbered conclusions with supports, followed by an additional first-level speculative conclusion.
3. There are five first-level conclusions when the unparented closing speculation is counted; the body is answer-led rather than chronological.
4. Surviving specifics: default “auto,” three to six months, month versus days, two-or-three people, APIs/database, and roughly a hundred tools. The exact handoff figures, ten-plus-ten formulation, and 20-degrees/GPS analogy are absent.
5. All load-bearing claims carry timestamp ranges.
6. Review, testing, and operational feedback are gathered in the first branch, though the analogies are omitted.
7. Estimates and anecdotes are explicitly attributed to the speaker; no invented number, name, company, or citation appears.
8. None of the listed apparatus appears, but the closing speculative paragraph creates an extra branch.

### out-08

1. The top is one contestable claim, not a topic description or noun list.
2. It shows top → six conclusions → supports, then repeats much of the structure as review questions.
3. Six first-level conclusions largely follow the talk’s broad chronology.
4. Surviving specifics: default “auto,” three to six months, month versus days, two-or-three people, APIs/database, and roughly a hundred tools. The exact handoff figures, ten-plus-ten formulation, and literal 20-degrees/GPS example are absent.
5. No minute markers or other locators are present.
6. Feedback is split between operating-model change and autonomy/feedback-loop branches.
7. Estimates and anecdotes are consistently framed as the speaker’s reports or proposals; no clear invented fact, name, number, or citation appears.
8. The six groups form a partial chronological retelling; there is no marker legend, mermaid, findings table, order commentary, or file.

## 3. Output notes

- **out-01:** A strong top is diluted into a 14-row chronological inventory whose evidence lacks locators and sometimes invents measurement.
- **out-02:** The compact four-cause hierarchy and locators are strong, but the IDE-ban proposal is converted into an event and many decisive examples disappear.
- **out-03:** The evidence is well nested and located, but the answer is delayed and the adoption and service-redesign claims are materially underrepresented.
- **out-04:** It preserves the widest range of concrete examples without clear invention, but hides its conclusions beneath topical section labels and supplies no locators.
- **out-05:** Four visible branches cover the talk well, but unsupported strengthening and absent locators weaken the evidence.
- **out-06:** The three action groups are clean and located, but the opening invents a result for the reader’s teams and omits the adoption and business-function evidence.
- **out-07:** It is the most reader-oriented treatment of evidence and caveats, but its speculative epilogue becomes a fifth overlapping first-level branch.
- **out-08:** It is comprehensive and appropriately attributed, but six overlapping groups plus a duplicate review checklist undermine compression and hierarchy.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| More than four first-level conclusions | Core loop §4, “Groups — 3–4 first-level groups” | ignored | 3: out-01, out-07, out-08 |
| Missing source locators on load-bearing support | Core loop §4, “Depth follows the material”; Mode 4 | ignored | 4: out-01, out-04, out-05, out-08 |
| Answer delayed behind introductory framing | Mode 4, “answer in the first sentence” | buried | 2: out-03, out-06 |
| Speaker estimates or tentative anecdotes strengthened into facts | Core loop §4, “Keep the owner of every number” | ignored | 5: out-01, out-02, out-03, out-05, out-06 |
| Feedback evidence divided between parallel branches | Core loop §6, duplication test | ignored | 2: out-01, out-08 |
| First-level labels are topics or mixed diagnoses/actions rather than parallel conclusions | Core loop §4, same-kind test | vague | 3: out-04, out-05, out-08 |

## 5. Observation

The stronger outputs state the bottleneck claim immediately, reduce the talk to three or four parallel conclusions, preserve concrete anecdotes as the speaker’s evidence, and place feedback in one branch with locators. The weaker outputs either recreate the transcript as many chronological claims, substitute topical buckets for conclusions, omit timestamps and diagnostic figures, or strengthen anecdotes into measured facts.

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
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
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
      "output": "out-02",
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
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 1,
        "levels": 2,
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
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
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
        "total": 7,
        "top": 2,
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
      "output": "out-05",
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
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 1,
        "levels": 2,
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
        "invented_facts"
      ],
      "checks": {
        "answer_first": false,
        "first_level_count": 3,
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
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 2
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
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
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
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 2
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
        "more_than_four_first_level"
      ],
      "checks": {
        "answer_first": true,
        "first_level_count": 6,
        "first_level_kind_matches": false,
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