## Key thought

The speaker’s central claim is that coding agents will not produce major speed gains merely by adding them to today’s SDLC. Gains depend on redesigning the process around agent autonomy, fast feedback, human control of critical boundaries, and a distinct research cycle for probabilistic systems.

The talk is experiential, not proof: it reports observations from the speaker’s consultancy and illustrative cases rather than comparative data.

## What this rests on

### 1. Classical delivery processes become the constraint

- Giving every developer Cursor did not change behaviour by itself: most used the default “auto” mode. The speaker estimates that learning to work effectively with agents takes three to six months.
- Agents make producing code cheap, but make line-by-line human review unrealistic. The proposed response is to move people upward—from authoring and inspecting code to directing agents and judging outcomes.
- Humans should retain control over high-accountability interfaces: contracts, APIs, and databases. Everything else can be delegated more freely.
- If agents generate code, agent review should feed back to the coding agent, not create another stream of comments for people to process.
- Unit tests, browser/server signals, and user-error data become essential feedback loops. Humans remain the external source of context and correction, while agents need substantial autonomy.
- Faster individual roles can make handoffs more visible and costly. The speaker argues that conventional Agile workflows and Jira tasking can preserve waiting and encourage familiar administrative work instead of progress.

### 2. Faster teams need broader ownership, not narrower roles

- The speaker contrasts a conventional team that can spend a month without writing code with a strong “product engineer” who can ship a mobile app and website in days.
- Because such people are scarce, the suggested interim model is small, T-shaped teams—two or three people covering more roles—rather than fully separated Agile functions.
- This is presented as a practical response to uncertainty, not as a proven ideal operating model.
- An unresolved consequence is junior development: effective agent management requires enough technical maturity to understand what is being delegated.

### 3. Agent systems require both engineering and research disciplines

- An agent system has an engineering side: integrations, MCP, deployment, infrastructure, and agent access rights.
- It also has a research side: representative datasets, benchmarks, evaluation, business metrics, and experiments. The speaker says neither a conventional backend engineer nor an NLP specialist covering infrastructure alone is sufficient.
- Therefore an agent effort needs either a person with both capabilities or a partnership between engineering and research roles.
- Treating poor agent answers as ordinary Jira bugs causes teams to stall. The claimed better model is an embedded experiment loop: collect failures, build benchmarks, test hypotheses, and improve against metrics.
- A sprint may therefore contain hypotheses and experiments as well as features. Clients need to be aligned on this uncertainty and shown what was tested, what worked, and what did not.
- The speaker found the ML System Design Doc useful for recording experiments and decisions, provided the team has the discipline to maintain it.

## Design implications for agent products

- Describe agents as business functions to automate, rather than starting with vague labels such as “an analyst agent.” The speaker says IDEF0 helped analysts, clients, and teams align on inputs, outputs, controls, and integrations.
- Keep agents focused. In one case, an agent with roughly 100 tools did many things poorly; decomposing it into functions exposed unnecessary scope.
- Treat the agent as a new system actor, not simply another user. Services may need agent-facing entry points, different authorization models, and defences for compromised user agents.
- The talk offers security questions—such as a shopping agent interacting with a retailer’s MCP server—rather than answers.

## Claims most worth testing in the process review

1. Are handoffs and role boundaries now a larger delivery constraint than coding throughput?
2. Which boundaries—especially API, database, contract, and security changes—must remain under explicit human approval?
3. Do coding agents receive continuous, machine-consumable feedback from tests, runtime signals, browser checks, and user failures?
4. For agent features, do we run a measurable experiment/evaluation loop rather than create one Jira issue per failed query?
5. Does each agent initiative have ownership for both engineering integration and research/evaluation?
6. Are we designing services, permissions, monitoring, and recovery paths for agents as independent actors?