To capture acceleration and manage risks, shift from code review to control points, adopt T-shaped product engineers, and treat agent development as a research cycle.

Your teams have adopted coding agents, but the speaker warns that classical processes now block the promised acceleration and fail for probabilistic agent systems. The market ran into problems because developers resist losing code visibility, Agile handoffs create waiting time, and agent errors are treated as bugs rather than research data. The speaker's experience shows that the only barrier to 10x acceleration is human process inertia.

**Shift from code review to control points and feedback loops**
Stop line-by-line review; it is impossible with agents. Focus on control points (APIs, DB, contracts) where humans retain accountability. Implement feedback loops where the human acts as an external correction source to guide the agent. [00:04, 00:06, 00:08]

**Adopt T-shaped product engineers to eliminate handoff delays**
Classical Agile handoffs slow down agent-assisted work. Move to T-shaped, 2–3 person teams or "product engineers" who own the full stack. This reduces waiting time and leverages the speed of individuals who can build features in days rather than months. [00:10, 00:12]

**Treat agent development as a research cycle using ML System Design Docs**
Agent systems require both engineering and research (benchmarks, metrics). Jira is unsuitable for research cycles. Use ML System Design Docs to track experiments and hypotheses, as agent errors are data for improvement, not bugs. [00:14, 00:16, 00:20, 00:22]

**Define new roles and security for agents as autonomous actors**
Agents are new actors; services must be built for them. Plan for security risks in agent-to-agent interactions. Humans will shift to maintaining the "agent layer" (skills, infrastructure, memory) while QA ensures quality. [00:24, 00:26]
