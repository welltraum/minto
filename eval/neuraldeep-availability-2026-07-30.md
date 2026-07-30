# NeuralDeep evaluation availability — 2026-07-30

## Outcome

The NeuralDeep integration authenticated and returned valid responses from all
three requested model IDs, but provider stability was insufficient for a
complete release matrix. No quality scores or skill-versus-control conclusions
were produced from the incomplete outputs.

Claude was not attempted because it was unavailable for this run.

## Evidence

| Model | Short control prompt | Representative full skill prompt | Expanded run | Release status |
|---|---|---|---|---|
| `gemma-4-31b` | Completed | Timed out after 300 seconds with a 4096-token output budget | Some early cells completed; another skill cell ended after repeated remote connection closures, and later cells stalled | Unavailable |
| `gpt-oss-120b` | Completed | Timed out after 300 seconds with both 8192- and 4096-token output budgets | Not launched after the representative preflight failed | Unavailable |
| `qwen3.6-35b-a3b` | Completed | Completed with `finish_reason=stop` | Several cells completed, but latency ranged from tens of seconds to more than ten minutes and a later skill cell stalled | Unavailable for a complete matrix |

The short tests establish that the API key, base URL, model IDs, request schema,
and response parser were valid. They do not establish that the models were
available for the sustained benchmark workload.

## Runner changes validated

- NeuralDeep uses the OpenAI-compatible `/v1/chat/completions` endpoint.
- Credentials are read from `NEURALDEEP_API_KEY` and are not written to
  repository files or evaluation metadata.
- The three model IDs are selectable as eval engines.
- NeuralDeep concurrency defaults to two requests.
- Retryable HTTP failures are retried, while every API attempt has a five-minute
  read timeout.
- The outer process has a hard deadline, preventing an unresponsive socket from
  blocking the full run indefinitely.
- Blind shuffling and judging accept a caller-supplied number of outputs per
  fixture, allowing matrices larger than the historical four-output setup.
- Engine metadata records the dirty/clean worktree state and SHA256 values for
  the tested skill, rules, and templates.

## Interpretation

The repository change under evaluation added a maintainer-facing source index
and evaluation infrastructure; it did not change `SKILL.md`, `rules.md`, or
`templates.md`. The generated skill prompts therefore contained the same
runtime instructions as before. A future behavioral MECE change still requires
a fresh, complete skill-versus-control run.

Before that run:

1. Rotate the API key used during this session.
2. Run the documented representative preflight for every selected NeuralDeep
   model.
3. Start the full matrix only when both arms complete for every model.
4. Preserve incomplete cells as availability evidence; do not replace them with
   another model or assign scores.
