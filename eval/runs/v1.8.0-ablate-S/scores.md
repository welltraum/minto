# Deterministic scores: v1.8.0-ablate-S

Generated 2026-09-16T13:46:48Z by `eval/aggregate.py` from 6 judged cells. Commit `d1bb1d02077958a5254497a455b25cbd88271d61`, worktree dirty, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 5.33 (66.7%) | 6.67 (83.3%) | +1.33 | +16.6 | +25.0% |
| Quality (as judged) /10 | 6.67 (66.7%) | 7.67 (76.7%) | +1.00 | +10.0 | +15.0% |
| Quality (after hard-failure penalty) /10 | 6.00 (60.0%) | 7.00 (70.0%) | +1.00 | +10.0 | +16.7% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 66.7% | 66.7% | 0.0 | 3 |
| `no_invented_facts` | 33.3% | 33.3% | 0.0 | 3 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 0 |
| `mode_respected` | 66.7% | 100.0% | +33.3 | 3 |
| `answer_first` | 100.0% | 66.7% | -33.3 | 3 |
| `first_level_count_within_limit` | 33.3% | 100.0% | +66.7 | 3 |
| `readers_question_literal` | 0.0% | 0.0% | 0.0 | 0 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 0 |
| `scq_intro_present` | 100.0% | 100.0% | 0.0 | 3 |
| `no_hard_failure` | 0.0% | 33.3% | +33.3 | 3 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 75.0% → 100.0% | 70.0% → 90.0% | +20.0 |
| gpt-oss-120b | 1 | 37.5% → 62.5% | 40.0% → 60.0% | +20.0 |
| qwen3.6-fp8 | 1 | 87.5% → 87.5% | 90.0% → 80.0% | -10.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 2 | 2 |
| `more_than_four_first_level` | 2 | 0 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 67% | 77% | +10 |
| `structure` | Structure, share of the judge's 8 points | 67% | 83% | +16 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 67% | 67% | +0 |
| `answer-first` | Answer in the first sentence | 100% | 67% | -33 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
