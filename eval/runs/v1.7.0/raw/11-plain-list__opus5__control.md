The integration core is fine — layers 1 and 3 are covered. The gaps are all in trust, failure handling, and the path to production: eight blocks to add (nine with staging, which the reference model treats as optional for internal platforms), three to take off.

Add — trust boundary (layer 2), currently just a "SSO later" note, with two external SaaS connectors already on the diagram:
- identity provider
- service-to-service auth
- secrets store

Add — failure handling (layer 4):
- message queue; today every connector calls the next system synchronously, so one slow partner stalls the chain
- dead-letter store; failed messages currently vanish

Add — path to production (layers 5 and 6):
- CI/CD; the legend describes deploys as manual and fortnightly
- structured log pipeline
- per-message tracing; operators reconstruct incidents from connector logs by hand
- staging environment (optional per the reference model, but nothing sits between a laptop and prod right now)

Remove:
- blockchain audit ledger — no inbound arrows, nothing writes to it
- future ML anomaly detection — dotted, no owner
- the second retention DB — it's drawn once per environment, but the reference model treats it as one logical block

The first two are inherited from a previous architect and survive by inertia.
