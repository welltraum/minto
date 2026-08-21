The integration core is fine — gateway, routing, mapping and schema registry all match the reference model. The gaps cluster in three places: trust, failure handling, and the path to production. Eight blocks are missing (nine if we count staging, which the reference model makes optional for internal platforms), and three should come off.

Add — trust boundary:
1. Identity provider block, replacing the "SSO later" note.
2. Service-to-service auth between connectors.
3. Secrets store — we have two external SaaS connectors on the diagram and nowhere for their credentials to live.

Add — failure handling:
4. Message queue. Right now every connector calls the next system synchronously, so one slow partner stalls the whole chain.
5. Dead-letter store. Failed messages currently vanish.

Add — path to production:
6. CI/CD block. Deploys are "manual, fortnightly" per the legend and appear nowhere in the architecture.
7. Structured log pipeline.
8. Per-message trace. Operators reconstruct incidents from connector logs by hand today.
9. Staging environment (optional under the reference model, but worth a decision either way).

Remove:
1. "Blockchain audit ledger" — no inbound arrows, nothing writes to it.
2. "Future ML anomaly detection" — dotted, not part of the current architecture.
3. The duplicate retention DB. It is drawn once per environment; the reference model treats it as one logical block.
