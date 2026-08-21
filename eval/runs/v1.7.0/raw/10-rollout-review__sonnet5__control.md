# FIELDBOOK ROLLOUT REVIEW — RECOMMENDATION FOR Q1 DECISION

## Recommendation

**Extend Fieldbook to North and Islands in Q1 — but only after fixing the two root causes that made South and West lag, so the new regions replicate Central/East's fast payback rather than South/West's break-even drag.**

This rests on three points:

1. **The value case is proven, not hypothetical.** Where adoption was fast (Central, East), Fieldbook paid back its running cost within one quarter through scheduling density and travel-time gains. Where adoption was slow (South, West), the same platform delivered only break-even results — the technology works; adoption speed is what varies.
2. **Adoption speed is fixable, not regional.** The single cause of every slow-adoption symptom — one-off classroom training with no path for late hires or absentees — is a program design choice, not a property of South, West, North, or Islands.
3. **Two known integration gaps are inflating cost and risk, and both already have vendor-ready fixes awaiting a Kestrel decision, not vendor work.** Left unresolved, they will repeat in North and Islands exactly as they did in all four live regions.

**Decision requirement before Q1 go-live:** replace the one-time classroom model with a rolling/repeatable onboarding track, and assign an owner to schedule the two pending vendor fixes (asset-register feed, invoicing code mapping). Without these two changes, extension carries meaningful risk of reproducing the South/West cost profile in two more regions.

---

## 1. The rollout works when onboarding is complete — Central/East vs. South/West is a training gap, not a technology gap

- Central and East reached full adoption in six weeks and paid back program cost within the second quarter.
- South and West lagged (11 weeks to 80%, and still 71% at nine weeks, respectively) for one shared reason: the two-day classroom course ran once per region, so anyone hired late or absent learned second-hand. In West, 34 of 118 technicians never attended a session at all.
- The cost of this gap is concrete: ~380 technician-hours lost to improvised shadowing, and 44% of all 1,940 support tickets are password/login issues concentrated among technicians who never attended training.
- Dispatchers, by contrast, adopted instantly everywhere — because the old scheduling spreadsheet was switched off on day one, leaving no fallback. This confirms the mechanism: adoption speed tracks whether an alternative path exists, not technician willingness or regional readiness.

**Implication:** fix the training model — a rolling onboarding track for late hires — and North/Islands should track Central/East, not South/West.

## 2. Operational gains are real, but two unresolved integration gaps are taxing them

- Where the platform is fully used, it delivers: completed jobs per technician per day rose from 4.6 to 5.3, travel time fell 18%, and emergency insertion dropped from a phone-chase to a 4-minute automatic process. Overtime spend fell 12% and fuel cost per job fell 9% in the live regions.
- Two specific, unrelated gaps are eating into this benefit:
  - **Missing asset-register feed:** technicians can't see equipment history, causing 9% of audited jobs to replace already-warrantied parts, and making the equipment-history panel useless for warranty and dispute purposes. Requested from the asset-register team in month two; still in their backlog.
  - **Job-completion code mismatch with invoicing:** forces manual re-keying of ~300 records/week, causes customer-facing billing errors, drove hiring of a temporary clerk (£8,400/two quarters), and produces a 2–4% weekly discrepancy between Fieldbook and invoicing job counts that finance reconciles by hand.
- Both have vendor-supplied solutions (a configurable mapping table for codes, a supported connector for the asset register) sitting idle because no one at Kestrel owns the integration — not because the vendor is slow. The vendor relationship itself is performing within contract.

**Implication:** these are Kestrel decision gaps, not technical unknowns, and should be closed before — not after — extension, since each new region reproduces the same cost until they are.

## 3. A smaller, related gap compounds support load and data quality: exact-postcode search

- The customer search screen matches on exact postcode only, so technicians who can't find an existing record create a duplicate — 19% of all support tickets, merged manually at ~70/week.
- This also splits job-history views for affected customers until merged, a data-quality issue distinct from (and additive to) the asset-register and invoicing gaps.
- This is a low-effort fix (relax the search match) relative to its ticket and data-quality cost, and should be bundled with the other two fixes rather than treated as routine ongoing support load.

## 4. Financial case for extension

- Extension adds £13,500/month in licence cost for North and Islands, plus winter travel costs for classroom training under the current model.
- The economics are favourable **only if** adoption speed matches Central/East; a repeat of the West pattern would put North and Islands underwater for at least two quarters — consistent with points 1–3 above, since the West pattern has an identified, fixable cause.

## 5. Why this didn't get fixed already, and why it will this time

- Every issue in this review was visible by week four of the Central go-live. The program had no mechanism to feed early field observations into program-level fixes, so each issue simply replayed in the next region.
- That gap is itself the thing to close for Q1: a standing feedback loop from support/regional reports into program-level fixes, not just a one-time patch before North/Islands go live — otherwise a new, unforeseen issue in North or Islands will again go unaddressed until it has repeated twice more.
