The core is fine — the diagram is missing eight blocks, all in trust, failure handling and the path to production, and three blocks should come off.

Add to close the trust boundary (three blocks): an identity provider instead of the "SSO later" note, service-to-service auth, and a secrets store — we have two external SaaS connectors on the diagram and nowhere to keep their credentials.

Add to make failures survivable (two blocks): a message queue, so one slow partner stops stalling the whole chain of synchronous connector calls, and a dead-letter store, so failed messages stop vanishing.

Add to get a real path to production (four blocks): a CI/CD block, since deploys are currently in the legend as "manual, fortnightly", a structured log pipeline and a per-message trace, so operators stop reconstructing incidents from connector logs by hand, plus a staging environment (optional in the reference model for internal platforms, so count it as the ninth block if you want it in).

Remove three blocks: the "blockchain audit ledger" (nothing writes to it — no inbound arrows), the dotted "future ML anomaly detection" block, and the duplicate retention DB — it is drawn once per environment, but the reference model treats it as one logical block.

Layers 1 and 3 need nothing: gateway, rate limiting, mapping service and schema registry are all present and correct.
