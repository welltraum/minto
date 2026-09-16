## 1. Score table

Sub-score order: Structure = top / key-line composition / levels / order and kind; Quality = top / same-kind grouping / explainable order / MECE / visible structure.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2/1/2/1) | 8 (2/2/1/1/2) | — |
| out-02 | 6 (2/1/2/1) | 6 (2/2/1/0/1) | `more_than_four_first_level` |
| out-03 | 7 (2/2/2/1) | 7 (2/1/1/1/2) | `invented_facts` |
| out-04 | 5 (2/1/1/1) | 5 (2/1/1/0/1) | `invented_facts`, `more_than_four_first_level` |
| out-05 | 6 (2/1/2/1) | 7 (2/2/1/1/1) | `invented_facts` |
| out-06 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | — |
| out-07 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | — |
| out-08 | 6 (2/1/2/1) | 8 (2/2/1/1/2) | `invented_facts` |

## 2. Decisive questions

### out-01

1. The top is a contestable causal claim, followed by a proposed response.
2. It shows three levels: top → three actions → supporting observations.
3. There are three first-level conclusions, organized as actions rather than chronology.
4. Only the “two to three people” example survives exactly. Handoffs, research metrics, and feedback remain, but the other listed figures and examples are lost.
5. Most supporting paragraphs have minute markers, though not every claim is individually located.
6. Feedback is incomplete rather than duplicated: the human-feedback point appears once, while the CI/CD and unit-test supports are omitted.
7. The source is generally treated as practitioner evidence, but “proving effective” and the repeated “we must” slightly strengthen the speaker’s recommendations. No new number, name, company, or citation is invented.
8. None of the listed apparatus appears; it is not a chronological retelling and no file is written.

### out-02

1. The top is one contestable claim about the bottleneck moving beyond code.
2. It has top → conclusions → supports, but expands the conclusion layer to six branches.
3. Six thematic conclusions follow the answer; their sequence loosely follows the talk while remaining topic-based.
4. Surviving details are default “auto,” three to six months, the month-versus-days comparison, two or three people, contracts/APIs/databases, and roughly 100 tools. The exact two-hours/half-hour contrast, “ten plus ten,” and 20-degree example are lost; GPS, handoffs, and hypotheses survive only in generalized form.
5. No support carries a minute marker or other locator.
6. Feedback is split: CI/CD review appears under tool rollout, while external and automated feedback appear under a separate branch.
7. Estimates and anecdotes are carefully attributed to the speaker. No unsupported number, name, company, or citation is asserted.
8. None of the listed apparatus appears; the six-part expansion is thematic rather than a source-by-source retelling.

### out-03

1. The top is a contestable causal claim, though it bundles several required changes into the same sentence.
2. It displays the required three levels.
3. There are four thematic conclusions, not a strict chronological retelling.
4. It retains default “auto,” three to six months, month versus days, two or three people, contracts/APIs/databases, and the GPS/thermostat analogies. It omits the exact handoff figures, 100-tool count, “ten plus ten,” and the 20-degree detail.
5. No minute markers or other locators are supplied.
6. CI/CD and the GPS/thermostat analogy are gathered into one feedback point; unit tests are omitted.
7. Several anecdotes become firmer facts: the marketplace is said to have implemented the review agent, juniors are declared unable to manage agents effectively, and the ML System Design Doc becomes “essential.” “Usage data” also overstates an internal anecdote. No new numerical value or named organization is introduced.
8. None of the listed apparatus appears, and no file is written.

### out-04

1. The top is a contestable claim about the human side blocking acceleration.
2. It nominally separates claims from evidence, but the needed conclusion layer is fragmented into a flat table of 14 small claims.
3. There are 14 first-level claims, ordered substantially by the talk’s chronology.
4. It retains “auto,” three to six months, contracts/APIs/databases, and the GPS/heating analogies. The exact handoff times become “minutes/hours,” month versus a couple of days becomes weeks versus days, and it loses two or three people, 100 tools, “ten plus ten,” and 20 degrees.
5. No minute markers or equivalent locators are given.
6. Feedback is split across separate CI/CD and human-feedback rows; unit tests are absent.
7. Source numbers are mostly reused, but the output invents “measured output,” “training data,” and “measured learning curves,” and invents a failure in which agents caused loss of accountability over contracts.
8. A claims/evidence table and chronological retelling appear. There is no marker legend, mermaid, findings table, group-order commentary, or written file.

### out-05

1. The first sentence is a contestable answer, though it combines several changes.
2. It has three substantive levels, preceded by redundant labeled SCQA apparatus.
3. Four thematic claim groups follow the answer.
4. It retains default “auto” and three to six months. Waiting, days-long delivery, hypotheses, and the aircraft analogy survive only abstractly; the exact handoff times, month comparison, two or three people, control points, 100 tools, “ten plus ten,” GPS, and 20 degrees are absent.
5. The evidence bullets generally carry minute markers.
6. CI/CD and the aircraft-feedback analogy are gathered in one branch; unit tests are omitted.
7. The output invents that the reader’s teams expect the 10× gain and assigns the anonymized speaker a male pronoun. The remaining figures are mostly presented as the speaker’s evidence.
8. None of the specifically listed items appears, but the labeled SCQA line and “see the four claim groups below” are unrequested digest apparatus.

### out-06

1. The top is a clear, contestable claim that tool adoption alone cannot deliver the gains.
2. It consistently shows top → four conclusions → concrete supports.
3. Four reader-relevant conclusions follow the answer in a coherent operating-model sequence.
4. It retains default “auto,” three to six months, month versus days, contracts/APIs/databases, and roughly 100 tools. Handoffs and hypotheses survive without their exact figures; it omits two hours versus half an hour, two or three people, “ten plus ten,” and 20 degrees/GPS.
5. Every load-bearing section and support has a minute-range locator.
6. CI/CD review, automated checks, runtime signals, and human feedback are gathered into one control-and-feedback conclusion; only the illustrative analogies are omitted.
7. Estimates and anecdotes are explicitly attributed and qualified as practitioner evidence. Nothing is invented.
8. None of the listed apparatus appears; no chronological retelling or file is produced.

### out-07

1. The top is a contestable causal claim rather than a topic description.
2. It shows top → topic buckets → claims → supports; the real conclusions are therefore buried one level too low.
3. Four first-level topic categories appear in loose source order, rather than four direct conclusions answering the top.
4. It preserves default “auto,” three to six months, the exact two-hours/half-hour/waiting contrast, a month without code, two or three people, contracts/APIs/databases, 100 tools, and GPS plus 20 degrees. It loses the couple-of-days half of one comparison and the “ten features plus ten hypotheses” figure.
5. No minute markers or other locators are provided.
6. CI/CD and GPS/floor heating are gathered into one feedback claim; unit tests are omitted.
7. The estimates are mostly framed as the speaker’s observations or claims. No new number, name, company, or citation is invented.
8. None of the listed apparatus appears, and no file is written.

### out-08

1. The first sentence is a contestable causal claim; the second turns it into a recommendation.
2. It shows the required three levels.
3. Four action-oriented groups follow the answer in a broad organizational-to-operational sequence.
4. It retains two or three people, contracts/APIs/databases, and GPS, while preserving days, hypotheses, and unit tests without the associated exact contrasts. It omits “auto,” three to six months, the exact handoff figures, 100 tools, “ten plus ten,” and 20 degrees.
5. The supporting bullets consistently carry minute markers.
6. CI/CD review, GPS, and unit tests are gathered under the same control-and-feedback group.
7. Most claims track the speaker, but saying the marketplace “tried” the CI/CD agent turns a presented proposal into an implemented event. No new number or organization name is added.
8. None of the listed apparatus appears, and no file is written.

## 3. Output notes

- **out-01:** Clear and compact, but it drops nearly all of the talk’s diagnostic figures and omits the tool-adoption claim that explains why buying Cursor alone failed.
- **out-02:** It preserves broad coverage and careful attribution, but six overlapping branches and missing locators make the digest harder to test against the talk.
- **out-03:** The hierarchy is strong and concrete, but unsupported certainty turns several open questions and anecdotes into settled findings.
- **out-04:** The good top is followed by a chronological 14-row inventory, flattening the talk’s few conclusions into slide-level claims and adding unsupported “measured” evidence.
- **out-05:** Four claim groups and timestamps are visible, but explicit SCQA scaffolding intrudes on the chat digest and several distinctive examples disappear.
- **out-06:** This is the strongest synthesis: four direct conclusions, consistently nested evidence, locators, and careful separation of practitioner thesis from established evidence.
- **out-07:** It retains the richest set of concrete examples, but topical headings insert an unnecessary level above the actual conclusions and all locators are missing.
- **out-08:** The action structure is readable and feedback is well consolidated, but adoption evidence is absent and the marketplace proposal is incorrectly reported as an attempted implementation.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| More than four branches or a flattened conclusion layer | Core loop §4 “Groups”; Mode 4 “digest” | ignored | out-02, out-04 |
| Actual conclusions placed beneath topic labels | Core loop §4 “Depth follows the material” | buried | out-07 |
| Load-bearing supports lack source locators | Mode 4 “a source reference on every load-bearing claim” | missing | out-02, out-03, out-04, out-07 |
| Exact quantitative contrasts are softened or omitted | Mode 4 “concrete supports”; Core loop §4 depth test | missing | out-01, out-02, out-03, out-04, out-05, out-06, out-08 |
| Speaker anecdotes or tentative claims become established facts | Core loop §8 source-grounding check | ignored | out-03, out-04, out-05, out-08 |
| Feedback evidence is divided across branches instead of synthesized | Core loop §6 “MECE” | ignored | out-02, out-04 |
| Formal apparatus displaces plain chat prose | Mode 4 presentation rules | ignored | out-04, out-05 |

## 5. Observation

The stronger outputs treat the talk as four contestable conclusions, attach concrete timestamped anecdotes beneath each, and keep the speaker’s uncertainty visible. The weaker outputs either flatten the talk into too many chronological claims, bury conclusions beneath topic categories, strip out the diagnostic figures, or strengthen practitioner anecdotes into facts.

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
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
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
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 2,
        "same_kind_grouping": 2,
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
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
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
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
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
        "same_kind_grouping": 2,
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
      "output": "out-08",
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