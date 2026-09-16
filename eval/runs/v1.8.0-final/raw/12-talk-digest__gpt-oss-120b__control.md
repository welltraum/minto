**Key Thought**  
The promised “10 × speed‑up” from coding agents has not materialised. The single biggest barrier is **human – process mismatch**: people, roles, and legacy workflows are not adapted to the way agents actually work. Until the organisation re‑defines control points, feedback loops, and job‑functions around agents, acceleration will stay modest.

---

### 1.  Agents are not “plug‑and‑play” – they need proper set‑up and training  

| Claim | What it rests on |
|------|-------------------|
| Default “auto” mode (e.g., Cursor’s auto setting) is the most used but ineffective. | Teams that simply turned on the auto mode quickly hit limits; they discovered that a **Plan/Act** configuration (defining MCP servers, skills, prompts) is required. |
| Mastery takes 3‑6 months even for eager developers. | Observation of internal onboarding curves; anecdotal reports of companies considering bans on traditional IDEs to force learning. |
| One tool is never enough; a toolbox of agents is required. | Experience assembling a “whole course on agentic development” and still seeing resistance. |

---

### 2.  Loss of code‑level visibility creates resistance and a new managerial layer  

| Claim | Evidence |
|------|----------|
| When agents generate and rewrite code continuously, traditional clean‑architecture checks become impossible. | “I cannot imagine watching line‑by‑line what is happening now… endless pieces of code and fixes.” |
| Managers become the “maturity” gate – they must understand the black‑box to give commands. | Observation that only those who grasp the internals can effectively **manage agents**; junior developers lack a clear path. |
| Trying to police agents with existing CI/CD reviews is flawed. | A large marketplace tried an “agent‑in‑CI that reviews code written by agents” – the speaker argues the review should feed back to the coding agents, not to humans. |

---

### 3.  Preserve human‑controlled **control points** (contracts, APIs, DB)  

| Claim | Evidence |
|------|----------|
| These points are the only places we can safely keep accountability. | “Everything related to changing contracts, APIs, and the database … is the foundation everything stands on.” |
| Agents can safely “dance” around them, but should never own them. | Real‑life example (not fully detailed) where an agent altered a contract and caused breakage. |

---

### 4.  Classical Agile hand‑offs become a new bottleneck  

| Claim | Evidence |
|------|----------|
| Speed gains at the individual level are erased by waiting time between analysts, developers, and product people. | Developers finish in 2 h, analysts in 30 min, but the **handoff** still consumes days. |
| Teams that cling to Jira‑driven tasks (writing requirements, filing bugs) stall agent progress. | “People file tasks in Jira… but not writing agents. That process helps do anything at all except what is needed.” |
| “Product engineers” who own idea‑to‑implementation end‑to‑end achieve dramatic speed (mobile + web in a few days). | Internal case where a classical team went a month without code, while a product engineer delivered a full product in days. |

---

### 5.  Agents need continuous **feedback** – they cannot operate in a vacuum  

| Claim | Evidence |
|------|----------|
| Without external signals (UI state, DB changes, error streams) an agent cannot self‑correct. | Aircraft analogy (gyroscopes vs. GPS) and under‑floor‑heating example where the human supplies the missing context. |
| An agent without feedback “cannot exist.” | Teams that tried to run agents without unit‑test‑style monitoring quickly hit failure. |

---

### 6.  Building an agent requires **two distinct roles** (engineering + research)  

| Claim | Evidence |
|------|----------|
| Engineering side: integrations, MCP knowledge, security, deployment. | Backend developers repeatedly built their own frameworks for months with no result. |
| Research side: dataset collection, benchmark design, metric definition. | NLP engineer was busy wiring auth/DB while the product manager expected the agent to already work; the speaker notes that a single person with both skill‑sets is “super‑human.” |
| If no single person has both, you must staff **two** people. | Observation across multiple companies that teams split these responsibilities. |

---

### 7.  Analysts struggle to describe agents; use **business‑function (IDEF0) framing**  

| Claim | Evidence |
|------|----------|
| Talking about “agents” confuses analysts; framing as “business functions to automate” clarifies scope. | Splitting an agent into **control points** (prompts, skills, loop) and **integration** (memory, sub‑agents) maps cleanly onto IDEF0. |
| Decomposing a “100‑tool” assistant into functional blocks revealed unnecessary bloat and enabled simplification. | Internal case where a massive open‑source assistant was trimmed after functional analysis. |

---

### 8.  Traditional sprint planning must incorporate **experiments / hypotheses**  

| Claim | Evidence |
|------|----------|
| A sprint now equals “ten features **and** ten experiments.” | Teams tried to log agent‑failure tickets in Jira; engineers didn’t know how to treat them as data for model improvement. |
| The **ML System Design Doc** successfully captured experiments, metrics, and client communication. | Adoption of the doc gave visibility to clients and forced a culture of documentation. |

---

### 9.  Services must expose new **agent‑centric entry points** and address security  

| Claim | Evidence |
|------|----------|
| Agents are a new actor that connects to services, other agents, and tools; existing APIs are not ready. | Thought experiment: a shopping‑assistant agent compromised via a retailer’s MCP server; raises questions of defense and user remediation. |
| Ignoring this need forces a “no‑agent” future, which is unrealistic (everyone wants a “Jarvis”). | No concrete solution yet; the speaker calls for proactive design. |

---

### 10.  Future production model: humans **maintain the agent layer**  

| Claim | Evidence |
|------|----------|
| Product owners feed ideas to the agent layer; the layer auto‑generates features; QA validates at the end. | Example where an open‑source assistant auto‑cleaned its memory after disk‑full, but required human monitoring to prevent data loss. |
| Human work will focus on UI kits, skill libraries, infrastructure health (DB growth, storage). | The speaker envisions a small team overseeing the agent ecosystem rather than writing every line of code. |
| The only remaining obstacle to 10× acceleration is the **human** finding a new role. | Closing statement: “The human has to find their new place… agents already cope quite well.” |

---

### Bottom‑Line for the Process Review  

- **Ask:** Are our current tools, training, and onboarding pipelines aligned with the need for configured, feedback‑rich agents?  
- **Ask:** Do we have clear, human‑controlled “control points” and a governance model that keeps agents from over‑stepping them?  
- **Ask:** How will we restructure Agile hand‑offs, sprint planning, and role definitions (engineering + research) to accommodate the research‑cycle that agents introduce?  
- **Ask:** What concrete steps can we take now to expose agent‑friendly APIs, embed continuous feedback, and address security for the new agent actor?  

These questions map directly to the speaker’s claims and the evidence he provided, giving you a ready‑made framework to decide which points to raise at the review.
