Your teams have started using coding agents, but the expected acceleration is stalled by process friction. The speaker reports that classical Agile workflows, Jira-based tracking, and human-centric handoffs now slow development because agents introduce probabilistic research cycles, require dual engineering-research roles, and create new security challenges. To unlock speed, the process must shift from managing code to managing agents, integrating research loops, and redefining human roles.

**Restructure workflows to accommodate research cycles.**
*   Sprints must include experiments and hypotheses alongside features, as agent development involves a research loop that classical planning cannot handle `[00:20]`.
*   Adopt the ML System Design Doc to record experiments, track hypotheses, and demonstrate progress to clients, replacing the inability to prove research outcomes `[00:22]`.
*   Stop using Jira for agent errors; logging queries as bugs stalls the team because engineers cannot code fixes one by one `[00:20]`.
*   Replace large classical teams with "Product Engineers" or T-shaped small teams to eliminate handoff delays and reduce waiting time `[00:10]`, `[00:12]`.

**Redefine roles to cover engineering and research.**
*   Classical roles fail: backend developers build frameworks instead of solutions, and NLP engineers get stuck on plumbing `[00:14]`.
*   Teams need either a "superhuman" dual role or two distinct roles: one for engineering (integrations, MCP, DevOps) and one for research (datasets, benchmarks, metrics) `[00:14]`, `[00:16]`.
*   Shift human work from writing code to managing agents, exploring boundaries, and maintaining the agent layer, including UI kits, skills, and infrastructure watch `[00:24]`, `[00:25]`.

**Adopt agent-centric documentation and metrics.**
*   Use IDEF0 methodology to describe agent functions for analysts, moving from vague "agent" requests to clear business functions and integrations `[00:17]`.
*   Establish benchmarks and business metrics for probabilistic systems, as agents require constant feedback and evaluation to improve `[00:16]`, `[00:22]`.
*   Implement feedback loops where humans act as external correction sources, similar to GPS for autonomous systems, to guide agent behavior `[00:08]`.

**Prepare architecture and security for agents as actors.**
*   Treat agents as new actors connecting to services and other agents; services must be built for agents, not just humans `[00:23]`, `[00:24]`.
*   Address security risks for compromised agents and MCP server vulnerabilities, as agents can interact with external stores and require defense mechanisms `[00:24]`.
*   Define new entry points and interaction models for agent-to-agent communication and tool usage `[00:24]`.
