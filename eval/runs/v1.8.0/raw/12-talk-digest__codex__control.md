## Key thought

The speaker’s central claim is that coding agents do not automatically create 10× delivery speed. The limiting factor is the surrounding operating model: teams must shift from supervising code line by line to setting boundaries, supplying feedback, running experiments, and designing services that agents can use safely.

This is a practitioner’s view from one consultancy’s first year of building AI teams, supported mostly by internal cases and observations rather than comparative evidence.

## What this rests on

1. **Teams need new skills and controls before coding agents become productive.**  
   The speaker says that simply issuing Cursor subscriptions did not change practice: many people stayed with defaults and needed roughly three to six months to learn agentic development. They argue that teams should retain human control over consequential interfaces—API contracts, database changes, and other accountable decisions—while delegating more routine implementation and review loops to agents.

2. **Speed gains are lost in handoffs and weak feedback loops.**  
   In the speaker’s account, analysts, developers, and product staff may each work faster with agents, yet traditional Agile handoffs still create waiting time. They contrast a classical team that can spend a month without coding with a strong “product engineer” who can assemble an app and website in days. Their proposed response is smaller, more cross-functional teams, stronger testing, and agent-accessible feedback from execution, browsers, servers, and users.

3. **Agent products require both engineering and research work.**  
   The speaker argues an agent is simultaneously an integrated software component and a probabilistic system. Building one therefore requires engineering capabilities—integrations, MCP, infrastructure, access rights—and research capabilities—datasets, benchmarks, evaluation, and business metrics. They say treating poor user queries as individual Jira bugs stalls teams; instead, failures should feed an experiment and evaluation cycle. They found the ML System Design Doc useful for recording hypotheses, experiments, and decisions with clients.

4. **Describe agents as business functions, not vague role labels.**  
   Terms such as “analyst agent” led teams into ambiguity, according to the speaker. Breaking the work into business functions, inputs, outputs, controls, integrations, memory, tools, and agent loops—using IDEF0 as a framing device—helped teams start. In one cited case, this decomposition exposed that an agent with about 100 tools was overbuilt and enabled simplification.

5. **Services must be redesigned for agents as a new actor.**  
   The speaker believes agents will need purpose-built entry points, permissions, security models, and recovery paths. Their example is a shopping agent interacting with a retailer’s MCP server: a compromised agent creates risks current user-centric services may not handle. This is presented as an unresolved design problem, not a solved recommendation.

## Implications worth testing in the process review

- Are our bottlenecks now coding capacity, or handoffs, unclear ownership, and slow feedback?
- Which decisions must remain human-controlled: contracts, schemas, permissions, deployments, spend limits?
- Do agent-enabled initiatives have explicit benchmarks, hypotheses, and business metrics—not just Jira tickets?
- Do we have the paired capabilities needed for agent systems: software/infrastructure engineering and evaluation/research?
- Can teams define an agent by the business function it automates and measure its outcome?
- Which internal services need agent-specific access, observability, safeguards, and incident recovery?

The speaker’s strongest actionable point is not “remove people from development.” It is to move people toward defining outcomes and boundaries, interpreting feedback, and maintaining the environment in which agents operate.