# Fieldbook Q1 Extension Decision

## Recommendation

Approve Q1 extension to North and Islands, conditional on completing three pre-launch actions before either region goes live:

1. Replace one-off classroom training with repeatable, attendance-controlled onboarding.
2. Assign ownership and implement the asset-history and invoicing-code integrations.
3. Establish a rollout control process that turns early field evidence into fixes before the next go-live.

Fieldbook is delivering material operating gains in the four live regions, but the current deployment model would risk repeating West’s slow adoption and delaying payback in the remaining regions.

## Why extension is justified

Fieldbook has improved route efficiency and reduced operating cost where it is in use.

- Completed jobs per technician per day increased from 4.6 to 5.3.
- Travel time between jobs fell 18%; fuel cost per job fell 9%.
- Same-day emergency work can be assigned in a median four minutes.
- Overtime in live regions is down 12% quarter over quarter.
- Central and East recovered running costs within the second quarter.

The platform is operationally viable: all 41 dispatchers adopted scheduling from week one, Fieldbook is now the job-status source of record, and vendor response times are within contract.

## What must change before extension

### 1. Make onboarding repeatable and complete

Slow adoption is primarily an onboarding failure, not a platform failure.

South required eleven weeks to pass 80% of work orders in Fieldbook, and West remains at 71% after nine weeks. Both regions held only one classroom course, leaving later hires and absent technicians to learn informally. In West, 34 of 118 technicians received no training; improvised shadowing consumed 380 technician-hours of route time.

The same gap drives support demand: 44% of the 1,940 tickets were login or password issues concentrated among untrained technicians, while the support desk’s weekly webinars are compensating for missed onboarding.

Before launch, each new region should have:

- Multiple training sessions, including sessions for absentees and new starters.
- Named attendance and first-login completion targets.
- A supported first-use window after go-live.
- Local super-users whose time is planned rather than taken from active routes.

### 2. Resolve the two known integration gaps

The unresolved integrations create avoidable operational cost, data risk, and customer-facing errors.

Without asset-register history, technicians cannot see prior service or warranty status. In 9% of audited jobs, parts were replaced despite having been replaced under warranty in the prior year. The missing history also weakens dispute-resolution audit trails.

The mismatch between Fieldbook completion codes and invoicing requires roughly 300 records a week to be re-keyed. It has required a temporary clerk costing £8,400 over two quarters and leaves completed-job counts 2–4% out of sync between systems.

Both issues have available vendor-supported solutions: a nightly asset-history export or connector, and a configurable completion-code mapping table. IT considers the connectors straightforward; the blocker is that no Kestrel owner has been assigned.

Before launch, assign an accountable integration owner and complete:

- Asset-register history feed into Fieldbook.
- Completion-code mapping between Fieldbook and invoicing.
- Acceptance testing of data quality, warranty visibility, invoice accuracy, and reporting reconciliation.

### 3. Run the remaining rollout as a controlled sequence

Known issues were visible by week four of Central’s go-live but were repeated in later regions because no mechanism converted local observations into programme-wide changes.

North and Islands should therefore not launch simultaneously. Launch North first, review performance after four weeks, apply any required adjustments, then launch Islands.

The programme office should report weekly against:

- Technician training completion and first login.
- Share of work orders created and closed in Fieldbook.
- Ticket volume and causes.
- Duplicate-customer records.
- Billing re-key volume and reporting reconciliation.
- Jobs per technician, travel time, overtime, and fuel cost.

## Decision and conditions

Approve Q1 extension, with North as the first launch and Islands following only after North meets readiness and early-adoption thresholds.

Do not proceed to either launch until onboarding capacity, integration ownership, and tested fixes for asset history and invoicing codes are in place. This preserves the economics demonstrated in Central and East and avoids the slower, break-even pattern seen in South and West.