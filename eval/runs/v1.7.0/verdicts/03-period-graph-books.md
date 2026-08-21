## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 4 (1, 1, 1, 1) | 5 | None |
| out-02 | 7 (2, 1, 2, 2) | 9 | None |
| out-03 | 5 (2, 1, 1, 1) | 5 | None |
| out-04 | 6 (2, 1, 1, 2) | 8 | None |
| out-05 | 5 (2, 1, 1, 1) | 5 | None |
| out-06 | 5 (2, 1, 1, 1) | 6 | None |
| out-07 | 7 (2, 1, 2, 2) | 9 | None |
| out-08 | 7 (2, 1, 2, 2) | 8 | None |
| out-09 | 5 (2, 1, 1, 1) | 5 | `invented_facts` |
| out-10 | 6 (2, 1, 2, 1) | 6 | `invented_facts` |
| out-11 | 1 (1, 0, 0, 0) | 3 | `unacknowledged_source_loss` |
| out-12 | 4 (1, 1, 1, 1) | 6 | None |
| out-13 | 7 (2, 1, 2, 2) | 9 | None |
| out-14 | 5 (2, 1, 1, 1) | 6 | `invented_facts` |
| out-15 | 4 (1, 1, 1, 1) | 6 | None |
| out-16 | 5 (2, 1, 1, 1) | 6 | `invented_facts` |

## 2. Decisive questions

| output | 1. Required changes absent? | 2. Missing vs buried distinguished? | 3. Streamlining undeveloped? | 4. Incomplete logic / failure points? | 5. Suggested key line uses actions? | 6. False positives or inventions | 7. Diagnosis-only with apparatus? |
|---|---|---|---|---|---|---|---|
| out-01 | Partial | No | Partial | Partial | No; it asks for supporting reasons | Demands a timeline and implementation review without source support | Diagnosis-only, but no markers, findings table, score, or top-three fixes |
| out-02 | Yes | Yes | Yes | Yes | Partial; it permits reasons or changes | Overstates the need to define ownership, scope, and resourcing | Yes |
| out-03 | Yes | Yes | Yes | Partial | No; proposed branches are topics and constraints | Adds evidence, impact, alternatives, timing, and management-risk requirements | Diagnosis-only, but exceeds seven findings and omits markers, score, and top-three fixes |
| out-04 | Yes | Yes | Yes | Partial | Yes | Treats resources as the “actual ask” and demands counts, cost, owner, and date | Yes |
| out-05 | Yes | Yes | Yes | Partial | No; change, ownership, and requirements are mixed | Adds impact quantification, headcount implications, timing, and proof demands | Diagnosis-only, but lacks the prescribed audit apparatus and exceeds seven findings |
| out-06 | Yes | Yes | Yes | Partial | No; suggested first-level claims mix diagnosis and action | Introduces an outside or dedicated team as the likely solution | Diagnosis-only, but lacks markers, findings table, score, and top-three fixes |
| out-07 | Yes | Yes | Yes | Partial | Yes | Adds options, owner, date, and redesign-approval requirements | Yes |
| out-08 | Yes | Yes | Yes | Yes | No; its final proposed grouping is causes | Adds representativeness, workload evidence, and outside-help requirements | Yes |
| out-09 | Yes | Partial | Yes | Partial | No; reasons, consequences, and actions are mixed | Invents delayed reporting and resource-allocation relevance; formatting complaints are also weak | Diagnosis-only, but lacks markers, score, and top-three fixes and exceeds seven findings |
| out-10 | Yes | Yes | Yes | Partial | No; it proposes parallel reasons beneath the answer | Invents timeliness as an operating requirement and adds immediate safeguards | Diagnosis-only, but lacks the required apparatus |
| out-11 | Yes | No | Partial | No | No; root causes, impact, and actions are mixed | Mislabels the closing question as a buried conclusion | Apparatus is present, but the “annotated memo” silently omits the opening paragraph |
| out-12 | Yes | Yes | Yes | No | No; root causes and symptoms remain the key line | Adds impact ordering; otherwise limited | Diagnosis-only with most apparatus, but the marker legend is absent |
| out-13 | Yes | Yes | Yes | No | Yes | Single ownership is less directly grounded than the automation and entry-point changes | Yes |
| out-14 | Yes | Partial | Yes | Partial | No concrete action key line is supplied | Invents “lost prior-period data”; the source says it must be re-entered | Diagnosis-only, but lacks markers, findings table, score, and top-three fixes |
| out-15 | Yes | Partial | Yes | No | No; it explicitly proposes reasons beneath the recommendation | Adds resource allocation and central control beyond the stated evidence | Yes |
| out-16 | Yes | Yes | Yes | Partial | No; root cause, impact, and solution are mixed | Invents a Q3 pilot and an unsupported implementation protocol | Diagnosis-only, but lacks the required apparatus |

## 3. Output notes

- **out-01:** It identifies the delayed assessment but treats it too much like a buried solution, without isolating the missing corrective actions.
- **out-02:** The strongest separation is its explicit distinction between an absent actionable answer and the buried diagnosis, plus its careful stage-completeness annotation.
- **out-03:** Its opening diagnosis is sound, but eleven findings dilute the central defects and introduce numerous content wishes.
- **out-04:** It correctly derives an action-kind answer, though unsupported measurement, ownership, and resourcing demands weaken the audit.
- **out-05:** It makes the missing-versus-buried distinction especially clearly, but sprawling content requirements obscure the stage-specific structural problem.
- **out-06:** It identifies the absent resolution and buried diagnosis, but substitutes an unsupported outside-team solution and omits the audit apparatus.
- **out-07:** It is disciplined, source-located, and complete in form, but never isolates the graph-generation and later-change failure points.
- **out-08:** It is unusually attentive to incomplete process mapping, but its replacement grouping falls back to causes rather than actions.
- **out-09:** It has a clear top-level diagnosis, but its long checklist mixes structural findings with formatting and invented business-impact claims.
- **out-10:** It concisely links process evidence to conclusions, though it adds an unsupported timeliness requirement and lacks formal audit apparatus.
- **out-11:** It loses source material and mistakes the closing request for a conclusion, undermining both annotation fidelity and hierarchy.
- **out-12:** It captures the missing top and buried streamlining conclusion, but offers only a lightly annotated audit without a legend or stage-specific diagnosis.
- **out-13:** Its hierarchy and action-kind replacement are strong, but it misses the distinct graph-point-generation and presenter-change control failures.
- **out-14:** It is concise and correctly sees the inverted structure, but “lost prior-period data” changes the source’s meaning.
- **out-15:** Its presentation is complete, yet it promotes a compound assessment as the top and proposes reasons rather than an action key line.
- **out-16:** It delivers a coherent summary audit, but its mixed root-cause/impact/solution grouping and invented Q3 pilot weaken it.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Missing corrective actions were blurred with the buried diagnosis | Mode 2 — Audit, check 1: Top | ignored | out-01, out-09, out-11, out-14, out-15 |
| Failure points were not separated across process completion, graph-point generation, and later changes | Mode 2 — Audit, check 4: MECE and process completeness | missing | out-01, out-03, out-04, out-05, out-06, out-07, out-09, out-10, out-11, out-12, out-13, out-14, out-15, out-16 |
| Suggested first-level structure used causes, reasons, or mixed categories instead of actions | Core loop §4 — Groups and required kind | ignored | out-01, out-02, out-03, out-05, out-06, out-08, out-09, out-10, out-11, out-12, out-14, out-15, out-16 |
| Audit apparatus was absent or incomplete | Mode 2 — Audit, required delivery order | ignored | out-01, out-03, out-05, out-06, out-09, out-10, out-11, out-12, out-14, out-16 |
| Audits demanded unsupported evidence, decisions, or implementation details | Mode 2 — “finding is a structural defect, not a wish for more content” | ignored | out-03, out-04, out-05, out-08, out-09, out-10, out-14, out-16 |

## 5. Observation

The stronger outputs separate two different diagnoses: the memo contains a buried conclusion that streamlining is needed, but it never supplies the corrective actions management requested. They also keep current-process evidence below structural findings and provide the prescribed annotation, limited findings, score, and prioritized fixes. The weaker outputs either promote “streamlining” as though it were already the answer, organize proposed key lines around causes or reasons instead of actions, or add unsupported evidence and implementation demands.

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
        "top": 1,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 5,
        "top": 1,
        "same_kind_grouping": 1,
        "explainable_order": 1,
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
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 1,
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
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
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
        "total": 5,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
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
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-04",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 1,
        "levels": 1,
        "order_and_kind": 2
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
        "order_type_named": false,
        "scq_intro_present": "na"
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
        "total": 5,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 0,
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
        "order_type_named": true,
        "scq_intro_present": "na"
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
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
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
        "total": 9,
        "top": 2,
        "same_kind_grouping": 2,
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
        "order_type_named": true,
        "scq_intro_present": "na"
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
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-09",
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
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-10",
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
        "order_type_named": false,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-11",
      "completed": true,
      "structure": {
        "total": 1,
        "top": 1,
        "key_line_composition": 0,
        "levels": 0,
        "order_and_kind": 0
      },
      "quality": {
        "total": 3,
        "top": 1,
        "same_kind_grouping": 0,
        "explainable_order": 0,
        "mece": 0,
        "visible_structure": 2
      },
      "hard_failures": [
        "unacknowledged_source_loss"
      ],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": false,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-12",
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
        "order_type_named": false,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-13",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 1,
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
      "hard_failures": [],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-14",
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
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": false,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-15",
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
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    },
    {
      "output": "out-16",
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
      "hard_failures": [
        "invented_facts"
      ],
      "checks": {
        "answer_first": "na",
        "first_level_count": "na",
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": "na",
        "order_type_named": true,
        "scq_intro_present": "na"
      }
    }
  ]
}
```