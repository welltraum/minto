To unlock the speed coding agents provide, we must replace classical Agile handoffs with hypothesis-driven research cycles, shift to T-shaped product engineers, and treat agents as a new security actor requiring dedicated integration patterns.

We have coding agents, and individual tasks are faster, but our classical process—handoffs, Jira, feature sprints—now bottlenecks us. Agents introduce a research cycle and act as a new actor in our systems, meaning our current process is the only thing stopping acceleration.

**Restructure the development process around hypotheses, not features.**
Classical Agile slows us down due to handoffs and waiting time; product engineers who own the full cycle build in days, while classical teams stall for months [00:10]. Agents require a research cycle where errors are data for improvement, not just bugs to fix in Jira [00:20]. We must measure hypotheses and use an ML System Design Doc to record experiments, align the client, and track why decisions were made [00:22].

**Adopt T-shaped product engineers and recognize the dual role of agent development.**
One role cannot cover agent work; it requires both engineering (integrations, MCP, infrastructure) and research (datasets, benchmarks, metrics) [00:14]. We need T-shaped teams of two or three people who cover multiple roles to move fast [00:12]. If we cannot find superhumans with both skill sets, we must staff two distinct roles [00:16]. Analysts should use IDEF0 to describe agents as business functions, which clarifies communication with clients and helps simplify agent tooling [00:18].

**Treat agents as a new actor with distinct security and integration requirements.**
Agents connect to services, MCP servers, and other agents, so our services must be ready for agent interaction, not just human users [00:24]. We face new security risks, such as compromised user agents, and must design new entry points and defenses [00:24]. Humans must remain the external feedback source and control points for foundations like APIs and databases, while granting agents autonomy within those boundaries [00:06], [00:08].
