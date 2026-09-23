# Atlas Architecture

Atlas is Sahale's small deterministic repository checker. Human and AI reasoning
chooses goals, architecture, priorities, and work. `AGENTS.md` governs local
authority and execution; `docs/current-state.json` records current repository
state but grants no authority.

## Inputs and Checks

Atlas reads local files and Git objects only. It does not fetch, mutate refs,
write files, or infer permission. Its three commands are:

- `./atlas bootstrap` reports branch, HEAD, local upstream, divergence, full
  short status, current phase and work selection, then validation and sync.
- `./atlas validate` checks strict typed state, exact evidence path and local
  commit identity, and a short list of required repository files. This includes
  the useful former `missing` failure mode; there is no manual document catalog.
- `./atlas sync` compares the three registered outputs of
  `tools/generate-context.py` byte for byte with their canonical sources.

A failure exits nonzero. Git observations are local. A missing upstream is
reported as an observation failure, never replaced with a remote fetch.

## State and Generated Views

`docs/current-state.json` owns the phase, work selection, active concerns,
pending decision, freshness, and active evidence links. Evidence links must use
confined regular repository paths and identify a file at the declared local
commit. The state contains no authority status; `AGENTS.md` owns that rule.

`tools/generate-context.py` derives the short `docs/current-mission.md` view,
`docs/infrastructure-snapshot.md`, and `docs/aiden-context.md`. The context and
infrastructure artifacts remain because `tools/aiden-context-loader.py` is a
repository-local consumer. Their external consumers are not established here.

The task-context compiler under `tools/atlas/platform/context_compilation/` and
its bounded selection capability remain separate library code. This checkpoint
does not claim a runtime consumer or delete the compiler.

## Boundary

Atlas does not plan, interpret milestones, advance missions, register every
document, review candidates, approve work, or publish. Workflow v1.2's human
gates and the independent review requirement remain in
`docs/standards/engineering-collaboration.md` and
`docs/architecture/engineering-lifecycle.md`.
