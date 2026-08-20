# Deterministic scores: v1.7.0-final

Generated 2026-08-20T20:29:29Z by `eval/aggregate.py` from 172 judged cells. Commit `f4813ce76aa4da6c0296c9ee558889238ffcbd8a`, worktree clean, rubric penalty version 1.

Generated over 2 commits (`f4813ce76aa4`, `f4813ce76aa4`); the skill text was identical throughout.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.76 (59.4%) | 5.27 (65.8%) | +0.51 | +6.4 | +10.8% |
| Quality (as judged) /10 | 7.17 (71.7%) | 7.90 (79.0%) | +0.72 | +7.3 | +10.0% |
| Quality (after hard-failure penalty) /10 | 6.34 (63.4%) | 7.08 (70.8%) | +0.74 | +7.4 | +11.7% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 53.5% | 66.3% | +12.8 | 86 |
| `no_invented_facts` | 51.2% | 43.0% | -8.2 | 86 |
| `no_unacknowledged_source_loss` | 61.5% | 65.4% | +3.9 | 78 |
| `mode_respected` | 98.8% | 100.0% | +1.2 | 86 |
| `answer_first` | 84.3% | 74.3% | -10.0 | 70 |
| `first_level_count_within_limit` | 88.6% | 97.1% | +8.5 | 70 |
| `readers_question_literal` | 13.0% | 34.8% | +21.8 | 46 |
| `order_type_named` | 14.8% | 27.8% | +13.0 | 54 |
| `scq_intro_present` | 47.8% | 97.8% | +50.0 | 46 |
| `no_hard_failure` | 30.2% | 31.4% | +1.2 | 86 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 11 | 60.2% → 67.0% | 74.5% → 81.8% | +7.3 |
| gpt-oss-120b | 11 | 50.0% → 52.3% | 52.7% → 63.6% | +10.9 |
| haiku45 | 11 | 53.4% → 62.5% | 67.3% → 76.4% | +9.1 |
| opus5 | 11 | 62.5% → 84.1% | 73.6% → 90.0% | +16.4 |
| qwen3.6-35b-a3b | 11 | 58.0% → 67.0% | 75.5% → 79.1% | +3.6 |
| qwen3.6-fp8 | 11 | 63.6% → 69.3% | 74.5% → 80.0% | +5.5 |
| qwen3.8-27b | 9 | 62.5% → 62.5% | 78.9% → 81.1% | +2.2 |
| sonnet5 | 11 | 65.9% → 61.4% | 78.2% → 80.0% | +1.8 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 42 | 49 |
| `more_than_four_first_level` | 8 | 2 |
| `unacknowledged_source_loss` | 30 | 27 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 72% | 79% | +7 |
| `structure` | Structure, share of the judge's 8 points | 59% | 66% | +7 |
| `readers-question` | The reader's question is written down | 13% | 35% | +22 |
| `kind-matches` | First-level points are all the same kind | 54% | 66% | +12 |
| `answer-first` | Answer in the first sentence | 84% | 74% | -10 |
| `source-kept` | No source material lost without saying so | 62% | 65% | +3 |
