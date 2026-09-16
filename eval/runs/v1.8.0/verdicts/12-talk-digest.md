## 1. Score table

Structural sub-scores are `(top, key-line composition, levels, order and kind)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 5 (2, 1, 1, 1) | 6 | `invented_facts` |
| out-02 | 6 (2, 1, 2, 1) | 8 | `invented_facts` |
| out-03 | 5 (2, 1, 1, 1) | 6 | — |
| out-04 | 5 (2, 1, 1, 1) | 8 | `more_than_four_first_level` |
| out-05 | 8 (2, 2, 2, 2) | 10 | — |
| out-06 | 2 (2, 0, 0, 0) | 4 | `invented_facts`, `more_than_four_first_level` |

## 2. Decisive questions

### out-01

1. The top is one falsifiable claim: classical handoffs and agents’ probabilistic character, rather than coding speed, block the promised acceleration.
2. It shows three levels: top → four proposed changes → supporting claims and examples.
3. Four first-level conclusions follow a thematic/action grouping, not chronology.
4. The exact examples that survive are two-to-three-person teams and human control of APIs/contracts/databases. Handoffs and feature-plus-hypothesis sprints survive only abstractly; default “auto,” three-to-six months, the timed handoff comparison, month-versus-days, 100 tools, ten-plus-ten, and 20 degrees/GPS do not.
5. Yes; the load-bearing supports carry minute markers.
6. The surviving feedback material is gathered under the fourth branch, but the CI/CD and unit-test examples are omitted.
7. Attribution is uneven: anecdotes become fairly categorical prescriptions. “Malicious MCP servers” is invented; the source describes a compromised shopping agent interacting with a retailer’s MCP server.
8. No marker legend, mermaid, findings table, ordering commentary, chronological retelling, or file.

### out-02

1. The top is one contestable claim about classical processes preventing organizations from realizing agent value.
2. It clearly shows top → three conclusions → claim/evidence supports.
3. Three thematic conclusions follow the answer rather than chronology.
4. It retains two hours versus thirty minutes plus waiting, two-to-three-person teams, APIs/databases, and the GPS analogy. It loses default “auto,” three-to-six months, month-versus-days, 100 tools, ten features plus ten hypotheses, and the 20-degree example.
5. No; none of the supports has a locator.
6. CI/CD feedback and GPS are gathered under the third conclusion; unit tests are missing.
7. Several statements are presented as general facts rather than the speaker’s experience. Calling ML System Design Docs “essential,” implying one person rarely possesses both capabilities, and referring to “risky MCP servers” strengthen or add claims beyond the source.
8. None of the listed apparatus or mode problems appears.

### out-03

1. The top is one falsifiable claim: process and role redesign are prerequisites for 10× acceleration.
2. It shows three levels, but some supports sit under the wrong or overlapping conclusion.
3. Four thematic conclusions appear; their order is workable but not clearly principled.
4. It retains default “auto,” three-to-six months, APIs/databases, and GPS. It omits the timed handoff comparison, month-versus-days, two-to-three people, 100 tools, ten-plus-ten, and 20 degrees.
5. Yes; every support has a minute marker, although several ranges are imprecise.
6. Feedback is spread: the GPS/runtime material is in branch 1, while CI/CD review is in branch 2.
7. The framing identifies these as the speaker’s arguments, though bullet wording is categorical. No number, name, company, citation, or other fact is invented.
8. No marker legend, mermaid, findings table, ordering commentary, chronological retelling, or file.

### out-04

1. The top is a falsifiable claim, completed by the second sentence: the operating model, not automatic code generation, limits speed.
2. It shows top → conclusions → prose supports, though the business-function point is promoted into a separate conclusion.
3. Five first-level conclusions follow a thematic order; this exceeds the permitted four. The later review questions are implications, not counted as the key line.
4. It retains default use without naming “auto,” three-to-six months, month-versus-days, APIs/databases, and about 100 tools. It omits the timed handoff comparison, the exact two-to-three-person figure, ten-plus-ten, and 20 degrees/GPS.
5. No; the supports have no minute markers.
6. Feedback and testing are gathered in branch 2, but the CI/CD and GPS/floor examples are omitted.
7. Estimates and anecdotes are consistently attributed to the speaker. No asserted source fact is invented; “spend limits” and “observability” are added review prompts rather than presented evidence.
8. No marker legend, mermaid, findings table, ordering commentary, chronological retelling, or file.

### out-05

1. The top is one clear, falsifiable claim about why tool adoption alone cannot produce the promised gain.
2. It consistently shows top → four conclusions → concrete, located supports.
3. Four action-oriented conclusions follow the answer in a coherent operating-model sequence rather than chronology.
4. It retains default “auto,” three-to-six months, month-versus-days, two-to-three people, APIs/databases, and about 100 tools. It omits the exact two-hour/half-hour comparison, ten features plus ten hypotheses, and 20 degrees/GPS.
5. Yes; every load-bearing support has a minute range or marker.
6. CI/CD review and runtime/test feedback are gathered in branch 1; only the GPS/floor analogy is omitted.
7. Figures, cases, forecasts, and uncertainty are consistently attributed to the speaker. Nothing is invented.
8. None of the listed apparatus or mode problems appears.

### out-06

1. The top is one falsifiable claim about human organization being the decisive blocker.
2. It technically has top → numbered conclusions → details, but it promotes evidence into 12 separate first-level branches and then adds another takeaway list.
3. There are 12 principal first-level conclusions, ordered mainly by the talk’s chronology rather than by the answer.
4. It retains auto mode, three-to-six months, month-versus-days, two-to-three people, APIs/databases, 100 tools, and GPS. It mentions feature/experiment/hypothesis sprints and the temperature analogy without preserving ten-plus-ten or 20 degrees; it replaces the two-hour/half-hour evidence with an invented “2–3× faster” figure.
5. No; the digest supplies no minute locators.
6. Feedback is split between separate control-point and correction-mechanism branches.
7. Multiple anecdotes become facts. Invented or unsupported strengthenings include a year of Cursor “auto” use followed by no 10× gain, agents breaking the named control points, a 2–3× speed increase, retraining datasets, and categorical claims that no single backend or AI engineer can cover both sides.
8. It is a chronological retelling with extensive report apparatus; there is no marker legend, mermaid, findings table, ordering commentary, or file.

## 3. Output notes

- **out-01:** It has a strong answer and located evidence, but overlapping research, team, and management branches obscure the hierarchy and the tool-adoption claim largely disappears.
- **out-02:** Its compact claim/evidence hierarchy is effective, but missing locators and unsupported categorical strengthening reduce trust in an otherwise clean digest.
- **out-03:** The visible three-level structure is useful, but feedback, dual-role work, and new-actor implications are split or duplicated across branches.
- **out-04:** Attribution and source skepticism are strong, but the business-function material should sit under engineering-plus-research rather than becoming a fifth conclusion.
- **out-05:** This is the strongest synthesis: four distinct process claims, concrete evidence, locators, explicit uncertainty, and no factual overreach.
- **out-06:** The clear top is followed by a slide-by-slide inventory whose 12 branches flatten the intended pyramid and introduce several unsupported specifics.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Concrete figures and examples are abstracted or dropped | Core loop §4, “Supports keep the source’s concreteness” | ignored | out-01, out-02, out-03, out-04 |
| Load-bearing supports lack locators | Mode 4, “a source reference on every load-bearing claim” | ignored | out-02, out-04, out-06 |
| Feedback evidence is split or incompletely consolidated | Core loop §6, “MECE” | ignored | out-03, out-06 |
| First-level boundaries overlap or promote subordinate material | Core loop §4, “Depth follows the material” | vague | out-01, out-03, out-04, out-06 |
| The digest exceeds four first-level groups | Core loop §4, “3–4 first-level groups” | ignored | out-04, out-06 |
| Tentative anecdotes are strengthened or unsupported facts are added | Core loop §4, “Keep the owner of every number” | ignored | out-01, out-02, out-06 |

## 5. Observation

The stronger outputs convert the talk into three or four distinct claims, place concrete anecdotes beneath the claim they support, preserve the speaker’s uncertainty, and attach locators. The weaker outputs either fracture the talk into chronological slide points, duplicate themes such as feedback and research across branches, omit source-specific evidence, or turn anecdotes into general facts.

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
        "mece": 0,
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
        "total": 2,
        "top": 2,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
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
    }
  ]
}
```