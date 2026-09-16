## 1. Score table

Structural sub-scores are `(top, key-line composition, levels, order and kind)`; quality sub-scores are `(top, grouping, order, MECE, display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 8 (2, 2, 2, 2) | 10 (2, 2, 2, 2, 2) | — |
| out-02 | 5 (2, 1, 1, 1) | 7 (2, 2, 1, 1, 1) | `invented_facts` |
| out-03 | 7 (2, 2, 2, 1) | 8 (2, 2, 1, 1, 2) | `invented_facts` |
| out-04 | 6 (2, 1, 2, 1) | 7 (2, 1, 1, 1, 2) | — |
| out-05 | 4 (2, 0, 1, 1) | 4 (2, 0, 1, 0, 1) | `invented_facts`, `more_than_four_first_level` |
| out-06 | 6 (2, 1, 2, 1) | 7 (2, 2, 1, 1, 1) | `more_than_four_first_level` |

## 2. Decisive questions

### out-01

1. The top is one falsifiable claim: tool adoption alone cannot produce the acceleration because the surrounding operating model must change.
2. It shows three levels: top → four conclusions → timestamped supports.
3. Four conclusions follow an operating-model progression rather than transcript chronology.
4. Preserved: default “auto,” three to six months, contracts/APIs/databases, roughly 100 tools, and the month-versus-days comparison in shortened form. It omits the exact two-hours/half-hour contrast, two-or-three-person figure, ten-features/ten-hypotheses figure, and 20-degree/GPS details.
5. Yes; every supporting bullet has a minute range.
6. The review-agent, external correction, and runtime/test feedback material is gathered under the old-delivery-model conclusion, though the floor/GPS details are compressed.
7. Estimates and anecdotes are consistently attributed to the speaker; no unsupported number, name, company, or citation is added.
8. None of the listed apparatus appears; it is thematic rather than chronological and writes no file.

### out-02

1. The top is a falsifiable claim, not a topic or noun list.
2. It is principally a top followed by four compact paragraphs; conclusions and evidence are distinguishable, but the third level is weakly displayed.
3. Four first-level conclusions follow a thematic “pillars” cut, not chronology.
4. Of the specified examples, only contracts/APIs/databases clearly survives. The learning curve, handoff timings, team-size figure, 100-tool case, ten-plus-ten formulation, and temperature/GPS analogies are lost.
5. Yes; each numbered paragraph has a locator.
6. The CI/CD feedback point is kept in one branch, but the GPS/floor and unit-test supports are omitted.
7. Attribution is uneven. “Run wild” is an invented quotation, and the marketplace example is incorrectly called a failed experiment; the source only presents it as a flawed design.
8. No marker legend, mermaid, findings table, order commentary, chronological retelling, or file.

### out-03

1. The top is one contestable causal claim.
2. It clearly shows top → three conclusions → claim/evidence supports.
3. Three first-level conclusions are thematic, although the Jira research-cycle material overlaps the engineering/research branch.
4. Preserved: two hours versus thirty minutes and waiting, two-to-three-person teams, contracts/APIs/databases, and the GPS analogy. Default “auto,” three to six months, month versus a couple of days, 100 tools, ten features plus ten hypotheses, and 20 degrees are absent.
5. No; none of the load-bearing supports has a timestamp.
6. CI/CD review and GPS are gathered under human oversight; unit tests are omitted.
7. The anecdotes are often stated as evidence without explicit speaker qualification. Calling the ML System Design Doc “essential” strengthens the speaker’s “very useful” assessment into an unsupported necessity; no name or citation is invented.
8. None of the listed apparatus appears, and the organization is thematic rather than chronological.

### out-04

1. The top is one actionable claim about how to change the operating model.
2. It shows top → four actions/conclusions → short timestamped supports.
3. Four first-level actions follow the recommended process changes, not transcript chronology.
4. Preserved: contracts/APIs/databases and two-to-three-person teams; the month-versus-days case is generalized. The remaining named examples and exact figures are omitted.
5. Yes; each branch has grouped minute markers.
6. Control points and external correction are gathered in one branch, but the CI/CD, unit-test, GPS, and 20-degree specifics are mostly omitted.
7. Claims are generally framed as the speaker’s warning or experience. No new number, name, company, or citation is asserted.
8. No listed apparatus, chronological retelling, or file appears.

### out-05

1. The top is a falsifiable claim, but it expands into several prescriptions.
2. It has subordinate bullets within sections, yet the controlling key line is a twelve-part transcript outline rather than three or four synthesized conclusions.
3. There are twelve first-level sections, ordered substantially by the talk’s chronology; a later six-item recap adds another competing summary.
4. Preserved or partly preserved: default “auto,” three to six months, month versus days, two-to-three-person teams, contracts/APIs/databases, 100 tools, and GPS without the 20-degree example. The two-hours/half-hour example is replaced by an unsupported 2–3× statistic, and the ten-plus-ten formulation is generalized away.
5. No; the digest contains no minute markers.
6. Feedback is split between the control-point/CI discussion and a separate feedback-mechanism section.
7. Estimates are repeatedly labeled “Fact” or “Data” rather than kept as the speaker’s anecdotes. Inventions or unsupported strengthenings include a year of “auto” use producing no uplift, the 2–3× speed figure, an unspecified case supposedly showing agents breaking control points, retraining, and authentication.
8. It is a chronological retelling with formal document-like apparatus; there is no marker legend, mermaid, findings table, order commentary, or file.

### out-06

1. The top is one falsifiable claim about the operating model surrounding agents.
2. It shows top → five conclusions → prose supports.
3. Five first-level conclusions use a thematic rather than chronological arrangement, but exceed the four-group limit.
4. Preserved: three to six months, contracts/APIs/databases, roughly 100 tools, and the month-versus-days contrast in abbreviated form. “Auto,” exact handoff times, two-or-three people, ten plus ten, and the temperature/GPS examples are lost.
5. No; none of the load-bearing supports has a minute marker.
6. The surviving testing and runtime-feedback material is consolidated in one branch; the CI/CD and analogy supports are omitted.
7. Estimates and cases are carefully marked as the speaker’s account, belief, or example; no unsupported number, name, company, or citation is introduced.
8. No listed apparatus, chronological retelling, or file appears.

## 3. Output notes

- **out-01:** The strongest synthesis: it preserves four distinct conclusions, concrete examples, locators, and a useful process-review close without losing the three-level hierarchy.
- **out-02:** Its concise four-pillar frame is readable, but it flattens the evidence, omits most diagnostic examples, and invents both a quotation and a failed experiment.
- **out-03:** The claim/evidence hierarchy is strong, but absent locators and the unsupported “essential” characterization weaken an otherwise coherent digest.
- **out-04:** It converts the talk into four useful process changes with locators, though the final branch mixes roles, service design, security, and future-state speculation.
- **out-05:** It retains broad coverage but follows the transcript through twelve overlapping sections, making the output a retelling rather than a selective digest.
- **out-06:** It is judicious about evidential status and offers practical review questions, but five branches and missing timestamps leave the synthesis less disciplined than the strongest output.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Load-bearing evidence lacks locators | Mode 4 — reference every load-bearing claim; Core loop §4 | ignored | out-03, out-05, out-06 |
| Concrete figures and examples are abstracted away | Mode 4 — preserve anything that could change action; Core loop §4 | ignored | out-02, out-04, out-06 |
| More than four first-level groups | Core loop §4; Mode 4 — two to four groups | ignored | out-05, out-06 |
| Source claims are strengthened or supplemented | Core loop §§4 and 8 — stay inside the material and verify support | ignored | out-02, out-03, out-05 |
| The thematic synthesis is replaced or weakened by source-order presentation | Mode 4 — key groups to the reader’s question, not the source sequence | ignored | out-05 |
| Supporting evidence is present but not visibly nested as a third level | Core loop §4 — long-source depth rule | buried | out-02 |

## 5. Observation

The stronger outputs turn the talk into a single contestable top, three or four thematic conclusions, and concrete timestamped evidence beneath each. The weaker outputs either compress away the examples that let the reader test the claims or reproduce the talk’s sequence as too many overlapping headings.

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
      "output": "out-06",
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
    }
  ]
}
```