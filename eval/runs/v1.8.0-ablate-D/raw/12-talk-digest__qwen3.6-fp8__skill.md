Teams have adopted coding agents this year expecting rapid acceleration, but the promised 10x gains have not materialized. Classical Agile processes now slow development through handoff delays and role mismatches, while agents introduce probabilistic behavior and new infrastructure risks that traditional engineering roles cannot manage. To move forward, we must restructure our process to treat agents as a new actor requiring research cycles and dual-role teams, because classical Agile and single-role engineering cannot handle the probabilistic nature and integration complexity of agents.

**Restructure teams to combine engineering and research skills.**
- Agents require both infrastructure work (integrations, MCP, access rights) and research work (datasets, benchmarks, metrics); one role cannot cover both, so teams must include dual skills or two people `[00:14]`.
- Adopt T-shaped teams of two to three people who split roles but cover more, as large companies are cutting Agile squads to move fast in uncertainty `[00:12]`.
- Empower product engineers who take the whole process from idea to implementation, as they deliver speed that classical teams cannot match `[00:10]`.

**Shift from feature sprints to research cycles with hypothesis tracking.**
- Replace feature-only sprints with cycles that include experiments and hypotheses, since agent development introduces a research loop where errors are data collection for improvement `[00:20]`.
- Use the ML System Design Doc to record experiments and communicate progress to clients in the language of hypotheses `[00:22]`.
- Stop treating agent errors as standard Jira bugs; recognize them as part of the evaluation loop rather than coding defects `[00:20]`.

**Treat agents as a new actor requiring dedicated integration and security controls.**
- Design services for the agent as a new actor, creating new entry points and interaction models beyond human use `[00:24]`.
- Define access rights and security protocols for the agent as a third actor, including defense against compromised agents interacting with external services `[00:14]`, `[00:24]`.
- Describe agent requirements using IDEF0 business functions and control points (prompts, skills, loops) to align with analyst and client understanding `[00:18]`.
