Add nine blocks to cover identity, resilience, deployment, and observability, and remove three legacy or speculative blocks that clutter the diagram.

Additions:
- Identity & trust boundary: identity provider block, service-to-service authentication, secrets store
- Failure handling: message queue, dead-letter store
- Deployment path: CI/CD pipeline, staging environment
- Observability: structured log pipeline, per-message trace

Removals:
- Blockchain audit ledger (no inbound data flow)
- Future ML anomaly detection (speculative/dotted)
- Duplicate retention database (already represented once)
