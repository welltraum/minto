The integration core is solid. Close three critical gaps — trust (unguarded external connectors), failure handling (sync-only design stalls on slow partners and loses messages), delivery (no CI/CD, no tracing) — by adding these blocks. Remove three that add noise.

Add for trust:
- Identity provider
- Service-to-service auth
- Secrets store

Add for failure handling:
- Message queue
- Dead-letter store

Add for delivery and observability:
- CI/CD pipeline
- Structured log pipeline
- Per-message tracing
- Staging environment (optional per reference model)

Remove:
- Blockchain audit ledger — no inbound arrows, unused
- Future ML anomaly detection — not yet built, marked dotted
- Duplicate retention DB — shown once per environment, not as one logical block
