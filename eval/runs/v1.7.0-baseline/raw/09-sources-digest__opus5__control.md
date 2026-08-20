**Bottom line: nothing on the compliance track is blocked on Aldergate alone — the one item you can move today is the architecture diagram, which is sitting in draft on your side and is the precondition for the biggest open question (where customer data may live). The other gap, the approved-package list, is 98 days late and needs escalation past Whitcombe to Okafor, the security owner you now have a name for.**

**Settled (no further action needed)**

- A security review before production is mandatory. A penetration test is *not* separately confirmed — the assigned reviewer decides that during the review itself, so treat it as a possible but unpriced addition.
- An internal hardening framework exists to build against, but conforming to it does not remove the review.
- An open-source dependency policy exists, and dependency usage is judged inside the security review rather than package-by-package in advance.
- Work from Ireland is acceptable.

**Still to obtain from Aldergate**

- **The approved-package list.** Promised by Mercer on 12 May, re-promised by Whitcombe on 9 July, still unreceived with no date ever attached (R-11). Whitcombe has relayed this twice without result; Okafor is the named information security owner and has never been in a joint meeting.
- **Data storage, encryption and logging requirements** (Q7). Declined outright pending an architecture diagram and a design walkthrough. Your draft has existed since 11 August and has not been sent (R-14) — this is the gating dependency, not Aldergate's reticence.
- **Dependency approval turnaround.** Explicitly case-by-case, so no number exists to plan against. You will have to bound this with an assumption and state it, or get Okafor to commit to a ceiling.
- **Confirmation on Lisbon.** Your PM raised the two Lisbon-based engineers on 9 July and no one from Aldergate responded. The gate review sanctions Ireland only and names no other country. Silence is not approval — assume Lisbon is unapproved until answered in writing.

**What this means for the price**

R-07 has been open since 3 May and cannot close while the pen-test decision, the storage requirements and the dependency turnaround are all indeterminate. Two of those three unblock only after the diagram goes over. Suggested moves today: send the draft diagram and request the design walkthrough date in the same message; ask Whitcombe for a direct introduction to Okafor and put the package list and the Lisbon question to Okafor with a deadline; and flag to the bank that build-phase pricing will carry a stated contingency for a penetration test until the reviewer rules.
