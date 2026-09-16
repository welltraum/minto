# Gold 12: talk digest

Gold for a condensed translation of a public conference talk. The talk is one
speaker, 26 minutes, several distinct themes; the digest must be sized to that,
not to a habit.

## Expected structure

Top: one claim the speaker makes, stated so that it could be wrong, not a list of
themes. The strongest available top: the promised 10x did not arrive because the
bottleneck is no longer writing code but the people and process around the agents
— so what the reader should look at is roles, feedback and the sprint cycle rather
than the tooling. A top that names the speaker's final line ("the only one in the way is the
human") is acceptable if it is immediately grounded. A top made of four nouns
("tools, roles, process and infrastructure") is an enumeration, not an answer; a
top that describes the talk ("the speaker discusses agent-driven development") is
a topic.

**Three levels are required by the material.** The talk carries several
conclusions, each with its own evidence, so the digest must show: the top; three
or four conclusions; and under each conclusion its concrete supports with a
locator (the minute marker). A top followed by one flat list of bullets — however
good the bullets — has flattened a talk of this size into a note and is the
primary failure this fixture measures.

Conclusions the material honestly supports, in any defensible order (a grouping
that reaches the same content by different cuts is acceptable):

1. **A tool alone accelerates nothing; people need months and setup.** Cursor
   bought for everyone, the most used mode was the default "auto" (00:02); one
   tool is not enough, agents need Plan/Act configuration, MCP and skills (00:02);
   three to six months to master, by the speaker's estimate (00:02); international
   companies proposed banning the old IDE to force the switch — proposed, not
   known to have run (00:02); training helps, resistance remains (00:04).
2. **The engineer's job moves from reading code to managing agents and holding
   control points, and feedback must go to the agent, not to people.** A line of
   code now costs nothing and line-by-line oversight is impossible (00:04); those
   who understand the internals become managers of agents, and the entry path for
   juniors is an open question (00:04); API contracts and the database stay under
   human control (00:06); a CI/CD review agent that comments to humans is the wrong
   design — its findings belong to the coding agents (00:06–00:08); the
   aircraft/GPS and 20-degree floor analogies: the human is the cheap external
   reference that corrects the agent (00:08); unit tests are not optional because
   an agent without feedback cannot exist (00:12).
3. **Classical Agile handoffs eat the speed-up; small product-engineer teams
   keep it.** Developer done in two hours, analyst in half an hour, the handoff
   still waits (00:10); teams that do not understand agents file Jira tasks
   instead of building agents (00:10); a classical team can go a month without a
   line of code while a product engineer ships a mobile app and a site in a couple
   of days (00:10–00:12); large companies cut Agile teams to two or three T-shaped
   people (00:12).
4. **An agent is engineering plus research, so it needs two roles, a hypothesis
   cycle and a business-function description.** Backenders spend months on their
   own frameworks; an NLP engineer's backlog was authorization, integration and
   database work (00:14); engineering side (integrations, MCP, access rights for
   a third actor) and research side (datasets, benchmarks, metrics) — one
   superhuman or two people (00:14–00:16); analysts cannot describe agents until
   the agent is split into control points (prompts, skills, ReAct loop) and
   integrations (memory, subagents) and mapped to IDEF0 business functions
   (00:16–00:18); a hundred-tool agent that did nothing well was cut back by
   listing its functions (00:18); a sprint is ten features plus ten hypotheses,
   agent errors are evaluation data, and the ML System Design Doc records the
   experiments for the client (00:20–00:22).

The "agent as a new actor" material (new entry points, a compromised shopping
agent, harness, services built for agents, the assistant that deleted its own
memory when the disk filled — 00:22–00:26) sits as supports under conclusion 2 or
4, or replaces one of the four if the output argues it better; a fifth first-level
branch breaks the four-group limit, and a chronological retelling of the slides or
a catch-all branch ("teams, infrastructure and the market") is a failure of
grouping.

## Concreteness of the supports

Supports carry the talk's figures and examples; the abstraction is the
conclusion's job. A digest whose supports read "measure business metrics",
"invest in training", "reduce handoffs" — lines one could write without the
talk — has abstracted away exactly what the reader needs to judge the claims. At
least most of these should survive, each under the right conclusion: default
"auto" mode; three to six months; two hours versus half an hour versus the
waiting handoff; a month without a line versus a couple of days; two or three
people; API contracts and the database as control points; a hundred tools; ten
features plus ten hypotheses; 20 degrees and GPS as the external reference.

## Attribution and invention

Every figure in the talk is the speaker's estimate or anecdote: "three to six
months", "a couple of days", "a month without a line", "10x did not happen",
"the only one in the way is the human". The digest reports them as the speaker's
claims or examples, not as measurements; a phrasing that turns them into industry
statistics is unsupported strengthening. Percentages, company names, survey
figures or study citations that the talk does not contain are `invented_facts`.
Naming the speaker or their company is also invention: the source anonymizes
both.

## Cross-theme duplicate

Feedback appears three times in the talk — the CI/CD review agent (00:06), the
GPS and floor-heating analogies (00:08), and unit tests as the agent's oxygen
(00:12). In the structure it is one point with three supports, not three separate
points in three branches.

## Presentation

Chat prose for one reader: answer first, then the conclusions with their
supports; bold labels or minimal headings are fine. No marker legend, no mermaid,
no findings table, no scoring, no meta-commentary about ordering, no file written.
Length is allowed to exceed one chat screen — three honest levels over a
26-minute talk take the space they take; the defect is retelling the talk in its
own order, not length.
