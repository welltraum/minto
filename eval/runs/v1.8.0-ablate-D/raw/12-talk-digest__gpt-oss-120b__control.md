**Key Thought**  
The ten‑fold speed‑up that AI‑driven coding agents were expected to deliver has not materialised. The decisive blocker is **human organisation** – the way people, processes and responsibilities are set up today cannot accommodate agents safely or efficiently. To realise any real acceleration, companies must redesign the development workflow around agents, keep critical control points in human hands, create new hybrid roles, and treat agent work as a research‑plus‑engineering activity rather than a straight‑line software project.

---

### 1.  Agents do not give instant productivity gains  
- **Observation:** After a year of using Cursor‑style “auto” mode, teams saw no 10× uplift.  
- **Root causes:**  
  - Most developers use default settings and never learn how the agent works (Plan/Act configuration, MCP integration, skill plugging).  
  - Mastery takes **3‑6 months** even for eager engineers; resistance to change is high.  
  - Experiments to force exclusive use of agents (e.g., banning IDEs) were only proposals, not proven solutions.

### 2.  One tool is insufficient; proper agent configuration is essential  
- **Evidence:** The speaker notes that “one tool is not enough” and that agents must be set up with **plans, actions, skills, and MCP servers**.  
- **Implication:** Without a disciplined configuration process, agents behave like black boxes and cannot be trusted for core work.

### 3.  The “cost of code” has collapsed, breaking traditional quality guards  
- **Fact:** A line of code now costs virtually nothing, so developers can no longer watch every change.  
- **Consequence:** Clean‑architecture practices (component boundaries, manual code reviews) become impossible, pushing senior engineers into **management‑level oversight of agents**.

### 4.  Critical control points must stay human‑controlled  
- **Control points:** contracts, public APIs, database schemas.  
- **Illustration:** A real‑life case (not detailed) showed agents breaking these points; the speaker argues they cannot be delegated to agents.  
- **Failed approach:** Putting an agent in CI/CD to review agent‑generated code only adds another human‑centric feedback loop; the feedback should be fed back to the coding agent directly.

### 5.  Human feedback remains the only reliable correction mechanism  
- **Analogy:** Aircraft autopilot needs external gyroscopes; agents need an external human “GPS” to correct drift (e.g., temperature‑control example).  
- **Result:** Agents must receive **continuous, external signals** (unit‑test results, UI checks, runtime errors) to stay aligned.

### 6.  Classical Agile hand‑offs become a new bottleneck  
- **Data:** Developers and analysts finish tasks 2‑3× faster with agents, but the **handoff time** (waiting, transferring responsibility) stays the same, eroding net speed.  
- **Behaviour:** Teams revert to familiar Jira‑driven processes, filing tasks instead of writing agents, which stalls progress.

### 7.  “Product engineers” who own end‑to‑end flow outperform traditional teams  
- **Case:** A single product engineer assembled a mobile app and website in days, while a conventional team could go a month without writing code.  
- **Limitation:** Such engineers are scarce; most organisations shrink Agile squads to 2‑3 T‑shaped people who split roles.

### 8.  Agent development requires **two distinct skill sets**  
- **Engineering side:** integration, MCP knowledge, security, deployment, access‑right design.  
- **Research side:** dataset collection, benchmark creation, metric definition, hypothesis testing.  
- **Observation:** No single “backend developer” or “AI engineer” alone can cover both; either a “super‑human” individual or a paired team is needed.

### 9.  Analysts struggle to describe agents; using business‑function language helps  
- **Problem:** Analysts try to map classic requirements onto agents and get lost.  
- **Solution:** Frame work in **IDEF0** terms (inputs, outputs, controls, mechanisms) – i.e., treat agents as “business functions” to be automated.  
- **Outcome:** Teams can break down a bloated 100‑tool assistant into essential functions and prune unnecessary parts.

### 10.  Agent errors become data for a **research cycle** inside sprints  
- **Pattern:** Bugs reported in Jira are not ordinary code fixes; they are **experiment results** that feed datasets for retraining or benchmarking.  
- **Shift:** A sprint now contains **features + experiments + hypotheses**.  
- **Tool:** The **ML System Design Doc** was adopted to record experiments, metrics, and client‑visible rationale.

### 11.  Services must expose new entry points for agents; security concerns rise  
- **New actor:** Agents connect to services, other agents, and tools, requiring **agent‑specific APIs** and authentication.  
- **Risk example:** A compromised shopping assistant could abuse an MCP server; defending the user now includes protecting the agent itself.

### 12.  Future organisational shape – “maintaining the agent layer”  
- **Vision:** Humans become custodians of the agent ecosystem:  
  - Curate prompts, skills, and context.  
  - Monitor resource usage (disk, memory) and intervene when agents self‑clean or overflow.  
  - Provide UI kits and infrastructure oversight.  
  - QA still validates final output, but most development (idea ingestion, feature generation) is automated by agents.  
- **Conclusion:** The only thing still standing between us and the promised 10× acceleration is **the human role** – we must find a new place for it.

---

**Take‑away for the process review**  
If you want to surface actionable insights, focus on the claims that directly affect your current workflow:

1. **Learning curve & resistance** – allocate time and structured training (Plan/Act, MCP, skill wiring).  
2. **Preserve control points** – keep contracts/APIs/DB schemas under human governance.  
3. **Redesign Agile hand‑offs** – empower product‑engineer style ownership or shrink‑team T‑shaped roles.  
4. **Create dual‑track roles** – pair an integration engineer with a researcher, or develop “super‑human” staff.  
5. **Adopt research artefacts** – use an ML System Design Doc to capture experiments and hypotheses.  
6. **Expose agent‑friendly service interfaces** and plan for security/monitoring of the agent layer.

These points capture the speaker’s core argument and the evidence he provides, giving you a concise basis for deciding which claims to bring to the upcoming review.
