## 1. Score table

Structural sub-scores are `(top / key-line composition / levels / order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 5 (2/0/2/1) | 4 | `invented_facts`, `more_than_four_first_level` |
| out-02 | 7 (2/2/2/1) | 8 | `more_than_four_first_level` |
| out-03 | 5 (2/1/1/1) | 6 | `invented_facts` |
| out-04 | 7 (2/2/2/1) | 8 | `invented_facts` |
| out-05 | 5 (1/1/2/1) | 7 | `invented_facts` |
| out-06 | 7 (2/2/2/1) | 8 | `more_than_four_first_level` |

## 2. Decisive questions

### out-01

1. The top is a disputable causal claim: human organization, rather than code generation, blocks the promised acceleration.
2. It shows three levels—top, conclusions, supports—but then adds a second, repetitive takeaway structure.
3. There are 12 first-level conclusions, ordered largely by the talk’s chronology rather than by a compact answer.
4. Surviving specifics: default “auto,” three to six months, waiting handoffs, a month versus “days,” two or three people, API contracts and databases, 100 tools, and GPS/temperature without the stated 20 degrees. It replaces the two-hours/half-hour example with an unsupported “2–3×,” and omits the exact ten-features-plus-ten-hypotheses comparison.
5. No minute markers or equivalent locators are supplied.
6. Feedback is split: CI/CD review is under control points, while GPS/floor heating and execution signals sit in a separate feedback branch.
7. Attribution is inconsistent. Unsupported additions include “after a year” linking default mode to the missing 10×, a measured-looking “2–3× faster,” and a supposedly real case of agents breaking the named control points.
8. It has no legend, mermaid, findings table, group-order commentary, or file; it does chronologically retell the talk through 12 sections.

### out-02

1. The top is one clear, disputable claim about operating-model redesign being necessary for major speed gains.
2. It shows top → conclusions → concrete supports.
3. There are five first-level conclusions; they form a mostly thematic progression, though they broadly track the talk’s sequence.
4. Surviving specifics: default “auto,” three to six months, waiting handoffs, a month versus days, API contracts and databases, and roughly 100 tools. It omits the exact two-hours/half-hour comparison, two or three people, ten features plus ten hypotheses, and 20 degrees/GPS.
5. Every main evidentiary paragraph carries minute locators.
6. Feedback is kept inside the conventional-software point; tests and operating signals survive, while the CI/CD and GPS/floor examples are omitted rather than duplicated.
7. Estimates and cases are consistently attributed to the speaker or consultancy; no invented numbers, names, companies, or citations appear.
8. None of the listed apparatus or mode violations appears.

### out-03

1. The top is a disputable claim, but it carries a four-part prescription inside the sentence.
2. It shows top → four clusters → supports.
3. There are four first-level clusters, but they mix a cause with required changes and duplicate control points across two branches.
4. Surviving specifics: default “auto,” three to six months, API contracts and databases, waiting handoffs without the task times, “days” without the month comparison, and a temperature analogy without 20 degrees or GPS. It omits two or three people, 100 tools, and ten features plus ten hypotheses.
5. The supports carry minute markers.
6. Feedback is spread: the CI/CD example is under the human-bottleneck branch, while external feedback is under a separate feedback branch.
7. The numbers themselves come from the source, but the output invents reader-specific Cursor adoption, says the marketplace “tried” the review setup when the source only says it presented it, and strengthens feedback into a real-time requirement.
8. None of the listed elements appears; it does add explicit Situation/Complication/Question labels.

### out-04

1. The top is one clear causal claim about classical processes blocking acceleration.
2. It shows top → three conclusions → claim/evidence supports.
3. There are three first-level conclusions, organized thematically rather than chronologically.
4. Surviving specifics: two hours versus thirty minutes and waiting, two or three people, API contracts and databases, and GPS without the 20-degree example. Default “auto,” three to six months, the month-versus-couple-of-days comparison, 100 tools, and ten features plus ten hypotheses are absent.
5. No support has a minute marker or other locator.
6. The CI/CD and GPS material is gathered under human oversight; unit tests are omitted.
7. Most material is presented as evidence within the speaker’s argument, but calling the ML System Design Doc “essential” strengthens “helped us a lot” into an unsupported necessity. No number, name, company, or citation is newly invented.
8. None of the listed apparatus or mode violations appears.

### out-05

1. The first sentence states the situation and failure, while the actual answer—restructure the process—arrives in the third sentence.
2. It shows an introductory top followed by three action groups and supporting bullets.
3. There are three first-level actions; they mostly follow the chronology of the talk’s latter half.
4. Of the specified examples, only the two-to-three-person team survives exactly. Hypotheses, handoffs, and control points appear only as abstractions; the other figures and examples are lost.
5. Every supporting bullet carries a minute marker.
6. The feedback theme—CI/CD review, GPS/floor heating, and unit tests—is absent.
7. The output adopts the speaker’s prescriptions as facts about “our” situation, invents that the reader’s teams expected rapid acceleration, and says one role cannot cover both sides despite the speaker explicitly allowing one person with both capabilities.
8. None of the listed apparatus appears; the three branches do follow the later talk sequence.

### out-06

1. The top is one clear, disputable claim that the operating model, not automatic code generation, limits speed.
2. It shows top → five conclusions → supporting examples.
3. There are five first-level conclusions, arranged substantially in talk order.
4. Surviving specifics: three to six months, waiting handoffs, a month versus days, API contracts and databases, and about 100 tools. “Auto” is reduced to “defaults”; the exact task times, two or three people, ten features plus ten hypotheses, and 20 degrees/GPS are absent.
5. No minute markers or equivalent locators are supplied.
6. Feedback is spread between the first branch’s delegated review loops and the second branch’s testing and runtime signals; the concrete CI/CD and GPS/floor examples are omitted.
7. Estimates and anecdotes are carefully identified as the speaker’s or consultancy’s experience; no invented facts, numbers, names, companies, or citations appear.
8. No listed apparatus or file appears. The result is thematic rather than a full retelling, although its five groups follow the source chronology.

## 3. Output notes

- **out-01:** It preserves many examples but flattens them into 12 overlapping, chronological branches and introduces several unsupported factual strengthenings.
- **out-02:** It is the strongest traceable digest, with careful attribution and locators, but its research-cycle branch partly duplicates agent development and raises the first level to five.
- **out-03:** Its four-cluster frame is visible, but “human bottleneck” and “control points and feedback” duplicate each other and several source claims are strengthened.
- **out-04:** It achieves the cleanest three-branch hierarchy and keeps feedback together, but supplies no locators and overstates the ML System Design Doc.
- **out-05:** It offers three concise actions with locators, but buries the answer and removes most of the concrete evidence needed to assess those actions.
- **out-06:** It is balanced and appropriately skeptical, but five largely chronological branches and absent locators weaken the pyramid.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| More than four first-level conclusions | Core loop §4 “Groups”; Mode 4 “digest” | ignored | out-01, out-02, out-06 |
| Load-bearing supports lack minute locators | Mode 4 “digest” | ignored | out-01, out-04, out-06 |
| Concrete figures and comparisons are replaced by abstractions | Core loop §4 “Supports keep the source’s concreteness” | missing | out-03, out-05 |
| Feedback is duplicated or split across first-level branches | Core loop §6 “MECE” | ignored | out-01, out-03, out-06 |
| Speaker anecdotes or tentative claims are strengthened into facts | Core loop §4 “Keep the owner of every number” | ignored | out-01, out-03, out-04, out-05 |

## 5. Observation

The stronger outputs state one causal answer, group the talk into a small set of conclusions, preserve concrete examples beneath the right conclusion, and distinguish the speaker’s anecdotes from evidence. The weaker outputs either replay the talk as many chronological topics, duplicate feedback and control across branches, or compress away the figures that let the reader judge the claims.

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
        "key_line_composition": 0,
        "levels": 2,
        "order_and_kind": 1
      },
      "quality": {
        "total": 4,
        "top": 2,
        "same_kind_grouping": 0,
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
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
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
      "output": "out-04",
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
      "output": "out-05",
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
    }
  ]
}
```