The integration core is fine — the gaps are all in trust, failure handling and the path to production: add eight blocks, take three off.

**Add, to close the trust boundary (three blocks).** An identity provider — the diagram only carries a "SSO later" note. Service-to-service auth between components. A secrets store, which two external SaaS connectors on the diagram currently have nowhere to keep credentials.

**Add, so failures stop disappearing (two blocks).** A message queue: every connector calls the next system synchronously, so one slow partner stalls the whole chain. A dead-letter store, without which failed messages vanish with no trace.

**Add, to make the path to production visible (three blocks, plus one optional).** A structured log pipeline and a per-message trace — today operators reconstruct incidents by hand from connector logs. A CI/CD block: deploys are described in the legend as manual and fortnightly, and no block represents them. A staging environment as well, which the reference model lists as optional for internal platforms, so treat it as the ninth and lowest-priority.

**Remove three blocks.** The "blockchain audit ledger", which has no inbound arrows — nothing writes to it. The dotted "future ML anomaly detection" block. Both were added by a previous architect and survive by inertia. And the retention DB, which is drawn twice, once per environment, where the reference model treats it as one logical block — keep one.
