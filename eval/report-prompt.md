# Release report instructions

Build a concise, evidence-based Markdown report for the supplied Minto
benchmark run from the engine metadata, output mapping, fixture verdicts, and
fixture list.

**Every number in this report is supplied to you already computed, in the
deterministic scores section. Quote those figures verbatim and compute nothing —
no averages, no percentages, no deltas, not even a subtraction.** If a figure you
want is not in that section, write that it is not available rather than deriving
it. Arithmetic done here cannot be reproduced by a reader, which is the whole
reason it is done upstream.

Include:

1. Scope and methodology.
2. A table by engine comparing `skill` and `control` structure and quality,
   quoted from the deterministic scores.
3. The behaviour pass rates, each with the denominator it was computed from, and
   the percentage-point change. State which rates moved against the skill.
4. A fixture-level table of the most decisive skill-versus-control result.
5. Strengths that recur across at least two engines.
6. Defects that recur across at least two engines and should be candidates for
   the next skill revision.
7. Hard failures, incomplete cells, and every pair the aggregator excluded, with
   the reason it gives.
8. Limitations: paraphrased English fixtures, one run per cell, model and judge
   dependence, provider or engine availability recorded in the metadata, and
   no direct comparability to historical Russian runs.
9. A plain conclusion that does not claim improvement unless the supplied
   scores support it. Where the effect reverses for an engine or a behaviour,
   say so in the conclusion rather than only in the tables.

Do not invent missing scores. Return only the finished report.
