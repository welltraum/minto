## Audit — "Period Graph Books"

**Reader:** senior management, who asked for corrective proposals.
**Reader's question:** *What should we do to stop the errors in the graph books?* — the answer must be a set of **changes**, not a description of the process and its faults.

### Legend

`▲` top/answer · `●` first-level group · `○` support · `⚠` violation · `↑` buried conclusion, promote · `⇄` wrong order type · `⊗` overlap · `⊕` gap · `✂` cut or move to appendix

### Annotated text

```text
⚠ Subject: Period Graph Books   — topic label, not an answer

⚠ Since Period 5, Financial Analysis has been responsible for producing four
  graph-presentation books previously handled by Corporate Planning. [○ acceptable
  Situation]  This memo describes issues that appeared after the transfer.
  ⚠ statement of purpose — names the topic, answers nothing; no Complication and
  no Question ever reach the page

● Production   ⚠ wrong kind: this is the current state, not the changes the reader asked for
  ○ 1. Gather data from divisional forms, internal documents, and telephone calls.
  ○ 2. Calculate graph points manually or on the corporate computer, including
       rolling values for revenue, cost, and percentages.
  ○ 3. Transcribe the points to input sheets. Analysts update the current period,
       then Color Graphics re-enters the points into its own database and
       generates the graphs.   ⊗ re-entry appears again under "Issues"
  ○ 4. Check the data and calculations.
  ⊕ process description incomplete: no stage for management review/sign-off, none
    for printing and distribution, none for carrying prior-period data forward
  ✂ belongs in an appendix as evidence, not on the first level

● Issues
  ⚠ mixed kinds: causes ("another person inserted", "fragmented", "three
    departments", "entered three times") sit alongside symptoms ("inconsistent
    data", "incorrect variable-cost calculations", "unexplained changes",
    "re-entry of prior-period data")
  ⇄ the one-book walkthrough is told in time order inside a section whose point is
    ranking of causes
  ⊕ no evidence of consequence: no count of errors, no cost, no instance of a
    faulty book reaching senior management

● Overall assessment
  ↑ "No one controls the data from beginning to end, responsibility is unclear,
    and errors can fall between stages." — this is the document's real diagnosis,
    sitting on the last page
  ↑ "The production process badly needs streamlining, both for each book and for
    common calculations." — the first proposed change, demoted to a remark
  ↑ "The current team cannot manage the required changes as well as ongoing
    production." — the second proposed change (and the actual ask: resources),
    hidden in a subordinate clause
  ⊕ neither change has an owner, a scope, a cost or a date

⚠ Could we discuss how best to proceed?  — the memo closes by asking the reader to
  supply the answer the reader commissioned
```

### Findings

| Location | Violation | Fix |
|---|---|---|
| Subject line + opening paragraph | **No answer anywhere in the document.** Nothing states what should be done; the closing line hands the question back to the reader. | Put the recommended changes in one sentence at the top: single end-to-end owner for the data, plus a streamlined single-entry production process. |
| First level as a whole | **Right kind, wrong kind.** Production / Issues / Assessment answers "what is the process and what is wrong with it"; the reader asked "what do we change". | Rebuild the first level from changes: 3–4 groups, each an instruction with a payoff. |
| "Overall assessment" | **Buried logic.** The diagnosis and both proposals are the lowest-placed material in the memo. | Promote the diagnosis into the top and the two proposals into first-level branches. |
| "Issues" section | **Mixed kinds** — causes and symptoms in one group; the reader cannot tell what to act on. | Split: symptoms become the evidence that a problem exists; causes become the ground for each change. |
| "Production" 1–4 | **Wrong level.** A state description occupies a first-level slot and proves nothing about what to change. | Move to an appendix; keep only the steps a proposed change removes. |
| "Production" step 3 vs. one-book walkthrough | **Overlap.** Triple re-entry is described twice as if two separate points. | State it once, under the change that eliminates it. |
| Whole document | **Gap: no consequence and no ask.** No error rate, no cost, no impact on senior-management presentations; no decision requested, no owner, no date. | Add the impact under the diagnosis, and close with the specific decision needed (⊕ `[data needed: error counts, rework hours, incident where a faulty book was presented]`). |

### Score — 3 / 10 · *not structured yet*

| Axis | Score | Note |
|---|---|---|
| Top | 0 | No answer; subject is a label, close is a question |
| Same-kind groups | 1 | Sections are internally near-uniform but of the wrong kind; "Issues" mixes causes and symptoms |
| Order | 1 | Time order inside "Production" is defensible; the three sections have no ordering principle, and causes are unranked |
| MECE | 1 | Re-entry duplicated; process description incomplete; no evidence of consequence |
| Display | 0 | Headings name topics, so a glance at the page reveals nothing about the argument |

### The three fixes that buy the most

1. Write the answer as the first line: one end-to-end data owner plus a single-entry production process — the changes, not the faults.
2. Promote the last paragraph. The diagnosis becomes the top; "streamline the process" and "the team cannot do both" become two first-level branches, the second one carrying the resource ask.
3. Demote "Production" to an appendix and split "Issues" so that symptoms prove the problem and causes support each change.

Say the word and I'll run `write` to produce the restructured memo.
