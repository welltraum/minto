**Answer:** The speaker argues that the only thing stopping the promised 10× speed‑up from coding agents is the human side of development – we must redesign roles, control points, and processes so that humans provide feedback and governance while agents handle most of the work.

**Why this matters (Situation → Complication → Question → Answer)**  
*Situation:* Your teams have already adopted coding agents (e.g., Cursor) and are seeing mixed results.  
*Complication:* Agents generate code so fast that traditional safeguards (clean architecture, line‑by‑line review, Agile hand‑offs) break down, and many engineers lack the skills to manage autonomous agents.  
*Question:* What concrete claims does the speaker make about why acceleration is stalled and what must change?  
*Answer:* The stall is caused by human‑centric bottlenecks; fixing it requires new governance points, a split‑role model (engineering + research), and revised processes that treat agents as first‑class actors.

### 1. Human bottleneck & new role (≈ [00:04‑00:10])
- **Claim:** Developers can’t keep up with agents because they still need to master the tools (3‑6 months) and cannot continuously monitor generated code.  
- **Support:** “price of code has dropped… but we can’t watch line‑by‑line” (00:04‑00:06); “only way out… is to teach control points” (00:06).  
- **Implication:** The human must shift from writing code to supervising agents, defining contracts, APIs, and database boundaries.

### 2. Control points & feedback loops (≈ [00:06‑00:12])
- **Claim:** Reliable agent operation hinges on a small set of immutable control points (contracts, APIs, DB) and continuous external feedback, similar to aircraft autopilot systems.  
- **Support:** “everything related to changing contracts, APIs, and the database… is the foundation” (00:06); analogy to aircraft feedback systems (00:08).  
- **Implication:** Build explicit feedback channels (human‑provided context, monitoring tools) so agents can self‑correct without human line‑by‑line review.

### 3. Dual engineering‑research model & process overhaul (≈ [00:14‑00:22])
- **Claim:** One skill set can’t cover both building agents and measuring their performance; you need separate “engineer” (integration, MCP, skills) and “researcher” (datasets, benchmarks, business metrics) roles, or a super‑human who can do both.  
- **Support:** “An agent consists of two parts… engineering approach… research work” (00:14‑00:16); “sprint now includes ten experiments/hypotheses” (00:20‑00:22).  
- **Implication:** Redefine team structures (e.g., product‑engineer + analyst‑engineer) and adopt research‑style documentation (ML System Design Doc) to track experiments and metrics.

### 4. Risks, security, and service redesign (≈ [00:22‑00:26])
- **Claim:** Agents become new actors that need dedicated entry points, security models, and service interfaces; existing services aren’t ready for autonomous agents.  
- **Support:** “agent has a dualism… must interact differently” (00:22); “what if an assistant agent is compromised?” (00:24‑00:26).  
- **Implication:** Plan for agent‑specific APIs, sandboxing, and monitoring; treat agents as first‑class consumers of services rather than just code generators.

**What to take to the process review:**  
- Highlight the human‑centric bottleneck and propose a governance framework around control points and feedback.  
- Suggest reorganizing teams into engineering + research roles (or hiring “super‑human” hybrids).  
- Recommend updating Agile/sprint planning to include experiment cycles and metric tracking.  
- Flag the need for security and service redesign to accommodate agents as autonomous actors.
