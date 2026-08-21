The draft is solid in entry/routing (API gateway, rate limiting) and transformation (mapping service, schema registry), and it already has a metrics dashboard; against the reference model it needs nine additions—eight required plus optional staging—and three removals.

Add to the trust boundary:
Identity provider block — the diagram only has a “SSO later” note
Service-to-service auth — two external SaaS connectors are on the diagram
Secrets store — two external SaaS connectors are on the diagram

Add to failure handling:
Message queue — every connector currently calls the next system synchronously, so one slow partner stalls the chain
Dead-letter store — failed messages currently vanish

Add to the path to production:
CI/CD block — deploys are described in the legend as manual and fortnightly
Staging environment — the reference model lists this as optional for internal platforms
Structured log pipeline — operators currently reconstruct incidents from connector logs by hand
Per-message trace — operators currently reconstruct incidents from connector logs by hand

Remove:
Blockchain audit ledger block — no inbound arrows, nothing writes to it, and it was added by a previous architect and survives by inertia
Future ML anomaly detection block — marked dotted, added by a previous architect, and survives by inertia
Duplicate retention DB block — shown once per environment, but the reference model treats it as one logical block
