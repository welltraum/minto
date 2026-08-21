Add (8 blocks, clustered in trust, failure handling, and path to production):

Identity/security (layer 2) — closes the trust gap on our two external SaaS connectors:
- Identity provider
- Service-to-service auth
- Secrets store

Failure handling (layer 4) — stops one slow partner from stalling the whole chain:
- Message queue
- Dead-letter store

Path to production (layers 5-6) — gets us off manual fortnightly deploys and blind incident response:
- CI/CD pipeline
- Structured log pipeline
- Per-message trace

(Staging environment is a 9th, optional block per the reference model — worth adding but not required.)

Remove (3 blocks):
- Duplicate retention DB (layer 4 shown twice; it's one logical block)
- Blockchain audit ledger (nothing writes to it)
- Future ML anomaly detection (dotted, not real)

Layers 1 and 3 (gateway, mapping, schema registry) are solid as drawn — no changes there.
