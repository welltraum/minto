**Summary**  
Aldergate has already clarified the overall security‑review process and the policy framework, but the concrete artefacts needed to finalize the build‑phase price—approved‑package list, architecture diagram (to answer data‑storage questions), and dependency‑approval details—are still missing. Until those are received, pricing and compliance sign‑off cannot be completed.

---

### What is already answered  

| Question | Answer (as of the latest source) |
|----------|-----------------------------------|
| **Q1 – Is a security review required before production?** | **Yes** – mandatory; decision on a penetration test will be made during the review. |
| **Q2 – Is there a security standard or checklist to build against?** | An **internal hardening framework** exists, but a review is still required regardless of conformance. |
| **Q3 – Policy on open‑source dependencies?** | A policy exists; an **approved‑package list** will be sent to Fernway (owner D. Mercer, dated 12 May). |
| **Q4 – Must critical dependencies be approved individually?** | **Assessed during the security review** (no stand‑alone approval process). |
| **Q5 – Turn‑around time for dependency approval?** | **No standard SLA** – handled case‑by‑case. |
| **Q6 – Can Fernway staff work from outside the UK?** | **Work from Ireland is acceptable** (no other countries mentioned). |
| **Q7 – Where may customer data be stored, with what encryption & logging?** | **Not answered yet** – requires an architecture diagram and design walkthrough (see pending items). |

---

### What still needs to be obtained from Aldergate  

| Item | Why it’s needed | Current status |
|------|----------------|----------------|
| **Approved‑package list** | To confirm that all open‑source components meet Aldergate’s policy and to allow dependency‑approval assessment. | Promised by D. Mercer (12 May) and reiterated by R. Whitcombe (9 July); **still not received** (98 days open – R‑11). |
| **Architecture diagram / design walkthrough** | Required to answer Q7 (data‑storage location, encryption, logging) and to complete the security‑review scope. | Draft exists (11 Aug) but **has not been sent** to Aldergate (R‑14). |
| **Clarification on staff locations beyond Ireland** | Aldergate only mentioned Ireland; Fernway has engineers in Lisbon. Confirmation needed whether Lisbon (or other EU locations) is permissible. | No response from Aldergate (raised at 9 July sync). |
| **Dependency‑approval process details** | While the review will assess critical dependencies, the team needs guidance on any interim approvals or documentation required before the formal review. | No specific guidance provided beyond “assessed during review”. |
| **Turn‑around expectations for any pending approvals** | To plan the build schedule and price the phase accurately. | No SLA defined; need an estimate from Aldergate. |

---

### Immediate actions for the tech lead  

1. **Escalate the approved‑package list** – follow up with D. Mercer (or the newly identified contact S. Okafor) requesting the list by a concrete date.  
2. **Send the draft architecture diagram** to Aldergate **today** and request a design walkthrough in the next sync to lock down Q7.  
3. **Ask for a definitive stance on Lisbon‑based staff** – confirm whether work from Portugal is acceptable or if additional approvals are required.  
4. **Request any interim guidance** on how critical dependencies will be evaluated before the formal security review (e.g., provisional approvals, documentation).  
5. **Obtain an estimated turnaround** for dependency approval and any other pending items to feed into the build‑phase pricing model.  

Once these items are secured, the security‑review can proceed, and the build‑phase price can be fixed.
