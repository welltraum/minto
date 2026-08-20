<!-- Original fixture. The scenario, company, people, systems and numbers are
     invented for this benchmark. The defect pattern it tests — a digest of several
     read sources delivered answer-first into chat — is modeled on real usage. -->

# Fixture 09: sources digest

**Mode:** `digest`
**Language:** `en`

## Context

You are assisting the tech lead of Fernway Systems, a vendor building a customer
support assistant for Aldergate Bank. Before Fernway can price the build phase, the
bank's compliance office must confirm its security requirements. You have just read
the three sources below in full. The tech lead has not read them and will not; they
are deciding what to do about the compliance track today.

## Before

Source 1 — `gate-review.xlsx`, sheet "Security questions", filled in by Aldergate's
compliance office on 12 May:

```text
Q1 Is a security review required before production?
   A: Yes. A review is mandatory; whether a penetration test is also needed is
   decided during the review itself, by the assigned reviewer.
Q2 Is there a security standard or checklist we can build against?
   A: An internal hardening framework exists; a review is still required
   regardless of conformance.
Q3 What is the policy on open-source dependencies?
   A: A policy exists. The approved-package list will be sent to Fernway.
   Owner: D. Mercer. Date: 12 May.
Q4 Must critical dependencies be approved individually?
   A: Dependency usage is assessed during the security review.
Q5 What is the turnaround time for dependency approval?
   A: There is no standard turnaround; it is case by case.
Q6 Can Fernway staff work from outside the UK?
   A: Work from Ireland is acceptable. (No other country is mentioned.)
Q7 Where may customer data be stored, and with what encryption and logging?
   A: Declined — "cannot be answered without an architecture diagram and a
   design walkthrough". Encryption and logging requirements exist but are
   not applicable outside an architectural context.
```

Source 2 — follow-up note from the 9 July delivery sync, `sync-0709.md`:

```text
Attendees: R. Whitcombe (Aldergate, delivery), tech lead (Fernway), PM (Fernway).
- Whitcombe repeated that the approved-package list "is being prepared" and will
  reach Fernway "shortly". Action on Whitcombe, no date attached.
- Compliance contact named for the first time: S. Okafor, information security
  owner. Okafor has not attended any joint meeting so far; Whitcombe passes
  questions along.
- Agreed: Fernway sends the draft architecture diagram before the next sync so
  the storage and encryption questions can get a real answer.
- Fernway's PM noted two Fernway engineers are based in Lisbon. Nobody from
  Aldergate responded to the remark in the meeting.
```

Source 3 — Fernway's internal risk register, rows touching compliance, as of
18 August:

```text
R-07  Security requirements unconfirmed; build-phase price cannot be fixed.
      Owner: tech lead. Status: open since 3 May.
R-11  Approved-package list not received. First promised 12 May (Mercer, per
      gate review), promised again 9 July (Whitcombe). Status: open, 98 days.
R-14  Architecture diagram not yet sent to Aldergate; blocks the data-storage
      answer (gate review Q7). Draft exists since 11 August. Status: open.
```

## Task

Give the tech lead a digest of these three sources in chat: what is already
answered on the compliance track, and what still has to be obtained from
Aldergate. The tech lead will act on it today.
