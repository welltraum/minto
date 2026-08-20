# Fieldbook Extension to North and Islands — Recommendation for Q1

**Situation.** Fieldbook has been live for two quarters in Central, East, South, and West. You're deciding at the quarterly meeting whether to extend it to North and Islands in Q1.

**Complication.** The four live regions split sharply in outcome: Central and East reached full adoption within six weeks and paid back Fieldbook's running cost by the second quarter; South and West took two to three times as long to adopt and are only at break-even. That gap traces to three specific, already-diagnosed problems — not to any weakness in the platform itself — and each one has a known fix that nobody has yet been assigned to execute.

**Answer.** Extend Fieldbook to North and Islands in Q1 — but only once the three carried-over gaps are fixed and an onboarding backfill is built in. Done that way, the new regions should reproduce Central and East's fast payback; done as South and West were, they will sit underwater for at least two quarters.

## 1. Where onboarding was complete, Fieldbook paid for itself fast
- Central and East hit full adoption in six weeks and recovered the platform's running cost within one quarter.
- Scheduling gains are real and region-wide: completed jobs per technician per day rose from 4.6 to 5.3, travel time between jobs fell 18%, and emergency-job insertion dropped from a phone chain to a 4-minute median — gains North and Islands would get on day one regardless of adoption speed.
- Overtime is down 12% and fuel cost per job down 9% quarter over quarter across all four live regions, including the slow ones.

## 2. Where adoption lagged, three fixable causes account for nearly all of the extra cost — this is not a platform risk
- **One-time classroom training with no backfill.** A single scheduled session per region left latecomers and absentees (34 of 118 technicians in West alone) learning the platform second-hand. This alone drove South and West's slow adoption, 44% of all support tickets (password/login issues from technicians who never logged in during the supported window), the weekly training webinar the support desk now runs as an unplanned substitute, and 380 technician-hours lost to improvised shadowing.
- **No feed from the legacy asset register.** Technicians work every job blind to equipment history, which cost 9% of audited jobs a needlessly replaced in-warranty part, and leaves the equipment-history panel too empty to support a warranty or dispute claim.
- **Mismatched completion codes plus postcode-only search.** These two integration gaps together force roughly 300 job records a week to be re-keyed by hand into invoicing, cost one temporary clerk (£8,400), produce a 2–4% weekly discrepancy between Fieldbook and invoicing that finance reconciles manually, and add ~70 duplicate customer records a week for support to merge.

## 3. Each cause already has a low-cost fix — the only missing input is ownership
- The asset-register export and the invoicing code-mapping table are both listed as supported connectors in the vendor's integration catalogue; the code-mapping table takes the vendor roughly a day once someone requests it.
- Neither has been scoped or assigned on Kestrel's side — the rollout program was staffed for deployment and training only, and no one owns the integration work.
- The vendor relationship itself is not the constraint: response times are within contract, and both fixes are waiting on Kestrel decisions, not vendor delivery.

## Conditions to set before extending
1. Add a backfill training track (make-up sessions or paid shadowing time) so North and Islands don't repeat West's 29% never-trained rate.
2. Assign an owner to request the asset-register export and the invoicing code-mapping table before go-live, not after month two as happened this time.
3. Budget the £13,500/month extension cost against Central/East's payback pace, not South/West's — the difference is the fixes above, not the regions.

---
What changed structurally: the source's six report-by-department sections (adoption, operations, support, finance, data, program remarks) are replaced by one COO-facing pyramid answering the extension question directly. The three causes that were scattered across four sections as separate symptoms — training gap, asset-register gap, invoicing/search gap — are merged into single branches, each carrying its full set of downstream costs (tickets, hours, dollars) in one place instead of being re-counted per department.
