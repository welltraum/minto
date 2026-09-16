## 1. Score table

Sub-score order: Structure = top, key-line composition, levels, order/kind. Quality = top, same-kind grouping, explainable order, MECE, visible structure.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 3 (2, 1, 0, 0) | 3 (2, 0, 0, 0, 1) | `invented_facts`, `more_than_four_first_level` |
| out-02 | 6 (2, 1, 2, 1) | 8 (2, 2, 1, 1, 2) | `invented_facts` |
| out-03 | 6 (2, 1, 2, 1) | 8 (2, 2, 1, 1, 2) | `invented_facts` |
| out-04 | 6 (2, 1, 2, 1) | 7 (2, 2, 1, 1, 1) | `more_than_four_first_level` |
| out-05 | 5 (2, 1, 1, 1) | 7 (2, 1, 1, 1, 2) | `invented_facts` |
| out-06 | 6 (2, 1, 2, 1) | 6 (2, 1, 1, 1, 1) | `more_than_four_first_level` |

## 2. Decisive questions

### out-01

1. The top is a falsifiable causal claim, not merely a topic, though it expands into several prescriptions.
2. It visibly has top → claims → details, but evidence and sub-conclusions have been promoted into twelve parallel branches.
3. There are 12 first-level conclusions, following the talk’s chronology rather than a reader-oriented synthesis.
4. Surviving concrete supports: default “auto,” three-to-six months, month versus days, two or three people, contracts/APIs/database, 100 tools, and GPS; the two-hours/half-hour comparison, exact ten-features/ten-hypotheses formulation, and 20°C are lost.
5. No minute markers or equivalent locators are supplied.
6. Feedback is split between the control-point and human-feedback branches rather than gathered once.
7. Estimates are often presented as facts. Inventions include attributing the absent 10× gain to a year of Cursor “auto” use, a 2–3× speed figure, and an unspecified case in which agents allegedly broke the control points.
8. No legend, mermaid, findings table, ordering meta-comment, or file; it is a chronological retelling.

### out-02

1. The top is one prescriptive claim, but it turns the outsider’s claims into “we must” recommendations.
2. It has three levels: top → three actions → timestamped supports.
3. There are 3 first-level actions, grouped thematically rather than chronologically.
4. Surviving examples: month versus days and two or three people. The default mode, learning time, role-speed comparison, control points, 100 tools, exact ten-plus-ten formulation, and temperature/GPS analogy are absent or abstracted.
5. Every support has a timestamp, although several are shifted from the most precise source minute.
6. Only the human-as-external-correction point survives; CI/CD routing and unit tests are omitted.
7. The speaker’s material is partly revoiced as fact about the reader’s teams. Unsupported claims include that those teams’ expected acceleration has not materialized and that classical teams stall “for months.”
8. None of the listed apparatus appears, and the grouping is not a chronological retelling.

### out-03

1. The top is one clear, falsifiable causal claim.
2. It has top → three conclusions → evidence, with the evidence embedded in paragraphs.
3. There are 3 first-level conclusions, ordered thematically rather than by talk chronology.
4. Surviving examples: two hours versus thirty minutes, two or three people, contracts/APIs/databases, and GPS. The default mode, learning period, month-versus-days comparison, 100 tools, ten-plus-ten formulation, and 20°C example are absent.
5. No load-bearing claim has a minute marker or other locator.
6. CI/CD feedback and GPS are gathered under human oversight; unit tests are omitted.
7. Most claims remain attributable to the speaker, but calling the ML System Design Doc “essential” strengthens the speaker’s much narrower claim that it was useful in their work.
8. None of the listed apparatus or chronological retelling appears.

### out-04

1. The top is one falsifiable causal claim, immediately qualified as practitioner evidence rather than universal proof.
2. It has top → five conclusions → concrete supports in each paragraph.
3. There are 5 first-level conclusions, largely following the talk’s progression.
4. Surviving examples: default use, three-to-six months, month versus days, contracts/APIs/databases, and roughly 100 tools. The two-hours/half-hour comparison, two-or-three-person figure, ten-plus-ten formulation, and temperature/GPS analogy are omitted.
5. Each main paragraph has a usable minute range.
6. Review/test feedback is treated in the first branch and repeated as feedback loops in the second; the analogies are omitted.
7. Estimates and anecdotes are consistently presented as the speaker’s claims; no unsupported fact is added.
8. No legend, mermaid, findings table, ordering meta-comment, or file; the five branches largely retell the talk in sequence.

### out-05

1. The top is one clear causal claim.
2. It is mostly top → four conclusions with inline evidence; the support level is compressed rather than distinctly nested.
3. There are 4 first-level reasons, grouped by theme rather than strict chronology.
4. Only default “auto” and three-to-six months survive clearly; the remaining specified figures and examples are absent or reduced to generic statements.
5. Each bullet has a minute-range locator.
6. Only the CI/CD-review example survives; GPS/floor heating and unit tests are omitted.
7. Attribution is generally explicit, but the output invents that “auto” produced poor results and that the large marketplace itself realized the review design was wrong.
8. None of the listed apparatus or chronological retelling appears.

### out-06

1. The opening presents one claim, with its causal explanation in the next sentence.
2. It has top → five conclusions → supporting prose.
3. There are 5 first-level conclusions, following the talk’s broad chronology.
4. Surviving examples: defaults, three-to-six months, month versus days, API contracts/database changes, and about 100 tools. The role-speed comparison, two-or-three-person figure, ten-plus-ten formulation, and temperature/GPS analogy are absent.
5. No minute markers or equivalent locators are supplied.
6. Tests and runtime feedback are gathered under the handoff branch; CI/CD routing and the analogies are omitted.
7. Estimates and unresolved questions are carefully attributed; no unsupported factual assertion is added.
8. No legend, mermaid, findings table, ordering meta-comment, or file; the five supporting branches broadly reproduce the talk’s sequence.

## 3. Output notes

- **out-01:** The strong top is undermined by a twelve-part slide-by-slide inventory, duplicated feedback material, and several unsupported strengthenings.
- **out-02:** It forms a compact three-branch pyramid with locators, but omits the adoption/control evidence and improperly turns an outsider’s account into claims about “our” teams.
- **out-03:** Its three thematic conclusions are coherent and feedback is consolidated, but the absence of locators and several distinctive examples weakens traceability.
- **out-04:** This preserves the strongest attribution, caveats, concrete cases, and locators, but separates research work from experiment management and adds a fifth chronological branch.
- **out-05:** It is concise and properly attributed in form, but its inline support layer is thin and two causal details are stronger than the source allows.
- **out-06:** It gives a thoughtful practitioner-evidence caveat and useful implications, but five sequential branches, no locators, and an additional checklist make the hierarchy less proportionate.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| More than four first-level branches | Core loop §4, “Groups” and “Depth follows the material” | ignored | out-01, out-04, out-06 |
| Distinctive figures and examples replaced by generic summaries | Core loop §4, “Supports keep the source’s concreteness” | missing | out-02, out-03, out-05, out-06 |
| Load-bearing supports lack source locators | Core loop §4 and Mode 4, locator requirement | ignored | out-01, out-03, out-06 |
| Feedback evidence split across branches | Core loop §6, MECE duplication test | ignored | out-01, out-04 |
| Tentative anecdotes strengthened into facts | Core loop §4, source ownership and invention rule | ignored | out-01, out-02, out-03, out-05 |
| Talk chronology governs the key line | Core loop §5 and Mode 4, reader-question grouping | ignored | out-01, out-04, out-06 |

## 5. Observation

The stronger structures move directly from one causal top to three or four distinct conclusions and then to attributable, findable evidence. The weaker structures either reproduce the talk as five to twelve chronological themes or compress away the concrete comparisons and locators needed to judge the speaker’s claims.

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
        "total": 3,
        "top": 2,
        "key_line_composition": 1,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 3,
        "top": 2,
        "same_kind_grouping": 0,
        "explainable_order": 0,
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
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
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
        "mode_respected": false,
        "readers_question_literal": "na",
        "order_type_named": "na",
        "scq_intro_present": true
      }
    }
  ]
}
```