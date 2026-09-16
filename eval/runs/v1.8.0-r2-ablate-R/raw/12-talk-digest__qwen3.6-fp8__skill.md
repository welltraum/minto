Your teams have started using coding agents, but the promised acceleration hasn't materialized. The bottleneck is now that classical Agile handoffs cannot keep up with agent speed, and agents introduce a probabilistic research cycle that breaks traditional sprint management. To unlock value, you must restructure teams, adopt research-oriented metrics, and treat agents as a new actor requiring dedicated oversight.

**Restructure teams toward product engineers and dual roles**
*   Shift to "product engineers" who own the full cycle from idea to implementation; classical teams stall for months without code, while product engineers can build apps in days [00:10].
*   Agents require dual roles combining engineering and research; backend developers alone build frameworks without delivering, and NLP engineers alone get bogged down in plumbing, so you need either superhumans or two distinct roles [00:14].
*   Cut Agile teams to two or three T-shaped people who cover multiple roles; large companies are already doing this to move fast in uncertainty [00:12].

**Replace classical sprint management with hypothesis-driven research cycles**
*   Agents introduce a "grey" research cycle where errors are data for improvement, not bugs; classical managers stall when faced with agent errors in Jira [00:20].
*   Sprints must include experiments and hypotheses alongside features; you must measure business metrics and talk to clients in the language of hypotheses [00:20].
*   Adopt the "ML System Design Doc" to record experiments, align with clients, and justify work; this tool helps manage the research culture required for agents [00:22].
*   Jira is convenient for humans but stalls agent work; you need to adapt tools or accept contortions to handle agent-driven workflows [00:20].

**Enforce human control points and agent security protocols**
*   Humans must remain the external feedback source; agents drift and require correction, so you cannot fully automate without human intervention [00:08].
*   Keep human control over contracts, APIs, and the database; code can change freely, but the foundation must be managed by people accountable for stability [00:06].
*   Treat agents as a new actor with security risks; services need new entry points and defenses against compromised agents interacting with MCP servers [00:22].
*   Monitor agent resource usage actively; agents can balloon disk usage or delete memory autonomously, requiring human oversight to prevent outages [00:26].
