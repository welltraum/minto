# Deterministic scores: v1.7.0-baseline

Generated 2026-08-20T14:10:26Z by `eval/aggregate.py` from 172 judged cells. Commit `3c20ab42b8c0e79c11b843d80b503e073ada4132`, worktree clean, rubric penalty version 1.

Generated over 4 commits (`3c20ab42b8c0`, `3c20ab42b8c0`, `19c149257330`, `19c149257330`); the skill text was identical throughout.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.19 (52.3%) | 4.72 (59.0%) | +0.53 | +6.7 | +12.8% |
| Quality (as judged) /10 | 6.99 (69.9%) | 7.24 (72.4%) | +0.26 | +2.5 | +3.7% |
| Quality (after hard-failure penalty) /10 | 6.30 (63.0%) | 6.60 (66.0%) | +0.30 | +3.0 | +4.8% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 48.8% | 68.6% | +19.8 | 86 |
| `no_invented_facts` | 52.3% | 51.2% | -1.1 | 86 |
| `no_unacknowledged_source_loss` | 65.4% | 69.2% | +3.8 | 78 |
| `mode_respected` | 98.8% | 96.5% | -2.3 | 86 |
| `answer_first` | 85.7% | 77.1% | -8.6 | 70 |
| `first_level_count_within_limit` | 90.0% | 95.7% | +5.7 | 70 |
| `readers_question_literal` | 13.0% | 32.6% | +19.6 | 46 |
| `order_type_named` | 13.0% | 25.9% | +12.9 | 54 |
| `scq_intro_present` | 58.7% | 97.8% | +39.1 | 46 |
| `no_hard_failure` | 38.4% | 40.7% | +2.3 | 86 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 11 | 58.0% → 60.2% | 74.5% → 76.4% | +1.9 |
| gpt-oss-120b | 11 | 35.2% → 45.5% | 55.5% → 58.2% | +2.7 |
| haiku45 | 11 | 53.4% → 59.1% | 71.8% → 74.5% | +2.7 |
| opus5 | 11 | 62.5% → 77.3% | 76.4% → 79.1% | +2.7 |
| qwen3.6-35b-a3b | 11 | 44.3% → 55.7% | 64.5% → 70.0% | +5.5 |
| qwen3.6-fp8 | 11 | 55.7% → 56.8% | 71.8% → 69.1% | -2.7 |
| qwen3.8-27b | 9 | 56.9% → 52.8% | 72.2% → 74.4% | +2.2 |
| sonnet5 | 11 | 53.4% → 63.6% | 72.7% → 78.2% | +5.5 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 41 | 42 |
| `more_than_four_first_level` | 7 | 3 |
| `unacknowledged_source_loss` | 27 | 24 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 70% | 72% | +2 |
| `structure` | Structure, share of the judge's 8 points | 52% | 59% | +7 |
| `readers-question` | The reader's question is written down | 13% | 33% | +20 |
| `kind-matches` | First-level points are all the same kind | 49% | 69% | +20 |
| `answer-first` | Answer in the first sentence | 86% | 77% | -9 |
| `source-kept` | No source material lost without saying so | 65% | 69% | +4 |
