# Deterministic scores: v1.8.0-r2-ablate-R

Generated 2026-09-16T14:29:59Z by `eval/aggregate.py` from 8 judged cells. Commit `5092a71b580cb7dcb4e8303dbd363033ced0d14c`, worktree dirty, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 6.25 (78.1%) | 6.00 (75.0%) | -0.25 | -3.1 | -4.0% |
| Quality (as judged) /10 | 5.75 (57.5%) | 7.50 (75.0%) | +1.75 | +17.5 | +30.4% |
| Quality (after hard-failure penalty) /10 | 5.25 (52.5%) | 6.25 (62.5%) | +1.00 | +10.0 | +19.0% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 25.0% | 75.0% | +50.0 | 4 |
| `no_invented_facts` | 50.0% | 25.0% | -25.0 | 4 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 0 |
| `mode_respected` | 75.0% | 50.0% | -25.0 | 4 |
| `answer_first` | 100.0% | 50.0% | -50.0 | 4 |
| `first_level_count_within_limit` | 50.0% | 75.0% | +25.0 | 4 |
| `readers_question_literal` | 0.0% | 0.0% | 0.0 | 0 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 0 |
| `scq_intro_present` | 100.0% | 100.0% | 0.0 | 4 |
| `no_hard_failure` | 25.0% | 0.0% | -25.0 | 4 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 87.5% → 87.5% | 50.0% → 70.0% | +20.0 |
| gpt-oss-120b | 1 | 75.0% → 87.5% | 40.0% → 90.0% | +50.0 |
| qwen3.6-35b-a3b | 1 | 75.0% → 62.5% | 70.0% → 70.0% | 0.0 |
| qwen3.6-fp8 | 1 | 75.0% → 62.5% | 70.0% → 70.0% | 0.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 2 | 3 |
| `more_than_four_first_level` | 2 | 1 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 58% | 75% | +17 |
| `structure` | Structure, share of the judge's 8 points | 78% | 75% | -3 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 25% | 75% | +50 |
| `answer-first` | Answer in the first sentence | 100% | 50% | -50 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
