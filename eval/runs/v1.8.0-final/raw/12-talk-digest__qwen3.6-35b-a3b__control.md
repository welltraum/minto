**Key Thought**
The promised 10x acceleration from AI coding agents has not materialized because organizations are applying classical software development lifecycle (SDLC) rules to probabilistic agent systems. The primary bottleneck is now human adaptation; agents are capable, but the process, roles, and architecture must fundamentally shift from code-centric management to agent-centric governance, research-driven development, and new security models.

**Process and Workflow**
*   **Claim:** Classical Agile handoffs and task-based workflows negate speed gains and stall progress.
    *   **Rests on:** When every role works faster with agents, handoff waiting times dominate the cycle. Teams revert to Jira and requirements writing because it is familiar, which hinders actual development. Product engineers (T-shaped, full ownership from idea to implementation) achieve incredible speed, whereas classical teams stall.
*   **Claim:** Development must incorporate a research cycle for experiments and hypotheses.
    *   **Rests on:** Agent errors are not standard bugs; they are data for improving evaluation and benchmarks. Jira is ill-suited for this. Sprints must include experiments and hypotheses. The ML System Design Doc is essential for recording experiments, measuring business metrics, and communicating progress to clients.

**Roles and Skills**
*   **Claim:** Agent development requires a dual role structure (Engineering + Research), not just coding skills.
    *   **Rests on:** Backend developers tend to build frameworks instead of solutions. NLP engineers often get bogged down in plumbing. Agents have two sides: engineering (integrations, MCP, infrastructure, access rights) and research (datasets, benchmarks, metrics). One person needs both capabilities, or two people are required.
*   **Claim:** The path for junior developers is unclear; agents require management maturity.
    *   **Rests on:** The price of code has dropped, making line-by-line review impossible. Humans must manage agents, which requires understanding what happens under the hood. Juniors lack this maturity, and it is an open question how they can effectively manage agents that "do who knows what."

**Analysis and Design**
*   **Claim:** Analysis must map agents to business functions, not code descriptions.
    *   **Rests on:** Analysts struggle to describe agents using classical methods. Using IDEF0 methodology to map agents to business functions clarifies inputs, outputs, and control points for both clients and teams. This approach simplifies agents by identifying unnecessary tools and moves teams off dead starts.

**Architecture and Control**
*   **Claim:** Humans must manage control points and feedback loops, not code.
    *   **Rests on:** Developers can no longer watch line-by-line what agents generate. Humans must hold control over critical points: contracts, APIs, and the database. Agents need external feedback (like GPS correcting an aircraft) to self-correct; this feedback must come from unit tests, browser checks, and user errors. Agent reviews should be agent-to-agent, not agent-to-human.
*   **Claim:** Services and security models must evolve to treat agents as new actors.
    *   **Rests on:** Agents connect to services and other agents via tools (e.g., MCP). Services are not ready for this actor. New security risks exist (e.g., compromised user agents). Services need new entry points and security measures designed for agent interaction, not just human users.
*   **Claim:** Tool usage requires configuration and training; "auto" mode is insufficient.
    *   **Rests on:** Most users default to "auto" mode without understanding the tool. One tool is not enough; agents must be configured (Plan/Act, MCP servers, skills). Developers need three to six months to master these tools, and resistance is high.
