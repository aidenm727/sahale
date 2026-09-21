# I1 — Sahale Root Identity Migration Evidence

## Checkpoint Brief

- **Why:** Align root engineering entry points with Sahale while retaining stable compatibility contracts and historical truth.
- **Risk tier:** Tier 3: repository/compiler identity, provenance, canonical selection, and future public/application cutover.
- **Exact scope:** The 22 primary paths named in the owner I1 instruction: three compiler identity modules, two current request/foundation fixtures, four compiler test modules, public-surface tests, README, AGENTS heading, five current architecture/roadmap owners, current state/mission, generator, loader presentation, and Atlas document definitions. Derived scope is this dated evidence record, the two registered generated outputs, and temporary verification fixtures. The final handoff lists the exact changed paths.
- **Exclusions:** No staging, commit, source ref/remote changes, network, external writes, checkout move, app settings, Homelab extraction, schema/protocol/storage migration, dependencies, or broad editorial/refactoring work.
- **Authority established:** Owner accepted I0 and explicitly selected bounded I1 implementation, verification and adversarial review. Exact candidate acceptance and every publication/cutover operation remain pending. Repository state and Atlas grant no authority.
- **Protected boundaries:** No personal School data, credentials, protected trees/files/history, or owner-file content inspection. The owner separately authorized reading only commit object `fcbc5957b89fe65a4313a3c23eb814e02a014698` to reproduce the identical object in temporary test fixtures. Its SHA-1 was verified from Git's exact commit-object representation; no referenced tree or parent was accessed. Source protected refs remain untouched. Historical B1a/R1 anchors remain unchanged.
- **Observable result:** A local Sahale compiler/presentation candidate that accepts both old origin families, rejects old current-request identities, and explicitly records external cutover as pending.
- **Verification:** Focused compiler/public checks, generated reproducibility, full native suite after last mutation, Atlas validation/missing/sync, complete diff, scope and owner-file hash checks, exact candidate fingerprint, then independent adversarial review. Final results and fingerprint are supplied in the handoff without mutating the verified candidate.
- **Stop conditions:** Any non-derived scope expansion, protected access beyond the exact commit object, protocol/storage change, external action, or verification remediation outside the accepted boundary.
- **Next decision boundary:** Owner acceptance of the exact verified and independently reviewed local candidate; separate commit and cutover authorities afterward.

## Baseline and Native Environment

Base and locally observed origin/main: `13192c095dd48262b42eafca9173a0d06e4d7c18`, branch `main`, no tracked changes. Origin remains `git@github.com:aidenm727/aiden-platform.git`; checkout remains `~/src/t430-homelab`. R2 is published, with intentional idle observed before I1 selection. The only unrelated untracked file is `Summer_2027_Internship_Review_Aiden_Menefee.md`; only a byte-preservation hash is retained outside the repository.

Python 3.10.12 and Git 2.34.1 are available. Authorized repository files are writable. Verification uses `/tmp/sahale-i1/verification-checkout`, built only from local main history and overlaid with the exact candidate files, excluding the unrelated owner file. Bubblewrap mounts source read-only and disables networking; task-owned temporary roots provide `/tmp` and `/var/tmp`. No live School root, host service or device is needed. Bytecode writing and guarded historical tests are disabled. The original checkout is not moved.

The first main-only full baseline ran 556 tests with 56 fixture-setup failures, one setup error and one guarded skip: the pinned protected commit was absent. This was an environment failure before product assertions, not accepted product debt. After the exact owner authorization, temporary Git templates supply only that verified commit object to fixture object databases. A focused baseline covering current origins, selectors, selection, materialization and public surface passed 118 tests with one guarded skip. The public-surface baseline also separately passed 19 tests. No source protected reference was read or copied.

The bare-target test now clones only main from its source fixture. This avoids transport traversal of non-main protected references while preserving the bare-target rejection assertion. Fixture ref writes occur only in temporary test repositories. Historical source commits, blob anchors, and package examples are not rewritten.

## Candidate Contracts

Current request and normalized repository identity: `github.com/aidenm727/sahale`. Origins for `sahale`, `aiden-platform`, and `t430-homelab` each support exactly SCP SSH, ssh://, HTTPS with .git, and HTTPS without .git. Both former slugs are origin aliases only. Raw origin ordering and strict unrelated/malformed/conflicting-origin rejection remain intact.

The current request fixture changes its repository identity; only dependent request digest and package-identity-helper values are recalculated. Newly compiled identities differ intentionally. Synthetic historical packages retain their recorded repository identities, validate without byte mutation, and fail integrity validation if merely relabeled Sahale. Current snapshot/selection/materialization reject old request identities.

Generated output remains `docs/aiden-context.md`, rendered as Sahale Context only through `tools/generate-context.py`. `AIDEN_CONTEXT_GENERATED_FROM` and the loader filename remain unchanged. No duplicate artifacts or aliases are added. The generator also owns `docs/infrastructure-snapshot.md`, whose bytes should remain unchanged.

Retained contracts: `aiden.context-compilation`, `aiden.task-context.*`, `urn:aiden-platform:task-context:schema:*`, `aiden.school.*`, `AIDEN_SCHOOL_DATA_ROOT`, `~/.local/share/aiden-platform/school`, `AIDEN_RUN_GUARDED_B2A`, and established capability compatibility IDs including `ai-aiden-os`. Personal data existence is neither inspected nor inferred.

Canonical state retains the published R2 phase and selects I1 for local work. Empty checkpoint evidence_refs avoid inventing a commit for this uncommitted record; the mission links this record directly. Candidate acceptance and cutover remain pending. Current-facing wording changes only within authorized owners; historical examples, evidence, opportunities, commits and filenames remain historical.

## Future Cutover and External Unknowns

This plan grants no authority. After exact candidate acceptance:

1. Create one separately authorized local commit.
2. Re-verify GitHub target availability, stable repository identity, relevant settings and actual external consumers. Owner-supplied observations (Pages absent, Codex displayed as Aiden Platform) require fresh confirmation; no particular webhook or integration is assumed.
3. Separately authorize and perform the GitHub rename to `aidenm727/sahale`.
4. Verify required Git/web/API and applicable raw/archive URL behavior for new and both former slugs, including successive-rename and old-slug non-reuse assumptions. R1 observations are dated evidence, not current guarantees.
5. Under separate authority update origin, non-force publish to canonical main, and verify local HEAD, tracking and remote alignment.
6. Stop dependent sessions; separately authorize moving the full checkout from `~/src/t430-homelab` to `~/src/sahale`, preserving the unrelated owner file.
7. Update authorized Codex/IDE references and reopen; verify discovery, Atlas, generation and compiler behavior from the new location.
8. Complete any required publication/cutover lifecycle follow-up with its own verification, review, acceptance and publication boundary.

Identity migration precedes Homelab extraction; neither the Homelab repository nor its extraction is part of I1.

## Rollback

Before external rename, correct or discard only the authorized candidate, preserving unrelated owner changes. After rename, prefer finishing a healthy cutover; a reverse GitHub rename needs fresh verification and separate authority. Compiler rollback must retain any origin already put into use, including Sahale. Restore an old origin only after verifying its destination. Move the checkout back only after stopping dependent sessions and excluding path collisions; restore recorded application references under separate authority.

Presentation rollback changes canonical/generator sources and regenerates, never edits generated output directly. Schemas, School data, environment contracts and historical evidence need no migration rollback. Preserve this evidence and newly issued package identities even if a later current name changes.

## Final Verification and Review Boundary

Exact native command inside the isolated candidate checkout:

    PYTHONPATH=tools PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py'

Use focused context snapshot, selectors, selection, materialization, compilation, validation, inputs and public-surface modules first. Run the full suite after the last candidate mutation, followed by Atlas validate/missing/sync, generated byte comparison, complete diff and candidate fingerprint checks. Independent adversarial review challenges strict alias boundaries, old-request rejection, historical package integrity, scope/history preservation, pending-cutover truth, and rollback. Blocking corrections require renewed final verification and review. This record itself does not claim final acceptance, successful external cutover, or publication.

## Focused Results and Candidate Identification

The corrected focused command passed 241 tests in 36.144 seconds, one guarded skip, exit 0:

    PYTHONPATH=tools PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_context_snapshot tests.test_context_selectors tests.test_context_selection tests.test_context_materialization tests.test_context_compilation tests.test_context_validation tests.test_context_inputs tests.test_public_surface

Earlier focused correction findings were one newly identity-dependent snapshot hash expectation, two subtest errors copying immutable synthetic package mappings, and a missing temporary Git-template info directory. These were corrected without changing historical commit/blob anchors, product validation behavior, or privacy guards. Public-surface self-disposition adjustments change line locations only; match classes, functions, literal hashes and counts remain identical. The legacy-name inventory adds only the mission, its generated projection, and this evidence record to describe the pending checkout accurately.

The final full-suite and independent-review attestations are reported in the owner handoff after this record is frozen. The candidate fingerprint is SHA-256 of UTF-8 JSON with sorted keys and compact separators, containing base_commit and a path-sorted files array. Each entry records repository-relative path, Git-style mode (100644 or 100755), and SHA-256 of final file bytes. It covers every changed candidate file, including this untracked evidence, and excludes the unrelated owner file. The base commit is the baseline above. No commit identity is invented for the candidate.

## Exact Changed Paths

- `AGENTS.md`
- `README.md`
- `docs/aiden-context.md`
- `docs/architecture/engineering-environment.md`
- `docs/architecture/platform.md`
- `docs/architecture/repository.md`
- `docs/architecture/task-scoped-agent-context-compilation.md`
- `docs/current-mission.md`
- `docs/current-state.json`
- `docs/reviews/sahale-i1-root-identity-migration-evidence-2026-09-18.md`
- `docs/roadmaps/platform-strategy.md`
- `tests/fixtures/task_context/expected/example-eo-2026-013-foundation-values-v1.json`
- `tests/fixtures/task_context/requests/example-eo-2026-013-read-only-assessment-v1.json`
- `tests/test_context_materialization.py`
- `tests/test_context_selection.py`
- `tests/test_context_selectors.py`
- `tests/test_context_snapshot.py`
- `tests/test_public_surface.py`
- `tools/aiden-context-loader.py`
- `tools/atlas/platform/context_compilation/materialization.py`
- `tools/atlas/platform/context_compilation/snapshot.py`
- `tools/atlas/platform/document_definitions.py`
- `tools/atlas/platform/reasoning/context_selection.py`
- `tools/generate-context.py`
