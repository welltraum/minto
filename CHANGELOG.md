# Changelog

All notable changes to Minto are documented here. The project follows semantic
versioning for its plugin manifests.

## Unreleased - 2026-08-05

The skill itself is unchanged. Only the evaluation and the site moved.

### Added

- A deterministic scoring pipeline. Judges now emit a machine-readable block
  alongside the prose verdict, and `eval/aggregate.py` computes every published
  figure from it into `scores.json` and `scores.md`. Previously the arithmetic was
  done by a language model, so the numbers could not be reproduced from the
  committed artifacts.
- Four Claude models as evaluation engines through the Claude Code CLI at low
  effort, isolated the way the Codex arm already was.
- A wide skill-versus-control benchmark: 64 judged cells over four engines,
  reported in `eval/report-v1.5.0-wide.md`.
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
  acknowledging it more often than the control does — 11 runs against 4. This
  replicates a defect already recorded for v1.5.0 and is the first candidate for
  the next version. It is published on the site rather than held back.

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
