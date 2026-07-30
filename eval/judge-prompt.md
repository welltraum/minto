# Judge instructions

Evaluate all blinded outputs for one fixture. Every engine produced two arms:
one with the skill and one control. Do not infer engine or arm identities.

Read the supplied fixture, gold structure, rubric, decisive questions, frozen
skill, rules, and outputs. They are the complete evidence. Do not use outside
knowledge to reconstruct hidden source text.

Return one Markdown report with:

## 1. Score table

| output | Structure 0-8 | Quality 0-10 | Hard failures |
|---|---:|---:|---|

Show the four structural sub-scores in parentheses after each total.

## 2. Decisive questions

Answer every supplied decisive question for every output, concisely.

## 3. Output notes

One short paragraph per output covering top, key line, levels, invented or lost
material, and mode compliance.

## 4. Attribution

| recurring defect | skill section | cause | affected outputs |
|---|---|---|---|

Use only `vague`, `buried`, `missing`, or `ignored` as causes.

## 5. Observation

State what structurally separates stronger from weaker outputs, without
guessing engines or arms.

An empty or truncated output is `not completed` and receives no score. Do not
reward verbosity. If an output improves on a disputable gold assumption, note
the improvement and do not penalize it.
