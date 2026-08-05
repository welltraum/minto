## 1. Score table

Structural axes are `(top/key line/levels/order and kind)`; quality axes are `(top/grouping/order/MECE/display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (2/0/1/1) | 7 (1/1/2/1/2) | — |
| out-02 | 5 (2/1/1/1) | 6 (2/1/1/1/1) | — |
| out-03 | 3 (1/0/1/1) | 4 (1/1/0/1/1) | — |
| out-04 | 4 (1/1/1/1) | 6 (1/1/1/1/2) | — |
| out-05 | 2 (1/0/0/1) | 4 (1/0/1/1/1) | `invented_facts` |
| out-06 | 5 (2/1/1/1) | 8 (2/1/2/1/2) | — |
| out-07 | 4 (1/1/1/1) | 6 (1/1/1/1/2) | — |
| out-08 | 5 (1/1/1/2) | 7 (1/1/2/1/2) | — |

## 2. Decisive questions

1. Required changes absent.
2. Missing answer distinguished from buried conclusion.
3. Streamlining identified as an undeveloped conclusion.
4. Incomplete process logic and unseparated failure points identified.
5. Suggested replacement key line consists of actions.
6. False positives or invented details.
7. Diagnosis-only mode and required audit apparatus.

| output | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 |
|---|---|---|---|---|---|---|---|
| out-01 | Yes | Yes | Yes | Yes | No; it proposes reasons as the body’s key line | Treats the general and book-specific re-entry passages as duplication and asks for additional controls/decision details not established by the source; no invented facts | Yes |
| out-02 | Yes | Yes | Yes | Yes | Yes, although the action set is overbroad and misses presenter revalidation | Improperly requires coverage, frequency, materiality and impact evidence for all four books; no invented facts | Diagnosis only, but missing annotations, capped findings table, score and top-three fixes |
| out-03 | Yes | No | No | Partly; it notices mixed causes and effects but not incomplete stage logic | No | Calls the process steps dispensable background and recommends deleting the assessment rather than retaining them as properly subordinated evidence; no inventions | Diagnosis only, but required apparatus is absent |
| out-04 | Yes | Partly; it recognizes both conditions but calls the buried conclusion the governing answer | Yes | Partly; it subordinates the process evidence but does not isolate graph-generation and later-change failures | No | Misstates the reader’s question as “why are there errors,” proposes overlapping ownership categories and assumes a separately staffed redesign; no invented facts | Diagnosis only, but required apparatus is absent |
| out-05 | Yes | No | No | Partly; responsibility is discussed, but the actual stage failures are not isolated | No; its proposed body mixes process, pain points, impacts and recommendation | Invents a task force, 30-day deadlines, a 15 May date, a 3% rework rate and four analyst-hours; parallelism and filler findings are also weak false positives | Diagnosis rather than a full rewrite, but it exceeds seven findings and omits annotations, scoring and three prioritized fixes |
| out-06 | Yes | Yes | Yes | Yes, though it substitutes an all-four-books coverage demand for the precise missing stage separation | No; its replacement direction is generic and its body mixes causes, symptoms and changes | Treats the illustrative re-entry passage as duplication and demands full coverage, an owner and a timeline beyond the supported audit; no invented facts | Yes |
| out-07 | Yes | No; it incorrectly labels the final paragraph itself a recommendation | Partly; it locates streamlining but overstates its development | Partly; it notes mixed evidence and ownership logic without isolating the missing stages | No; it leaves the choice between reasons and actions unresolved | Claims unclear responsibility lacks support even though the source supplies multi-party and no-owner evidence; no invented facts | Yes |
| out-08 | Yes | No | No; streamlining appears only in the suggested fix | No; it notes grouping and order but not incomplete process logic or distinct failure stages | No; it recommends a reasons group beneath a generic action | Incorrectly describes the source groups as mixing actions with reasons and recommends labeled SCQ-style headings; no invented facts | Yes |

## 3. Output notes

- **out-01:** Strong apparatus and a precise missing-versus-buried diagnosis are offset by a replacement body made of reasons rather than the required corrective actions.
- **out-02:** Its opening judgment and concrete action list are useful, but nine overlapping sections introduce unsupported evidence demands and omit the mandated audit format.
- **out-03:** It identifies the missing proposal and bottom-up presentation, but loses the buried streamlining conclusion and wrongly treats necessary process evidence as removable noise.
- **out-04:** It is concise and visibly organized, but elevates the buried diagnosis into an answer and never separates the three required corrective stages.
- **out-05:** Its large table is readable but structurally diffuse, and its fabricated metrics, dates and implementation details are the fixture’s only hard factual failure.
- **out-06:** This is the strongest diagnosis and apparatus, especially on absent versus buried logic, although its proposed remedy remains generic and some completeness findings overreach the evidence.
- **out-07:** It follows the required audit format, but mistakes an undeveloped direction for a recommendation and leaves the replacement key-line kind unresolved.
- **out-08:** It has strong display and explicit order terminology, but misses the decisive buried-conclusion and incomplete-process diagnoses.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Missing corrective answer not cleanly separated from the buried conclusion | Mode 2 — Audit, Top and Buried logic | ignored | out-03, out-04, out-05, out-07, out-08 |
| Incomplete process logic and distinct generation/change failure points not identified | Mode 2 — Audit, Vertical and MECE | missing | out-03, out-04, out-05, out-07, out-08 |
| Replacement structure uses reasons, topics or mixed categories instead of corrective actions | Core loop, Groups | ignored | out-01, out-03, out-04, out-05, out-06, out-07, out-08 |
| Inline evidence, capped findings, five-axis score or top-three fixes omitted | Mode 2 — Audit, Deliver | ignored | out-02, out-03, out-04, out-05 |
| Ordering principle not named as time, structure, ranking, deduction or induction | Core loop, Order | missing | out-02, out-03, out-04 |
| Unsupported metrics, dates and implementation specifics introduced | Core loop, grounding and invention check | ignored | out-05 |

## 5. Observation

Stronger outputs explicitly separate “no corrective answer exists” from “streamlining is a buried but undeveloped conclusion,” attach findings to visible source evidence, and supply the complete audit apparatus. Weaker outputs either promote the buried diagnosis as if it were the answer, replace action branches with reasons or document-editing advice, or invent additional evidence requirements instead of isolating the three process-stage changes.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "03-period-graph-books",
  "mode": "audit",
  "outputs": [
    {
      "output": "out-01",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 0,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
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
        "total": 6,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": false
      }
    },
    {
      "output": "out-03",
      "completed": true,
      "structure": {
        "total": 3,
        "top": 1,
        "key_line_composition": 0,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 4,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 0,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": false
      }
    },
    {
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
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
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": false
      }
    },
    {
      "output": "out-05",
      "completed": true,
      "structure": {
        "total": 2,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 1
      },
      "quality": {
        "total": 4,
        "top": 1,
        "same_kind_grouping": 0,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    },
    {
      "output": "out-06",
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
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    },
    {
      "output": "out-07",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 1,
        "key_line_composition": 1,
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
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": false,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 5,
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 7,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true
      }
    }
  ]
}
```