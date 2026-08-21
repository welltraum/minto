**Bottom line:**  
Aldergate has answered the high‑level policy questions, but the two critical artefacts — the approved‑package list and the architecture diagram (needed to resolve data‑storage, encryption and logging requirements) — are still missing, so the security requirements remain unconfirmed and the build‑phase price cannot be fixed.

---

### What is already answered  

| Question | Answer (Aldergate) |
|----------|-------------------|
| **Q1 – Is a security review required before production?** | **Yes.** A review is mandatory; whether a penetration test is also required will be decided during that review. |
| **Q2 – Is there a security standard or checklist we can build against?** | An internal hardening framework exists, but a review is still required regardless of conformance. |
| **Q3 – What is the policy on open‑source dependencies?** | A policy exists; an **approved‑package list** will be sent to Fernway (owner D. Mercer, dated 12 May). |
| **Q4 – Must critical dependencies be approved individually?** | Dependency usage is assessed during the security review. |
| **Q5 – Turn‑around time for dependency approval?** | No standard turnaround; decisions are case‑by‑case. |
| **Q6 – Can Fernway staff work from outside the UK?** | Work from **Ireland** is acceptable (no other country mentioned). |
| **Other** | Compliance contact **S. Okafor** (information‑security owner) has been identified (see 9 July sync). |

### What still has to be obtained from Aldergate  

| Missing item | Why it matters | Current status / blockers |
|--------------|----------------|---------------------------|
| **Approved‑package list** | Needed to confirm open‑source compliance and to close R‑11. | Promised 12 May (Mercer) → promised again 9 July (Whitcombe). Still not received (98 days overdue). |
| **Architecture diagram (draft exists 11 Aug)** | Required to answer Q7 – where customer data will be stored, with what encryption and logging. Without it the security review cannot be completed and R‑14 remains open. | Fernway will send a draft before the next sync, but Aldergate has not yet provided feedback. |
| **Clarification on staff location (Lisbon engineers)** | Q6 only mentions Ireland; Aldergate has not responded to Fernway’s note about Lisbon staff. | No answer from Aldergate; risk that work may be deemed non‑compliant. |
| **Timeline for the security review & possible penetration test** | Q1 says a review is mandatory, but no schedule has been set; pricing depends on when the review can occur. | No date provided; still open (R‑07). |
| **Dependency‑approval turnaround expectations** | Q5 states “case‑by‑case,” but Fernway needs an estimate to plan the build schedule. | No guidance yet. |

### Immediate actions for the tech lead  

1. **Escalate the approved‑package list** – contact S. Okafor (or D. Mercer) to obtain the list today; note the 98‑day delay (R‑11).  
2. **Send the architecture diagram** to Aldergate now (if not already done) and request a concrete response on data‑storage, encryption and logging (to close Q7 and R‑14).  
3. **Ask for clarification on Lisbon staff** – confirm whether work from Portugal is permissible or if an exception is needed.  
4. **Request a tentative schedule** for the mandatory security review (and any penetration test) to unblock pricing (R‑07).  
5. **Seek any provisional guidance** on dependency‑approval turnaround to feed into the build plan.  

Once these items are secured, the security requirements will be confirmed and the build‑phase price can be fixed.
