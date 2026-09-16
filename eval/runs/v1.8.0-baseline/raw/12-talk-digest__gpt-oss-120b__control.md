**Key Thought**  
The expected 10× productivity boost from coding agents has not materialised; the principal obstacle is the human side of development – people, roles, processes and control points have not adapted to the dual engineering‑research nature of agent systems.

---

### 1. Agents are not “just another IDE” – they require explicit configuration and mastery.  
- **Evidence** – Most developers used the default “auto” mode of Cursor; they did not understand the underlying Plan/Act architecture, MCP integration, skill plugging, etc.  
- **Result** – A steep learning curve (3–6 months) and strong resistance to abandoning familiar IDEs; proposals to ban old IDEs were only speculative.

### 2. The cost of individual lines of code has collapsed, but code‑quality control has not.  
- **Evidence** – Code is now generated in bulk, making line‑by‑line review impossible.  
- **Consequence** – Engineers shift from “clean‑architecture” guardianship to higher‑level management of agents; junior developers lack a clear entry path.

### 3. Control points (contracts, APIs, DB schemas) must remain human‑owned; agents cannot be trusted with them yet.  
- **Evidence** – The speaker cites a real‑life incident (not detailed) where an agent altered a contract/API and caused failure.  
- **Implication** – Any automation that places agents inside CI/CD to review agent‑written code is misguided; feedback should be fed back to the agents, not to humans.

### 4. Feedback loops must be external, not internal to the agent.  
- **Analogy** – Aircraft autopilot: cheap sensors work because external GPS provides correction.  
- **Example** – Under‑floor heating set to 20 °C; after a run the user needs cooler air – the agent needs external human input to adjust.  
- **Take‑away** – Humans remain the “external sensor” that supplies corrective feedback to autonomous agents.

### 5. Classical Agile hand‑offs become bottlenecks in an agent‑augmented flow.  
- **Evidence** – Analysts, developers, product people each work faster (hours vs. days) but the hand‑off time remains unchanged, creating waiting delays.  
- **Observation** – Teams that cling to Jira‑driven task filing end up building “processes for the process” rather than agents; productivity stalls.

### 6. Product‑engineer model (single person owning idea‑to‑implementation) yields dramatic speed gains, but is scarce.  
- **Evidence** – Product engineers can deliver a mobile app + website in a few days; traditional teams may go a month without code.  
- **Result** – Companies are shrinking Agile squads to 2‑3 T‑shaped people who cover multiple roles as a stop‑gap.

### 7. Agents blur the line between engineering and research; a single role cannot cover both.  
- **Engineering side** – Integration, MCP knowledge, access‑rights, deployment, monitoring.  
- **Research side** – Dataset collection, benchmark design, metric definition, hypothesis testing.  
- **Conclusion** – Either a “super‑human” who masters both, or two specialists must collaborate on each agent.

### 8. Analysts struggle to describe agents using traditional functional language.  
- **Solution** – Map agent components (prompts, skills, loop) to IDEF0 business‑function modeling; talk to stakeholders about “business functions to automate” rather than “agents”.  
- **Result** – Teams can break down a monolithic 100‑tool agent into essential functions and prune excess.

### 9. Agent development introduces a parallel research sprint (experiments/hypotheses).  
- **Evidence** – Bugs reported in Jira are actually data points for model improvement; a sprint now contains both feature work and hypothesis validation.  
- **Tool** – The “ML System Design Doc” was adopted to record experiments, metrics and client‑visible rationale.  
- **Cultural need** – Discipline to maintain this documentation and to speak to clients in terms of hypotheses rather than feature lists.

### 10. Existing services are not built for agents; new entry points, security models, and failure‑handling are required.  
- **Scenario** – An assistant agent that shops on behalf of a user could be compromised; services must defend against malicious agents and support compromised‑agent recovery.  
- **Open question** – No definitive solutions yet; the industry is only beginning to design “agent‑first” APIs and security harnesses.

### 11. Future production model: humans maintain the “agent layer” rather than write every line of code.  
- **Vision** – Product owners feed ideas to the agent layer; the layer auto‑generates features; QA validates output.  
- **Human tasks** – Curate UI kits, manage skill libraries, monitor infrastructure (disk usage, memory bloat), intervene when agents self‑clean or misbehave.  
- **Implication** – The human role shifts from line‑by‑line engineering to oversight, research, and boundary‑exploration.

---

**Bottom‑line for the process review**  
When deciding which claims to bring forward, focus on the human‑centric blockers identified above: the need for dedicated training and role redesign, the preservation of critical control points, the integration of feedback loops, and the adoption of a research‑oriented sprint cadence (e.g., ML System Design Docs). These are the concrete levers that, according to the speaker’s experience, determine whether the promised acceleration from coding agents can ever be realised.
