# Release report instructions

Build a concise, evidence-based Markdown report for the supplied Minto
benchmark run from the engine metadata, output mapping, fixture verdicts, and
fixture list.

Include:

1. Scope and methodology.
2. A table by engine comparing average `skill` and `control` structure and
   quality scores when those values can be computed from the verdicts.
3. A fixture-level table of the most decisive skill-versus-control result.
4. Strengths that recur across at least two engines.
5. Defects that recur across at least two engines and should be candidates for
   the next skill revision.
6. Hard failures and incomplete cells.
7. Limitations: paraphrased English fixtures, one run per cell, model and judge
   dependence, provider or engine availability recorded in the metadata, and
   no direct comparability to historical Russian runs.
8. A plain conclusion that does not claim improvement unless the supplied
   scores support it.

Do not invent missing scores. If verdict formatting prevents an exact
calculation, say so and report the concrete decisive-question evidence instead.
Return only the finished report.
