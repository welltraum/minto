The diagram needs to add blocks in three areas and remove three blocks that don't add value.

Add three blocks in the trust boundary: identity provider, service-to-service auth, and secrets store. The diagram shows external SaaS connectors but no way to authenticate or manage credentials.

Add message queue and dead-letter store. Synchronous calls between connectors mean one slow partner stalls the chain; failed messages have no recovery path without a dead-letter store.

Add CI/CD automation, staging environment, structured logging, and per-message tracing. Manual fortnightly deploys with no staging environment are risky; operators currently diagnose incidents by reconstructing them from individual connector logs.

Remove the blockchain audit ledger (nothing feeds into it) and the "future ML anomaly detection" block (not part of the current architecture). Consolidate the retention database — it's shown twice but should be one logical block.
