## Key thought

The speaker’s central claim is that coding agents will not deliver major acceleration through tool rollout alone. The bottleneck shifts to how teams design feedback, controls, roles, and delivery processes around agents—especially for probabilistic agent products.

## What this rests on

1. **Teams need to learn to operate agents, not merely buy them.**  
   In the speaker’s experience, most developers used Cursor’s default “auto” mode; effective use required configuration, MCP/skills knowledge, and roughly 3–6 months of adoption time. Training helps, but resistance remains.

2. **Human control should move from code lines to accountable boundaries and outcomes.**  
   The speaker argues that line-by-line review no longer scales. Humans should retain control over contracts, APIs, databases, requirements, and external feedback, while agents perform implementation and internal checks. Agent-generated review feedback should, where possible, go back to coding agents rather than create more work for people.

3. **Feedback and automated verification become non-negotiable.**  
   Agents need continuous signals—tests, browser/server behavior, production errors, and human correction—to improve and self-correct. The analogy is a control system: autonomy is possible, but outside feedback remains necessary where context is missing.

4. **Classical Agile handoffs can erase local AI productivity gains.**  
   If analysts, developers, and product managers each work faster but still wait on sequential queues and Jira handoffs, end-to-end speed does not improve. The speaker cites “product engineers” who span idea-to-implementation as much faster, and observes teams shrinking toward broader, T-shaped roles.

5. **Agent systems require both engineering and research capabilities.**  
   Building an agent involves conventional engineering—integrations, deployment, permissions, MCP, infrastructure—and research work—datasets, benchmarks, evaluation, and business metrics. The speaker’s position is that one role alone is insufficient unless an individual has both capabilities.

6. **Agent work needs a different specification and management model.**  
   Rather than specify “an analyst agent,” define the business functions to automate, inputs/outputs, controls such as prompts and skills, and integrations such as memory and subagents. The speaker says IDEF0 made this discussion clearer and helped simplify an over-tooled agent with about 100 tools.

7. **Delivery of LLM systems includes an explicit experiment cycle.**  
   User failures are not simply Jira bugs to fix one at a time; they are data for benchmarks and hypotheses. Sprints therefore include experiments as well as features. The speaker found an ML System Design Doc useful for recording experiments, decisions, metrics, and client visibility.

8. **Services must be redesigned for agents as a new actor.**  
   Agents need suitable entry points, permissions, security controls, and recovery paths—especially when an agent acts on a user’s behalf or is compromised. The speaker sees this as an unresolved but unavoidable design problem.

## Implication for the process review

The strongest, most actionable claims to test are:

- Define non-delegable control points: API/contracts, database changes, permissions, and release criteria.
- Strengthen automated feedback: tests, observability, browser/server checks, and production-error loops.
- Reduce role handoffs for agent-enabled work; trial small cross-functional ownership.
- For LLM/agent products, separate feature delivery from experimentation and establish benchmarks and business metrics.
- Assess whether each agent initiative has both engineering and evaluation/research ownership.
- Treat agent access and service interfaces as a security and platform-design concern, not an implementation detail.