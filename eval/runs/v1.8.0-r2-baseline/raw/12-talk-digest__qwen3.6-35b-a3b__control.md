**Key Thought**
The speaker claims that the promised 10x development acceleration has not materialized because organizations are misapplying classical software development processes to probabilistic agent systems. The primary bottleneck is human adaptation, not agent capability. To realize acceleration, teams must shift from managing code lines to managing control points and research cycles, adopt T-shaped product engineers, treat agents as a new actor requiring dual engineering/research roles, and redesign feedback and security paradigms.

**What the Key Thought Rests On**

*   **Process Misalignment and Workflow Shifts**
    *   **Agile Handoffs Negate Speed:** Classical Agile handoffs between analysts, developers, and product people create waiting time that cancels out individual speed gains. Teams using agents become several times faster, but handoffs remain slow.
    *   **Product Engineers and T-Shaped Teams:** Speed is achieved by "product engineers" who take the whole process from idea to implementation, delivering in days what classical teams take months. Large companies are cutting Agile teams down to two or three T-shaped people who cover multiple roles.
    *   **Ineffective Jira and Bug Tracking:** Jira is convenient for humans but ineffective for agents. Probabilistic agent errors cannot be tracked as classical bugs; teams stall when engineers receive Jira tickets for agent failures.
    *   **Hypothesis-Driven Development:** Agent development introduces a research cycle. Sprints must include experiments and hypotheses, not just features. Teams must measure business metrics and communicate with clients in the language of hypotheses ("We will test X; some will work, some won't").
    *   **ML System Design Doc:** This tool is essential for recording experiments, tracking hypotheses, and maintaining alignment with clients during the research process.

*   **Role Transformation and Skill Requirements**
    *   **Learning Curve and Resistance:** Developers face a 3-6 month learning curve to master AI tools. Resistance is high; some companies have proposed banning old IDEs to force adoption.
    *   **Dual Roles Required:** One role is insufficient. Successful agent development requires two distinct roles:
        *   *Engineering:* Integrations, MCP, infrastructure, deployment, access rights, and security.
        *   *Research:* Datasets, benchmarks, metrics, and business evaluation.
        *   *Superhuman Exception:* A single person with both skill sets can build agents without problems, but such individuals are rare.
    *   **Misallocation of Talent:** Assigning agents to backend developers leads to wasted time building custom frameworks instead of using existing tools. NLP engineers often get bogged down in plumbing (authorization, database work) rather than agent logic.
    *   **Analyst Methodology:** Analysts struggle to describe agents using classical techniques. The speaker recommends using IDEF0 methodology to describe business functions rather than agents. This clarifies scope, improves client communication, and helps cut unnecessary features (e.g., reducing an agent with 100 tools to essential functions).
    *   **Junior Developer Viability:** The speaker questions how junior developers can thrive, as the role shifts to managing agents. A manager's position is now a position of maturity, requiring understanding of what happens under the hood.

*   **Control, Feedback, and Architecture**
    *   **Control Points:** Line-by-line code review is impossible with agents. Humans must retain control over foundational control points: contracts, APIs, and databases. Code can "dance" around these, but losing control of the foundation is unacceptable.
    *   **Feedback Loops:** Agents cannot exist without feedback. They require constant checks on code execution, browser behavior, server errors, and user feedback. Humans act as an external feedback source (analogous to GPS correcting an aircraft's drift).
    *   **Agent-to-Agent Review:** Putting an agent in CI/CD to review human-written agent code is flawed. The paradigm must shift to agent-to-agent review, where the reviewing agent passes information back to the coding agent, not the human.
    *   **Unit Tests:** Unit tests are mandatory. An agent without feedback cannot self-correct.
    *   **Agents as a New Actor:** Agents are a new actor connecting to services, other agents, and the outside world. Services must be designed for agent interaction, not just human users.
    *   **Security Risks:** New security challenges arise, such as compromised agents via MCP servers. Services need new entry points and defense strategies for agent actors.
    *   **Maintenance of Agent Layer:** Agents require human maintenance of the agent layer, including UI kits, skills, and infrastructure monitoring. Agents can cause issues like disk exhaustion or memory deletion if not watched.

*   **Conclusion on Acceleration**
    *   **Human is the Bottleneck:** Agents already cope well with execution. The only thing standing in the way of 10x acceleration is the human.
    *   **Future Role of Humans:** Humans will shift to maintaining the agent layer, managing context, and exploring boundaries. Development and experiments can be automated; humans will tighten constraints and ensure coherence. Code becomes like assembler, where humans manage the layer above it rather than writing every line.
