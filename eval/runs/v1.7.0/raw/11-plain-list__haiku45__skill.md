Add blocks for trust, failure handling, and production readiness; remove three that don't belong.

Trust (Layer 2):
- Identity provider
- Service-to-service auth
- Secrets store

Failure handling (Layer 4):
- Message queue
- Dead-letter store

Production readiness (Layers 5–6):
- CI/CD
- Staging environment
- Structured logging
- Per-message trace

Remove:
- Blockchain audit ledger (nothing writes to it)
- "Future ML anomaly detection" block (marked dotted)
- Retention DB duplicate
