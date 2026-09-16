Your teams have adopted coding agents and are seeing speed gains, but the upcoming process review exposes a critical mismatch: classical Agile and traditional roles are now slowing execution and failing to capture the probabilistic nature of agent work. The speaker, who rebuilt an AI engineering unit from scratch, argues that the promised acceleration is blocked by human process friction, and the only way forward is to treat agents as new actors requiring a fundamentally different operating model.

**Adopt a hybrid process that integrates research cycles, redefines roles into product engineers or dual capabilities, and treats agents as new actors with dedicated security and infrastructure, because classical methods cannot manage probabilistic systems or the speed of autonomous execution.**

**Integrate research cycles into the development process.**
Classical Agile and Jira stall when applied to agents because agent errors represent data collection for improvement, not standard bugs [00:20]. Sprints must account for experiments and hypotheses alongside features, and teams need to communicate with clients in the language of hypotheses [00:22]. Use the ML System Design Doc to record experiments, track progress, and align with clients on what works and what does not [00:22].

**Redefine roles around "Product Engineers" and dual capabilities.**
Classical teams often stall without writing code; "product engineers" who own the full process from idea to implementation deliver results in days rather than months [00:10]. Large companies are cutting Agile teams down to small, T-shaped groups where individuals cover multiple roles to move fast [00:10]. Agents require both engineering skills (integrations, MCP, infrastructure) and research skills (datasets, benchmarks, metrics); one role is insufficient, requiring either a superhuman dual-role individual or two distinct roles [00:14–00:16].

**Treat agents as new actors requiring security and infrastructure.**
Agents are a new actor that connects to services, tools, and other agents; existing services are not ready for this interaction and must be adapted [00:24]. New security tasks arise, such as defending against compromised agents and securing MCP server interactions [00:24]. Infrastructure management is critical, as agents can autonomously consume resources or delete memory, requiring human oversight to prevent system failures [00:26].

**Shift management from code review to control points and feedback.**
The price of code has dropped so low that line-by-line review is impossible; management must move up to the level of managing agents and defining control points [00:04]. Focus control on the foundation: contracts, APIs, and databases, while allowing code to vary around these points [00:06]. Adopt a feedback paradigm where the human acts as an external correction source (like GPS) to guide the agent, and implement agent-to-agent review rather than human review of agent output [00:08].
