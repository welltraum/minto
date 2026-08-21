Add nine blocks and remove three to align with the reference model.

Identity layer is missing an identity provider, service-to-service auth mechanism, and secrets store. State layer needs a message queue and dead-letter store to replace synchronous calls and prevent message loss. Delivery layer needs CI/CD automation and staging environment instead of manual fortnightly deploys. Observability layer needs structured logging and per-message tracing.

Remove the blockchain audit ledger block with no inbound arrows, the future ML anomaly detection block marked dotted, and the duplicate retention database.
