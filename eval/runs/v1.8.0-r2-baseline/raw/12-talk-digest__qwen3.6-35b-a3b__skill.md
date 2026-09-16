Your teams have started using coding agents this year. The speaker's year of experience shows that classical Agile, Jira, and single-role teams break down or slow down, creating a gap between speed and control, and introducing new security risks. What process changes are required? We must adapt workflows for research cycles, split roles to cover engineering and probabilistic management, and treat agents as first-class actors requiring dedicated security and integration.

**Adapt workflows to accommodate research cycles and reduce handoffs.**
*   Classical Agile slows speed due to handoffs between roles; while individual roles work faster, transfer time remains a bottleneck [00:10].
*   Shift toward "product engineers" or T-shaped small teams (2–3 people) who cover multiple roles and build end-to-end, avoiding the month-long cycles of classical teams [00:10, 00:12].
*   Jira is convenient for humans but stalls agent development; agent errors represent data for research, not bugs to fix one-by-one [00:20].
*   Introduce ML System Design Docs to record experiments, hypotheses, and business metrics, allowing clients to see research progress and agree on scope [00:22].
*   Measure progress in hypotheses tested rather than features delivered, and communicate with clients in the language of hypotheses [00:22].

**Redefine roles to cover both engineering and probabilistic system management.**
*   A single role cannot cover both the engineering side (integrations, MCP, access rights) and the research side (datasets, benchmarks, metrics); one role is insufficient [00:14].
*   Need either a "superhuman" with both skill sets or two distinct roles; backend developers tend to build frameworks rather than agents, and NLP engineers get bogged down in plumbing [00:14].
*   Junior developers struggle to enter this model; the role requires maturity to manage agents and understand under-the-hood mechanics [00:04, 00:26].
*   Human role shifts to maintaining the agent layer, defining UI kits and skills, monitoring infrastructure (e.g., disk usage), and QA, while product owners inject ideas [00:26].

**Treat agents as first-class actors with dedicated security and integration protocols.**
*   Agents are a new actor connecting to services, other agents, and tools; existing services are not ready for this interaction [00:24].
*   Security risks emerge: compromised user agents interacting with retailer MCP servers require new defense strategies [00:24].
*   Services must be designed for agents, not just humans, including new entry points and interaction patterns [00:24].
*   Humans must retain control over critical "control points" (APIs, database contracts) while allowing agents autonomy in the code layer [00:06].
*   Feedback loops are essential; humans act as the external correction source to guide probabilistic systems [00:08, 00:10].
