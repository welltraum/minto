<!-- Original fixture. Company, product, regions, people and numbers are invented.
     It tests the large-document behaviors: one pyramid per section plus a
     top-level pyramid, MECE across sections (planted cross-section duplicates),
     and geometry derived from the material rather than a fixed 3x3 habit. -->

# Fixture 10: rollout review

**Mode:** `write`
**Language:** `en`

## Context

Kestrel Maintenance Group services heating and cooling equipment across six
regions. Over the past two quarters it rolled out Fieldbook, a work-order and
scheduling platform, to four of the six regions. The draft below is the internal
review of that rollout, assembled by the program office from status reports. The
reader is the chief operating officer, who must decide at the quarterly meeting
whether to extend Fieldbook to the remaining two regions (North and Islands) in
Q1, and has asked to see this review beforehand.

## Before

```text
FIELDBOOK ROLLOUT — TWO-QUARTER REVIEW (DRAFT)

1. Adoption

Fieldbook is now live in four regions: Central, East, South, and West. Across
these regions 412 of 486 field technicians have activated their accounts, and
83% of work orders are now created and closed inside Fieldbook rather than on
paper or by phone. Central and East reached full adoption within six weeks.
South and West lagged: South took eleven weeks to pass 80% of orders in the
system, and West is still at 71% after nine weeks. Regional coordinators in
both slower regions report the same explanation: the two-day classroom course
was scheduled only once per region, so technicians hired after the course, or
absent during it, learned the platform second-hand from colleagues. In West,
34 of 118 technicians never attended any session. Coordinators improvised
shadowing arrangements, which worked but pulled experienced technicians off
their own routes. Uptake among dispatchers was faster: all 41 dispatchers
across the four regions were using Fieldbook scheduling from week one, since
the old scheduling spreadsheet was switched off on day one and they had no
alternative.

2. Operations

The clearest operational gain is scheduling density. With Fieldbook suggesting
route-aware assignment, completed jobs per technician per day rose from 4.6 to
5.3 across the four live regions, and average travel time between jobs fell
18%. Same-day emergency insertion, which previously required a dispatcher to
phone technicians until someone accepted, is now automatic and takes a median
of 4 minutes. However, the benefit is partly eaten by a data-transfer defect:
Fieldbook does not receive equipment service history from the legacy asset
register, so technicians open each job without knowing what was done at that
site before. They compensate by calling the back office, or by asking the
customer, and in 9% of audited jobs they replaced parts that had already been
replaced within warranty in the past year. The asset register team was asked
in month two for a nightly export; the request is still in their backlog. A
second, smaller friction: job-completion codes in Fieldbook do not match the
codes in the invoicing system, so the billing team re-keys roughly 300 job
records per week into the invoicing system by hand, introducing transcription
errors that customers catch on invoices. Operations leads in Central and East
also note that Fieldbook's parts-ordering screen is unpopular; most
technicians still order parts by phone, though this appears to be habit rather
than a defect, as the screen works correctly in testing.

3. Support and training

The support desk logged 1,940 Fieldbook tickets over the two quarters. Ticket
volume peaked in each region's third week and declined steadily after. 44% of
all tickets are password resets and login problems, concentrated among
technicians who missed the classroom course and had never logged in during the
supported window. Another 19% are duplicate-record tickets: technicians create
a second customer record when they cannot find the first, because the search
screen matches on exact postcode only. The support desk merges these
duplicates manually, at about 70 records per week. Support also fields a
steady trickle of calls from the billing team about mismatched job-completion
codes, which the desk cannot resolve and forwards to the vendor. The vendor's
response on the code mismatch has been that a configurable mapping table
exists and takes roughly a day to set up, but it has not been scheduled
because no one on Kestrel's side owns the integration. Training-wise, the desk
runs a weekly one-hour webinar that reaches 20 to 30 technicians; attendance
correlates strongly with regions that missed classroom slots. The desk lead's
written comment: "We are doing the training program's job at ticket prices —
most of what we handle is people who were never onboarded, plus the two known
system gaps."

4. Finance

Licence and hosting for Fieldbook run £31,000 per month for the four live
regions. Overtime spending in the live regions is down 12% quarter over
quarter, which finance attributes mainly to the scheduling gains, and fuel
cost per job is down 9%, consistent with the travel-time reduction. Against
that, the program has carried unplanned costs: the improvised shadowing
arrangements in South and West consumed an estimated 380 technician-hours of
lost route time, and the billing team added one temporary clerk (£8,400 for
the two quarters) to handle the re-keying of job records into the invoicing
system. The program office estimates that the rollout paid back its running
cost within the second quarter in Central and East, while South and West are
roughly at break-even because of the slower adoption. Extending to North and
Islands would add £13,500 per month in licences and require winter travel for
any classroom training. On the current evidence the economics of extension are
favourable if, and only if, the adoption pace of Central and East can be
reproduced; a repeat of the West pattern would put the new regions underwater
for at least two quarters. The program office therefore leans toward
extending in Q1, provided onboarding is restructured first.

5. Data and integrations

Fieldbook's reporting module is now the source of record for job status across
the four regions, and regional managers use its dashboard in the Monday
review. Data quality inside Fieldbook is generally good, with two exceptions.
First, the customer-record duplicates created through the search limitation
(support merges about 70 per week, as noted) mean that job-history views for
affected customers are split across records until merged. Second, the missing
feed from the legacy asset register leaves the equipment-history panel empty
on every job screen, which both hides warranty state from technicians and
makes the panel's audit trail useless for dispute resolution. The invoicing
mismatch also surfaces here: because completion codes are re-keyed by hand,
the reporting module and the invoicing system disagree on completed-job counts
by 2-4% in any given week, and finance reconciles the difference manually at
month end. The vendor's integration catalogue lists supported connectors for
both the asset register's database and the invoicing system's import format;
neither connector has been evaluated. IT's position is that both are
straightforward but that no integration work was scoped into the rollout
program, which was staffed for deployment and training only.

6. Program office remarks

Individual regional reports repeat most of the above in local detail. Two
further observations. First, every negative pattern in this review was visible
by week four of the Central go-live; the program had no mechanism to convert
early field observations into program-level fixes, so the same issues
replayed in each subsequent region. Second, the vendor relationship is good:
response times are within contract, and both known system gaps have vendor
solutions waiting on Kestrel decisions rather than on vendor work.
```

## Task

Restructure this review for the COO using the Minto Pyramid Principle. The COO's
decision is whether to extend Fieldbook to North and Islands in Q1.
