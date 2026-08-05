# Minto v1.5.0-wide release report

## Scope and methodology

The benchmark compared `skill` and `control` arms across the supplied write, audit, and visualization fixtures. The deterministic aggregate was generated on 2026-08-05 from 112 judged cells at commit `7dbae71baa7bd43af54c345292b861046233af8c`; the worktree was clean, and the skill text was identical across the two commits represented.

Each output was judged by `gpt-5.6-sol` at high reasoning effort. Structure was scored against an eight-point rubric, quality against a ten-point rubric, and hard failures were separately penalized. The blind mapping was used to restore engine and arm attribution.

## Pooled result

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.32 (54.0%) | 5.00 (62.5%) | +0.68 | +8.5 | +15.7% |
| Quality as judged /10 | 6.84 (68.4%) | 7.50 (75.0%) | +0.66 | +6.6 | +9.7% |
| Quality after hard-failure penalty /10 | 5.98 (59.8%) | 6.88 (68.8%) | +0.89 | +9.0 | +14.9% |

The pooled scores favor the skill, including after the hard-failure penalty. That aggregate result is not uniform across engines or reliability checks.

## Results by engine

| Engine | n per arm | Structure: control → skill | Quality: control → skill | Δ quality pp |
|---|---:|---:|---:|---:|
| codex | 8 | 56.3% → 62.5% | 65.0% → 77.5% | +12.5 |
| gpt-oss-120b | 8 | 51.6% → 51.6% | 67.5% → 63.8% | -3.7 |
| haiku45 | 8 | 39.1% → 59.4% | 61.3% → 75.0% | +13.7 |
| kimi | 8 | 54.7% → 68.8% | 70.0% → 77.5% | +7.5 |
| opus5 | 8 | 65.6% → 76.6% | 75.0% → 81.3% | +6.3 |
| qwen3.6-35b-a3b | 8 | 60.9% → 59.4% | 71.3% → 72.5% | +1.2 |
| sonnet5 | 8 | 50.0% → 59.4% | 68.8% → 77.5% | +8.7 |

Quality favors the skill on every scored engine except `gpt-oss-120b`, where it reverses. Structure improves on five engines, is unchanged on `gpt-oss-120b`, and reverses on `qwen3.6-35b-a3b`.

## Behaviour pass rates

| Check | Control | With skill | Δ pp | Denominator per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 48.2% | 71.4% | +23.2 | 56 |
| `no_invented_facts` | 46.4% | 42.9% | -3.5 | 56 |
| `no_unacknowledged_source_loss` | 91.1% | 71.4% | -19.7 | 56 |
| `mode_respected` | 100.0% | 100.0% | 0.0 | 56 |
| `answer_first` | 76.2% | 76.2% | 0.0 | 42 |
| `first_level_count_within_limit` | 88.1% | 100.0% | +11.9 | 42 |
| `readers_question_literal` | 17.1% | 48.6% | +31.5 | 35 |
| `order_type_named` | 19.0% | 35.7% | +16.7 | 42 |
| `no_hard_failure` | 37.5% | 33.9% | -3.6 | 56 |

The rates that moved against the skill were `no_invented_facts`, `no_unacknowledged_source_loss`, and `no_hard_failure`. `answer_first` and `mode_respected` were unchanged.

## Most decisive fixture-level contrast

Fixture-level aggregate figures are not present in the deterministic scores, so no numeric fixture delta is reported. The clearest qualitative reversal in the supplied verdicts was:

| Fixture | Engine | Control evidence | Skill evidence | Direction |
|---|---|---|---|---|
| Meeting note | gpt-oss-120b | Compact, answer-first request, although it upgraded feasibility to certainty | Extensive labeled scaffolding, mixed branches, and unsupported universal-availability and delay claims | Decisively against the skill |

This contrast is consistent with the engine-level quality reversal for `gpt-oss-120b`.

## Recurring strengths

- More consistent first-level grouping recurred across engines. The visualization fixture produced clear action-based hierarchies for engines including `sonnet5`, `kimi`, `qwen3.6-35b-a3b`, and `opus5`, while the pooled `first_level_kind_matches` rate rose from 48.2% to 71.4%.

- Compliance with the first-level display limit generalized across engines: `first_level_count_within_limit` rose from 88.1% to 100.0%, and `more_than_four_first_level` hard failures fell from 5 to 0.

- Making the reader’s question explicit recurred across engines including `gpt-oss-120b` and `kimi`. The pooled rate rose from 17.1% to 48.6%.

- Stronger answer-and-support hierarchies appeared across several engines in fixtures such as the Big Chief decision, the two-action visualization, and the technical-debt recommendation. This aligns with the pooled gains in structure and judged quality.

## Recurring defects and revision candidates

- Unsupported facts, certainty, timing, and causal claims remain the main reliability defect. They recur across multiple engines and fixtures, especially when tentative source language is rewritten as a definite result. `invented_facts` hard failures rose from 30 to 32, while `no_invented_facts` fell from 46.4% to 42.9%.

- Source preservation deteriorated across engines including `codex`, `haiku45`, `qwen3.6-35b-a3b`, `gpt-oss-120b`, and `opus5`. `unacknowledged_source_loss` hard failures rose from 5 to 16, and the corresponding pass rate fell from 91.1% to 71.4%. The next revision should require an explicit source-retention check after restructuring.

- Ordering remains under-specified across multiple engines. Although `order_type_named` rose from 19.0% to 35.7%, verdicts repeatedly found absent or weak ordering rationales. The skill should make the ordering test operational and require the chosen order to be visible when the task calls for it.

- Short-form writing often exposes too much method. The meeting-note fixture showed recurring SCQ labels, diagrams, and separate answer/key-line blocks across engines including `kimi`, `gpt-oss-120b`, and `opus5`. The revision should make proportionality a final gate for short notes and colleague messages.

- Several engines still promote source topics, constraints, or mechanics instead of synthesizing reader-facing reasons or actions. This recurred in the Big Chief, meeting-note, board-role, and audit fixtures.

## Hard failures, incomplete cells, and exclusions

| Hard-failure token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 30 | 32 |
| `more_than_four_first_level` | 5 | 0 |
| `unacknowledged_source_loss` | 5 | 16 |

No incomplete cell is identified among the 112 judged cells.

`fable5` was configured in the engine metadata but has no mapped or scored output for either arm on any supplied fixture:

| Missing engine–fixture pair | Status | Supplied reason |
|---|---|---|
| `fable5` — Big Chief | Both arms absent | Not available |
| `fable5` — TTV | Both arms absent | Not available |
| `fable5` — Period graph books | Both arms absent | Not available |
| `fable5` — Meeting note | Both arms absent | Not available |
| `fable5` — Role of board | Both arms absent | Not available |
| `fable5` — TTW visualization | Both arms absent | Not available |
| `fable5` — Headings audit | Both arms absent | Not available |
| `fable5` — Technical debt | Both arms absent | Not available |

The supplied aggregator output names no pair as explicitly excluded and gives no exclusion reason. The absent `fable5` pairs therefore cannot be classified more precisely without inventing an explanation.

## Limitations

- The English fixtures are paraphrases, so results are not directly comparable with historical Russian runs.
- There was one run per cell; the report cannot estimate run-to-run variance.
- Results depend on the participating models, their configured effort, the provider routes, and the `gpt-5.6-sol` judge and rubric.
- Engine and provider availability is only partially observable from the metadata. In particular, `fable5` was configured but is absent from the mapping and aggregate, with no supplied reason.
- The metadata spans two commits, although it states that the skill text was identical throughout.
- Fixture-level numeric deltas are not available in the deterministic scores and were therefore not derived from verdict-level scores.

## Conclusion

The skill improved pooled structure and judged quality, including penalty-adjusted quality, but the result is mixed rather than universal. Quality reversed on `gpt-oss-120b`; structure reversed on `qwen3.6-35b-a3b` and was unchanged on `gpt-oss-120b`. At the behaviour level, factual grounding, source retention, and freedom from hard failure all moved against the skill, while answer-first performance did not change.

The release evidence therefore supports better structural guidance, especially for same-kind grouping, explicit reader questions, and first-level limits. It does not support a claim of unqualified improvement. The next revision should preserve those structural gains while directly addressing invented certainty, lost source material, disproportionate scaffolding, and weak ordering discipline.