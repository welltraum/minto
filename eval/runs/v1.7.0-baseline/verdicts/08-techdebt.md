## 1. Score table

Structural subscores are `(top/key line/levels/order)`. Quality subscores are `(top/grouping/order/MECE/display)`.

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|
| out-01 | 6 (2/1/2/1) | 7 (2/1/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-02 | 4 (2/0/1/1) | 6 (2/0/1/1/2) | `invented_facts`, `unacknowledged_source_loss`, `more_than_four_first_level` |
| out-03 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | — |
| out-04 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | `invented_facts` |
| out-05 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | — |
| out-06 | 6 (2/2/1/1) | 8 (2/2/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-07 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | `invented_facts` |
| out-08 | 7 (2/2/1/2) | 8 (2/2/2/1/1) | `invented_facts`, `unacknowledged_source_loss` |
| out-09 | 6 (2/2/1/1) | 8 (2/2/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-10 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | `invented_facts` |
| out-11 | 6 (2/2/1/1) | 8 (2/2/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |
| out-12 | 7 (2/2/1/2) | 9 (2/2/2/1/2) | `invented_facts` |
| out-13 | 8 (2/2/2/2) | 10 (2/2/2/2/2) | `invented_facts` |
| out-14 | 8 (2/2/2/2) | 9 (2/2/2/2/1) | — |
| out-15 | 8 (2/2/2/2) | 9 (2/2/2/2/1) | `invented_facts` |
| out-16 | 5 (2/1/1/1) | 7 (2/1/1/1/2) | `invented_facts`, `unacknowledged_source_loss` |

## 2. Decisive questions

| output | Recommendation | First-level kind | Count | All nine correctly placed? | Backlog as SCQ complication? | Format | Invented material | Reader question literal? |
|---|---|---|---:|---|---|---|---|---|
| out-01 | First | actions/data | 3 | No; CX/Research evidence disappears and the interview shifts toward trust | No | Colleague message | Interview said to demonstrate loss of trust | No |
| out-02 | First | mixed | 5 | No; CX/Research evidence is lost and reasons are mixed with new actions | No | Compact but memo-like | “Exploding,” consistent trend, year-long surge, key-customer interview, formal grievance, recent measurable decline | No |
| out-03 | First | business losses | 3 | Yes | No | Colleague message | None | No |
| out-04 | First | business losses | 3 | Yes | No | Colleague message | Accelerating technical debt; interviews confirming instability and degraded experience; promised stabilization | No |
| out-05 | First, via subject | business losses | 3 | Yes | No | Colleague message | None | No |
| out-06 | First, via subject | business losses | 3 | No; churn chart, user posts, and major-account complaint are absent | No | Colleague message | Direct customer loss, blocked deal closure, plural interviews that “confirm” the claim | No |
| out-07 | First | business losses | 3 | Yes | No | Colleague message | Rough doubling, later sprints necessarily costing more, formal complaint, Friday deadline | Yes |
| out-08 | First, via subject | business losses | 3 | No; the interview is omitted and evidence precedes rather than supports the numbered reasons | Yes, but the labels make it heavier rather than stronger | Over-structured colleague note | Defects as a “key driver” and “directly linked” to churn | No |
| out-09 | First, via subject | business losses | 3 | No; CX, interview, and churn-chart evidence are collapsed or lost | No | Colleague message | Significant/accelerating growth, plural major clients and complaints, threatened retention | No |
| out-10 | First, via subject | business losses | 3 | Yes | Yes; this is a stronger two-loss key line | Colleague message | Rough doubling, customers explicitly citing bugs as why they left, prospect objections, prior “engineering hygiene” framing | No |
| out-11 | First, via subject | business losses | 3 | No; CX evidence is not retained distinctly and the account complaint is misplaced under immediate revenue loss | No | Compact formal note | Immediate revenue loss, formal complaint, widespread dissatisfaction, future-acquisition threat, unmanageable backlog and added complexity | Yes |
| out-12 | First | business losses | 3 | No; the charts are generically said to support every point rather than placed under their actual reasons | No | Colleague message | Unmanageable backlog, plural interviews directly correlating attrition, account escalation, defects as the core issue | No |
| out-13 | First, via subject | business losses | 3 | Yes | No | Colleague message with diagram | Plural interviews and an unsupported trust claim | No |
| out-14 | First | business losses | 3 | Yes | No | Colleague message | None | No |
| out-15 | First | business losses | 3 | Yes | No | Colleague message overextended by diagram and process note | Stable long-running trend, interview proving mechanism, complaint being public | No |
| out-16 | First | business losses | 3 | No; CX and interview evidence disappear | No | Colleague message | Strong correlation, formal complaint, direct pipeline threat and promised stabilization | No |

## 3. Output notes

- **out-01:** The recommendation is immediate, but evidence-category labels replace a clean line of business reasons and the interview changes meaning.
- **out-02:** The otherwise visible hierarchy is broken by placing invented implementation steps alongside the reasons.
- **out-03:** It cleanly preserves the three gold reasons and keeps every evidence unit under its natural parent.
- **out-04:** Its pyramid is structurally complete, but several qualitative claims are converted into unsupported certainties.
- **out-05:** The subject supplies the top while the compact numbered body preserves all evidence without unnecessary apparatus.
- **out-06:** The key line is sound, but aggressive compression drops most of the brand evidence and the churn chart.
- **out-07:** The hierarchy is excellent, but invented magnitude, economics, formality, and timing undermine factual fidelity.
- **out-08:** Backlog growth is usefully framed as the complication, but labeled SCQ apparatus, repetition, and missing interview evidence weaken the note.
- **out-09:** The three outcome headings are workable, though important churn evidence is collapsed and several claims are overstated.
- **out-10:** Treating backlog growth as the complication produces the strongest business-loss key line, but the supporting facts are embellished.
- **out-11:** The literal SCQ is unusually explicit, but evidence is misplaced across overlapping revenue and brand branches.
- **out-12:** The note is concise and readable, but its generic attachment sentence obscures which chart supports which reason.
- **out-13:** The prose and diagram expose a clean pyramid, with only small but material factual embellishments.
- **out-14:** It is the cleanest plain-prose version, preserving the evidence and hierarchy without adding unsupported detail.
- **out-15:** The business-cost grouping is strong and explicitly ordered, but the diagram and structural commentary make the delivered artifact disproportionate.
- **out-16:** It has a clear recommendation, but combining churn with brand while separating revenue creates overlap and hides missing evidence.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|
| Unsupported certainty, quantities, evidence, or causal mechanisms | Mode 3 — “Invent nothing” | ignored | out-01, out-02, out-04, out-06–out-13, out-15, out-16 |
| Source evidence omitted or collapsed beyond identifiable preservation | Mode 3 — “Keep every fact from the source” | ignored | out-01, out-02, out-06, out-08, out-09, out-11, out-16 |
| Governing reader question not written as a literal question | Core loop §1 and §3 | ignored | out-01–out-06, out-08–out-10, out-12–out-16 |
| Ordering principle left implicit | Core loop §5 — Order | missing | out-01–out-14, out-16 |
| Evidence categories or actions substituted for a same-kind line of reasons | Core loop §4 — Groups | ignored | out-01, out-02 |
| Compact colleague note burdened with excess structural apparatus | SCQ dose and visible-structure guidance | ignored | out-08, out-15 |

## 5. Observation

The stronger outputs put the sprint recommendation in the subject or opening sentence, follow it with three parallel business reasons, and keep each chart, report, interview, and complaint under the reason it supports. Weaker outputs either promote evidence categories or new actions into the key line, collapse distinct evidence during compression, overlap churn with brand or revenue, or preserve the visible pyramid while inventing stronger facts than the source permits.

## 6. Machine-readable scores

```json
{
  "schema_version": 1,
  "fixture": "08-techdebt",
  "mode": "write",
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
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-02",
      "completed": true,
      "structure": {
        "total": 4,
        "top": 2,
        "key_line_composition": 0,
        "levels": 1,
        "order_and_kind": 1
      },
      "quality": {
        "total": 6,
        "top": 2,
        "same_kind_grouping": 0,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss", "more_than_four_first_level"],
      "checks": {
        "answer_first": true,
        "first_level_count": 5,
        "first_level_kind_matches": false,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-03",
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
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-04",
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
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
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-06",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
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
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-07",
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-08",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
        "order_and_kind": 2
      },
      "quality": {
        "total": 8,
        "top": 2,
        "same_kind_grouping": 2,
        "explainable_order": 2,
        "mece": 1,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-09",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
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
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-10",
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-11",
      "completed": true,
      "structure": {
        "total": 6,
        "top": 2,
        "key_line_composition": 2,
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
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": true,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-12",
      "completed": true,
      "structure": {
        "total": 7,
        "top": 2,
        "key_line_composition": 2,
        "levels": 1,
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-13",
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
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": true
      }
    },
    {
      "output": "out-14",
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
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": [],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": false,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    },
    {
      "output": "out-15",
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
        "mece": 2,
        "visible_structure": 1
      },
      "hard_failures": ["invented_facts"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": false,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": true,
        "scq_intro_present": true
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
        "total": 7,
        "top": 2,
        "same_kind_grouping": 1,
        "explainable_order": 1,
        "mece": 1,
        "visible_structure": 2
      },
      "hard_failures": ["invented_facts", "unacknowledged_source_loss"],
      "checks": {
        "answer_first": true,
        "first_level_count": 3,
        "first_level_kind_matches": true,
        "invented_facts": true,
        "unacknowledged_source_loss": true,
        "mode_respected": true,
        "readers_question_literal": false,
        "order_type_named": false,
        "scq_intro_present": false
      }
    }
  ]
}
```