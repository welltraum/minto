# Deterministic scores: v1.7.0-ablate-S2

Generated 2026-08-20T17:03:28Z by `eval/aggregate.py` from 16 judged cells. Commit `a5312821438a65c3b009a76992f4da732b0ffd03`, worktree dirty, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 5.00 (62.5%) | 5.88 (73.4%) | +0.88 | +10.9 | +17.5% |
| Quality (as judged) /10 | 7.00 (70.0%) | 8.13 (81.3%) | +1.13 | +11.3 | +16.1% |
| Quality (after hard-failure penalty) /10 | 5.50 (55.0%) | 6.88 (68.8%) | +1.38 | +13.8 | +25.0% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 62.5% | 87.5% | +25.0 | 8 |
| `no_invented_facts` | 50.0% | 62.5% | +12.5 | 8 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 4 |
| `mode_respected` | 87.5% | 100.0% | +12.5 | 8 |
| `answer_first` | 62.5% | 62.5% | 0.0 | 8 |
| `first_level_count_within_limit` | 75.0% | 100.0% | +25.0 | 8 |
| `readers_question_literal` | 0.0% | 0.0% | 0.0 | 0 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 0 |
| `scq_intro_present` | 100.0% | 100.0% | 0.0 | 4 |
| `no_hard_failure` | 12.5% | 12.5% | 0.0 | 8 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 2 | 81.3% → 81.3% | 90.0% → 85.0% | -5.0 |
| gpt-oss-120b | 2 | 50.0% → 50.0% | 45.0% → 65.0% | +20.0 |
| qwen3.6-fp8 | 2 | 56.3% → 75.0% | 80.0% → 85.0% | +5.0 |
| sonnet5 | 2 | 62.5% → 87.5% | 65.0% → 90.0% | +25.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 4 | 3 |
| `more_than_four_first_level` | 2 | 0 |
| `unacknowledged_source_loss` | 4 | 4 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 70% | 81% | +11 |
| `structure` | Structure, share of the judge's 8 points | 63% | 73% | +10 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 63% | 88% | +25 |
| `answer-first` | Answer in the first sentence | 63% | 63% | +0 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
