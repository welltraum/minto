Agent development requires restructuring teams into dual roles, replacing classical Agile with hypothesis-driven cycles, and treating agents as a new system actor with dedicated security and integration controls.

Teams have adopted coding agents and seen speed gains, but the promised 10x acceleration has stalled due to resistance, broken handoffs, and the probabilistic nature of agents. Classical Agile and role definitions no longer fit. To unlock value, we must restructure teams into dual roles, replace classical Agile with hypothesis-driven cycles, and treat agents as a new system actor with dedicated security and integration controls.

**Restructure roles and team composition.**
- Classical role assignments fail: Backend developers build their own frameworks for months instead of shipping; NLP engineers get stuck on plumbing while product managers misunderstand tasks [00:14].
- A dual role is essential: Agents require both engineering skills (integrations, MCP, access rights) and research skills (datasets, benchmarks, metrics). One person must be a "superhuman," or the team needs two distinct roles [00:16].
- "Product engineers" deliver speed: Individuals who take the whole process from idea to implementation can assemble a mobile app and website in days, whereas a classical team may go a month without code [00:10].
- Teams are shifting to T-shaped structures: Large companies are cutting Agile teams down to two or three people who split roles but cover more ground to move fast in uncertainty [00:10].
- Junior developers face a maturity gap: Managing agents requires understanding what is under the hood; how young developers enter this workflow remains an open question [00:06].

**Adopt hypothesis-driven research cycles and new documentation.**
- Jira breaks the research loop: Logging agent errors as Jira tickets stalls the team because engineers do not know how to code fixes one by one; agent errors are actually data collection for benchmarks [00:20].
- Sprints must include hypotheses: A sprint now contains features plus experiments. Teams must measure business metrics and prove hypotheses to the client, not just deliver features [00:22].
- Use ML System Design Docs: This tool records experiments, shows the client all work, and explains agreements. It is critical for research processes but requires a culture of keeping the document [00:22].
- Shift client communication to hypotheses: The business must accept that "we will test this many hypotheses; something will work, something will not" [00:22].
- Human provides external feedback: Agents drift and need correction. The human acts as the external source (like GPS for an aircraft), feeding back on execution, browser state, and errors so the agent can self-correct [00:08].

**Design services and security for agents as a new system actor.**
- Agents introduce security risks: A compromised user agent could shop via a retailer's MCP server. Services are not ready for this new actor, and we need defenses for compromised agents [00:24].
- Services must be built for agents: The "harness" theme points to automating for agents. Services need new entry points and interaction modes designed for the agent, not just the human [00:24].
- Maintain the agent layer: Agents can balloon disk usage or delete their own memory. A team must maintain the agent layer, develop UI kits, and watch infrastructure to keep the picture coherent [00:26].
- Control points must remain human: While code can dance, contracts, APIs, and databases are foundation points that cannot be entrusted to agents yet [00:06].
