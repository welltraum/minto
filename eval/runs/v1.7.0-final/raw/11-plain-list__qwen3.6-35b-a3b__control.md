Update the Ledgerline diagram to match the reference model by adding nine required components and removing three obsolete ones.

Components to add:
- Trust boundary: identity provider, service-to-service authentication, secrets store
- Failure handling: message queue, dead-letter store
- Production path: CI/CD pipeline block, staging environment, structured log pipeline, per-message tracing

Blocks to remove:
- Blockchain audit ledger (no inbound data)
- Future ML anomaly detection (future work)
- Duplicate retention database (shown twice)
