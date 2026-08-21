Add:

Identity provider, service-to-service auth, secrets store (trust boundary — driven by the two external SaaS connectors)
Message queue, dead-letter store (so one slow partner can't stall the chain and failed messages don't vanish)
CI/CD pipeline
Structured log pipeline, per-message trace (so incidents don't need manual reconstruction from connector logs)

Staging environment is optional per the reference model, but worth adding given the manual fortnightly deploys.

Remove:

Blockchain audit ledger block (nothing writes to it)
Future ML anomaly detection block (dotted, not real)
Duplicate retention DB (keep one logical block, not one per environment)

Core integration layers (gateway/routing and transformation) are solid as-is.
