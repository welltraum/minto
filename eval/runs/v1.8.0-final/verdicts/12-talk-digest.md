## 1. Score table

Structural sub-scores are `(top / key-line composition / levels / order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2/1/2/1) | 7 | `invented_facts` |
| out-02 | 8 (2/2/2/2) | 9 | `invented_facts` |
| out-03 | 6 (2/1/2/1) | 5 | `invented_facts`, `more_than_four_first_level` |
| out-04 | 6 (2/1/2/1) | 7 | — |
| out-05 | 8 (2/2/2/2) | 10 | — |
| out-06 | 8 (2/2/2/2) | 10 | — |
| out-07 | 5 (1/1/2/1) | 7 | `invented_facts` |
| out-08 | 5 (1/1/2/1) | 7 | `invented_facts` |

## 2. Decisive questions

### out-01

1. The top is a contestable causal claim, not merely a topic, although its second sentence expands into several themes.
2. It shows three levels: top → four topical domains → claims and supports.
3. There are four first-level elements, grouped by subject rather than chronology; they are topic labels rather than conclusions.
4. Survive: default “auto,” three-to-six months, contracts/APIs/database, and GPS. The exact handoff figures, month-versus-days contrast, two-or-three-person figure, hundred tools, ten-plus-ten formulation, and 20°C example do not.
5. No minute markers or other usable locators.
6. The CI/CD review, GPS analogy, and unit-test feedback are gathered under one control-and-feedback claim.
7. The estimates are mostly stated as facts rather than the speaker’s anecdotes; “ML System Design Doc is essential” strengthens “very useful” without support.
8. No marker legend, mermaid, findings table, ordering commentary, chronological retelling, or file.

### out-02

1. The top is a clear, contestable claim.
2. It shows top → four conclusions → supports.
3. Four analytical conclusions follow the answer rather than the talk’s chronology.
4. Survive: three-to-six months, two-or-three people, contracts/APIs/database, hundred tools, GPS, and the floor-heating analogy, though not 20°C. Default “auto,” exact handoff figures, month-versus-days, and ten-features-plus-ten-hypotheses are absent.
5. No locators.
6. Feedback is spread across workflow, human-role, and architecture branches.
7. Estimates are insufficiently attributed; “essential” documentation and an industry-wide move to an “assembler” model strengthen the source.
8. None of the listed presentation artifacts appears.

### out-03

1. The opening paragraph eventually gives a contestable claim, but its first sentence states only that 10× did not happen.
2. It has three visible levels, but the top is followed by an over-fragmented set of ten conclusions.
3. Ten first-level conclusions largely track the talk’s chronology.
4. Almost everything survives: default “auto,” three-to-six months, two hours versus 30 minutes and waiting, month versus days, contracts/APIs/database, hundred tools, ten-plus-ten, and the GPS/floor analogy. The two-or-three-person team figure and exact 20°C detail do not.
5. No minute markers or equivalent locators.
6. Feedback is split among code review, control points, and a separate feedback section.
7. Several claims are strengthened or invented: “auto” was ineffective, a contract-changing agent caused breakage, handoffs consumed days, teams without monitoring demonstrably failed, and multiple companies split the two roles.
8. It uses numerous evidence tables and substantially retells the talk chronologically; there is no marker legend, mermaid, findings table, order commentary, or file.

### out-04

1. The top is the speaker’s contestable “human is the obstacle” claim, immediately tied to required redesign.
2. It shows top → four conclusions → short supports.
3. Four conclusions run roughly from current blockers to future architecture, partially echoing chronology.
4. Survive: default “auto,” contracts/APIs/database, and GPS. Three-to-six months, both delivery-time comparisons, two-or-three people, hundred tools, ten-plus-ten, and 20°C are absent.
5. Yes; supports carry minute ranges.
6. Feedback is partly spread between the first and third branches, while CI/CD review and unit-test evidence are omitted.
7. The claims remain framed as the speaker’s; no invented number, name, company, or citation appears.
8. None of the listed artifacts appears.

### out-05

1. The top is a contestable central claim about the operating model replacing code generation as the constraint.
2. It shows top → four arguments → concrete supports.
3. Four analytical arguments follow the answer rather than chronology.
4. Survive: default “auto,” three-to-six months, month versus days, two-or-three people, contracts/APIs/database, and hundred tools. Exact handoff times, ten-plus-ten, and 20°C/GPS do not.
5. No locators.
6. Feedback is divided between outcome control and the broader feedback/product-ownership branch.
7. Estimates and examples are consistently attributed to the speaker; no inventions appear.
8. None of the listed artifacts appears.

### out-06

1. The top is a clear, contestable claim and explicitly warns that it is based on consultancy experience rather than established evidence.
2. It shows top → four conclusions → concrete, located supports.
3. Four analytical conclusions follow the answer, not chronology.
4. Survive: default “auto,” three-to-six months, month versus days, contracts/APIs/database, and hundred tools. Exact handoff figures, two-or-three people, ten-plus-ten, and 20°C/GPS are omitted.
5. Yes; every load-bearing support has a minute marker.
6. CI/CD review, external human correction, and automated operational feedback are consolidated in the first branch.
7. Estimates and anecdotes are carefully attributed; no inventions appear.
8. None of the listed artifacts appears.

### out-07

1. The top is a prescriptive list of changes presented as the output’s own recommendation rather than a properly attributed single speaker claim.
2. It shows top → three action branches → supports.
3. Three first-level actions are analytically grouped, not chronological.
4. Survive: month-versus-days in distorted form, two-or-three people, and APIs/database. Default “auto,” three-to-six months, exact handoff figures, hundred tools, ten-plus-ten, and 20°C/GPS are absent.
5. Yes; the load-bearing paragraphs carry minute markers.
6. The surviving feedback material is kept in the architecture branch, but CI/CD review and unit-test support are lost.
7. The speaker’s claims are adopted as “we must” conclusions; “classical teams stall for months” changes the source’s “a month” anecdote.
8. None of the listed artifacts appears.

### out-08

1. The first sentence is situation and complication; the actual answer appears later and is framed as a recommendation.
2. It shows top material → three action branches → supports.
3. Three action branches follow an analytical grouping rather than chronology.
4. Survive: contracts/APIs/database and GPS. Default “auto,” three-to-six months, both delivery-time comparisons, two-or-three people, hundred tools, ten-plus-ten, and 20°C are absent.
5. Yes, though the control-point citation points to 00:04 rather than the relevant 00:06 passage.
6. GPS correction and agent-review feedback are mostly together in the workflow branch; unit-test evidence is omitted.
7. The output invents that the reader’s organization deployed agents expecting 10×, turns the speaker’s views into unqualified “must” statements, and specifies a backend/NLP pairing not proposed in the source.
8. None of the listed artifacts appears.

## 3. Output notes

- **out-01:** The hierarchy is visible, but its first level consists of overlapping subject buckets, and concrete evidence is frequently abstracted or left unlocated.
- **out-02:** It has a strong four-conclusion pyramid, weakened by scattered feedback evidence, missing locators, and unsupported strengthening.
- **out-03:** It preserves the most examples but becomes a ten-part chronological reference document rather than a proportionate chat digest.
- **out-04:** It is concise, attributed, and located, but too much of the talk’s discriminating evidence disappears beneath broad claims.
- **out-05:** It offers the strongest unlocated digest: four well-developed arguments, careful attribution, and useful process-review questions.
- **out-06:** It best combines a qualified top, four distinct conclusions, concrete supports, and traceable timestamps.
- **out-07:** Its three action branches are easy to scan, but they substitute direct recommendations for an attributed account of the outsider’s claims.
- **out-08:** Its evidence is visibly nested and timestamped, but the delayed answer and invented “we deployed” framing distort the requested reporting stance.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Load-bearing evidence has no locator | Mode 4 — digest: source reference on every load-bearing claim | ignored | 4 — out-01, out-02, out-03, out-05 |
| Long-talk supports lose the figures and examples needed to judge the claim | Core loop §4 and Mode 4 — digest: three levels with concrete supports | ignored | 5 — out-01, out-02, out-04, out-07, out-08 |
| First-level branches are topics or actions rather than the requested conclusions | Core loop §4 — derive the element kind from the reader’s question | ignored | 3 — out-01, out-07, out-08 |
| Feedback evidence is split across branches | Core loop §6 — MECE duplication test | ignored | 4 — out-02, out-03, out-04, out-05 |
| Speaker anecdotes are de-attributed or strengthened into general facts | Mode 4 — digest: report on read sources | vague | 4 — out-01, out-02, out-07, out-08 |
| The complete answer does not appear in the first sentence | Mode 4 — digest: answer in the first sentence | ignored | 2 — out-03, out-08 |

## 5. Observation

The stronger outputs reduce the talk to three or four distinct conclusions, keep concrete examples beneath the conclusion they support, preserve the speaker’s epistemic status, and make the evidence traceable. The weaker outputs either fragment the transcript into chronological mini-sections, replace conclusions with topical or prescriptive headings, or compress away the figures that would let the reader test the speaker’s claims.

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
      "output": "out-02",
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
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 2,
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
        "answer_first": false,
        "first_level_count": 10,
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
        "answer_first": true,
        "first_level_count": 3,
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
      "output": "out-08",
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
        "first_level_kind_matches": false,
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