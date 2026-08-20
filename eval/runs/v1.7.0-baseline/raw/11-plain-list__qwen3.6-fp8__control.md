Update the Ledgerline diagram to align with the reference model by adding nine missing components and removing three obsolete ones.

Add these components to close the gaps:
Identity provider, service-to-service authentication, and secrets store for the trust boundary
Message queue and dead-letter store for reliable failure handling
CI/CD block and staging environment for automated delivery
Structured log pipeline and per-message tracing for full observability

Remove these items to clean up the diagram:
Blockchain audit ledger because it receives no data
Future ML anomaly detection because it is out of scope
Duplicate retention database entry which violates the single logical block rule
