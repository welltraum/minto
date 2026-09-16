## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (2/1/0/1) | 5 | `invented_facts`, `more_than_four_first_level` |
| out-02 | 5 (2/1/1/1) | 7 | `invented_facts` |
| out-03 | 6 (2/1/2/1) | 8 | — |
| out-04 | 5 (2/1/1/1) | 6 | `invented_facts` |
| out-05 | 8 (2/2/2/2) | 10 | — |
| out-06 | 7 (2/2/2/1) | 9 | — |

Structural sub-scores are ordered: top / key-line composition / levels / order and kind.

## 2. Decisive questions

### out-01

1. The top is one challengeable claim: the human and process layer, rather than agent capability, blocks the promised acceleration.
2. It nominally has three levels, but material that should form supports or grouped conclusions is promoted into eleven parallel branches.
3. There are eleven first-level conclusions, ordered largely by the talk’s chronology rather than by a reader-oriented synthesis.
4. Surviving examples are default “auto,” three-to-six months, month versus a few days, two or three people, APIs/contracts/database, the 100-tool agent, and GPS/20°C. The two-hour/half-hour comparison and ten-features/ten-hypotheses formulation are lost.
5. No minute markers or other locators are supplied.
6. Feedback is split between the control-point and external-feedback branches; the unit-test support is largely lost.
7. Most estimates remain framed as the speaker’s experience, but the claimed incident in which an agent altered a contract/API and caused failure is invented.
8. It is a chronological retelling with eleven sections; it has no marker legend, mermaid, findings table, group-order commentary, or file.

### out-02

1. The top is one clear, disputable causal claim, though it is long and more categorical than the source.
2. It shows top → four conclusions → supports.
3. Four first-level conclusions follow a thematic rather than strictly chronological arrangement, although the branch boundaries are broad and overlapping.
4. Surviving examples are “auto,” three-to-six months, month versus a couple of days, two or three people, APIs/contracts/database, the 100-tool agent, and GPS/20°C. The precise handoff times and ten-plus-ten sprint example are absent.
5. No locators are supplied.
6. The CI/CD example, GPS/floor analogy, and unit-test requirement are gathered under the first branch.
7. Attribution is weak in places: the output universalizes the speaker’s anecdotes and invents that the marketplace implemented the CI/CD scheme rather than merely presenting it; compromise “via” the retailer’s MCP server is also unsupported.
8. None of the listed apparatus or chronological-retelling defects appears, and no file is written.

### out-03

1. The opening gives a challengeable claim about process friction and agent development, followed immediately by the proposed response.
2. It shows top → three action-oriented conclusions → supports.
3. There are three first-level conclusions, arranged by process, organization, and system design rather than chronology.
4. The month-versus-days contrast, two-or-three-person teams, and APIs/contracts/database survive. The default mode, learning period, exact handoff times, 100 tools, ten-plus-ten sprint, and GPS/20°C examples are omitted.
5. Every load-bearing bullet has a minute marker.
6. The feedback material that remains is gathered in the third branch, but the CI/CD and unit-test supports are omitted.
7. No facts, names, figures, or citations are invented, although “we must” makes the speaker’s claims sound like firmer recommendations to the reader.
8. None of the listed apparatus, chronological retelling, or file-writing defects appears.

### out-04

1. The top is one clear claim: human-side redesign is required for the claimed acceleration.
2. It shows top → four conclusions → claim/support/implication details, but the first two conclusions overlap.
3. There are four first-level conclusions, broadly following the talk’s progression and omitting the handoff/product-engineer conclusion.
4. Three-to-six months and APIs/contracts/database survive. The ten-experiment reference is only partial; the remaining listed figures and examples are absent or abstracted.
5. Most supports have minute ranges, but the three-to-six-month estimate is mislocated because it occurs at 00:02, outside the branch’s stated range.
6. Feedback and control are spread across the first two branches; CI/CD and unit tests are not preserved concretely.
7. The output invents that the reader’s teams are seeing mixed results and strengthens control points into “immutable” ones; “analyst-engineer” and sandboxing are also additions not grounded in the talk.
8. None of the enumerated apparatus appears, but it does add explicit SCQ labels and a formal claim/support/implication framework; no file is written.

### out-05

1. The top is one qualified, challengeable claim about process redesign being necessary for speed gains.
2. It shows top → four actionable conclusions → concrete supports.
3. Four conclusions follow a coherent progression from human control, through team flow and development discipline, to the surrounding system.
4. Surviving material includes default-tool use, three-to-six months, month versus days, two or three people, APIs/contracts/database, and the roughly 100-tool agent. The exact handoff times, ten-plus-ten sprint, and GPS/20°C examples are omitted.
5. Every load-bearing group has a usable minute range.
6. CI/CD feedback, human correction, tests, and runtime signals are gathered under the first conclusion.
7. Estimates and anecdotes are consistently attributed to the speaker or described as observations; no facts, numbers, names, companies, or citations are invented.
8. None of the listed apparatus, chronological retelling, or file-writing defects appears.

### out-06

1. The top is one clear, qualified claim that adding agents to the current SDLC is insufficient.
2. It shows top → four substantive conclusion groups → supports, followed by a practical checklist that restates the conclusions.
3. There are four first-level conclusions; they progress from delivery process to ownership, agent-development discipline, and product/service design.
4. Surviving examples are “auto,” three-to-six months, month versus days, two or three people, APIs/contracts/database, and roughly 100 tools. The exact handoff times, ten-plus-ten formulation, and GPS/20°C analogies are absent.
5. No minute markers or alternative locators are supplied.
6. CI/CD routing, unit/runtime feedback, and human correction are gathered under the first branch, then summarized in the review checklist.
7. The output explicitly distinguishes consultancy anecdotes from proof and introduces no unsupported facts, figures, names, or citations.
8. None of the listed apparatus or chronological-retelling defects appears, and no file is written.

## 3. Output notes

- **out-01:** It preserves many examples, but fragments the talk into a chronological eleven-point outline and adds an unsupported contract/API failure incident.
- **out-02:** It has a strong top and substantial evidence, but broad catch-all branches, absent locators, and unsupported strengthening weaken traceability.
- **out-03:** It is concise, properly layered, and fully located, but loses most of the concrete examples needed to assess the speaker’s claims.
- **out-04:** The answer is prominent, but overlapping control/feedback branches, a missing handoff conclusion, explicit SCQ apparatus, and invented additions reduce reliability.
- **out-05:** It most cleanly combines a qualified top, four distinct conclusions, concrete evidence, locators, and careful attribution.
- **out-06:** It is analytically strong and appropriately skeptical, but lacks locators and slightly blurs the key line by mixing conclusions with a final application checklist.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Load-bearing claims lack source locators | Mode 4 — digest: source reference on every load-bearing claim | ignored | out-01, out-02, out-06 |
| Concrete figures and examples are abstracted away | Mode 4 — digest: preserve anything that could change the reader’s action | missing | out-03, out-04 |
| Feedback evidence is split or duplicated instead of forming one point | Core loop §6 — MECE and duplicate-branch test | ignored | out-01, out-04 |
| First-level branches reflect source progression or topic fragments rather than a compact key line | Core loop §§4–5; Mode 4 — groups keyed to the reader’s question | ignored | out-01, out-04 |
| Source anecdotes are strengthened or supplemented with unsupported claims | Core loop §8 — verify every element rests on source material | ignored | out-01, out-02, out-04 |

## 5. Observation

The stronger outputs turn the talk into four distinct, qualified conclusions, keep concrete anecdotes underneath the right parent, and make each claim traceable. The weaker outputs either reproduce the speaker’s sequence as many small branches, collapse evidence into generic advice, overlap feedback with governance, or add certainty and detail the source does not provide.

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
        "first_level_count": 11,
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
    }
  ]
}
```