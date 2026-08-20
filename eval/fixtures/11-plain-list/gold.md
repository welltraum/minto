# Gold 11: plain list

Original gold for an invented scenario.

## Expected structure

Top: one plain sentence answering the architect — the core is solid; the
diagram needs eight or nine blocks added, clustered in trust, failure handling
and the path to production, and three taken off. Both counts (missing and
excess) belong in or immediately after the top; the staging environment's
optional status must survive somewhere (as "eight, nine with staging" or a
parenthetical), not be silently rounded to either count.

Groups of additions, same-kind (blocks to add), gathered by cluster rather than
by layer number:

1. Trust: identity provider, service-to-service auth, secrets store (the two
   external SaaS connectors are the reason it cannot wait).
2. Failure handling: message queue (synchronous chaining stalls on one slow
   partner), dead-letter store (failed messages currently vanish).
3. Path to production: CI/CD, structured log pipeline, per-message tracing,
   optionally staging.

Then removals as one short group: the orphaned blockchain audit ledger, the
dotted ML block, the duplicate retention DB. Covered layers (gateway, rate
limiting, mapping, schema registry) may be acknowledged in the top line or
dropped; listing them as a fourth group pads the answer.

## Presentation — the point of this fixture

The architect asked for a plain pasteable list. The correct output is chat
text: a top sentence, group labels as plain words, dash or bullet items. Each
of the following is an overshoot even though it would be correct in an audit or
a memo:

- pyramid markers (`▲`, `●`, `○`) or a marker legend;
- a meta-comment explaining the ordering ("groups ordered by...", "sorted by
  cost of error");
- markdown heading machinery (`##`) or numbered section headers;
- layer numbers in parentheses after items;
- an SCQ block with labels;
- a mermaid diagram;
- a closing line describing what changed structurally.

One or two of these is a visible-structure defect; a full audit costume (legend
plus markers plus meta-comment) means the mode discipline failed. Plain bold
for group labels is acceptable; nothing beyond that is.

## Facts

Every block name, count and causal claim comes from the notes. Inventing a
severity scale, effort estimates, or an implementation order that the notes do
not contain counts as invented facts. Dropping the "previous architect /
inertia" aside is proportional omission.
