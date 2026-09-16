**Key Thought**  
*The promised 10‑× speed‑up from coding agents has not materialised because the development process, tooling and organisational roles have not been re‑engineered to accommodate agents.  The single remaining blocker is the human side – learning, control, feedback and new responsibilities.*  

---

### Claims and What They Rest On  

| # | Claim (what the speaker says) | Evidence / Reasoning behind the claim |
|---|------------------------------|---------------------------------------|
| 1 | **Agents have not delivered 10× acceleration.** | The speaker measured team velocity after a year of using agents and found no order‑of‑magnitude gain; the market’s “10× hype” has not been realised. |
| 2 | **Adoption is slowed by a steep learning curve (3‑6 months).** | Teams were given Cursor subscriptions; most used the default “auto” mode without understanding the agent.  Even with training courses and material from Anthropic/OpenAI, developers still needed 3–6 months to become proficient. |
| 3 | **One tool is insufficient; proper “Plan/Act” configuration is required.** | Successful use demanded setting up MCP servers, selecting skills, and managing the agent’s loop (e.g., ReAct).  Without this, agents behaved unpredictably. |
| 4 | **Traditional code‑level control (clean architecture, line‑by‑line review) breaks down.** | Agents generate large, continuous code changes that cannot be inspected manually; the speaker observed that “watching line by line” became impossible. |
| 5 | **Human control must stay on the immutable contract points (APIs, DB schema).** | The speaker cites a real‑life incident where entrusting contract changes to an agent caused failure; therefore contracts, APIs and database schemas remain the “foundation” that only humans should modify. |
| 6 | **Putting an agent in CI/CD to review human‑written code is the wrong paradigm.** | A large marketplace tried this; the speaker argues that an agent reviewer should feed its feedback back to the coding agents, not to humans, otherwise the loop is duplicated and ineffective. |
| 7 | **Feedback must be external to the agent, analogous to GPS correcting a plane.** | Using the under‑floor‑heating analogy, the speaker explains that agents need continuous external signals (human‑provided context) to adjust their behaviour. |
| 8 | **Classical Agile hand‑offs become bottlenecks with agents.** | Although analysts and developers finish tasks faster (e.g., analysis in 30 min, coding in 2 h), the hand‑off time between roles does not shrink, and teams revert to filing Jira tickets instead of writing agents. |
| 9 | **“Product engineers” who own the whole idea‑to‑implementation pipeline achieve dramatic speed.** | In the speaker’s company, such engineers delivered a mobile app and website in days, while traditional teams could go a month without writing code. |
|10 | **Agent development requires two distinct skill sets: engineering integration *and* research/ML.** | Engineering tasks (MCP integration, rights, deployment) differ from research tasks (dataset collection, benchmarking, metric definition).  The speaker observed that a single person with both skill sets is “super‑human”; otherwise two roles are needed. |
|11 | **Analysts struggle to describe agents using traditional functional language.** | Teams attempted to define “analyst agents” but produced inconsistent designs.  Mapping agent inputs/outputs to IDEF0 business‑function diagrams clarified requirements and enabled teams to prune unnecessary tools. |
|12 | **Agent errors become data for a research cycle, not ordinary bugs.** | When agents mis‑answer user queries, managers logged each as a Jira ticket; engineers could not treat them as code bugs.  The speaker introduced the “ML System Design Doc” to capture experiments, hypotheses and metrics, turning the bug‑fix process into a research loop. |
|13 | **Services must expose new entry points for agents and address security.** | Agents act as new actors that call services, other agents, and tools.  The speaker raises scenarios (e.g., a shopping assistant compromised) to illustrate the need for agent‑focused APIs and security models. |
|14 | **Future production model: humans maintain the “agent layer”; product owners feed ideas; QA validates output.** | The speaker describes a vision where the agent layer autonomously develops features, while a small human team monitors resource usage, skill libraries, and infrastructure health (e.g., disk‑space cleanup). |
|15 | **Human adaptation is the only remaining obstacle to 10× acceleration.** | Summarising all the above, the speaker concludes that once humans find their new role—providing control points, feedback, and research discipline—agents can deliver the promised speed. |

---

**What to Take to the Process Review**  
- Highlight claims that directly affect your team’s workflow (learning curve, control points, Agile hand‑offs, dual‑role requirement, need for external feedback loops).  
- Use the supporting evidence (real‑world examples, observed failures, the ML System Design Doc) to argue for concrete changes: dedicated training, redefining contract ownership, introducing research‑style experiment tracking, and redesigning service APIs for agent consumption.
