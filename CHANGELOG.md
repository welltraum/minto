# Changelog

All notable changes to Minto are documented here. The project follows semantic
versioning for its plugin manifests.

## 1.7.0 - 2026-08-20

The first revision of the skill text since 1.5.0, driven by 21 real usage
sessions (26 invocations) and validated by a full baseline-versus-candidate
benchmark: the same eleven fixtures, eight engines and blind judge scored the
1.6.0 text and this text cell-for-cell. Skill-arm quality rose on all eight
engines; the skill-versus-control delta on judged quality went from +0.256 to
+0.721 points (penalized: +0.302 → +0.744). Full figures, including everything
that moved against the skill: `eval/report-v1.7.0.md`.

### Added

- **Mode 4 — `digest`**: an answer-first report on read sources delivered as
  chat prose with source references. This was the single most common real
  invocation (35%) and previously had no mode; the router and description now
  carry the digest/выжимка/саммари triggers. Its fixture (`09-sources-digest`)
  gained +2.12 judged quality over the 1.6.0 text.
- An SCQ-intro item in the core-loop self-check: the output must ground its
  answer in a situation and complication, or skip the story deliberately.
- A text-skeleton pyramid template; after `write` the pyramid is now appended
  as indented text by default, with mermaid only where it demonstrably renders
  or on request. Judged metrics are ambiguous on this one; it ships because
  raw mermaid in chat output is a real, repeatedly reported reading problem.
- Presentation discipline in `write`: markers and the legend belong to `audit`
  and `viz` only; no meta-commentary about ordering in the deliverable; a
  plain-list request gets plain text — with one exception the removal test
  taught us: a dropped fact still earns its one-line omission note.
- Intent-mode output dosing (context first, disagreements one at a time).
  No fixture exercises intent mode, so this ships unmeasured and is recorded
  as such.
- Three benchmark fixtures modeled on real usage with all client specifics
  invented from scratch: a multi-source digest, a large sectioned rollout
  review, and a plain pasteable list. A new conditional check
  (`scq_intro_present`) with per-mode applicability.
- `eval/compare-runs.py` — cell-for-cell comparison of two aggregated runs.
- Parallel engine lanes in `eval/run-cli.sh` (`PARALLEL_ENGINES=1`), a
  `NEURALDEEP_DEADLINE` override, 503 retries, and fixture-scoped blinding for
  deliberately partial runs.

### Rolled back during this cycle (negative results)

- A "Large or sectioned input" section made its own target fixture worse on
  every metric and was removed; the large-document pain remains open, with the
  fixture staying in the suite to measure the next attempt.
- A rewording of the group-count rule ("count from the material") hurt three
  fixtures and was reverted to the original "3–4 first-level groups".

### Known regressions shipped with eyes open

- `no_invented_facts` moved −8.2 pp against the skill in the final run
  (49 vs 42 hard failures) and `answer_first` remains −10.0 pp against the
  skill — both are on the page and in the report, and both are the top
  candidates for the next revision.

## 1.6.0 - 2026-08-05

**The skill instructions are byte-identical to 1.5.0.** `SKILL.md`, `rules.md` and
`templates.md` all carry the same SHA-256 as the 1.5.0 release, so installing 1.6.0
changes nothing about how the skill behaves. What changed is the evidence: how the
benchmark is measured, how much of it there is, and how honestly the site reports
it.

Note on the version number: `eval/report-v1.5.0.md` named the v1.6.0 priorities as
first-level grouping, MECE nesting, grounding and source preservation, decisive
reader framing, and reliable mode compliance. **None of those are addressed here.**
They remain open, and the wider benchmark in this release makes the case for two of
them stronger rather than weaker — source preservation measurably got worse. They
carry forward to the next skill revision, which will need its own run to validate.

### Added

- A deterministic scoring pipeline. Judges now emit a machine-readable block
  alongside the prose verdict, and `eval/aggregate.py` computes every published
  figure from it into `scores.json` and `scores.md`. Previously the arithmetic was
  done by a language model, so the numbers could not be reproduced from the
  committed artifacts.
- Claude Opus 5, Sonnet 5 and Haiku 4.5 as evaluation engines through the Claude
  Code CLI at low effort, isolated the way the Codex arm already was.
- A wide skill-versus-control benchmark: 112 judged cells over seven engines,
  including Claude Opus 5, Sonnet 5 and Haiku 4.5, reported in
  `eval/report-v1.5.0-wide.md`.
- `eval/universal-checks.md`, defining behaviour checks with an explicit
  per-mode applicability matrix, so a check is never pooled across modes where it
  means different things.
- `eval/test-eval.py` — 54 cases covering the verdict validator, the penalty map,
  the applicability matrix and the aggregator's refusals.
- `scripts/check_benchmark_numbers.py`, which fails the build when a figure on the
  site disagrees with `scores.json` or with the visible copy beside it.

### Changed

- The judge no longer applies hard-failure penalties itself. It reports raw axis
  scores and a failure list; `eval/rubric.md` pins the failure-to-axis map and the
  aggregator applies it identically in every cell.
- The landing page reports percentages and shares of the judge's maximum instead
  of bare points on an undeclared scale, and its example is now a real benchmark
  document with the blind judge's score rather than a fictional before and after.
- Benchmark bar geometry moved from per-value CSS classes into the markup, so a
  new run no longer requires a stylesheet edit.

### Fixed

- A failed generation cell no longer leaves its output on disk, where it survived
  the resume check and was judged as if a model had produced it.
- Re-running a finished run directory no longer overwrites the provenance of the
  cells already in it.
- `eval/shuffle.sh` blinds only the engines named in `engines.txt` and refuses a
  `(fixture, engine)` pair with one arm missing.

### Known issue

- Under the wider benchmark, models given the skill lose source material without
  acknowledging it more often than the control does — 16 runs against 5, and the
  clean rate falls from 91% to 71%. This replicates a defect already recorded for
  v1.5.0, now across seven engines, and is the first candidate for the next
  version. It is published on the site rather than held back.
- Quality fell for one of the seven engines, `gpt-oss-120b`. The effect is useful
  but not uniform, and the site says so.
- `fable5` is excluded from the matrix: on this account the `fable` alias resolves
  to `claude-opus-5`, so running it would have double-weighted Opus under a second
  engine name.

### Evaluation

The release benchmark is `eval/report-v1.5.0-wide.md`, backed by
`eval/runs/v1.5.0-wide/`. Its name refers to the skill text it tested, which 1.6.0
ships unchanged — the recorded `skill_sha256` matches this release, so the run is
this release's benchmark despite the earlier version in its name. Renaming it would
have restated when it ran and what it measured.

Pooled across seven engines and 112 cells: structure 4.32 → 5.00 of 8, quality
6.84 → 7.50 of 10, and 5.98 → 6.88 after the rubric's hard-failure penalty. Quality
improved for six of the seven engines. The two measures that moved against the
skill are in the Known issues above and on the site.

Not comparable with `eval/report-v1.5.0.md`: that round used two engines, a judge
that applied hard-failure penalties at its own discretion, and LLM-computed
averages. The 32 outputs from it were re-judged under the new contract as a
validation step, reproducing its effect size to within 0.06 points.

## 1.5.0 - 2026-07-30

### Added

- Native Claude Code and Codex plugin manifests and marketplace catalogs.
- One portable, shared skill with Codex UI metadata.
- English installation, usage, development, and evaluation documentation.
- An English eight-fixture, two-engine evaluation harness.
- Reproducible isolated judging and benchmark reporting.

### Changed

- Made SCQ introductions narrative rather than a visible four-slot template.
- Calibrated Situation length to what the reader already knows.
- Required the reader's question to remain visible in delivered writing.
- Replaced host-specific tool instructions with portable behavior.

### Evaluation

The release benchmark is recorded in `eval/report-v1.5.0.md`. It uses faithful
English paraphrases of the source examples; earlier Russian-language runs are
not directly comparable.

## 1.4.0

An experimental removal of the key-line-kind rules was rejected. Across the
measured fixtures and four engines, removing those rules reduced structural
quality, especially where a document's mechanics had to be converted into
reader benefits. Version 1.5.0 retains the rules.

## 1.3.0

- Strengthened the distinction between the topic and the reader's real
  decision question.
- Added explicit tests for converting mechanics into reader payoffs.
- Clarified duplicate-branch detection and promotion of the missing branch.

## 1.2.0

- Added stronger self-checks for the top, key-line kind, evidence, order, and
  MECE structure.
- Separated human-facing release history from the skill instructions to avoid
  evaluation leakage.

## 1.1.0

- Tightened routing among `intent`, `audit`, `write`, and `viz`.
- Added fixed audit markers, scoring, output limits, and format templates.
- Added an initial controlled evaluation suite.

## 1.0.0

Initial Minto Pyramid Principle skill.
