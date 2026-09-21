# Current Mission

`docs/current-state.json` is the canonical typed active-state record. This
document is its short human-readable companion. Machine-readable state wins if
the two disagree.

## Phase

R2 — Sahale Repository Architecture Refresh — Published

## Active State

W2 — Engineering Workflow v1.2 is the published repository workflow at
`d40c2891bd5cf79f674498ac6b5fed6bb1beac47`, as confirmed by the current
owner instruction. W1 remains historical published workflow evidence. Clean
Foundation F1 remains historical published foundation evidence rather than
active selected work. R1 — Repository Identity and Public/Private Boundary is
owner-accepted, published, and complete. G14 Storage Orientation Snapshot is
owner-accepted, published, and complete. SL2-A — School Learning v0.2 Semester
Core & Intake is owner-accepted, published, and complete. Its substantive
publication identity is `faf99fdadae8e9ce035c8ee4f6dfb1aae1d4cf95`, and the
normal publication push was verified on `origin/main` before this lifecycle
synchronization. The School Learning Operational Loop passed its final
independent Tier-2 review with no BLOCKING, MATERIAL, or MINOR findings, is
owner-accepted, and is published and complete at
`00805e67057fcd68e9ea465749a2c8a1df2cd7f7`. Publication completed on
2026-08-31.

R2 — Sahale Repository Architecture Refresh is owner-accepted, published, and
complete at `b8d5b9ea0ccc7f6084c723f96a3c79382abf6d62`
(`docs: refresh Sahale architecture for R2`). The owner accepted the exact
independently reviewed candidate with fingerprint
`9a05e56ed478908812e7b144c1bdc55c506abebb68dfbffa6bf33e2c4e3c2a54`,
then separately authorized its one commit and non-force publication to canonical
main. Publication succeeded on 2026-09-18. At lifecycle-synchronization startup,
local HEAD, origin/main and freshly observed remote main all matched that commit.
R2 no longer awaits candidate acceptance or publication and is no longer active
selected implementation work. I1 is now selected for local implementation only.

Canonical state effective date: 2026-09-18.

C1 is the owner-confirmed published baseline at
`5dc5ccb75556aee74a6684a231fa012350d403e4`, also the locally observed base
and tracking identity at R2 startup. No remote verification was performed. Its
historical pre-publication verification and acceptance boundary is recorded in
`docs/reviews/current-state-baseline-debt-c1-evidence-2026-09-16.md`. The
September 8 School storage spike is retained only as provisional dated
evidence; its proposed architecture is not accepted and its unfinished review
gate remains open. No School runtime or storage change is selected here.

## Mission Intent

Preserve published W2, historical W1, completed R1, G14, SL2-A, and the School Learning
Operational Loop, human authority, generated ownership, and all public/private
boundaries after completed R2 while preparing the bounded I1 local candidate.
No deployment, live-data migration, Canvas/Gmail/Calendar integration, or operational-runtime state is
established.

## Work Selection

- Status: Selected.
- Selected checkpoint: I1 — Sahale Root Identity Migration.
- I1 lifecycle: Selected local implementation; not owner-accepted or published.
- R2 lifecycle: Owner-accepted, published, and complete at
  `b8d5b9ea0ccc7f6084c723f96a3c79382abf6d62`; not active selected work.
- I0 design: Accepted by the owner for the bounded I1 implementation.
- G14 lifecycle: Owner-accepted, published, and complete; not active selected
  work. Deployment, live collection, and operational runtime are not claimed.
- W2 lifecycle: Published repository workflow; not active selected work.
- W1 lifecycle: Historical, published and complete; not active selected work.
- R1 lifecycle: Owner-accepted, published, and complete; not active selected
  work.
- SL2-A lifecycle: Owner-accepted, published, and complete; not active selected
  work.
- School Learning Operational Loop lifecycle: Owner-accepted, published, and
  complete at `00805e67057fcd68e9ea465749a2c8a1df2cd7f7`; not active selected
  work. No deployment, live migration, or external integration is claimed.
- S1, F2, F3, SL2-B, and all other future implementation checkpoints: Not
  selected.

## Next Milestone

I1 — Sahale Root Identity Migration

## Blockers

None recorded in canonical active state.

## Unknowns

None recorded in canonical active state.

## Owner Decision Required

Owner acceptance of the exact verified and independently reviewed I1 local
candidate. S1, F2, F3, SL2-B, and other future checkpoints remain unselected.
Staging, commit, GitHub rename/settings, remote mutation, publication, checkout
move, and Codex/IDE updates remain separately authorized gates.

## I1 Candidate and Pending Cutover Boundary

Sahale is the human-facing personal capability platform identity. The local
I1 candidate requires `github.com/aidenm727/sahale` in current compiler requests.
Origins for `sahale`, `aiden-platform`, and `t430-homelab` normalize to it; old
request identities are not silently upgraded. The observed GitHub origin still
names `aidenm727/aiden-platform`, and the checkout remains `~/src/t430-homelab`.
The accepted future checkout is `~/src/sahale`; no cutover has occurred.
Schemas, protocols, environment variables, persisted data, and history remain
unchanged. `docs/aiden-context.md` keeps its filename and now displays Sahale.
Context coordination is a cross-cutting responsibility
above the existing deterministic compiler, with no new runtime. Homelab's
workspace, source/domain, and execution roles remain distinct from Sahale
capability ownership. No UI, Homelab extraction, or external action is authorized.

The owner reports that the ChatGPT Project is now Sahale, with functional
workspace names and one bounded `sahale-orientation.md` source replacing six
static dated sources. This is supplied interaction/design evidence, not
independently inspected configuration or canonical engineering truth. Durable
architecture belongs in the designated repository owners; Project configuration
is not managed by R2.

## Authority Boundary

Repository state selects work but grants no task, implementation, publication,
deployment, or external-write authority. Atlas observes and explains state but
grants no authority. Any task, implementation, staging, commit, ref or remote
mutation, publication, deployment, GitHub action, or other external write
requires explicit owner authority outside repository state and Atlas.
`AGENTS.md` is the primary repository-local authority-interpretation contract.

## Evidence and History

- `docs/reviews/sahale-i1-root-identity-migration-evidence-2026-09-18.md` —
  local uncommitted I1 evidence; no fabricated publication identity.

- `docs/reviews/sahale-r2-architecture-refresh-evidence-2026-09-18.md` at
  `b8d5b9ea0ccc7f6084c723f96a3c79382abf6d62` — immutable R2 implementation
  and pre-publication evidence. Its uncommitted/unaccepted/unpublished wording
  describes the historical candidate boundary, not the current R2 lifecycle.
  Owner acceptance and completed publication are attested above; the historical
  record is preserved unchanged.
- `docs/reviews/sahale-r2-lifecycle-synchronization-evidence-2026-09-18.md` —
  local follow-up lifecycle evidence and verification/acceptance boundary.
  Published synchronization commit: `13192c095dd48262b42eafca9173a0d06e4d7c18`.

- `docs/reviews/engineering-workflow-v1-2-evidence-2026-09-16.md` — W2
  implementation evidence at `d40c2891bd5cf79f674498ac6b5fed6bb1beac47`.
  Its pre-publication narrative is historical; the current owner confirms
  publication. No remote was contacted during C1.
- `docs/reviews/school-learning-vnext-storage-spike-evidence-2026-09-08.md`
  — provisional synthetic storage findings, retained without architecture
  promotion or completion of the original review gate.

- `docs/current-state.json` — canonical typed active state and repository-local
  evidence references.
- `docs/reviews/engineering-workflow-v1-1-evidence-2026-08-01.md` — compact W1
  checkpoint, acceptance, and publication evidence at the accepted candidate
  commit `27d99c1eb0ab30f7fcd11158f4c1d856bd6913de`.
- `docs/reviews/clean-foundation-f1-acceptance-and-publication-2026-07-31.md`
  at `7339e1676f7588e319e3cb004d56baf56a37bed6` — historical accepted and
  published F1 foundation evidence.
- `docs/reviews/repository-identity-r1-evidence-2026-08-02.md` — compact R1
  chronology through owner acceptance, first publication, the verified rename,
  post-rename identity finalization, and the published-and-complete lifecycle
  transition.
- `docs/reviews/g14-storage-orientation-snapshot-implementation-evidence-2026-08-08.md`
  — compact Tier 3 G14 implementation, review, acceptance, verification,
  residual-limitation, and publication-boundary evidence.
- `docs/reviews/school-learning-v0-2-a-semester-core-intake-evidence-2026-08-26.md`
  — dated non-canonical compound SL2-A implementation, correction/review,
  candidate acceptance, repository-finalization, publication, and
  post-publication lifecycle-synchronization evidence.
- `docs/reviews/school-learning-operational-loop-implementation-evidence-2026-08-30.md`
  — dated non-canonical compound Operational Loop implementation, final review,
  owner acceptance, publication, and lifecycle-synchronization evidence at
  `00805e67057fcd68e9ea465749a2c8a1df2cd7f7`.
- Git history — immutable implementation and publication identities.
