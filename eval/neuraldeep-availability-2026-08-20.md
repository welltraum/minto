# NeuralDeep evaluation availability — 2026-08-20

Fresh snapshot of `GET /v1/models` and a preflight of every chat-capable
candidate before the v1.7.0 baseline/candidate runs. Same procedure as
`neuraldeep-availability-2026-08-05.md`: one short control prompt and the two
bracketing skill prompts (`04-meeting-note`, 24.5 KB, shortest output;
`03-period-graph-books`, 26.1 KB, audit, longest output), single attempt,
550-second read timeout.

## What the hub lists today

Twenty models. Chat-capable candidates: `gpt-oss-120b`, `qwen3.6-35b-a3b`,
`qwen3.6-fp8`, `qwen3.8-27b`, `kimi-k2.6`, `gemma-4-31b`, plus `-noreason`
variants of the three reasoning models. The rest are embedding, reranker and
speech models (`e5-large`, `bge-m3`, `bge-reranker`, `whisper-1`, `frida`,
`jina-embeddings-v4`, `qwen3-embedding-4b`, `giga-embeddings`,
`whisper-podlodka-turbo`, `gigaam-v3`, `gemma-4-31b-noreason`,
`qwen3.6-fp8-noreason`, `qwen3.8-27b-noreason`) and are not evaluation
candidates.

New since 2026-08-05: `kimi-k2.6`, `qwen3.6-fp8(-noreason)`,
`qwen3.8-27b(-noreason)`, `gigaam-v3`, `whisper-podlodka-turbo`.

## Preflight results

At the default `NEURALDEEP_MAX_TOKENS=8192`, both new reasoning models returned
an **empty assistant message** on skill prompts after long latencies: the entire
completion budget went to reasoning tokens and no visible content survived. The
second pass below raised the budget to 24576 for the two affected models.

| Model | Control | 24.5 KB skill prompt | 26.1 KB skill prompt (audit) | Status |
|---|---|---|---|---|
| `gpt-oss-120b` | 8 s | 19 s | 42 s | **Admitted** |
| `qwen3.6-35b-a3b` | 36 s | 62 s | 59 s | **Admitted** |
| `qwen3.6-fp8` | 26 s | 50 s | 62 s | **Admitted** (new) |
| `qwen3.8-27b` | 21 s | empty at 8192; 145 s at 24576 | empty at 8192; **464 s** at 24576 | **Admitted at `NEURALDEEP_MAX_TOKENS=24576`** |
| `kimi-k2.6` | 117 s | empty at 8192; 226 s at 24576 | empty at 8192; timeout at 550 s even at 24576 | **Excluded** |
| `gemma-4-31b` | 46 s | read timeout at 550 s | read timeout at 550 s | **Excluded** (unchanged since 2026-08-05) |

## Decisions

- The run matrix uses `NEURALDEEP_MODELS="gpt-oss-120b qwen3.6-35b-a3b
  qwen3.6-fp8 qwen3.8-27b"` with `NEURALDEEP_MAX_TOKENS=24576` and
  `NEURALDEEP_TIMEOUT=550` for the whole batch, recorded in `engines.txt`. The
  raised token budget applies to all four so the arm conditions stay uniform
  within the run; it makes these cells not directly comparable to the 8192-budget
  cells of `v1.5.0-wide`, which is one more reason the v1.7.0 comparison re-runs
  its own baseline instead of borrowing old cells.
- `qwen3.8-27b` is in despite its 464-second worst case because its results are
  an explicitly requested point of interest for this round. Its margin under the
  660-second process deadline is thin; if it times out on the new long-document
  fixture, the pair is dropped by `--allow-partial` and the absence is reported,
  not backfilled.
- `kimi-k2.6` is excluded for the same reason `gemma-4-31b` was on 2026-08-05:
  it completes easy cells and fails exactly the hard ones, so its presence would
  bias the delta rather than reduce `n`.
- `-noreason` variants are excluded: they are the same weights as their
  reasoning counterparts with reasoning disabled, so admitting both would put one
  model in the matrix twice under two names.
- The Kimi Code CLI engine (`kimi`, `kimi-code/k3-low`) is out of this round's
  matrix entirely: k3 is not available on this account at run time.

## Key handling

The key came from the gitignored `.env`, exported into the environment for the
preflight only. Nothing key-shaped is written to this file, `engines.txt`, or
any log. The rotation asked for on 2026-07-30 is still outstanding.
