**Key Thought**  
The promised 10‑fold speed‑up from coding agents has not materialised; the main blocker is the human side of the process. Agents work well when they own the low‑level “inside” work, but people must relearn roles, control points and feedback loops, and the whole SDLC has to be reshaped around a new “agent‑as‑actor” model.

---

### Claims & What They Rest On  

| # | Claim | What it rests on (evidence / observation) |
|---|-------|--------------------------------------------|
| 1 | **10× acceleration is still missing.** | Measured output vs. promised gains; teams still spend 3‑6 months learning agents; code‑cost has dropped to near‑zero but productivity gains are modest. |
| 2 | **A single coding‑assistant (e.g., Cursor) is not enough.** | Most users default to “auto” mode; effective use requires “Plan/Act” configuration, MCP integration, skill plugging, and understanding the agent’s internals. |
| 3 | **Developers need months to become proficient with AI tools.** | Internal training program; anecdote of companies considering banning traditional IDEs to force adoption; observed 3‑6 month ramp‑up depending on readiness. |
| 4 | **Human‑controlled “contractual” points (APIs, DB schemas) must stay under human oversight.** | Real‑life failure example (not detailed) where entrusting these to agents caused loss of accountability; agents cannot yet be trusted with core contracts. |
| 5 | **Putting an agent in CI/CD to review code for humans is the wrong paradigm.** | Large marketplace case where the agent’s comments piled up for developers; the speaker argues feedback should be fed back to the coding agents themselves, not to people. |
| 6 | **Human role becomes high‑level requirement‑setter and external feedback source.** | Aircraft‑feedback analogy (expensive sensors vs. cheap GPS); under‑floor‑heating example showing the agent needs outside temperature perception from the human. |
| 7 | **Classic Agile hand‑offs become a new bottleneck despite faster individual work.** | Developers and analysts finish tasks in minutes/hours, but transfer time (waiting, hand‑off) dominates; teams revert to Jira tickets and fall back to old processes. |
| 8 | **Product‑engineer “T‑shaped” individuals can bypass the bottleneck, but they are scarce.** | Observed teams where a single engineer assembled a mobile app + website in days, while traditional squads spent weeks on non‑coding activities. |
| 9 | **Building agents requires two complementary skill sets: engineering + research.** | Engineering side (MCP, security, deployment) vs. research side (datasets, benchmarks, business‑metric methodology); a single “super‑human” can cover both, otherwise two people are needed. |
|10 | **Analysts struggle to describe agents; framing them as business functions (IDEF0) works.** | Split agents into “control points” (prompts, skills, loop) and “integration” (memory, sub‑agents); using IDEF0 helped teams move from dead‑ends to concrete designs. |
|11 | **Agent development injects a research‑experiment cycle into sprints.** | Bugs logged as “bad queries” in Jira become data for model improvement; sprint now contains hypotheses/experiments, not just feature count; ML System Design Doc used to track experiments. |
|12 | **Existing services are not ready for agents as first‑class actors.** | Need new entry points, security models, and defenses (e.g., compromised shopping assistant); services must be re‑architected for agent interaction. |
|13 | **Future production will revolve around maintaining the “agent layer”.** | Speculation: product owners feed ideas to agents, agents auto‑develop features, QA validates final output; humans monitor agent resources (disk, skills) and intervene only when the agent misbehaves (e.g., self‑deleting memory). |
|14 | **The only thing standing in the way of 10× acceleration is the human.** | Summative conclusion that humans must find a new place—researcher/maintainer of the agent ecosystem—because agents already handle much of the low‑level work. |

---  

**What to take to the process review**  
- Highlight claims that directly affect your current SDLC (e.g., control‑point ownership, Agile hand‑off bottlenecks, need for dual‑skill roles).  
- Use the supporting observations (real‑world examples, training data, measured learning curves) to argue for or against adopting any of the speaker’s recommendations.
