The integration core is fine — the gaps are all in trust, failure handling and the path to production. Eight blocks need adding (nine if we want staging, which the reference model makes optional for internal platforms), and three should come off.

To add:

- Identity provider — the diagram just says "SSO later"
- Service-to-service auth
- Secrets store — we have two external SaaS connectors and nowhere to keep their credentials
- Message queue — right now every connector calls the next system synchronously, so one slow partner stalls the whole chain
- Dead-letter store — failed messages currently vanish
- CI/CD — deploys are "manual, fortnightly" per the legend
- Structured log pipeline
- Per-message trace — operators reconstruct incidents from connector logs by hand
- Staging environment (optional, but worth a decision)

To remove:

- Blockchain audit ledger — nothing writes to it, no inbound arrows
- Future ML anomaly detection — dotted, not planned work
- The duplicate retention DB — it's drawn once per environment, but the reference model treats it as one logical block

Layers 1 and 3 (entry/routing and transformation) are covered as drawn.
