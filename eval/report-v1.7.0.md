# Minto benchmark release report: v1.7.0-final

## Scope and methodology

This report covers the skill and control arms of the supplied Minto benchmark across the listed fixtures and engines. The deterministic aggregation was generated on 2026-08-20 from 172 judged cells at commit `f4813ce76aa4da6c0296c9ee558889238ffcbd8a`; the worktree was clean, the skill text remained identical throughout, and rubric penalty version 1 was applied.

Outputs were blindly mapped to engines and arms, judged against fixture-specific verdicts and universal checks, then aggregated from the verdict JSON. Quality is reported both as judged and after the supplied hard-failure penalty.

| Pooled measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.76 (59.4%) | 5.27 (65.8%) | +0.51 | +6.4 | +10.8% |
| Quality (as judged) /10 | 7.17 (71.7%) | 7.90 (79.0%) | +0.72 | +7.3 | +10.0% |
| Quality after hard-failure penalty /10 | 6.34 (63.4%) | 7.08 (70.8%) | +0.74 | +7.4 | +11.7% |

## Results by engine

| Engine | n per arm | Structure: control → skill | Quality: control → skill | Δ quality pp |
|---|---:|---:|---:|---:|
| codex | 11 | 60.2% → 67.0% | 74.5% → 81.8% | +7.3 |
| gpt-oss-120b | 11 | 50.0% → 52.3% | 52.7% → 63.6% | +10.9 |
| haiku45 | 11 | 53.4% → 62.5% | 67.3% → 76.4% | +9.1 |
| opus5 | 11 | 62.5% → 84.1% | 73.6% → 90.0% | +16.4 |
| qwen3.6-35b-a3b | 11 | 58.0% → 67.0% | 75.5% → 79.1% | +3.6 |
| qwen3.6-fp8 | 11 | 63.6% → 69.3% | 74.5% → 80.0% | +5.5 |
| qwen3.8-27b | 9 | 62.5% → 62.5% | 78.9% → 81.1% | +2.2 |
| sonnet5 | 11 | 65.9% → 61.4% | 78.2% → 80.0% | +1.8 |

Quality moved toward the skill for every reported engine. Structure also moved toward the skill for codex, gpt-oss-120b, haiku45, opus5, qwen3.6-35b-a3b, and qwen3.6-fp8. It was unchanged for qwen3.8-27b and reversed for sonnet5.

## Behaviour pass rates

The denominator is the supplied `n` per arm. Smaller denominators indicate conditional checks.

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

The rates that moved against the skill were `no_invented_facts` at -8.2 pp and `answer_first` at -10.0 pp. All other reported behaviour rates moved toward the skill.

## Most decisive fixture-level result

| Requested result | Fixture | Control | With skill | Finding |
|---|---|---:|---:|---|
| Most decisive skill-versus-control fixture | Not available | Not available | Not available | The deterministic scores contain no fixture-level arm scores or fixture-level deltas. Selecting a fixture from the verdict cells would require new aggregation, which this report does not perform. |

## Recurring strengths

- Better structural grouping recurred across codex, gpt-oss-120b, haiku45, opus5, qwen3.6-35b-a3b, and qwen3.6-fp8. The pooled checks support this pattern: `first_level_kind_matches` moved by +12.8 pp and `first_level_count_within_limit` by +8.5 pp.
- Stronger framing recurred across engines. The skill more often supplied an SCQ introduction, wrote down the reader’s question, and named an ordering principle: +50.0 pp, +21.8 pp, and +13.0 pp respectively.
- The fixture verdicts repeatedly identify strong skill outputs from different engines as action-led, visibly hierarchical, and appropriately nested—for example in the visualization and rollout-review fixtures.
- Source preservation improved overall: `no_unacknowledged_source_loss` moved by +3.9 pp.

## Recurring defects and revision candidates

- Unsupported factual strengthening recurred across multiple engines and modes: tentative outcomes became certain, new causal links appeared, and implementation details or forecasts were added. This is the clearest grounding defect: `no_invented_facts` moved against the skill by -8.2 pp.
- Source loss remained common across multiple engines even though its aggregate rate improved. Verdicts repeatedly cite omitted evidence, context, safeguards, qualifications, and optional-status details.
- Several engines still promoted mechanics, topics, constraints, or source sections to the first level instead of deriving decision-bearing reasons or actions. The big-chief, board-role, audit, and plain-list verdicts all exhibit this pattern.
- Answer-first delivery weakened by -10.0 pp. Skill guidance on SCQ and visible structure should preserve the direct opening rather than delay it behind framing or apparatus.
- Audit outputs from multiple engines missed required apparatus or made claims beyond the visible evidence. The next revision should reinforce evidence boundaries and mode-specific delivery contracts.
- Some outputs became disproportionate to the requested format, especially short notes, colleague messages, digests, and plain lists. The revision should explicitly subordinate framework labels and formal apparatus to the requested medium.

## Hard failures, incomplete cells, and exclusions

| Hard-failure token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 42 | 49 |
| `more_than_four_first_level` | 8 | 2 |
| `unacknowledged_source_loss` | 30 | 27 |

The hard-failure tokens can coexist within a cell. The corresponding `no_hard_failure` pass rate was 30.2% for control and 31.4% with skill, a +1.2 pp change.

All verdict cells that are present are marked complete. The blind mapping contains no cells for the following engine–fixture pairs:

| Engine | Fixture | Missing arms | Aggregator’s reason |
|---|---|---|---|
| qwen3.8-27b | `02-ttv` | skill and control | Not available in the supplied deterministic scores or metadata |
| qwen3.8-27b | `10-rollout-review` | skill and control | Not available in the supplied deterministic scores or metadata |

These omissions are consistent with qwen3.8-27b having `n per arm` of 9. The supplied aggregator summary does not enumerate excluded pairs or provide exclusion reasons beyond the missing mapping, so no provider-failure explanation can be assigned.

## Limitations

- The fixtures are paraphrased English material, so the results are not directly comparable with historical Russian runs.
- There was a single run per cell; the report therefore does not measure run-to-run variance.
- Results depend on the selected engine models, their configured reasoning effort, the judge, the rubric, and the hard-failure penalty.
- The metadata records Codex, Claude, and Neuraldeep engine configurations, as well as a Kimi configuration that was not among the reported run engines. It does not provide a complete provider-availability or outage account.
- qwen3.8-27b lacks mapped cells for the listed fixture pairs, and the supplied material gives no reason for their absence.
- No fixture-level aggregate was supplied, so the most decisive individual fixture cannot be named without performing prohibited new calculations.

## Conclusion

This run supports a pooled improvement in judged structure and quality, including quality after the hard-failure penalty. Quality moved toward the skill for every reported engine. The result is not uniform: sonnet5’s structure reversed, qwen3.8-27b’s structure was unchanged, `answer_first` fell by -10.0 pp, and `no_invented_facts` fell by -8.2 pp while `invented_facts` rose from 42 to 49.

The next skill revision should retain the gains in grouping, SCQ framing, reader-question clarity, and source preservation while tightening factual grounding and restoring answer-first discipline.
---

## Appendix A — comparison with the v1.6.0 baseline (added by the maintainer run)

The sections above describe the `v1.7.0-final` run in isolation, as the report
model sees only one run. The release decision, however, rests on the
baseline-versus-final comparison below. All figures come from
`eval/compare-runs.py` over the two runs' `scores.json`; both runs score the
same 172 (fixture, engine, arm) cells, so the deltas are cell-for-cell.

`v1.7.0-baseline` ran the byte-identical 1.6.0 skill text on the same eleven
fixtures, engines and judge as `v1.7.0-final`. The control arms of the two runs
answered identical prompts, so their drift is the judge-and-sampling noise
floor.

| Measure (pooled mean) | Arm | v1.6.0 baseline | v1.7.0 final | Δ |
|---|---|---:|---:|---:|
| Structure /8 | skill | 4.721 | 5.267 | +0.547 |
| Quality (as judged) /10 | skill | 7.244 | 7.895 | +0.651 |
| Quality (penalized) /10 | skill | 6.605 | 7.081 | +0.477 |
| Structure /8 | control | 4.186 | 4.756 | +0.570 |
| Quality (as judged) /10 | control | 6.988 | 7.174 | +0.186 |
| Quality (penalized) /10 | control | 6.302 | 6.337 | +0.035 |

The controlled comparison — the within-run skill-minus-control delta — moved
from **+0.256 to +0.721** on quality as judged and from **+0.302 to +0.744**
on penalized quality, while structure stayed flat (+0.535 → +0.511). Skill-arm
quality improved on **all eight engines** (from +0.18 on haiku45 and sonnet5 to
+1.09 on opus5 and qwen3.6-fp8), against a control-arm drift of +0.186.

Skill-arm per fixture (structure / quality as judged, mean over engines):

| Fixture | baseline → final structure | baseline → final quality |
|---|---|---|
| 01-big-chief | 3.38 → 3.00 (−0.38) | 9.12 → 8.50 (−0.62) |
| 02-ttv | 4.29 → 5.43 (+1.14) | 7.14 → 7.29 (+0.14) |
| 03-period-graph-books | 4.38 → 3.88 (−0.50) | 6.25 → 6.50 (+0.25) |
| 04-meeting-note | 3.75 → 4.88 (+1.12) | 5.00 → 6.88 (+1.88) |
| 05-role-of-board | 2.88 → 2.38 (−0.50) | 7.38 → 7.00 (−0.38) |
| 06-ttw-viz | 6.38 → 7.00 (+0.62) | 8.00 → 9.00 (+1.00) |
| 07-headings-audit | 4.50 → 5.88 (+1.38) | 7.38 → 8.12 (+0.75) |
| 08-techdebt | 7.12 → 6.88 (−0.25) | 8.88 → 8.38 (−0.50) |
| 09-sources-digest | 5.25 → 6.62 (+1.38) | 6.50 → 8.62 (+2.12) |
| 10-rollout-review | 5.71 → 6.14 (+0.43) | 6.71 → 8.14 (+1.43) |
| 11-plain-list | 4.38 → 6.00 (+1.62) | 7.25 → 8.38 (+1.12) |

The three fixtures built from real usage for this round — the source digest,
the large sectioned review, and the plain pasteable list — carry the largest
gains, which is where the 1.7.0 changes were aimed.

## Appendix B — what was tried and rolled back (negative results)

The shipped text is not the first candidate. An intermediate candidate
(`eval/runs/v1.7.0`, commit `03975451e3c9`) carried two more changes, and each
added SKILL.md section then went through a removal test
(`eval/runs/v1.7.0-ablate-*`: the candidate minus one section, four engines,
the section's target fixtures, controls reused byte-identically from the
candidate run). Two changes failed their test and are **not** in the release:

- **A "Large or sectioned input" section** (pyramid per section, cross-section
  MECE pass, geometry from the material). Removing it *improved* its own target
  fixture on every metric (skill-minus-control on `10-rollout-review`:
  structure −1.000 with the section → −0.250 without; quality −1.000 → +0.750;
  penalized +0.250 → +1.000). The owner's large-document pain (П7) therefore
  remains open: this mechanism made things worse and was rolled back, and the
  fixture stays in the suite for the next attempt. Notably, `10-rollout-review`
  still improved +1.43 quality over baseline without any dedicated section.
- **A rewording of core-loop §4** ("count from the material, two honest groups
  beat three padded ones..."). Removing it helped all three target fixtures
  (01/02/04 pooled skill-minus-control: structure +0.500 → +1.167, quality
  −0.833 → −0.167). The original "3–4 first-level groups" wording is retained.

Sections that survived their removal test and shipped: the `digest` mode
(removal hurt every metric on `09-sources-digest`), the SCQ intro self-check
(removal cost −0.500 penalized on its four fixtures), and the presentation
split (kept with one amendment: the removal test surfaced that a blanket "no
closing note" suppressed omission notes and produced `unacknowledged_source_loss`,
so the shipped text explicitly owes a one-line omission note even in plain
lists). The text-skeleton default is ambiguous under the judge (raw quality
prefers removal, penalized prefers keeping) and ships on the owner's grounds:
mermaid frequently fails to render in real chat use, which a judge reading
markdown source cannot observe. The intent-dosing paragraph is exercised by no
fixture and ships unmeasured; that is recorded here rather than claimed.

## Appendix C — run-context notes the report model could not see

- The two missing qwen3.8-27b pairs (`02-ttv`, `10-rollout-review`) are hub
  failures, not judge exclusions: the model spent the whole per-cell deadline
  reasoning (660 s, retried at 1500 s) and the hub closed the connection
  without a response after ~20 minutes on every attempt. `02-ttv` completed in
  the final run but is excluded from `raw/` before blinding to pin cell
  composition to the baseline's; the pair is preserved unjudged in
  `raw-excluded/`. See `eval/neuraldeep-availability-2026-08-20.md`.
- The Kimi CLI configuration in `engines.txt` is the runner's static
  provenance block; `kimi-code/k3` was unavailable on this account and the
  engine was not part of the matrix. `kimi-k2.6` via the NeuralDeep hub was
  preflighted and excluded for failing exactly the long fixtures.
- These figures are not comparable with `report-v1.5.0-wide.md`: this round
  added three fixtures and one check, changed the NeuralDeep token budget to
  24576, and swapped the engine set. That is why the baseline was re-run in
  full rather than borrowed.
