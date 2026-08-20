Add nine blocks across identity, failure handling, delivery, and observability; remove three legacy or speculative blocks.

Identity & trust boundary:
- Identity provider block
- Service-to-service authentication
- Secrets store for external SaaS connectors

Failure handling & async routing:
- Message queue to prevent synchronous stalls
- Dead-letter store to capture failed messages

Delivery & observability:
- CI/CD pipeline block
- Staging environment
- Structured log pipeline
- Per-message tracing

Remove speculative & redundant elements:
- Blockchain audit ledger (no data writes to it)
- Future ML anomaly detection (marked dotted)
- Duplicate retention DB entry
