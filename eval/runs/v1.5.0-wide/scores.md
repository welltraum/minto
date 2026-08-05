# Deterministic scores: v1.5.0-wide

Generated 2026-08-05T16:20:05Z by `eval/aggregate.py` from 64 judged cells. Commit `7dbae71baa7bd43af54c345292b861046233af8c`, worktree clean, rubric penalty version 1.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.28 (53.5%) | 4.75 (59.4%) | +0.47 | +5.9 | +10.9% |
| Quality (as judged) /10 | 6.91 (69.1%) | 7.38 (73.8%) | +0.47 | +4.7 | +6.8% |
| Quality (after hard-failure penalty) /10 | 5.94 (59.4%) | 6.88 (68.8%) | +0.94 | +9.4 | +15.8% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 50.0% | 68.8% | +18.8 | 32 |
| `no_invented_facts` | 43.8% | 53.1% | +9.3 | 32 |
| `no_unacknowledged_source_loss` | 87.5% | 65.6% | -21.9 | 32 |
| `mode_respected` | 100.0% | 100.0% | 0.0 | 32 |
| `answer_first` | 83.3% | 75.0% | -8.3 | 24 |
| `first_level_count_within_limit` | 87.5% | 100.0% | +12.5 | 24 |
| `readers_question_literal` | 15.0% | 65.0% | +50.0 | 20 |
| `order_type_named` | 16.7% | 37.5% | +20.8 | 24 |
| `no_hard_failure` | 34.4% | 40.6% | +6.2 | 32 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 8 | 54.7% → 67.2% | 68.8% → 76.3% | +7.5 |
| gpt-oss-120b | 8 | 46.9% → 51.6% | 67.5% → 70.0% | +2.5 |
| kimi | 8 | 53.1% → 59.4% | 72.5% → 75.0% | +2.5 |
| qwen3.6-35b-a3b | 8 | 59.4% → 59.4% | 67.5% → 73.8% | +6.3 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 18 | 15 |
| `more_than_four_first_level` | 3 | 0 |
| `unacknowledged_source_loss` | 4 | 11 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 69% | 74% | +5 |
| `structure` | Structure, share of the judge's 8 points | 54% | 59% | +5 |
| `readers-question` | The reader's question is written down | 15% | 65% | +50 |
| `kind-matches` | First-level points are all the same kind | 50% | 69% | +19 |
| `answer-first` | Answer in the first sentence | 83% | 75% | -8 |
| `source-kept` | No source material lost without saying so | 88% | 66% | -22 |
