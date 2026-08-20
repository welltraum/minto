The diagram covers routing and transformation well, but needs nine additions and three removals.

Add:
- Identity provider, service-to-service auth, secrets store
- Message queue, dead-letter store
- CI/CD pipeline, staging environment, structured logging, per-message tracing

Remove:
- Blockchain audit ledger (no consumers)
- ML anomaly detection (future placeholder)
- Retention DB duplicate
