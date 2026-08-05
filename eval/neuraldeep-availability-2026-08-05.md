# NeuralDeep evaluation availability — 2026-08-05

Re-preflight of the three NeuralDeep models before the wide skill-versus-control
run, following the four steps set out in `neuraldeep-availability-2026-07-30.md`.

## Outcome

Two of the three models now complete both arms on the longest fixture and were
admitted to the matrix. One still cannot and was excluded.

| Model | Short control prompt | 24.5 KB skill prompt (`04-meeting-note`) | 26.1 KB skill prompt (`03-period-graph-books`, audit) | Status |
|---|---|---|---|---|
| `gpt-oss-120b` | Completed, 7 s | Completed, 12 s | Completed, 55 s | **Admitted** |
| `qwen3.6-35b-a3b` | Completed, 45 s | Completed, 73 s | Completed, 40 s | **Admitted** |
| `gemma-4-31b` | Completed, 27 s | Completed, 47 s | Read timeout at 300 s, and again at 550 s | **Excluded** |

`gpt-oss-120b` is a clear improvement on 2026-07-30, when it timed out on the
representative skill prompt at both output budgets. `qwen3.6-35b-a3b` no longer
shows the ten-minute-plus latencies recorded then. `gemma-4-31b` is unchanged.

## Why `gemma-4-31b` was excluded rather than partially included

It completes short fixtures and fails long ones. Including it would have
contributed only the fixtures it finds easy, so its per-engine numbers would
describe a subset chosen by its own latency rather than by the benchmark.

The harness would have handled the gap correctly — `shuffle.sh` and
`aggregate.py` both enforce both-arms-or-neither per `(fixture, engine)`, and
`--allow-partial` would have dropped the affected pairs with a recorded reason.
That protects the pooled delta. It does not make a systematically incomplete
engine worth reporting.

A uniformly absent engine only reduces `n`. An engine absent from exactly the hard
fixtures is a bias, which is the distinction the exclusion turns on.

## Runner behaviour confirmed by this preflight

- The failed `gemma-4-31b` cell left no file: `FAIL … (0 B, removed)`. Before the
  poison-pill fix, a zero-byte output would have survived the resume skip, been
  blinded, and been judged as a model output.
- `NEURALDEEP_TIMEOUT` above roughly 600 seconds is pointless: the outer process
  deadline is 660 seconds, so 550 is the practical ceiling for a single attempt.
- The key was supplied through a gitignored `.env`, read into the environment for
  the run only. `engines.txt` records the base URL, temperature, token budget,
  timeout, attempts, and concurrency — never the key.

## Still outstanding

Rotate the API key after this run. Step 1 of the 2026-07-30 note asked for a
rotation that does not appear to have happened; the key used today was supplied in
plain text in a chat session, which is reason enough on its own.
