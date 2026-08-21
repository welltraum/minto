The integration core is solid (API gateway, rate limiting, mapping service and schema registry are present) and the metrics dashboard is already there; add eight required blocks (nine if staging) and remove three excess blocks.

Add trust-boundary blocks (the diagram already shows two external SaaS connectors):
- Identity provider
- Service-to-service auth
- Secrets store

Add failure-handling blocks:
- Message queue (every connector currently calls the next system synchronously, so one slow partner stalls the chain)
- Dead-letter store (failed messages currently vanish)

Add production-path and observability blocks:
- CI/CD block (deploys are currently manual and fortnightly)
- Staging environment (optional for internal platforms)
- Structured log pipeline
- Per-message trace (operators currently reconstruct incidents from connector logs by hand)

Remove excess blocks:
- Blockchain audit ledger (no inbound arrows, so nothing writes to it; added by a previous architect and surviving by inertia)
- Future ML anomaly detection (dotted; added by a previous architect and surviving by inertia)
- Duplicate retention DB (shown once per environment; the reference model treats it as one logical block)
