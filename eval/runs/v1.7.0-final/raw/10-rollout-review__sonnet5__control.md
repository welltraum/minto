# FIELDBOOK ROLLOUT — TWO-QUARTER REVIEW

## Governing Thought

Extend Fieldbook to North and Islands in Q1, but only after fixing three root causes — single-session onboarding, the missing asset-register feed, and the unowned code-mismatch integration — that turned Central/East's clean rollout into South/West's costly one. Left unfixed, the same three issues will replay in the new regions and put them underwater for at least two quarters.

---

## 1. The platform works: adoption that got proper onboarding delivered strong, fast returns

- Central and East reached full adoption within six weeks; both paid back Fieldbook's running cost within the second quarter.
- Where adopted, technicians complete more jobs per day (4.6 → 5.3) with 18% less travel time, and emergency job insertion dropped from a phone chase to a 4-minute median.
- Overtime is down 12% and fuel cost per job down 9% quarter over quarter in the four live regions, driven by these scheduling gains.
- Dispatchers adopted instantly (all 41, week one) because the old spreadsheet was switched off — proving that removing the fallback, not just training, drives adoption.

## 2. Where onboarding was thin, adoption stalled and created cascading costs

- South and West lagged (11 and 9+ weeks to reach comparable adoption) because the two-day classroom course ran only once per region; 34 of 118 West technicians never attended any session.
- The gap was patched with improvised shadowing that cost an estimated 380 technician-hours of lost route time, and South/West are only at break-even as a result.
- Downstream, the support desk absorbed the shortfall: 44% of its 1,940 tickets are password/login issues concentrated among technicians who missed the course — effectively the desk running training at ticket prices.
- **Root cause:** onboarding was scheduled once per region with no path for late hires or absentees; nothing else in the data explains the South/West gap.

## 3. Two unresolved system gaps are quietly taxing every live region, independent of adoption speed

- **Missing asset-register feed:** technicians see no equipment history on any job, causing warranty part replacement errors on 9% of audited jobs, and leaving the audit trail useless for dispute resolution. A vendor connector exists and a nightly export was requested in month two; it is still in the asset-register team's backlog.
- **Code-mismatch with invoicing:** Fieldbook's completion codes don't map to the invoicing system, forcing ~300 manual re-keyed records per week, transcription errors customers catch on invoices, a £8,400 temporary clerk hire, and a 2–4% weekly discrepancy that finance reconciles by hand. The vendor's fix (a mapping table) takes about a day to configure but has no Kestrel owner.
- **Search limitation:** exact-postcode-only matching creates duplicate customer records (~70/week merged by hand), splitting job history until merged and generating 19% of all support tickets.
- **Root cause common to all three:** the rollout was scoped and staffed for deployment and training only — no integration work was scoped in, so vendor-side fixes are sitting on Kestrel decisions, not vendor delays.

## 4. These are not new problems — the program lacked a mechanism to fix them once and stop them recurring

- Every negative pattern in this review was visible by week four of the Central go-live.
- With no feedback loop from early regions to later ones, the same onboarding gap and the same two system defects replayed in each subsequent region rather than being fixed once.
- The vendor relationship is not the constraint: response times are within contract, and both known system gaps already have vendor-side solutions waiting on Kestrel to decide and schedule.

## 5. Recommendation

Extend to North and Islands in Q1, conditional on three fixes going in before go-live:
1. Run more than one onboarding session per region, with a defined path for late hires/absentees, to reproduce the Central/East adoption curve rather than the South/West one.
2. Assign an owner to schedule the asset-register export and the invoicing code-mapping table — both are vendor-ready and low-effort; the blocker is ownership, not engineering.
3. Fix the customer search to match on more than exact postcode, to stop duplicate-record creation before it starts.

At £13,500/month plus winter classroom travel, the economics favor extension only if adoption matches Central/East's pace; a repeat of the West pattern would leave North and Islands underwater for at least two quarters.
