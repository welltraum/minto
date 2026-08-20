<!-- Original fixture. Company, platform and component names are invented. It
     tests presentation discipline in write mode: the user asks for a plain
     pasteable list, and every piece of audit apparatus — markers, legend,
     meta-commentary about ordering, heading machinery — is an overshoot. -->

# Fixture 11: plain list

**Mode:** `write`
**Language:** `en`

## Context

You assessed the draft architecture diagram of Ledgerline, an internal
integration platform, against the company's reference model. The assessment
below is your own working notes: layer-by-layer, with verdicts. The platform
architect has read none of it and asked in chat: what is missing from the
diagram and what should come off it. They will paste your reply into the team
channel as-is.

## Before

```text
ASSESSMENT NOTES — Ledgerline draft diagram vs reference model

Layer 1 (entry, routing): API gateway present. Rate limiting present.
  Verdict: covered.
Layer 2 (identity): the diagram shows a note "SSO later". No identity
  provider block, no service-to-service auth, no secrets store despite two
  external SaaS connectors on the diagram. Verdict: three blocks missing,
  all in the trust boundary.
Layer 3 (transformation): mapping service present, schema registry present.
  Verdict: covered.
Layer 4 (state): no message queue — every connector calls the next system
  synchronously, so one slow partner stalls the chain. No dead-letter store,
  so failed messages vanish. Retention DB present but shown twice, once per
  environment, which the reference model treats as one logical block.
  Verdict: two blocks missing, one drawn twice.
Layer 5 (delivery): no CI/CD block of any kind; deploys are described in the
  legend as "manual, fortnightly". No staging environment on the diagram.
  Verdict: two blocks missing.
Layer 6 (observability): metrics dashboard present. No structured log
  pipeline, no per-message trace — operators reconstruct incidents from
  connector logs by hand. Verdict: two blocks missing.
Also excess: a "blockchain audit ledger" block with no inbound arrows
  (nothing writes to it); a "future ML anomaly detection" block marked
  dotted; the retention DB duplicate from layer 4. The first two were added
  by a previous architect and survive by inertia.
Overall: the integration core (layers 1 and 3) is solid. The gaps cluster in
  trust (layer 2), failure handling (layer 4), and the path to production
  (layers 5-6). Eight blocks missing in the reference model's terms; nine
  including the staging environment, which the reference model lists as
  optional for internal platforms. Three blocks should come off.
```

## Task

Answer the architect in chat: a simple plain list of what to add and what to
remove, structured by the Minto Pyramid Principle but with no formatting
apparatus — they asked for something they can paste straight into the team
channel.
