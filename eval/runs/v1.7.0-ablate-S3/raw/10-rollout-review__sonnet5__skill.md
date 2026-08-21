# Fieldbook Rollout — Decision for Q1

**Situation.** Fieldbook has been live in Central, East, South, and West for two quarters, and the COO must decide at the quarterly meeting whether to extend it to North and Islands in Q1.

**Complication.** The two quarters split into two different stories. Central and East adopted fast and paid back the rollout's running cost within a quarter. South and West are still below 80% adoption after nine-plus weeks and are only at break-even, because the one-off classroom course left anyone hired or absent afterward to learn the platform informally — 34 of West's 118 technicians never attended a session at all. On top of that, two system gaps have sat unfixed since month two: Fieldbook has no feed from the legacy asset register, and its completion codes don't match the invoicing system's. Both are generating rework, billing errors, and hundreds of manual reconciliation hours a week — and both already have vendor-ready fixes, waiting only on someone at Kestrel to own and schedule them.

**Question.** Should Kestrel extend Fieldbook to North and Islands in Q1?

**Answer.** Yes — extend in Q1, but only after restructuring onboarding to reach every technician and closing the two known integration gaps. On the current evidence, extension pays off only if North and Islands reproduce the Central/East adoption pattern, and neither blocker is a Fieldbook defect: both are unresolved Kestrel decisions, not vendor work, and both are cheap to close before go-live.

## Why

**1. The gains are real, and reproducible when onboarding is done right.**
- In Central and East, completed jobs per technician rose from 4.6 to 5.3/day, travel time between jobs fell 18%, overtime is down 12%, fuel cost per job is down 9% — and the rollout paid back its running cost within the second quarter.
- Those gains track adoption speed, not the software: South and West show the same platform delivering only break-even results, because slower, incomplete onboarding delayed the same scheduling and dispatch benefits.

**2. The costs so far are self-inflicted and already quantified — and they will recur unless fixed before go-live.**
- Missing onboarding for late/absent hires cost South and West an estimated 380 technician-hours in improvised shadowing, and drove most of the 1,940 support tickets logged (44% are password resets/logins from technicians never onboarded).
- The missing asset-register feed hides warranty history from technicians, has already led to replacing already-warrantied parts in 9% of audited jobs, and leaves the audit trail useless for disputes — the request for a nightly export has sat in another team's backlog since month two.
- The invoicing code mismatch requires re-keying roughly 300 job records a week by hand, cost one added clerk (£8,400), and leaves reporting and invoicing disagreeing on completed-job counts by 2–4% weekly, reconciled manually at month end.
- None of these three traces to a Fieldbook defect: the vendor has a mapping table ready for the code mismatch and supported connectors for both the asset register and invoicing formats already in its catalogue — none evaluated, because no integration work was ever scoped into the program and no one owns it.

**3. Closing these gaps before North and Islands go live is cheap next to repeating West twice more.**
- The vendor's code-mismatch fix takes about a day to configure; IT calls both remaining connectors straightforward.
- Every one of these failure patterns was visible by week four of the very first go-live (Central) — nothing here is new information, only unconverted early warning.
- Extending £13,500/month of licence cost into two more regions without fixing onboarding cadence risks repeating West: a region stuck at break-even for at least two quarters, per the program office's own estimate.

**What I need:** a decision to extend Fieldbook to North and Islands in Q1, contingent on (a) an onboarding plan that reaches every technician before winter travel closes the window, and (b) named Kestrel owners for the asset-register and invoicing integrations, scheduled ahead of go-live.

---

### Pyramid

```
Top: Extend Fieldbook to North and Islands in Q1, conditional on fixing
     onboarding cadence and the two known integration gaps first.
  1. The gains are real and reproducible when onboarding is done right
     - Central/East: density, travel-time, overtime, fuel gains; paid back in Q2
     - South/West: same platform, only break-even — onboarding is the variable
  2. Current costs are self-inflicted, quantified, and not Fieldbook defects
     - onboarding gap: 380 lost hours, most of 1,940 support tickets
     - asset-register gap: warranty rework, dead audit trail, unowned backlog item
     - invoicing code mismatch: 300 records/week hand re-keyed, added clerk, 2-4% reconciliation gap
     - all three have vendor-ready fixes waiting on a Kestrel owner
  3. Fixing first is cheap against repeating West twice more
     - vendor fixes: ~1 day (codes), connectors already cataloged and "straightforward" per IT
     - failure patterns were visible since week four of the first go-live
     - unfixed, extension risks two more break-even regions at £13,500/month
```
