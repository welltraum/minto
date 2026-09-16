The speaker argues that agent development demands a shift from classical engineering to a hybrid research-engineering model, requiring new team structures, hypothesis-driven workflows, and agent-to-agent feedback loops, or we risk stalled velocity and uncontrolled costs.

We adopted coding agents expecting a tenfold speed boost, but the speaker's experience shows that acceleration is blocked by human resistance, broken classical handoffs, and the probabilistic nature of agents. To move forward, we must treat agent development as a dual engineering-research discipline, restructure teams, and replace classical feedback mechanisms with direct agent-to-agent loops and hypothesis-driven documentation.

**Restructure teams and roles around dualism and product engineering.**
*   Abandon strict Agile handoffs and move to T-shaped, product-engineer-led teams; classical handoffs slow velocity while product engineers can build full apps in days versus months. [00:10], [00:12]
*   Recognize that one role cannot cover agent development; agents require both engineering (integrations, infrastructure) and research (datasets, benchmarks), necessitating either a "superhuman" or two distinct roles. [00:14], [00:16]

**Replace classical workflows with hypothesis-driven documentation and agent-native tools.**
*   Stop using Jira for agent errors; treating agent failures as classical bugs stalls the research cycle, whereas an ML System Design Doc allows recording experiments and tracking hypotheses to the client. [00:20], [00:22]
*   Shift from feature-based sprints to experiment-based sprints; teams must learn to measure business metrics and communicate progress in terms of tested hypotheses rather than completed tickets. [00:22]

**Redesign feedback loops and control points for probabilistic systems.**
*   Implement agent-to-agent feedback rather than human-in-the-loop reviews; an agent reviewing agent code for humans is a waste, and the paradigm must shift to agents checking each other while humans provide external correction like a GPS. [00:06], [00:08]
*   Protect control points (APIs, contracts, database) while allowing code to vary; developers must manage agents at the level of these foundations rather than trying to control generated code line-by-line. [00:04]

**Prepare for agent-specific risks and infrastructure demands.**
*   Treat agents as a new actor requiring service adaptation; agents connect to tools and other agents, creating new security vectors and interaction models that services must support. [00:22]
*   Monitor infrastructure and resource usage actively; agents can autonomously consume resources or delete memory, requiring human oversight to prevent operational failures like disk exhaustion. [00:24]
