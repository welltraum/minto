## Audit — "Period Graph Books"

**Reader:** senior management, who asked for corrective proposals.
**Reader question:** *What should we change so the graph books stop coming out wrong?*
**Kind of answer required:** actions/changes — not a description of the process, not reasons the process is bad.

**Legend:** `▲` top/answer · `●` first-level group · `○` support · `⚠` violation · `↑` buried conclusion · `⇄` wrong order type · `⊗` overlap · `⊕` gap · `✂` cut or move to appendix

---

```text
Subject: Period Graph Books          ⚠ topic label, not an answer

Since Period 5, Financial Analysis has been responsible for producing four
graph-presentation books previously handled by Corporate Planning.   ← Situation, sound
This memo describes issues that appeared after the transfer.   ✂ statement of purpose;
                                        ⊕ no Complication, no Question, no Answer

Production                             ⚠ first-level group is a description of the
                                          current state, not an action or a reason
1. Gather data from divisional forms, internal documents, and telephone calls.
2. Calculate graph points manually or on the corporate computer, including
   rolling values for revenue, cost, and percentages.
3. Transcribe the points to input sheets. Analysts update the current period,
   then Color Graphics re-enters the points into its own database and generates
   the graphs.
4. Check the data and calculations.
   ○ ✂ correct time order internally, but the whole block belongs in an appendix:
     it answers "how does this work?", a question management did not ask

Issues                                 ⚠ mixed kinds inside one group: causes
                                          ("another person inserted", "fragmented"),
                                          symptoms ("inconsistent data",
                                          "incorrect variable-cost calculations")
                                          and one book's walkthrough
The transfer inserted another person into an already fragmented process.
Divisional staff and three corporate departments participate, and the same
information may be entered into computer systems three times.     ⊗ same content
                                        as "cumbersome fragmented process" below

For one book, divisional data are loaded into a dedicated corporate program,
calculated, transferred to Color Graphics input sheets, entered again, and
returned for updates.                  ⊗ repeats the Production block at a lower level
Problems include inconsistent data between periods and regions, incorrect
variable-cost calculations, unexplained changes to points that were previously
correct, and prior-period data that must be re-entered.
   ⚠ no ordering principle — recall order; ⊕ no scale (how often, how costly)

Overall assessment                     ⚠ heading not on the key line's level

Most problems arise from a cumbersome fragmented process.        ↑ this is the
                                        diagnosis; it belongs above everything
No one controls the data from beginning to end, responsibility is unclear, and
errors can fall between stages.                                  ↑ the real cause,
                                        buried three levels down
The production process badly needs streamlining, both for each book and for
common calculations.                   ↑ closest thing to an answer, in the last
                                        paragraph, and only as a direction
The current team cannot manage the required changes as well as ongoing
production.                            ⊕ implies a resourcing ask that is never made

Could we discuss how best to proceed?  ⚠ management asked for proposals and is
                                        handed the question back
```

---

### Findings

| Location | Violation | Fix |
|---|---|---|
| Whole memo | **No answer anywhere in the document.** Management asked for corrective proposals; the memo delivers a process description plus a diagnosis and closes by asking for a discussion. This is not "the answer sits at the end" — no proposal is stated at any level. | Decide the actions and put them on top: single ownership of data end-to-end, one entry point per data item, streamlined common calculations, plus the resource needed to do it while producing. |
| Subject line + first paragraph | Top is a topic label ("describes issues"). Nothing the memo asserts appears until the last paragraph. | Subject = the recommendation in one line; open with the answer. |
| First-level structure: *Production / Issues / Overall assessment* | Mixed kinds across levels: a description, a symptom list, and a conclusion presented as peers. None of the three is an action or a reader payoff. | First level = 3–4 proposed changes, each written as an instruction; symptoms become evidence under them. |
| "Overall assessment" para | Buried logic — the diagnosis (no end-to-end control, unclear responsibility, errors fall between stages) is the intermediate conclusion the whole memo exists to support, sitting last. | Promote to the key line directly under the top. |
| "Production" block | Answers "how does this work?", a question not asked; it also duplicates the one-book walkthrough under *Issues*. | Move to an appendix; delete the duplicate walkthrough. |
| *Issues* list | Symptoms in recall order, with no ordering principle and no scale. | Order by damage to the presentations (ranking), and attach frequency/impact — `⊕ [data needed: error counts per book per period]`. |
| Last line | The ask is a request to discuss, so the reader cannot act on reading. | State what you need: approval of the redesign, a named owner, and the interim resource. |

No findings omitted.

### Score

| Axis | Score | Note |
|---|---|---|
| Top | 0 | no answer present in the document |
| Same-kind groups | 0 | description / symptoms / conclusion as peers |
| Order | 1 | time order correct inside *Production*; symptom list unordered |
| MECE | 1 | two clear overlaps; process cause and its symptoms conflated |
| Display | 1 | headings exist but do not mirror any hierarchy |

**Total: 3 / 10 — not structured yet.**

### The three fixes that buy the most

1. Replace the subject line and opening with the recommended changes themselves — management asked for proposals, so the answer is a set of actions, not a description.
2. Promote "no one controls the data end-to-end, responsibility is unclear" from the last paragraph to the key line, and hang the symptoms under it as evidence.
3. Cut the *Production* walkthrough to an appendix and turn the closing question into a specific ask: owner, mandate, and interim resource.

Want me to run `write` and rebuild it answer-first?
