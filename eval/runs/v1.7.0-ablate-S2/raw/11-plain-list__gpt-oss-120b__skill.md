Add the missing blocks and remove the unnecessary ones as follows:

Add:
- Identity provider block (trust boundary)
- Service‑to‑service authentication block (trust boundary)
- Secrets store for external SaaS connectors (trust boundary)
- Message queue for asynchronous processing (state layer)
- Dead‑letter store for failed messages (state layer)
- Staging environment for deployments (delivery layer)
- CI/CD pipeline block (delivery layer)
- Structured log pipeline (observability layer)
- Per‑message tracing capability (observability layer)

Remove:
- Duplicate retention DB block (state layer)
- “Blockchain audit ledger” block with no inbound connections
- “Future ML anomaly detection” placeholder block (dotted)
