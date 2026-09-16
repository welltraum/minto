**Key Thought**
The promised 10x acceleration from AI coding agents has not materialized because organizations are applying classical software development lifecycles to probabilistic systems; realizing speed requires shifting from code generation to hypothesis-driven research, redefining roles to combine engineering with ML research, modeling agents as business functions, and positioning humans as the external feedback source and boundary explorers.

**Supporting Arguments**

**1. Process Bottlenecks and Shifts**
*   **Claim:** Classical Agile handoffs and Jira-based bug tracking negate individual speed gains and stall agent development.
    *   **Rests on:** Speed gains (e.g., a developer finishes in two hours, an analyst in half an hour) are lost to transfer time between roles. Agent "bugs" are actually research data for benchmarks; treating them as Jira tickets causes stalls because engineers do not know how to code fixes one by one. Success requires tracking hypotheses via tools like the ML System Design Doc and empowering product engineers who own the full cycle, as T-shaped teams (two or three people covering multiple roles) outperform classical silos where a team may go a month without writing code.
*   **Claim:** Feedback must be automated within the agent loop, not routed to humans.
    *   **Rests on:** A large marketplace recently proposed putting an agent into CI/CD to review code written by coding agents; this is flawed because the review comments go to people who must read them, whereas the information should pass to the coding agents themselves. Humans act as the external correction source (like GPS for an aircraft using cheap instruments) to provide context (e.g., a user just returned from a run and wants cooler underfloor heating than the set 20 degrees), but the internal checks of UI, code, and database should fall on the agent's role.

**2. Role and Skill Requirements**
*   **Claim:** Building agents requires a dual engineering-research capability that classical roles do not provide, forcing a shift in human responsibility.
    *   **Rests on:** Backend developers tend to build custom frameworks for months rather than using agents. NLP engineers get bogged down in plumbing (authorization, integration, database) and miss the agent logic, while product managers misunderstand the blockage. Effective agent creation requires either a "superhuman" with both skill sets or paired roles: one for engineering (integrations, MCP servers, access rights, infrastructure) and one for research (collecting datasets, setting up benchmarks, measuring business metrics). Humans must move from line-by-line code review to managing control points (APIs, database, contracts) because the price of code has dropped to zero and watching every line is impossible.
*   **Claim:** Resistance to change is high and mastery takes time.
    *   **Rests on:** Most users of tools like Cursor default to "auto" mode without understanding the agent. Developers need three to six months to master the technology. Resistance is so large that some international companies proposed banning old IDEs to force learning, though it is unclear if this was run. Juniors struggle to live in this environment as managing agents requires maturity.

**3. Analytical and Design Methodologies**
*   **Claim:** Traditional software specifications fail for agents; analysis must use business-function modeling to define scope and integration.
    *   **Rests on:** Analysts struggle to describe agents using classical methods, leading to confusion where everyone invents their own way. Mapping agents to business functions using IDEF0 clarifies inputs, outputs, and integrations, enabling better client communication and moving teams from zero. This approach also simplifies scope; for example, an agent with a hundred tools was found to do nothing well, and breaking it down by function allowed the team to cut unnecessary tools and simplify the ideology.

**4. Systemic and Security Implications**
*   **Claim:** Agents introduce a new actor that requires agent-to-agent security protocols and a future where humans maintain the agent layer.
    *   **Rests on:** Services are not currently ready for agents as autonomous actors, creating security risks (e.g., a compromised shopping agent interacting with a retailer's MCP server). The 10x acceleration is blocked only by humans finding their new place: maintaining the agent layer (developing UI kits, skills, watching infrastructure to prevent database ballooning or disk exhaustion where an agent might delete its own memory), while agents handle execution. The human role shifts to exploring boundaries and becoming researchers, as code generation becomes like assembler where no one looks at the code anymore.
