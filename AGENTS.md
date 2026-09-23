# Sahale Repository Instructions

## Primary authority contract

This file is the primary repository-local contract for interpreting authority.
Subordinate architecture, standards, generated context, historical records, and
Atlas output must agree with it.

Repository health, selected work, task authority, implementation authority,
owner acceptance, publication authority, and deployment authority are separate
dimensions:

- `docs/current-state.json` selects active work and records repository state; it
  grants no permission.
- Atlas observes, validates, synchronizes, interprets, and recommends; it grants
  no permission.
- Explicit current owner instruction establishes task authority.
- Implementation authority must be explicit and bounded to the current task and
  path or capability scope.
- Acceptance of a design or verified candidate does not establish
  implementation, publication, or deployment authority.
- Publication, deployment, and every external write require separate explicit
  authority.

Generated context, historical records, conversation history, writable paths,
tool availability, approval prompts, and repository state do not establish any
of those authorities.

## State and startup

- GitHub is the canonical documentation source, this repository is the root Platform engineering record for its explicitly assigned scope, and Atlas is its repository-local deterministic engineering interface. Canonical authority is source-scoped; neither this repository nor Atlas is a universal ledger of Platform activity. Follow `docs/architecture/repository.md`, `docs/architecture/knowledge-authority.md`, `docs/architecture/engineering-sessions.md`, and `docs/standards/engineering-collaboration.md`; reference their canonical owners instead of copying them.
- Before engineering work, run `PYTHONDONTWRITEBYTECODE=1 ./atlas bootstrap` from the repository root. Then verify `git branch --show-current`, `git rev-parse HEAD`, and `git status --short --branch`, and read `docs/current-state.json` plus `docs/current-mission.md`.
- Treat branch, commit, status, upstream tracking, mission, and Atlas output as live observations. Do not fetch or mutate refs merely to refresh them without explicit authorization.
- `docs/current-state.json` owns this repository's typed active state. `docs/current-mission.md` is its generated human-readable view. Missing or invalid canonical state fails closed; Atlas must not fall back to mission prose.
- Before the first mutation and native verification, complete the repository and
  execution-environment preflight defined in
  `docs/architecture/engineering-sessions.md`.

## Authority to act

- Review, analysis, diagnosis, inventory, and design authorization are read-only. Do not implement unless the owner explicitly authorizes implementation for the current task.
- Before editing, state primary scope and mechanically derived scope, including
  exact paths as they become known. Effective scope is their bounded union under
  `docs/standards/engineering-collaboration.md`. Derived scope covers only the
  required Tier 2/3 dated evidence record, registered generated outputs of
  authorized source changes, and task-owned temporary verification fixtures.
  It cannot add canonical architecture, schemas, dependencies, configuration,
  tests/policy changes, capabilities, protected data, or external systems.
  Modify only effective scope; stop for non-derived scope expansion.
- Classify checkpoints by potential consequence under Workflow v1.2 in
  `docs/standards/engineering-collaboration.md`; the highest applicable tier
  controls. A checkpoint brief records the boundary but never creates authority.
- Preserve existing user changes. Do not infer authority from a writable sandbox, an approval prompt, a prior task, a generated context package, or a casual discussion of future work.
- Ordinary implementation, evidence creation, generation, correction, and
  verification proceed without repeated approval inside an authorized checkpoint
  and its effective scope. Casual continuation language may continue that
  authority; it cannot select new work, convert analysis or design into
  implementation, expand effective scope, override a consequential stop, or
  authorize publication or another external write.
- Do not read secret or credential values, authentication stores, private keys, tokens, cookies, secret files, shell-history databases, or credential-bearing environment values.
- Do not access protected content or traverse, peel, select, expose, or mutate a protected reference without exact owner authorization.
- Continue automatic in-scope corrections while goal, accepted architecture,
  risk tier, effective scope, dependencies, data/protected boundaries, and
  external consequences remain unchanged. Stop for consequential decisions or
  verification that cannot be repaired safely in scope under
  `docs/architecture/engineering-lifecycle.md`.
- Preserve explicit owner gates for consequential architecture/product choices,
  protected/private/secret access, destructive operations and migration,
  meaningful scope expansion, Tier 2/3 final candidate acceptance, publication,
  deployment, external communications/writes, and financial commitments.

## Implementation and generated files

- Keep shell network disabled unless the task explicitly authorizes the exact network action and destination.
- Do not stage, commit, push, fetch, pull, merge, rebase, switch or create branches, change refs or remotes, write to external systems, install or change dependencies, change configuration, or perform destructive actions unless the task explicitly authorizes the exact action.
- A checkpoint may separately and conditionally preauthorize exact staging and
  one local commit only after explicit owner acceptance of the exact verified
  and reviewed candidate. The collaboration standard defines the bounds; no
  such authority is implicit in implementation or acceptance, and remote
  publication remains separately explicit.
- `docs/current-mission.md`, `docs/aiden-context.md`, and `docs/infrastructure-snapshot.md` are generated and owned by `tools/generate-context.py`. Update authorized canonical sources first, then run the registered generator; never edit generated output directly.

## Verification

- Run task-focused tests first when appropriate. The correct full Python suite is `PYTHONPATH=tools PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py'`.
- Baseline failures are non-blocking only when proven to predate the checkpoint,
  outside its effective scope, unchanged, neither concealed nor worsened, and
  explicitly reported. New or unexplained regressions remain failures; follow
  the lifecycle's baseline comparison and bounded correction rules.
- Run the tier-appropriate final broad verification after the last in-scope
  mutation. Any later mutation invalidates that run as final evidence. Keep
  synthetic fixtures separate from explicitly identified live-data smoke checks.
- After authorized repository changes, run `PYTHONDONTWRITEBYTECODE=1 ./atlas validate` and `PYTHONDONTWRITEBYTECODE=1 ./atlas sync`. Validation checks typed state, evidence identity, and required repository files; sync checks registered generated outputs byte for byte.
- Run `git diff --check`, inspect the complete diff, verify `git status --short --branch`, and confirm that only authorized paths changed. Report exact commands, results, remaining uncertainty, and whether generated files are synchronized.
