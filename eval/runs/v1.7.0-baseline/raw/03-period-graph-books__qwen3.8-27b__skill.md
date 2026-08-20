**Legend:**  
▲ top / answer  
● first-level group  
○ supporting detail  
⚠ violation (mixed kinds, unexplainable order, false grouping)  
↑ conclusion buried lower than it belongs — promote it  
⇄ wrong order type here  
⊗ overlap (ME broken)  
⊕ gap (CE broken)  
✂ cut, or move to an appendix  

```text
Subject: Period Graph Books ⚠ [topic label, not the answer]

Since Period 5, Financial Analysis has been responsible for producing four graph-presentation books previously handled by Corporate Planning. ○ [situation] This memo describes issues that appeared after the transfer. ✂ [purpose statement; does not close the reader’s question]

Production ● [current-state group, not a corrective action]
1. Gather data from divisional forms, internal documents, and telephone calls. ○
2. Calculate graph points manually or on the corporate computer, including rolling values for revenue, cost, and percentages. ○
3. Transcribe the points to input sheets. Analysts update the current period, then Color Graphics re-enters the points into its own database and generates the graphs. ○
4. Check the data and calculations. ○

Issues ● ⚠ [mixed kinds: cause, burden, mechanics, symptoms]
The transfer inserted another person into an already fragmented process. ↑ [key cause buried]
Divisional staff and three corporate departments participate, and the same information may be entered into computer systems three times. ○ [burden/mechanics]

For one book, divisional data are loaded into a dedicated corporate program, calculated, transferred to Color Graphics input sheets, entered again, and returned for updates. ○ [process detail] Problems include inconsistent data between periods and regions, incorrect variable-cost calculations, unexplained changes to points that were previously correct, and prior-period data that must be re-entered. ⚠ [symptom list] ⊗ [overlap among items]

Overall assessment ● ↑ [conclusion section sits below details]
Most problems arise from a cumbersome fragmented process. ○
No one controls the data from beginning to end, responsibility is unclear, and errors can fall between stages. ○
The production process badly needs streamlining, both for each book and for common calculations. ▲ [vague answer; should be the top]
The current team cannot manage the required changes as well as ongoing production. ⊕ [implied ownership/resource change left unspecified]

Could we discuss how best to proceed? ⊕ [asks for discussion, not the corrective decision/proposal]
```

### Findings

| Location | Violation | Fix |
|---|---|---|
| First line / whole memo | Top is a topic label; the only answer (“needs streamlining”) is vague and buried | Make the first line a precise controlling idea: the corrective action(s) proposed |
| “Overall assessment” | Key conclusions are buried below details: no single owner, fragmented process, need to streamline | Promote the main conclusion and implied ownership/resource change to the top |
| “Production” section | Wrong kind for a corrective-proposal request: current-state steps instead of actions/changes | Demote process steps to support/appendix; make first-level elements actions |
| “Issues” paragraphs | Mixed kinds: cause, participation burden, process mechanics, and symptoms in one group | Split into same-kind groups or nest under one root cause |
| “Problems include …” | Overlapping problem items: inconsistent data, unexplained changes, and prior-period re-entry claim similar territory | Merge duplicates or reformulate non-overlapping problem classes |
| “This memo describes issues …” | Statement of purpose instead of SCQ answer; the reader’s question is not closed | Delete or replace with an answer-first line / explicit question + answer |
| Final sentence | Gap: asks to discuss rather than specifying the corrective decision/action needed | End with the specific decision or approval sought |

### Score

| Axis | Score |
|---|---:|
| Top | 1 |
| Same-kind groups | 1 |
| Order | 1 |
| MECE | 0 |
| Display | 1 |
| **Total** | **4/10** |

Band: **4–6 — baseline workable**

### Three highest-value fixes

1. Put the corrective recommendation on the first line: what process/ownership changes are proposed.  
2. Recast the first-level sections as actions/changes, moving current production steps to support or appendix.  
3. Promote “no single owner/end-to-end control” and “streamline common calculations” into the top argument, then state the decision needed.  

Next: I can run `write` to restructure this memo.
