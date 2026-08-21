**Bottom line:**  
Aldergate has answered most policy‑level questions, but the concrete artefacts needed to satisfy compliance (approved‑package list, architecture diagram, and the resulting storage/encryption/logging details) are still missing; without them Fernway cannot finalize the build‑phase price or confirm that all security requirements are met.

---

### What is already answered  

| Question | Answer (from Aldergate) |
|----------|------------------------|
| **Q1 – Is a security review required before production?** | **Yes.** A mandatory review will decide if a penetration test is also needed. |
| **Q2 – Is there a security standard or checklist to build against?** | An internal hardening framework exists, but a review is still required regardless of conformance. |
| **Q3 – Policy on open‑source dependencies?** | A policy exists; an **approved‑package list** will be supplied (owner = D. Mercer, dated 12 May). |
| **Q4 – Must critical dependencies be approved individually?** | Dependency usage is assessed **during the security review** (no per‑dependency pre‑approval required). |
| **Q5 – Turnaround time for dependency approval?** | **No standard turnaround** – approvals are handled case‑by‑case. |
| **Q6 – Can Fernway staff work from outside the UK?** | Work from **Ireland** is acceptable (no other countries mentioned). |
| **Q7 – Where may customer data be stored, with what encryption & logging?** | **Not answerable yet** – requires an architecture diagram and design walkthrough (encryption/logging requirements exist but are context‑dependent). |

*Additional context from the July sync:*  
- The approved‑package list is “being prepared” and will be sent “shortly” (action assigned to R. Whitcombe, no date).  
- S. Okafor is now the information‑security owner (has not yet attended a joint meeting).  
- Fernway will send a **draft architecture diagram** before the next sync to enable a concrete answer to Q7.  
- Two Fernway engineers are based in Lisbon; Aldergate gave no response regarding that location.

---

### What still has to be obtained from Aldergate  

| Item | Why it’s needed | Current status |
|------|----------------|----------------|
| **Approved‑package list** | To verify open‑source dependencies against the bank’s policy and to close R‑11. | Promised 12 May (Mercer) → promised again 9 July (Whitcombe); **still not received** (98 days open). |
| **Final architecture diagram & design walkthrough** | Required to answer Q7 (data‑storage location, encryption, logging) and to complete the security review. | Draft exists (since 11 Aug) but **has not been sent** to Aldergate (R‑14). |
| **Concrete storage, encryption & logging specifications** | Needed for compliance evidence and to determine any additional controls. | Dependent on the architecture diagram; **pending**. |
| **Confirmation on staff locations beyond Ireland** (e.g., Lisbon engineers) | To ensure remote work complies with any location‑specific rules. | No response from Aldergate; **open**. |
| **Schedule for the mandatory security review (and possible penetration test)** | To lock in the build‑phase timeline and pricing. | Not yet defined; **open**. |

---

### Immediate actions for today  

1. **Escalate the approved‑package list request** to R. Whitcombe (or directly to D. Mercer) with a firm deadline (e.g., end of week).  
2. **Send the draft architecture diagram** to Aldergate (copy S. Okafor) and request a design walkthrough slot before the next sync.  
3. **Ask Aldergate to confirm** whether Lisbon‑based engineers are acceptable or if additional approvals are needed.  
4. **Request a tentative schedule** for the mandatory security review (and any subsequent penetration test).  

Completing these items will unblock R‑07, R‑11, and R‑14, allowing Fernway to finalize the build‑phase price and proceed with compliance‑aligned development.
