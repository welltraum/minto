▲ `⚠` `●` `○` `⚠` `↑` `⇄` `⊗` `⊕` `✂`

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

```text
⚠ Subject: Period Graph Books

Since Period 5, Financial Analysis has been responsible for producing four
graph-presentation books previously handled by Corporate Planning. This memo
describes issues that appeared after the transfer. ✂

● ⚠ Production
1. Gather data from divisional forms, internal documents, and telephone calls.
2. Calculate graph points manually or on the corporate computer, including
   rolling values for revenue, cost, and percentages.
3. Transcribe the points to input sheets. Analysts update the current period,
   then Color Graphics re-enters the points into its own database and generates
   the graphs.
4. Check the data and calculations.

● ⚠ Issues
The transfer inserted another person into an already fragmented process.
Divisional staff and three corporate departments participate, and the same
information may be entered into computer systems three times.

For one book, divisional data are loaded into a dedicated corporate program,
calculated, transferred to Color Graphics input sheets, entered again, and
returned for updates. Problems include inconsistent data between periods and
regions, incorrect variable-cost calculations, unexplained changes to points
that were previously correct, and prior-period data that must be re-entered.

↑ ⚠ Overall assessment
Most problems arise from a cumbersome fragmented process. ⊕ No one controls the
data from beginning to end, responsibility is unclear, and errors can fall
between stages. The production process badly needs streamlining, both for each
book and for common calculations. The current team cannot manage the required
changes as well as ongoing production.

⚠ Could we discuss how best to proceed?
```

### Findings

| Location | Violation | Fix |
|---|---|---|
| First paragraph / Subject | Top does not answer; topic label | Promote "Overall assessment" to top; state recommendation to streamline process. |
| "Overall assessment" | Buried logic; Vertical gap | Move conclusion to top; move "No one controls" to supports under a group. |
| "Production" | Wrong group kind; Context disguised as argument | Demote to intro context or supports under "Fragmentation causes errors"; remove as top-level group. |
| "Issues" | Mixed kinds; Evidence without grouping | Group elements as reasons for errors or symptoms; ensure same-kind classification. |
| Intro | Meta-commentary | Remove "This memo describes..."; draft SCQ story dosed to reader's knowledge. |
| Closing | Vague ask | Request specific decision on streamlining proposal rather than open discussion. |

### Score

| Axis | Score |
|---|---|
| Top | 0 |
| Same-kind groups | 0 |
| Order | 0 |
| MECE | 0 |
| Display | 1 |
| **Total** | **1** |

**Band:** `0–3` not structured yet

### Three fixes that buy the most

1. Move the recommendation to the top: "We recommend streamlining the graph book process to eliminate errors and clarify data control."
2. Rebuild groups to support the top: e.g., 1. Fragmentation causes recurring errors and inconsistencies. 2. Current team lacks capacity to redesign the process while maintaining output.
3. Replace the intro with an SCQ story dosed to the reader's knowledge of the transfer and the resulting errors.
