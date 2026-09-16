We expected a ten‑fold speed‑up from coding agents, yet progress has stalled because humans still have to control, monitor, and constantly feed agents — the human role is the primary bottleneck.

**1. Human control and feedback are essential**  
- Agents cannot replace line‑by‑line code review; they need external feedback loops (e.g., human‑provided context, UI checks, database state) to stay correct. [00:08‑00:12]  
- Critical control points (contracts, APIs, database schemas) must remain under human oversight; otherwise agents can drift or break. [00:06‑00:07]  
- Attempts to let agents review code in CI/CD fail unless the feedback is routed back to the agents themselves, not to humans. [00:07‑00:08]

**2. Two complementary roles are required for agent development**  
- One role (engineering) handles integration, prompts, skills, and the agentic cycle (ReAct, etc.). [00:14‑00:16]  
- A second role (research) builds datasets, benchmarks, and metrics to evaluate the probabilistic behavior of agents. [00:16‑00:18]  
- Neither a pure backend developer nor a sole AI engineer can cover both; teams need either a “super‑human” who combines them or a pair of specialists. [00:14‑00:18]

**3. Process redesign is needed**  
- Classic Agile handoffs (analyst → developer → product) add waiting time; agents speed individual tasks but the handoff chain still dominates overall cycle time. [00:10‑00:12]  
- Product‑engineers who own the full idea‑to‑implementation loop can achieve days‑long delivery, but such talent is scarce. [00:12‑00:13]  
- Future production will shift to a “agent layer” that humans maintain (monitor resources, update skills, ensure security), while agents handle most development work. [00:24‑00:26]  

These three pillars—human‑centric control, dual engineering/research roles, and a revamped process—summarize what the speaker claims and the evidence he cites. Use them to decide which points to raise at the upcoming process review.
