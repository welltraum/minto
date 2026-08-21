Add the missing blocks
  Identity Provider (layer 2 – trust boundary)
  Service‑to‑Service Authentication (layer 2 – trust boundary)
  Secrets Store (layer 2 – trust boundary)
  Message Queue (layer 4 – failure handling)
  Dead‑Letter Store (layer 4 – failure handling)
  CI/CD pipeline (layer 5 – delivery)
  Staging Environment (layer 5 – delivery, optional but recommended)
  Structured Log Pipeline (layer 6 – observability)
  Per‑Message Trace (layer 6 – observability)

Remove the unnecessary blocks
  Blockchain audit ledger block (no inbound connections)
  Future ML anomaly detection block (placeholder, dotted)
  Duplicate Retention DB block (keep a single logical instance)
