# Deterministic scores: v1.8.0-ablate-C

Generated 2026-09-16T13:36:52Z by `eval/aggregate.py` from 6 judged cells. Commit `d1bb1d02077958a5254497a455b25cbd88271d61`, worktree dirty, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 5.67 (70.8%) | 6.33 (79.2%) | +0.67 | +8.4 | +11.8% |
| Quality (as judged) /10 | 6.33 (63.3%) | 8.00 (80.0%) | +1.67 | +16.7 | +26.3% |
| Quality (after hard-failure penalty) /10 | 5.33 (53.3%) | 7.67 (76.7%) | +2.33 | +23.4 | +43.8% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 66.7% | 100.0% | +33.3 | 3 |
| `no_invented_facts` | 33.3% | 66.7% | +33.4 | 3 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 0 |
| `mode_respected` | 66.7% | 100.0% | +33.3 | 3 |
| `answer_first` | 100.0% | 100.0% | 0.0 | 3 |
| `first_level_count_within_limit` | 33.3% | 100.0% | +66.7 | 3 |
| `readers_question_literal` | 0.0% | 0.0% | 0.0 | 0 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 0 |
| `scq_intro_present` | 100.0% | 100.0% | 0.0 | 3 |
| `no_hard_failure` | 0.0% | 66.7% | +66.7 | 3 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 75.0% → 100.0% | 70.0% → 100.0% | +30.0 |
| gpt-oss-120b | 1 | 50.0% → 62.5% | 40.0% → 70.0% | +30.0 |
| qwen3.6-fp8 | 1 | 87.5% → 75.0% | 80.0% → 70.0% | -10.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 2 | 1 |
| `more_than_four_first_level` | 2 | 0 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 63% | 80% | +17 |
| `structure` | Structure, share of the judge's 8 points | 71% | 79% | +8 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 67% | 100% | +33 |
| `answer-first` | Answer in the first sentence | 100% | 100% | +0 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
