**Key Thought**
The promised 10x acceleration from coding agents is currently unrealized because the bottleneck is human adaptation; successful agent development requires shifting from classical code-centric engineering to a model where humans manage strategic control points and agent layers, integrating research cycles, and adopting product-engineer workflows.

**1. The 10x Promise is Blocked by Human Adaptation**
*   **Claim:** Acceleration is stalled by developer resistance and the need for role maturity; mastery takes 3–6 months, and juniors struggle to manage black-box agents.
*   **Rests on:**
    *   Usage data shows most users default to "auto" mode without understanding the agent, proving one tool is insufficient; proper setup requires Plan/Act approaches and configuration of MCP servers and skills.
    *   Resistance is large; some companies proposed banning old IDEs to force learning, though this is risky.
    *   Developers watch code fiercely for clean architecture, but agents generate endless code, making line-by-line review impossible; this forces a shift to management-level oversight.
    *   Juniors lack the maturity to manage agents effectively; the role requires understanding under-the-hood mechanics to give commands.

**2. Development Processes Must Shift to Product Engineers and Agent-Centric Feedback**
*   **Claim:** Classical Agile handoffs negate agent speed; high-performing "Product Engineers" and T-shaped micro-teams are the effective solution; feedback mechanisms must be agent-centric rather than human-centric.
*   **Rests on:**
    *   Agents work several times faster than humans, but handoff times between analysts, developers, and product people consume the gained time.
    *   Jira and requirements processes fail for agent tasks; teams revert to filing tasks rather than writing agents, stalling progress.
    *   Product engineers who take the whole process (idea to implementation) build apps in days, whereas classical teams may go a month without code; T-shaped teams of 2–3 people are cutting friction.
    *   A large marketplace implemented an agent in CI/CD to review developer code; this is flawed because human review is unnecessary overhead; agent review should feed feedback directly to coding agents.
    *   Feedback loops require human correction; like an aircraft using GPS or a thermostat needing input after a run, the human provides external context the agent lacks.

**3. Agent Creation Requires a Dual Engineering-Research Model**
*   **Claim:** Agents cannot be built by single classical roles; they require simultaneous engineering and research capabilities, managed via specific design artifacts.
*   **Rests on:**
    *   Backend developers tend to build custom frameworks for months rather than using agents; NLP engineers get bogged down in plumbing (authorization, DB) and miss the agent logic.
    *   Agents have a dual nature: engineering (integrations, MCP, access rights) and research (datasets, benchmarks, business metrics).
    *   IDEF0 methodology helps analysts describe agents as business functions, moving teams from zero to actionable designs and simplifying "god agents" with too many tools.
    *   ML System Design Docs are essential for tracking experiments and hypotheses; they allow recording work and explaining to clients why certain experiments succeeded or failed.
    *   Sprints must include experiments and hypotheses, not just features; managers must learn to measure business metrics and talk to clients in terms of hypotheses.

**4. Architecture Must Enforce Human Control Points and Agent-Centric Services**
*   **Claim:** Humans must retain control over foundational contracts and APIs; services must be designed for agents as new actors; humans maintain the agent layer.
*   **Rests on:**
    *   Code can change freely, but control points (APIs, database, contracts) must remain human-controlled to maintain accountability.
    *   Agents are new actors connecting to services, other agents, and tools; services are not ready for this and need new entry points and interaction models.
    *   Security risks arise from compromised agents; retailers releasing MCP servers must defend against agents acting on behalf of users.
    *   Access rights are improvised; a third actor (the agent) requires new infrastructure and deployment considerations.
    *   Humans must maintain the agent layer; an example showed a product owner's agent ballooning disk usage and deleting its own memory, requiring human oversight.
    *   Future roles involve maintaining UI kits, skills, and infrastructure; development and experiments can become automated, but humans explore boundaries and manage the agent layer.
