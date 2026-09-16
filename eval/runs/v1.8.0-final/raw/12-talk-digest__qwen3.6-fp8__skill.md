We deployed coding agents expecting a tenfold acceleration, but the promised speed did not materialize. The bottleneck is no longer the tool but the process: classical Agile handoffs slow teams down, code review by agents is redundant, and the probabilistic nature of agents introduces a research cycle that standard Jira workflows cannot handle. To unlock speed, we must restructure our development process around these realities.

Building agent systems requires shifting from classical engineering to a hybrid model that integrates research cycles, redefines roles into product engineers or dual-role superhumans, and establishes external human feedback loops, because agents are probabilistic systems that cannot be managed by standard Agile or code-review mechanisms.

**Restructure teams around product engineers and dual-role capabilities.**
*   Shift to product engineers who own idea-to-implementation to avoid classical team stalls and achieve rapid delivery; [00:10]
*   Adopt a "superhuman" profile or pair a backend engineer with an NLP/researcher, as one role cannot cover both engineering and probabilistic system research; [00:14]
*   Train analysts to map business functions using IDEF0 rather than describing agent specs, which enables clear communication with clients and simplifies agent tooling; [00:16]

**Adopt a research-integrated workflow with explicit feedback and documentation.**
*   Introduce a research cycle where sprints include experiments and hypotheses, and measure business metrics alongside features; [00:20]
*   Use an ML System Design Doc to record experiments, track business metrics, and align the client on the research process; [00:22]
*   Implement external human feedback loops where the human corrects agent drift, similar to a GPS correction, rather than relying solely on internal mechanisms; [00:08]
*   Stop using Jira for agent errors and route agent reviews back to coding agents, as Jira stalls the research process and agent review is redundant for humans; [00:06]

**Rethink technical architecture and security for the agent as a new actor.**
*   Treat the agent as a new actor requiring dedicated security, entry points, and services built for agents rather than just humans; [00:24]
*   Maintain strict human control over foundational contracts, APIs, and databases while allowing code to vary, as these are the points of accountability; [00:04]
*   Prepare for agent-to-agent interactions and compromised agents, which introduces new security tasks and requires defense mechanisms; [00:24]
