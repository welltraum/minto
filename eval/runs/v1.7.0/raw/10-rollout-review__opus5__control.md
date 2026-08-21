# Fieldbook Rollout Review — Recommendation for the Quarterly Meeting

## Recommendation

**Extend Fieldbook to North and Islands in Q1, but gate the go-live on three fixes Kestrel already controls: continuous onboarding, the asset-register feed, and the invoicing code mapping.** The platform's core benefit is proven and repeatable — scheduling density is up 15% and overtime down 12% in the live regions. Every material problem in two quarters traces to work Kestrel never assigned an owner, not to the product or the vendor. Extending without closing those three items would reproduce the West pattern and leave the new regions underwater for at least two quarters; closing them first makes the £13,500/month extension favourable.

---

## 1. The platform works, and the gains are attributable

Fieldbook delivers the operational effect it was bought for, in every region that adopted it properly.

- **Scheduling density rose.** Completed jobs per technician per day went from 4.6 to 5.3 across the four live regions; travel time between jobs fell 18%.
- **Emergency response is now automatic.** Same-day insertion, previously a round of phone calls, has a 4-minute median.
- **The financial trace is consistent.** Overtime is down 12% quarter over quarter and fuel cost per job down 9% — the second figure matching the travel-time reduction independently.
- **Payback is demonstrated where adoption was fast.** Central and East cleared their running cost within the second quarter. South and West sit at break-even, and the difference between the two groups is adoption speed, not the product.

## 2. All the drag comes from three unowned items, not from the product

Adoption gaps, support load, data-quality defects and unplanned cost are four symptoms of the same three root causes. Each has a known fix, and each fix sits on Kestrel's side of the line.

**a. Onboarding was a one-time event, so late joiners were never trained.**
The two-day classroom course ran once per region. In West, 34 of 118 technicians never attended any session; West is still at 71% of orders in the system after nine weeks, against six weeks to full adoption in Central and East. This single cause produces:
- 44% of all 1,940 support tickets (password resets and logins, concentrated among technicians who missed the course and never logged in during the supported window);
- 380 technician-hours of lost route time from improvised shadowing in South and West;
- the weekly webinar's attendance pattern, which tracks the regions that missed classroom slots.

*Fix:* replace the one-off course with continuous onboarding tied to hiring — no new region should go live on a single-event model.

**b. No feed from the legacy asset register, so technicians work blind on equipment history.**
The equipment-history panel is empty on every job screen. Technicians compensate by calling the back office or asking the customer, and **in 9% of audited jobs they replaced parts already replaced under warranty within the past year** — the single largest cash leak in the review. The same gap makes the audit trail useless for dispute resolution. A nightly export was requested in month two and remains in the asset register team's backlog; the vendor's catalogue lists a supported connector, unevaluated.

**c. Completion codes don't map to the invoicing system, so records are re-keyed by hand.**
The billing team re-keys ~300 job records per week, adding one temporary clerk (£8,400 over two quarters), generating transcription errors that customers find on invoices, and leaving the reporting module and invoicing system 2–4% apart on completed-job counts every week — reconciled manually at month end. The vendor has confirmed a configurable mapping table that takes **roughly one day** to set up. It has not been scheduled because no one at Kestrel owns the integration.

**What is not a problem:** the parts-ordering screen is unpopular but tests correctly — habit, not defect. Dispatcher uptake was immediate and total (41 of 41). The vendor is performing inside contract, and both known system gaps are waiting on Kestrel decisions, not vendor work.

**One item still needs a vendor answer:** customer-record search matches on exact postcode only, so technicians create duplicates when they can't find a record — 19% of tickets and ~70 manual merges per week, splitting job history across records. Unlike (b) and (c), no confirmed fix exists yet. This should be raised with the vendor now, but it is not a reason to hold the extension.

## 3. The economics of extension turn entirely on adoption pace

- Extension adds **£13,500/month** in licences plus winter travel for any classroom training in North and Islands.
- At the Central/East adoption curve, the extension pays back on the demonstrated pattern.
- At the West curve, the new regions stay underwater for at least two quarters.
- The three fixes above are what separates those two curves, and they cost a day of vendor configuration, a scheduled export from the asset register team, and a change to how training is delivered — trivial against £13,500/month.
- Note that winter travel makes the classroom model even weaker for these two regions; the continuous-onboarding change is not optional here, it is the only workable model.

## 4. The structural lesson to fix before the next go-live

**Every negative pattern in this review was visible by week four of the Central go-live, and the program had no mechanism to turn early field observations into program-level fixes — so each issue replayed in each subsequent region.** Extending to two more regions without that feedback loop risks a third and fourth replay.

## What we ask of you

1. **Approve extension to North and Islands in Q1**, conditional on items 2–4 completing before each go-live date.
2. **Assign an integration owner** — the single missing role. Their first two tasks: schedule the vendor's mapping table (one day) and land the nightly asset-register export.
3. **Approve the move to continuous onboarding**, replacing the one-off classroom course in all six regions.
4. **Mandate a weekly field-observation review** for the first six weeks of each new go-live, with authority to make program-level changes.
5. **Open a vendor request** on postcode-only customer search.
