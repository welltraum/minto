# Decision: extend Fieldbook to North and Islands in Q1—only after the rollout is reset to reproduce the Central/East adoption model and close the known integration gaps.

Fieldbook has delivered material operating gains in the four live regions: more jobs per technician, less travel, lower overtime and fuel costs. But South and West show that a poorly supported rollout erodes those gains quickly, and the two unresolved integrations now create avoidable warranty, billing and reporting risk. North and Islands should proceed only with these conditions approved before go-live.

## 1. Make full, supported adoption a release condition

- Provide repeatable onboarding for every technician, including hires and absentees—not a single two-day classroom session per region.
  - Central and East reached full adoption within six weeks.
  - South needed eleven weeks to exceed 80% of orders in the system; West remains at 71% after nine weeks.
  - In West, 34 of 118 technicians attended no session; across the live regions, 412 of 486 technicians have activated accounts.
- Schedule classroom training before go-live, with winter travel included in the North and Islands plan, then run weekly webinars and supported login windows.
  - The support desk’s weekly webinars reach 20–30 technicians and attendance is strongest in regions where classroom slots were missed.
  - Forty-four percent of 1,940 support tickets were password-reset or login issues among technicians who missed onboarding.
- Avoid relying on informal shadowing.
  - Shadowing in South and West cost an estimated 380 technician-hours of route time.
  - It works operationally, but removes experienced technicians from productive routes.
- Retain the day-one dispatcher cutover model.
  - All 41 dispatchers adopted Fieldbook scheduling from week one once the legacy spreadsheet was switched off.

## 2. Close the known data and billing gaps before expansion

- Integrate equipment service history from the legacy asset register.
  - Technicians currently start every job without prior service history, then call the back office or customer.
  - In 9% of audited jobs, parts were replaced despite having been replaced under warranty in the prior year.
  - The missing history leaves the equipment panel empty, prevents useful dispute-resolution audit trails, and keeps warranty state hidden.
  - The asset-register team’s requested nightly export has remained in backlog since month two; the vendor lists a supported connector.
- Configure the Fieldbook-to-invoicing completion-code mapping and assign a Kestrel owner.
  - Billing re-keys roughly 300 records per week, requiring a temporary clerk costing £8,400 over two quarters.
  - Manual re-keying introduces invoice errors and produces a 2–4% weekly difference between Fieldbook and invoicing completed-job counts, reconciled manually each month.
  - The vendor says the mapping table takes about one day to configure; it has not been scheduled because no Kestrel owner exists.
  - A supported connector for the invoicing import format is also available for evaluation.
- Fix or mitigate duplicate customer records before they impair the larger rollout.
  - Exact-postcode search causes technicians to create duplicate records; support merges about 70 each week.
  - Duplicate records account for 19% of tickets and split customer job history until manually merged.
- Treat parts-ordering adoption separately from system defects.
  - Most technicians still order parts by phone, although the Fieldbook screen works correctly in testing; this is a habit-change issue, not a technical blocker.

## 3. Run North and Islands as a controlled rollout, not two more regional deployments

- Set explicit go/no-go gates: training completion, technician activation, work-order usage, integration readiness, and an accountable integration owner.
  - Fieldbook already handles 83% of work orders in the live regions.
  - The program’s economics depend on reproducing Central/East adoption speed; repeating West’s pattern would leave the new regions underwater for at least two quarters.
- Use week-four evidence to correct the next wave immediately.
  - Every negative pattern was visible by week four of the Central launch, but no mechanism converted field observations into program-level fixes.
  - The same issues therefore replayed in later regions.
- Establish a weekly cross-functional rollout review covering operations, support, finance, IT, the asset-register team and billing.
  - IT considers both integrations straightforward, but integration work was never scoped because the programme was staffed only for deployment and training.
  - The vendor relationship is not the constraint: response times are within contract, and both known system gaps have vendor solutions awaiting Kestrel decisions.
- Track the operating and financial outcome by region through the first quarter.
  - Scheduling gains have raised completed jobs per technician per day from 4.6 to 5.3 and reduced travel time between jobs by 18%.
  - Same-day emergency insertion now takes a median four minutes rather than dispatcher phone calls.
  - Overtime is down 12% quarter over quarter and fuel cost per job is down 9%.
  - Central and East repaid running costs in the second quarter; South and West are roughly break-even.
  - Current licences and hosting cost £31,000 per month across four regions; North and Islands would add £13,500 per month.

**Approval requested:** approve a Q1 extension to North and Islands, conditional on the onboarding plan, integration ownership, code mapping and asset-history solution being committed before either region goes live.

Top: Extend Fieldbook to North and Islands in Q1, conditional on fixing the repeatable causes of slow adoption and data risk before go-live.
  1. Make full, supported adoption a release condition.
     - Train every technician, including absentees and later hires.
     - Retain supported login and webinar coverage.
     - Avoid route-time-consuming informal shadowing.
  2. Close the known data and billing gaps before expansion.
     - Supply asset-service history.
     - Configure completion-code mapping and evaluate supported connectors.
     - Reduce duplicate customer records.
  3. Run the new regions as a controlled rollout.
     - Gate each go-live against adoption and integration readiness.
     - Turn early field evidence into programme-wide fixes.
     - Track regional operating and financial outcomes.