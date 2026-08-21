Add:
- Identity provider block, service-to-service auth, secrets store — the diagram has two external SaaS connectors with no trust boundary around them
- Message queue and dead-letter store — right now one slow partner stalls the whole chain and failed messages vanish with no trace
- CI/CD pipeline — deploys are manual and fortnightly with nothing on the diagram to show it
- Staging environment — optional for internal platforms per the reference model, but worth adding given the gaps above
- Structured log pipeline and per-message tracing — operators currently reconstruct incidents by hand from connector logs

Remove:
- Blockchain audit ledger block — nothing writes to it
- Future ML anomaly detection block — dotted/speculative, not real
- Duplicate retention DB — same logical block shown once per environment, should be one

The core (routing and transformation layers) is solid as-is. The gaps are concentrated in trust, failure handling, and the path to production.
