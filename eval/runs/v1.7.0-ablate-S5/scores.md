# Deterministic scores: v1.7.0-ablate-S5

Generated 2026-08-20T17:29:10Z by `eval/aggregate.py` from 16 judged cells. Commit `a5312821438a65c3b009a76992f4da732b0ffd03`, worktree dirty, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 5.38 (67.2%) | 5.63 (70.3%) | +0.25 | +3.1 | +4.7% |
| Quality (as judged) /10 | 8.13 (81.3%) | 7.63 (76.3%) | -0.50 | -5.0 | -6.2% |
| Quality (after hard-failure penalty) /10 | 7.25 (72.5%) | 6.38 (63.8%) | -0.88 | -8.7 | -12.1% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 50.0% | 50.0% | 0.0 | 8 |
| `no_invented_facts` | 25.0% | 25.0% | 0.0 | 8 |
| `no_unacknowledged_source_loss` | 75.0% | 62.5% | -12.5 | 8 |
| `mode_respected` | 100.0% | 100.0% | 0.0 | 8 |
| `answer_first` | 100.0% | 100.0% | 0.0 | 8 |
| `first_level_count_within_limit` | 100.0% | 100.0% | 0.0 | 8 |
| `readers_question_literal` | 25.0% | 50.0% | +25.0 | 8 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 4 |
| `scq_intro_present` | 25.0% | 100.0% | +75.0 | 4 |
| `no_hard_failure` | 25.0% | 0.0% | -25.0 | 8 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 2 | 75.0% → 62.5% | 85.0% → 80.0% | -5.0 |
| gpt-oss-120b | 2 | 62.5% → 56.3% | 75.0% → 65.0% | -10.0 |
| qwen3.6-fp8 | 2 | 56.3% → 81.3% | 75.0% → 80.0% | +5.0 |
| sonnet5 | 2 | 75.0% → 81.3% | 90.0% → 80.0% | -10.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 6 | 6 |
| `unacknowledged_source_loss` | 2 | 3 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 81% | 76% | -5 |
| `structure` | Structure, share of the judge's 8 points | 67% | 70% | +3 |
| `readers-question` | The reader's question is written down | 25% | 50% | +25 |
| `kind-matches` | First-level points are all the same kind | 50% | 50% | +0 |
| `answer-first` | Answer in the first sentence | 100% | 100% | +0 |
| `source-kept` | No source material lost without saying so | 75% | 63% | -12 |
