Teams have begun adopting coding agents, yet the anticipated tenfold acceleration has not materialized; resistance persists, and classical Agile handoffs now slow progress because agents introduce probabilistic behavior, new security risks, and a research cycle that Jira cannot manage. To capture value, the speaker recommends shifting to T-shaped product engineers, embedding research cycles, and defining explicit human control points, because agents require a dual engineering-research approach and act as a new actor that breaks traditional feedback and security models.

**Restructure teams into T-shaped product engineers.**
*   Classical teams stall for months without code, while product engineers build full apps in days `[00:10]`.
*   Large companies are cutting Agile teams to 2–3 people who cover multiple roles to move fast `[00:10]`.
*   Agents require both engineering and research skills; one role is insufficient, necessitating either a "superhuman" or two distinct roles `[00:16]`.

**Embed research cycles and replace Jira bug-tracking with hypothesis management.**
*   Agent errors are data collection for improvement, not bugs; logging them in Jira stalls teams `[00:20]`.
*   Sprints must include experiments and hypotheses alongside features `[00:20]`.
*   Use the ML System Design Doc to record experiments, track hypotheses, and communicate progress to clients `[00:22]`.

**Define explicit human control points and treat agents as a new security actor.**
*   Humans must manage control points (contracts, APIs, database) while allowing code flexibility `[00:06]`.
*   Agents act as a new actor connecting to services and other agents, requiring new entry points and security models `[00:24]`.
*   Risks include compromised agents and resource exhaustion (e.g., disk full, memory deletion) requiring human oversight `[00:26]`.

**Adopt IDEF0-based design to clarify agent scope and integrations.**
*   Classical analysis fails for agents; IDEF0 maps agent components (prompts, skills, loops, integrations) to business functions `[00:18]`.
*   This approach helped teams move from zero to implementation and simplified over-engineered agents by cutting unnecessary tools `[00:18]`.
