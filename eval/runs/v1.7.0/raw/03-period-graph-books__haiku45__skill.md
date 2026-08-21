# Audit: Period Graph Books

## Markers legend

| Marker | Meaning |
|---|---|
| `▲` | top / answer |
| `●` | first-level group |
| `○` | supporting detail |
| `⚠` | violation (mixed kinds, unexplainable order, false grouping) |
| `↑` | conclusion buried lower than it belongs — promote it |
| `⇄` | wrong order type here |
| `⊗` | overlap (ME broken) |
| `⊕` | gap (CE broken) |
| `✂` | cut, or move to an appendix |

---

## Annotated text

`▲` [no answer] Subject: Period Graph Books

Since Period 5, Financial Analysis has been responsible for producing four graph-presentation books previously handled by Corporate Planning. `⚠` [topic label, not situation] This memo describes issues that appeared after the transfer.

`●` `⚠` [wrong kind—describes current state, not what to change] Production

1. Gather data from divisional forms, internal documents, and telephone calls.
2. Calculate graph points manually or on the corporate computer, including rolling values for revenue, cost, and percentages.
3. Transcribe the points to input sheets. Analysts update the current period, then Color Graphics re-enters the points into its own database and generates the graphs.
4. Check the data and calculations.

`●` Issues

The transfer inserted another person into an already fragmented process. Divisional staff and three corporate departments participate, and the same information may be entered into computer systems three times.

For one book, divisional data are loaded into a dedicated corporate program, calculated, transferred to Color Graphics input sheets, entered again, and returned for updates. Problems include `⊕` [ungrouped—four symptoms of one root cause?] inconsistent data between periods and regions, incorrect variable-cost calculations, unexplained changes to points that were previously correct, and prior-period data that must be re-entered.

`↑` [conclusion buried; should be the top] Overall assessment

Most problems arise from a cumbersome fragmented process. No one controls the data from beginning to end, responsibility is unclear, and errors can fall between stages. The production process badly needs streamlining, both for each book and for common calculations. The current team cannot manage the required changes as well as ongoing production.

`⚠` [defers answer instead of stating it] Could we discuss how best to proceed?

---

## Findings

| Location | Violation | Fix |
|---|---|---|
| Opening through closing | Rule 1: no top. Topic label at start; conclusion buried at end; question deferred to reader. Reader asks "what should we do?" and receives diagnosis with no answer. | Move "The production process badly needs streamlining" to the opening as the answer. Recast as a recommendation, not a question. |
| "Production" section | Rule 3: wrong kind. Lists current-state steps (what is done now), not actions/changes (what should be done). Observations masquerade as a first-level group. | Delete or move to appendix. Recast as the changes needed: consolidate data entry points, assign single ownership, automate calculations across book types. |
| "Issues" section, problems listed | Rule 5: not MECE. Four symptoms (inconsistent data, incorrect calculations, unexplained changes, re-entry) are grouped implicitly under "fragmented process" but never stated as such. Relationship to root cause is invisible. | Group the four problems under types of damage the fragmented process produces. Name the grouping: data integrity failures, calculation errors, wasteful re-entry. Make it explicit. |
| "Issues" to "Overall assessment" | Rule 4: no explicable order. Moves from specific problems to general assessment without naming the principle. Current induction (facts roll up to diagnosis) works but is unstated. | Name the order type: induction. Helps reader see why these facts lead to that conclusion. |
| Opening and intro structure | Rule 6: SCQ not in story form. Situation is there (context of transfer) but Complication is buried in Issues. Question never reaches the page (only "Could we discuss..."). Answer never appears as the opening. | Rewrite intro as Situation → Complication → Question → Answer in running prose. Situation: transfer moved production. Complication: four new errors/inconsistencies emerged. Question: what should we change? Answer: streamline and consolidate. |

---

## Score

| Axis | Score | Reasoning |
|---|---|---|
| Top | 0 | No answer. Opening is topic label; conclusion is buried and deferred. |
| Same-kind groups | 1 | Production describes current state; Issues lists symptoms. Neither group answers the reader's question about what to change. |
| Order | 0 | No explicit order principle stated. Production is procedural; Issues is inductive but unnamed. |
| MECE | 1 | Four problems listed without grouping; relationship to root cause unclear. Not obviously overlapping, but coverage is ungrouped. |
| Display | 1 | Sections labeled, but hierarchy is weak. Conclusion buried. No skeleton visible. |

**Total: 3/10 · Band: not structured yet** — the document diagnoses but never answers. Requires a top, reorganization around the reader's question (what to change, not how it works), and explicit grouping before it can guide a decision.

---

## Three highest-impact fixes

1. **State the answer first.** Lift the diagnosis from the closing ("needs streamlining") into a one-sentence top at the opening: "We should consolidate data entry, assign a single owner, and automate shared calculations to eliminate the errors introduced by the transfer."

2. **Replace Production with what to change.** Delete the four-step process description or move it to an appendix as historical context. Rebuild the body around the specific changes needed: consolidate entry points, assign single data owner, automate recalculation. These answer the reader's question; the process description does not.

3. **Group Issues around the root cause.** Reorganize the four problems as symptoms of the fragmented process: data inconsistency, calculation errors, and process waste. Make the grouping and logic explicit so the reader sees why these three changes matter.
