# Fieldbook rollout — decision brief for the COO

## Top-level pyramid

**Situation:** Fieldbook has been live for two quarters in four of Kestrel’s six regions: Central, East, South, and West.

**Complication:** Results are strong where adoption was fast, but weaker where onboarding was thin. Two integration gaps and one data-quality limitation remain open.

**Question:** Should Kestrel extend Fieldbook to North and Islands in Q1?

**Answer:** Yes — approve a conditional Q1 extension. Proceed only if three preconditions are in place before go-live:

1. Rolling onboarding replaces the one-off classroom model.  
2. The asset-register feed and invoicing code mapping are scheduled and owned.  
3. A weekly early-warning review converts field issues into program-level fixes.  

If these preconditions cannot be met, defer the extension.

**Key lines:**

1. The platform’s core scheduling value is proven where adoption is fast.  
2. The weak results are caused by onboarding coverage and unowned integrations, not by the platform’s core function.  
3. The financial case is favourable only if Central/East adoption is reproduced.  
4. The required fixes are small, vendor-ready, and achievable within Q1.  

---

## 1. Core scheduling gains prove the platform’s value

**Key message:** Where Fieldbook is actually used, it improves route density, reduces travel, and speeds emergency work.

**Supporting points:**

- Completed jobs per technician per day rose from 4.6 to 5.3 across the four live regions.  
- Average travel time between jobs fell 18%.  
- Same-day emergency insertion is now automatic, with a median of 4 minutes, replacing the previous dispatcher phone-chase process.  
- All 41 dispatchers used Fieldbook scheduling from week one because the legacy scheduling spreadsheet was switched off on day one; forced migration produced immediate adoption.  

---

## 2. Slow adoption is an onboarding failure, not a platform failure

**Key message:** Regional adoption differences track onboarding coverage, not region type or platform usability.

**Supporting points:**

- Fieldbook is live in Central, East, South, and West. Across these regions, 412 of 486 field technicians have activated accounts, and 83% of work orders are created and closed inside Fieldbook rather than on paper or by phone.  
- Central and East reached full adoption within six weeks.  
- South took eleven weeks to pass 80% of orders in-system.  
- West is still at 71% after nine weeks.  
- The two-day classroom course was scheduled only once per region, so technicians hired after the course, or absent during it, learned the platform second-hand from colleagues. In West, 34 of 118 technicians never attended any session. Coordinators improvised shadowing arrangements as a stopgap.  
- Support evidence points to the same cause: the desk logged 1,940 Fieldbook tickets over the two quarters. Ticket volume peaked in each region’s third week and then declined steadily. 44% of all tickets were password resets and login problems, concentrated among technicians who missed the classroom course and had never logged in during the supported window.  
- The weekly one-hour webinar reaches only 20 to 30 technicians, and attendance correlates strongly with regions that missed classroom slots.  
- The support desk lead’s written comment: “We are doing the training program’s job at ticket prices — most of what we handle is people who were never onboarded, plus the two known system gaps.”  

**Implication:** Extension must use rolling onboarding, mandatory first login during a supported window, and backfill for absences rather than relying on a single classroom event.

---

## 3. Known system and data gaps are the main value leaks

**Key message:** Fieldbook reporting is now the source of record, but missing feeds, code mismatches, and duplicate records are creating avoidable errors and manual work.

**Supporting points:**

- Fieldbook’s reporting module is now the source of record for job status across the four regions, and regional managers use its dashboard in the Monday review. Data quality inside Fieldbook is generally good, with the exceptions below.  
- **Missing asset-register feed:** Fieldbook does not receive equipment service history from the legacy asset register, so the equipment-history panel is empty on every job screen. Technicians compensate by calling the back office or asking the customer. In 9% of audited jobs, they replaced parts that had already been replaced within warranty in the past year. The empty panel also hides warranty state from technicians and makes the audit trail useless for dispute resolution. A nightly export was requested in month two and remains in the asset register team’s backlog. The vendor’s integration catalogue lists a supported connector for the asset register’s database, but it has not been evaluated.  
- **Invoicing completion-code mismatch:** Job-completion codes in Fieldbook do not match the codes in the invoicing system. The billing team re-keys roughly 300 job records per week by hand, introducing transcription errors that customers catch on invoices. Support also receives billing-team calls about the mismatch and forwards them to the vendor. Because the codes are re-keyed, the reporting module and the invoicing system disagree on completed-job counts by 2–4% in any given week, and finance reconciles the difference manually at month end. The vendor has confirmed that a configurable mapping table exists and takes roughly a day to set up, but it has not been scheduled because no one on Kestrel’s side owns the integration.  
- **Customer-search limitation:** The search screen matches on exact postcode only. When technicians cannot find the first customer record, they create a second one. Another 19% of all support tickets are duplicate-record tickets. The support desk merges these duplicates manually, at about 70 records per week, and affected customers’ job-history views remain split across records until merged.  
- **Parts-ordering screen:** Most technicians still order parts by phone, but testing shows the screen works correctly. This appears to be habit rather than a defect and should not block extension.  

---

## 4. Extension is financially viable only if fast adoption is reproduced

**Key message:** The rollout is recovering its running cost in fast-adoption regions and is marginal in slow-adoption regions; extension economics depend on avoiding the West pattern.

**Supporting points:**

- Licence and hosting for Fieldbook run £31,000 per month for the four live regions. Extending to North and Islands would add £13,500 per month in licences.  
- In the live regions, overtime spending is down 12% quarter over quarter, which finance attributes mainly to the scheduling gains. Fuel cost per job is down 9%, consistent with the travel-time reduction.  
- The program recovered its running cost within the second quarter in Central and East. South and West are roughly at break-even because slower adoption delayed the savings.  
- Unplanned costs include approximately 380 technician-hours of lost route time from improvised shadowing in South and West, and a temporary billing clerk costing £8,400 over the two quarters to absorb the re-keying described in Section 3.  
- On the current evidence, the economics of extension are favourable if, and only if, the adoption pace of Central and East can be reproduced. A repeat of the West pattern would leave North and Islands loss-making for at least two quarters.  
- Classroom training for the new regions would require winter travel. Rolling onboarding reduces that cost and schedule exposure.  

---

## 5. The preconditions are achievable in Q1

**Key message:** The program’s main weakness was failing to convert early warnings into fixes; the vendor and internal capabilities are sufficient to correct this before extension.

**Supporting points:**

- Every negative pattern in this review was visible by week four of the Central go-live. The program had no mechanism to convert early field observations into program-level fixes, so the same issues replayed in each subsequent region.  
- The vendor relationship is good: response times are within contract, and the unresolved items are ownership and scheduling issues on Kestrel’s side rather than vendor delays.  
- IT considers the asset-register and invoicing integrations straightforward. They were not completed because no integration work was scoped into the rollout program, which was staffed for deployment and training only.  

**Required pre-go-live actions:**

1. Appoint an integration owner and schedule the asset-register feed and invoicing code mapping. Evaluate the vendor-supported connectors before North/Islands go-live.  
2. Restructure onboarding as rolling, role-based sessions with mandatory first login during a supported window, backfill for absences, and removal of legacy paths where safe.  
3. Stand up a weekly early-warning review of adoption, support tickets, and data-quality exceptions, with authority to trigger program-level fixes.  
4. Gate the North/Islands go-live on completion of the onboarding plan and scheduling of the integration fixes. If the gate is not met, defer rather than extend.
