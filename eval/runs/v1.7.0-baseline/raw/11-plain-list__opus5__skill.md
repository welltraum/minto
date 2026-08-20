The core is fine — layers 1 and 3 are covered. Eight blocks are missing (nine with staging, which the reference model makes optional), and three should come off. The gaps sit in three places: trust, failure handling, and the path to production.

Add — trust boundary (layer 2), where we currently have only a "SSO later" note and two live external SaaS connectors:
- identity provider
- service-to-service auth
- secrets store

Add — failure handling (layer 4), because today every connector calls the next system synchronously, so one slow partner stalls the whole chain and failed messages disappear:
- message queue
- dead-letter store

Add — path to production (layers 5-6), because deploys are manual and fortnightly and operators reconstruct incidents from connector logs by hand:
- CI/CD
- structured log pipeline
- per-message trace
- staging environment (optional per the reference model, but worth having)

Remove:
- blockchain audit ledger — no inbound arrows, nothing writes to it
- future ML anomaly detection — dotted placeholder, not architecture
- the second retention DB — it's drawn once per environment, but the reference model treats it as one logical block
