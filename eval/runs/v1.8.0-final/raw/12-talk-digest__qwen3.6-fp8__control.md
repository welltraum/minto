**Key Thought**
The promised 10x acceleration from AI coding agents has not materialized because teams are applying deterministic software development processes to probabilistic systems; achieving acceleration requires adopting a hybrid engineering-research workflow, restructuring teams into T-shaped product engineers, and redefining the human role as a manager of boundaries and feedback rather than a reviewer of code.

**What It Rests On**

**1. Workflow must shift from classical Agile to a research-integrated cycle**
*   **Handoffs kill speed:** Classical Agile handoffs negate speed gains; teams using Product Engineers (who handle idea to implementation) or T-shaped teams (2–3 people covering multiple roles) deliver significantly faster.
*   **Errors are research data:** Agent errors represent data for improvement, not bugs to fix one-by-one. Development must include hypothesis testing and benchmarking. Jira is ill-suited for agent errors; teams must track experiments and hypotheses.
*   **Feedback is mandatory:** Agents require continuous feedback (unit tests, browser checks, error logs) to self-correct; without this, they cannot function.
*   **Documentation aligns progress:** ML System Design Docs are essential for tracking experiments, aligning clients on hypothesis-based progress, and documenting decisions.

**2. Agent development demands a dual skill set (Engineering + Research)**
*   **Single roles fail:** Backend developers waste months building frameworks; NLP engineers get bogged down in plumbing and misalignment with product goals.
*   **Hybrid skills required:** Successful agent creation requires combining infrastructure/integration skills (MCP, access rights, deployment) with dataset collection, benchmarking, and metric analysis.
*   **Business function mapping:** Analysts should use IDEF0 methodology to define agents as business functions, enabling clearer communication and scope control (e.g., cutting bloat from an agent with 100 tools that did nothing well).

**3. Human role shifts to boundary management and external feedback**
*   **Control points:** Line-by-line code review is impossible due to generation volume; humans must control critical points (APIs, contracts, database schemas) while allowing agents autonomy elsewhere.
*   **External feedback source:** Humans act as the external feedback source (like GPS for an aircraft or adjusting underfloor heating based on post-run comfort), providing context and corrections that agents cannot infer.
*   **Maturity and learning curve:** Junior developers face a steep learning curve (3–6 months); managing agents requires maturity to understand underlying mechanics. The industry is moving toward an "assembler" model where code is generated without human inspection.

**4. Tooling and architecture must adapt to agents as autonomous actors**
*   **Agent-to-agent review:** Automated code review by agents should target other agents, not humans. A large marketplace's attempt to use an agent in CI/CD to review human code was flawed because it piled comments on developers instead of feeding back to the coding agent.
*   **Services for agents:** Services must be designed for agent interaction (security, MCP servers), as agents are a new actor with distinct access and safety requirements.
*   **Infrastructure oversight:** Infrastructure risks (e.g., an agent consuming disk space and deleting its own memory/skills) require human oversight to maintain system stability.
