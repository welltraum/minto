**Key Thought**
The promised 10x acceleration in software development has not materialized because organizations are misapplying deterministic, human-centric processes to probabilistic, agent-driven systems; achieving acceleration requires a fundamental shift in team structure, feedback mechanisms, and system design to treat agents as autonomous actors rather than coding assistants, as the primary bottleneck is now human adaptation rather than agent capability.

**Supporting Arguments**

**1. Development Process Must Shift from Handoffs to Autonomous Feedback Loops**
*   **Agile handoffs slow speed:** Classical Agile handoffs between analysts, developers, and product people create waiting time that negates individual speed gains. Teams where everyone works several times faster still stall due to transfer of responsibility.
    *   *Example:* A classical team can go a month without writing code; a product engineer can assemble a mobile app and website in a couple of days.
*   **Rise of Product Engineers and T-shaped teams:** The solution is fewer, broader roles. Product engineers take the whole process from idea to implementation. Large companies are cutting Agile teams down to two or three people who split roles but cover more, enabling speed and uncertainty management.
*   **Feedback is critical for self-correction:** An agent cannot exist without feedback; it needs constant checks on code execution, browser behavior, server errors, and user feedback to understand the system and correct itself.
    *   *Analogy:* An aircraft needs expensive gyroscopes for autonomy, but with GPS (an external source), it can use cheap instruments corrected from the outside. The human is the external source providing feedback.
    *   *Example:* Underfloor heating set to 20 degrees is comfortable normally, but after a run, the user wants it cooler; the agent needs this external human information to adjust.
*   **CI/CD must review agents, not humans:** Reviewing developer code with an agent is a flawed paradigm.
    *   *Example:* A large marketplace implemented an agent in CI/CD to review developers writing code with an agent. The flaw is that the agent should pass information to coding agents, not people.
    *   *New Paradigm:* The human sets requirements and looks at results (e.g., unit tests); the agent checks internal quality, UI, code, and database.

**2. Team Roles Must Shift from Coding to Management and Research**
*   **Code cost dropped; focus moves to control points:** A line of code costs nothing now, making line-by-line review impossible. Developers must move to management level, controlling contracts, APIs, and databases.
    *   *Risk:* Juniors struggle to manage agents that "do who knows what"; the manager's position requires maturity to understand under the hood and give commands.
*   **Agent development requires dual roles:** One role is insufficient. An agent consists of engineering (integrations, MCP, access rights) and research (datasets, benchmarks, business metrics).
    *   *Example:* Backend developers build their own frameworks for months instead of using open-source tools.
    *   *Example:* An NLP engineer paired with a product manager did all the plumbing (authorization, integration, database) while the manager expected the agent to appear; the agent was missing.
    *   *Conclusion:* You need a "superhuman" with both skills, or two roles (Engineering + Research).
*   **Analysts must use IDEF0, not classical specs:** Analysts struggle to describe agents classically. Mapping agents to business functions using IDEF0 methodology clarifies scope and communication.
    *   *Example:* An agent with 100 tools could do everything but nothing well; breaking it down by business functions revealed bloat, allowing the team to cut unnecessary tools and simplify the ideology.
    *   *Benefit:* Talking about business functions makes it easier to communicate with clients and teams, moving them from zero to starting.

**3. Evaluation and Design Must Accommodate Probabilistic Systems**
*   **Sprints include hypotheses, not just features:** Developing agents introduces a research cycle. Sprints contain experiments and hypotheses alongside features.
    *   *Pain:* Jira is convenient for humans but not for agents; errors in Jira are data for research, not bugs to code one-by-one.
    *   *Solution:* Teams must measure business metrics and talk to clients in the language of hypotheses ("We will test this many hypotheses; some will work, some won't").
*   **ML System Design Doc is essential:** This tool records experiments, tracks work, and shows the client why decisions were made, requiring a culture of keeping the document.
*   **Services must be designed for agents, not just humans:** Agents are new actors connecting to services, other agents, and the outside world via tools. Services are not ready for this.
    *   *Requirements:* New entry points, different interaction models, and security for agent-to-agent communication.
    *   *Risk:* If a user's shopping agent is compromised via an MCP server from a retailer, services must defend the user.
    *   *Trend:* OpenAI discusses "harness" to automate everything for agents; services must be built for the agent.

**4. Tooling Requires Configuration and Autonomy**
*   **Default modes are insufficient:** Most users use Cursor's "auto" mode blindly without understanding the tool.
    *   *Requirement:* Agents must be configured properly using Plan/Act approaches, MCP servers, and skills.
*   **Mastery takes time and resistance is high:** Developers need three to six months to master AI tools.
    *   *Example:* Some international companies proposed banning the old IDE to force learning, facing large resistance.
*   **Maintenance is required:** Agents consume resources and can act unpredictably.
    *   *Example:* A product owner deployed an open-source assistant that ran out of disk space and deleted its own memory and skills to clean up; this requires human monitoring.
*   **Future role of humans:** Humans will maintain the "agent layer" (UI kits, skills, infrastructure monitoring) while agents handle development and experiments. The human role shifts to exploring boundaries and research.
    *   *Analogy:* Like assembler, code goes in and no one looks at it; humans become researchers maintaining the layer.
    *   *Conclusion:* The only thing standing in the way of 10x acceleration is the human; agents already cope well.
