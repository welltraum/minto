Your teams have started using coding agents this year, but the promised acceleration is stalled because classical Agile handoffs and role definitions clash with how agents work, and agents introduce a research dimension that breaks standard sprint planning. To unlock value and avoid the pitfalls the speaker encountered, we must shift from classical Agile to a model that treats agents as a new actor requiring research cycles, T-shaped product engineers, and explicit control points, while redefining human roles toward boundary exploration and agent-layer maintenance.

**Restructure teams toward T-shaped product engineers and dual-role agent builders.**
*   Classical teams slow down; "product engineers" who take the whole process can build apps in days, not months [00:10].
*   Large companies are cutting Agile teams to two or three T-shaped people [00:10].
*   Agents require two roles simultaneously: engineering (integrations, MCP, infrastructure) and research (datasets, benchmarks, metrics); one person is rare, so you need two or a superhuman [00:14–00:16].
*   Backend devs build frameworks instead of agents; NLP engineers do plumbing; analysts struggle to describe agents without IDEF0 mapping [00:14–00:18].

**Introduce research cycles and hypothesis-based management into the SDLC.**
*   Developing agents creates a "research process" inside the classical scheme; sprints must include experiments and hypotheses, not just features [00:20].
*   Use the ML System Design Doc to record experiments and align with the client on what worked and what didn't [00:22].
*   Adopt a "language of hypotheses" with the business: "We will test this many hypotheses; something will work, something will not" [00:22].
*   Jira is convenient for humans but stalls agent development when errors are logged as bugs; engineers don't know how to code Jira bugs one by one [00:20].

**Establish explicit control points and treat agents as a new actor.**
*   Code cost has dropped, but developers must hold control points: contracts, APIs, and the database; agents can "dance" around these, but losing control here is fatal [00:06].
*   Agents should review agents; feedback loops must fall on the agent's role, with the human outside checking results like unit tests [00:08].
*   Agents are a new actor connecting to services; services need new entry points and security models for agent-to-agent interaction [00:24].
*   A large marketplace tried an agent-in-CD review, but it piles comments on humans unnecessarily; the human is the external source for feedback, like GPS correcting a plane [00:08].

**Shift human work to boundary exploration and agent-layer maintenance.**
*   The only thing blocking 10x acceleration is the human; agents cope well, but humans must find their new place [00:26].
*   Humans become researchers and maintain the "agent layer": developing UI kits, skills, and watching infrastructure (e.g., disk usage, memory) [00:26].
*   Product owners throw ideas into the agent layer; QA still answers for quality, but the main task is maintaining the layer that does the developing [00:26].
*   A product owner's agent ran out of disk and deleted its own memory; this requires human oversight [00:26].
