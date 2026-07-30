# Changelog

All notable changes to Minto are documented here. The project follows semantic
versioning for its plugin manifests.

## 1.5.0 - 2026-07-30

### Added

- Native Claude Code and Codex plugin manifests and marketplace catalogs.
- One portable, shared skill with Codex UI metadata.
- English installation, usage, development, and evaluation documentation.
- An English eight-fixture, four-engine evaluation harness.
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
