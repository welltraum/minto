Missing 8 blocks, mostly in trust and failure handling — add these before the diagram is final; remove 3 dead blocks.

Add:
- Identity provider block, service-to-service auth, secrets store (both SaaS connectors currently sit outside any trust boundary)
- Message queue between connectors (a slow partner currently stalls the whole chain)
- Dead-letter store (failed messages currently vanish)
- CI/CD pipeline block (deploys are manual, fortnightly)
- Structured log pipeline, per-message trace (operators currently reconstruct incidents by hand from connector logs)

Optional: staging environment — reference model lists it as optional for internal platforms.

Remove:
- Blockchain audit ledger block — no inbound arrows, nothing writes to it
- Future ML anomaly detection block — dotted, not built
- Duplicate retention DB — same logical block shown twice, once per environment

Solid as-is: entry/routing (gateway, rate limiting) and transformation (mapping service, schema registry).
