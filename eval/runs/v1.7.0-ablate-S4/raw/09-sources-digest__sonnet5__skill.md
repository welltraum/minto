The compliance track can't yet support a fixed build-phase price — the one hard blocker is the unsent architecture diagram, which is a Fernway-side delay, not a bank-side one.

**What's settled.** A security review is mandatory before production; a pen test may or may not be added, decided by the reviewer during that review. Aldergate has an internal hardening framework Fernway can build against, but conformance to it doesn't replace the review. Fernway staff can work from Ireland (Lisbon was raised at the 9 July sync and drew no response — treat it as unresolved, not approved).

**What's blocked, and by whom:**

- **On Fernway:** the draft architecture diagram, promised at the 9 July sync, has existed since 11 August but hasn't been sent. It's the single gate on the biggest open item — where data is stored, encryption, and logging (gate review Q7, risk R-14) — which in turn is the one open question likely to reshape build-phase architecture and cost. Send it today; nothing else on the compliance track unblocks until Aldergate can react to it.
- **On Aldergate:** the approved open-source package list, promised twice (D. Mercer on 12 May, R. Whitcombe on 9 July) and still not delivered — 98 days open (R-11). No individual dependency approval is required outside the review, and there's no standard turnaround to hold anyone to, so this won't move without a direct ask. S. Okafor is the named information-security owner but has never joined a call; Whitcombe has just been relaying questions. Push to get Okafor into the next sync directly, since Whitcombe passing messages is likely why the list has slipped twice already.

**Net for pricing today:** R-07 (security requirements unconfirmed, blocking the price) stays open regardless — it needs the review itself, which hasn't been scheduled in any of these sources. Sending the diagram is the one action inside Fernway's control that moves the compliance track forward today.
