# Deterministic scores: v1.8.0-baseline

Generated 2026-09-16T13:17:39Z by `eval/aggregate.py` from 6 judged cells. Commit `344ed93513381d3ce39b2ed0e328633bfc10cf4c`, worktree clean, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 5.33 (66.7%) | 6.33 (79.2%) | +1.00 | +12.5 | +18.8% |
| Quality (as judged) /10 | 7.00 (70.0%) | 8.00 (80.0%) | +1.00 | +10.0 | +14.3% |
| Quality (after hard-failure penalty) /10 | 6.33 (63.3%) | 8.00 (80.0%) | +1.67 | +16.7 | +26.3% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 33.3% | 66.7% | +33.4 | 3 |
| `no_invented_facts` | 33.3% | 66.7% | +33.4 | 3 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 0 |
| `mode_respected` | 66.7% | 66.7% | 0.0 | 3 |
| `answer_first` | 100.0% | 100.0% | 0.0 | 3 |
| `first_level_count_within_limit` | 66.7% | 100.0% | +33.3 | 3 |
| `readers_question_literal` | 0.0% | 0.0% | 0.0 | 0 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 0 |
| `scq_intro_present` | 100.0% | 100.0% | 0.0 | 3 |
| `no_hard_failure` | 33.3% | 66.7% | +33.4 | 3 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 87.5% → 100.0% | 90.0% → 100.0% | +10.0 |
| gpt-oss-120b | 1 | 50.0% → 62.5% | 50.0% → 60.0% | +10.0 |
| qwen3.6-fp8 | 1 | 62.5% → 75.0% | 70.0% → 80.0% | +10.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 2 | 1 |
| `more_than_four_first_level` | 1 | 0 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 70% | 80% | +10 |
| `structure` | Structure, share of the judge's 8 points | 67% | 79% | +12 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 33% | 67% | +34 |
| `answer-first` | Answer in the first sentence | 100% | 100% | +0 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
