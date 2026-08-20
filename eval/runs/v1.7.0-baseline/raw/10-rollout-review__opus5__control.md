# Fieldbook Rollout — Two-Quarter Review

**For:** Chief Operating Officer | **Decision:** whether to extend Fieldbook to North and Islands in Q1

---

## Recommendation

**Extend to North and Islands in Q1, but only after three fixes are completed and signed off — restructured onboarding, named owners for two integrations, and a weekly fix loop.** Fieldbook's operating gains are proven and repeatable; every loss recorded in two quarters traces to one of three causes, all of which sit on Kestrel's side of the table and none of which require vendor work. Fixed first, the extension is economically favourable. Repeated, the West pattern would leave the two new regions underwater for at least two quarters.

The argument runs in three steps:

1. The platform delivers what it was bought for, and pays back where adoption is fast.
2. Everything that went wrong has three causes, not thirty — and all three are inside our control.
3. The extension economics depend entirely on whether those three causes are fixed before go-live, not on the platform.

---

## 1. The platform delivers what it was bought for

**Where Fieldbook is properly adopted, it produces the scheduling and cost gains that justified the purchase.**

- **Scheduling density improved materially.** Completed jobs per technician per day rose from 4.6 to 5.3 across the four live regions, and average travel time between jobs fell 18%. Same-day emergency insertion — previously a dispatcher phoning technicians until one accepted — is now automatic, with a median of 4 minutes.
- **The gains show up in the finances.** Overtime spending in live regions is down 12% quarter over quarter and fuel cost per job is down 9%, consistent with the travel-time reduction, against licence and hosting of £31,000 per month.
- **Adoption is real, not nominal.** 412 of 486 field technicians have activated accounts and 83% of work orders are created and closed in Fieldbook. All 41 dispatchers were live from week one.
- **Where onboarding worked, payback arrived inside two quarters.** Central and East reached full adoption within six weeks and paid back their running cost during Q2. South and West sit at roughly break-even — the difference is onboarding speed, not platform capability.

---

## 2. Every loss traces to three causes, all of them ours

**The rollout's problems are not a long list of platform defects; they are three unmanaged programme decisions whose effects surfaced in operations, support, finance, and reporting alike.**

### 2.1 Onboarding was run as a one-off event, not a process

The two-day classroom course ran once per region, so anyone hired after it or absent during it learned the platform second-hand.

- **Consequence — slow adoption:** South took eleven weeks to pass 80% of orders; West is still at 71% after nine weeks, with 34 of 118 technicians never attending any session.
- **Consequence — lost route time:** improvised shadowing worked but consumed an estimated 380 technician-hours.
- **Consequence — support load:** 44% of all 1,940 tickets are password and login problems, concentrated among technicians who missed the course and never logged in during the supported window. The weekly webinar's attendance correlates with exactly those regions.
- The support desk lead's summary is the fair one: *"We are doing the training program's job at ticket prices."*

### 2.2 Two integrations were never scoped, and therefore never owned

The programme was staffed for deployment and training only. Two connectors were left out — and the vendor's catalogue supports both.

- **Missing asset-register feed.** Technicians open every job with an empty equipment-history panel. They compensate by calling the back office or asking the customer, and in 9% of audited jobs replaced parts already replaced under warranty within the past year. A nightly export was requested in month two and remains in the asset-register team's backlog.
- **Mismatched job-completion codes.** Billing re-keys roughly 300 job records per week by hand, generating transcription errors that customers find on invoices, and requiring one temporary clerk (£8,400 over two quarters). Reporting and invoicing consequently disagree on completed-job counts by 2–4% weekly, reconciled manually at month end. The vendor has confirmed a configurable mapping table exists and takes about a day to set up; it is unscheduled because no one on Kestrel's side owns the integration.
- **A third, related data limitation:** the customer search matches on exact postcode only, so technicians create duplicate records — 19% of tickets, about 70 manual merges per week — splitting job history until merged.

### 2.3 There was no mechanism to turn field observations into fixes

Every negative pattern in this review was visible by week four of the Central go-live. Nothing converted those observations into programme-level action, so each issue replayed unchanged in East, South, and West. This is why two fixable causes produced four quarters' worth of cost across four regions.

*Note on scope:* the unpopular parts-ordering screen is not in this list. It works correctly in testing; technicians ordering parts by phone is habit, and it costs nothing measurable. It should not consume attention in Q1.

---

## 3. The extension economics turn on the fixes, not on the platform

**North and Islands are worth doing at £13,500 per month in additional licences if they reproduce Central and East — and not otherwise.**

- **The upside case is the Central/East case:** adoption within six weeks, payback inside the second quarter.
- **The downside case is the West case:** a repeat leaves both regions underwater for at least two quarters, before counting shadowing losses and re-keying.
- **The variable that separates the two cases is onboarding coverage**, which is a programme design choice we now know how to get right.
- **Two extension-specific constraints:** winter travel makes any classroom-only model in North and Islands worse than it was in West, and the two known integration gaps would be inherited on day one rather than discovered.
- **The vendor is not a constraint.** Response times are within contract and both system gaps have vendor solutions waiting on Kestrel decisions.

---

## 4. What must be true before go-live

Four conditions, all achievable inside Q1 planning:

| # | Condition | Owner | Test of completion |
|---|---|---|---|
| 1 | Onboarding replaced with a continuous model — remote-first modules, joiner enrolment on hire, no single classroom window | Programme office + Training | Every technician in North and Islands has logged in before their region's day one |
| 2 | Asset-register feed live in the four current regions | Named IT owner | Equipment-history panel populated; warranty state visible at job open |
| 3 | Completion-code mapping table configured with the vendor | Named IT owner | Reporting and invoicing agree within tolerance; temporary billing clerk released |
| 4 | Weekly fix loop from field observation to programme action, running from week one | Programme office | Week-four issues from Central-equivalent are closed, not logged |

Conditions 2 and 3 are days of work each, already specified by the vendor, and they retire the £8,400 clerk, the 9% duplicate-parts exposure, and the monthly finance reconciliation. Condition 1 is the one that determines whether the extension earns money. Condition 4 is what stops the next two regions from re-teaching us the same lesson.

**Requested decision:** approve Q1 extension to North and Islands, contingent on conditions 1–4 being signed off before each region's go-live date, with the asset-register and code-mapping fixes proven in the existing four regions first.
