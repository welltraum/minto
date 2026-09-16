**Answer:** The promised 10× acceleration from coding agents has not materialised because teams face steep adoption hurdles, lose control over critical code paths, clash with existing Agile processes and tooling, and must redesign security and service interfaces for agents as new actors.

**Why**

1. **Adoption hurdles** – Most developers use the “auto” mode without understanding agents, need 3‑6 months to become proficient, and resist change even when forced to switch IDEs.  
   *[00:02] “auto” mode popularity; [00:04] training courses, resistance, code‑cost drop, monitoring difficulty.*

2. **Loss of control & need for feedback** – Core contracts, APIs and databases become fragile control points; agents cannot be trusted to modify them without human oversight. The CI/CD‑agent review example shows the flaw of feeding feedback to humans instead of agents, and the aircraft‑feedback analogy illustrates the necessity of an external human “sensor”.  
   *[00:06] control points, example of CI/CD agent; [00:08] feedback system analogy.*

3. **Process and role mismatch** – Traditional Agile handoffs add latency; product‑engineer roles that own end‑to‑end development can speed things up but are scarce. Agent work demands two complementary roles (engineering for integration/control points and research for datasets/benchmarks). Existing tools like Jira are ill‑suited, while the ML System Design Doc helps capture experiments.  
   *[00:10] handoff delays; [00:12] product engineers’ speed; [00:16] dual engineering/research tasks; [00:20‑22] Jira mismatch, experiments, ML System Design Doc.*

4. **Security and service redesign** – Agents are a new actor requiring fresh entry points, access‑right models, and protection against compromise; services must be built for agents, not just humans.  
   *[00:24] security concerns, compromised agents, need for new service interfaces.*
