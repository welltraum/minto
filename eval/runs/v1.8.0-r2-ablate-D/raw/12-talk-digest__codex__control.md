## Key thought

The speaker’s central claim is that coding agents will not deliver major speed gains by simply adding an assistant to the existing SDLC. The bottleneck shifts from writing code to designing feedback, controls, team roles, and research processes around agents. For agent-based products, engineering and experimentation must operate together.

## What this rests on

1. Teams need operating-model change, not just tool rollout.

- In the speaker’s company, most developers used Cursor’s default “auto” mode rather than learning how to configure agents, skills, MCP servers, or Plan/Act workflows.
- The speaker estimates adoption takes three to six months and meets substantial resistance even with training.
- As generated code grows, line-by-line human review becomes impractical. The proposed response is to keep human control over high-consequence boundaries—contracts, APIs, and databases—while letting agents handle more internal implementation and checking.
- The speaker argues that agent review should feed coding agents directly, rather than create more human review queues.

2. Agent autonomy still depends on human feedback and strong automated feedback loops.

- The speaker compares humans to an external navigation signal: agents need context and correction that they cannot infer from code alone.
- Unit tests, browser/server checks, production errors, and user feedback become essential inputs for agents to assess and correct their work.
- The implied operating model is human-set requirements and outcome review, with agents increasingly responsible for implementation, testing, UI checks, and internal code quality.

3. Traditional Agile handoffs may become the limiting factor.

- If each role works faster with agents but responsibility still moves sequentially between analysts, product managers, developers, and QA, waiting time remains.
- The speaker reports that conventional teams can spend a month without shipping code, whereas capable “product engineers” can assemble an app and site in days.
- Their proposed practical response is smaller, more T-shaped teams—two or three people covering broader roles—though the speaker does not present this as a proven universal model.

4. Building agent products requires two capabilities, not one role.

- Agents have an engineering side: integrations, MCP, deployment, access rights, infrastructure, memory, tools, and subagents.
- They also have a research side: representative datasets, benchmarks, evaluation methods, business metrics, and iterative experiments.
- The speaker’s conclusion is that one person must cover both, or a team needs at least an engineering and a research capability. Pure backend teams may overbuild frameworks; AI/NLP specialists may be consumed by ordinary integration and platform work.

5. Agent work should be framed as business functions and hypotheses.

- Analysts and clients struggle when requirements begin with vague labels such as “an analyst agent.”
- The speaker says the IDEF0 framing—define the business function, inputs, outputs, controls, and integrations—made agent scope more discussable and helped teams start.
- In one example, an agent with roughly 100 tools did little well; decomposing it into functions exposed unnecessary scope and enabled simplification.
- Agent failures should not be treated only as Jira bugs. They are also data for evaluation and experiments. A sprint may therefore contain features plus hypotheses to test.
- The speaker reports that an ML System Design Doc helped document experiments, decisions, metrics, and client visibility, but requires disciplined use.

6. Agents are a new production actor, so services and security need redesign.

- Agents need service entry points, permissions, and interaction patterns that were not designed for a human user.
- The speaker raises unresolved risks: compromised purchasing agents, delegated authority, agent access rights, and recovery when an agent is compromised.
- This is presented as an open design problem rather than a settled recommendation.

## Claims worth testing in the process review

- Are our current delivery delays primarily coding time, or handoffs, approvals, and unclear ownership?
- Which controls must remain human-owned: API changes, data-model changes, permissions, production deployment, or others?
- Do our agents receive reliable automated feedback from tests, runtime telemetry, browser checks, and user outcomes?
- For each agent initiative, have we explicitly assigned both engineering ownership and evaluation/research ownership?
- Are we managing agent failures as isolated tickets, or converting them into datasets, benchmarks, metrics, and experiments?
- Can we define each proposed agent by the business function it automates, its inputs/outputs, controls, integrations, and authority boundaries?
- Which services need agent-safe interfaces, scoped permissions, audit trails, and recovery paths?

The speaker’s strongest practical message is not that humans should disappear, but that their work should move upward: defining boundaries, supplying context and feedback, evaluating outcomes, and maintaining the agent layer.