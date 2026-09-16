**Key Thought**

The promised 10x acceleration from AI coding agents has not materialized because organizations are misapplying deterministic development processes to probabilistic agent systems; achieving acceleration requires shifting from code-level management to managing control points and feedback loops, adopting dual engineering-research roles, treating agents as new actors, and transitioning to hypothesis-driven workflows.

**Supporting Claims**

**1. Classical Agile processes slow development due to handoffs and mismatched workflows; teams must adopt product-engineer models and hypothesis-driven tracking.**
*   **Rests on:** Speaker observed teams stalling when using Jira to log agent errors as bugs; handoffs between analysts, developers, and product people create waiting time even when individual tasks are faster; product engineers (T-shaped, small teams) build apps in days versus classical teams taking months; Jira is convenient for humans but not agents; the ML System Design Doc is required to record experiments, track hypotheses, and communicate progress to clients in a research context.

**2. Agent development requires dual roles combining engineering and research; single classical roles are insufficient.**
*   **Rests on:** Backend developers tend to build custom frameworks rather than agents; NLP engineers get bogged down in plumbing and integration work; agents are probabilistic systems requiring dataset collection, benchmarking, and metric development alongside engineering tasks; speaker found one person with both skill sets is rare, necessitating two roles or a "superhuman" individual.

**3. Technical management must shift from line-by-line code review to controlling critical interfaces and establishing feedback loops.**
*   **Rests on:** The price of code has dropped, making line-by-line review impossible with agents generating endless code; control points (APIs, database, contracts) must remain human-controlled to maintain accountability; agents require constant feedback (unit tests, execution results, browser/server status) to self-correct, analogous to aircraft feedback systems; the human acts as an external correction source (like GPS) to guide the agent; the speaker cites a large marketplace example where an agent reviewing code in CI/CD was flawed because feedback should go to coding agents, not humans.

**4. Agents function as new actors requiring agent-centric services and new analysis methods.**
*   **Rests on:** Agents connect to services, other agents, and tools, but services are not designed for this actor; security risks arise if an agent is compromised or interacts maliciously with MCP servers; analysts struggle to describe agents using classical requirements; the IDEF0 methodology successfully maps agent business functions, distinguishes control points from integrations, and helps simplify scope by identifying unnecessary tools.

**5. Adoption faces significant human resistance and learning curves; acceleration is currently blocked by human adaptation.**
*   **Rests on:** Users default to "auto" mode in tools like Cursor without understanding configuration; mastery takes three to six months; resistance to switching from old IDEs is large; junior developers struggle to manage agents due to lack of maturity; the speaker concludes that agents cope well, but the human is the bottleneck, requiring a shift to maintaining the agent layer, exploring boundaries, and managing infrastructure (e.g., disk/memory usage).
