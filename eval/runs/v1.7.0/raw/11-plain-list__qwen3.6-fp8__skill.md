To align the Ledgerline diagram with the reference model, add nine blocks across identity, resilience, delivery, and observability, and remove three speculative or redundant blocks.

Add these blocks:
- Identity provider, service-to-service auth, and secrets store (trust boundary)
- Message queue and dead-letter store (failure handling)
- CI/CD pipeline and staging environment (delivery)
- Structured log pipeline and per-message trace (observability)

Remove these blocks:
- Blockchain audit ledger (no inbound arrows)
- Future ML anomaly detection (speculative)
- Duplicate retention DB entry
