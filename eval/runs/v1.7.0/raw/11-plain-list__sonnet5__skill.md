Add: identity provider, service-to-service auth, secrets store (trust boundary — you have two external SaaS connectors with nothing guarding them), message queue, dead-letter store (one slow partner currently stalls the whole chain, and failures just vanish), CI/CD pipeline, staging environment (deploys are manual/fortnightly right now), structured log pipeline, per-message tracing (incidents get reconstructed by hand from connector logs).

Remove: the duplicate retention DB (same logical block drawn twice across environments), the blockchain audit ledger (nothing writes to it), the future ML anomaly detection block (dotted placeholder, no substance yet).

Core integration layers (gateway, mapping, schema registry) are solid — the work is entirely in trust, failure handling, and the path to production.
