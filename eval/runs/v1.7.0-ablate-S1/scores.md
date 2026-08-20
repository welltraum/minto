# Deterministic scores: v1.7.0-ablate-S1

Generated 2026-08-20T16:56:55Z by `eval/aggregate.py` from 8 judged cells. Commit `03975451e3c979d733f5e2053a239bac29c7cea9`, worktree dirty, rubric penalty version 1.

Generated over 2 commits (`03975451e3c9`, `a5312821438a`); the skill text was identical throughout.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.50 (56.3%) | 4.75 (59.4%) | +0.25 | +3.1 | +5.6% |
| Quality (as judged) /10 | 7.00 (70.0%) | 7.50 (75.0%) | +0.50 | +5.0 | +7.1% |
| Quality (after hard-failure penalty) /10 | 6.50 (65.0%) | 7.00 (70.0%) | +0.50 | +5.0 | +7.7% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 25.0% | 75.0% | +50.0 | 4 |
| `no_invented_facts` | 25.0% | 25.0% | 0.0 | 4 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 0 |
| `mode_respected` | 75.0% | 100.0% | +25.0 | 4 |
| `answer_first` | 100.0% | 100.0% | 0.0 | 4 |
| `first_level_count_within_limit` | 100.0% | 100.0% | 0.0 | 4 |
| `readers_question_literal` | 0.0% | 0.0% | 0.0 | 0 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 0 |
| `scq_intro_present` | 100.0% | 100.0% | 0.0 | 4 |
| `no_hard_failure` | 25.0% | 25.0% | 0.0 | 4 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 75.0% → 50.0% | 90.0% → 70.0% | -20.0 |
| gpt-oss-120b | 1 | 37.5% → 50.0% | 40.0% → 70.0% | +30.0 |
| qwen3.6-fp8 | 1 | 50.0% → 87.5% | 70.0% → 90.0% | +20.0 |
| sonnet5 | 1 | 62.5% → 50.0% | 80.0% → 70.0% | -10.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 3 | 3 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 70% | 75% | +5 |
| `structure` | Structure, share of the judge's 8 points | 56% | 59% | +3 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 25% | 75% | +50 |
| `answer-first` | Answer in the first sentence | 100% | 100% | +0 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
