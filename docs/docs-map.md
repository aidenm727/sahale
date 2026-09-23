# Documentation Map

## Purpose

This document is the navigation starting point for the root Sahale engineering
repository and its assigned scope. `docs/architecture/repository.md` defines
selective specialized ownership; `docs/architecture/knowledge-authority.md`
defines source-scoped authority.

```text
Why it exists
  -> How it is structured
  -> Which capabilities it develops
  -> What is active
  -> What currently exists
  -> How changes are performed
  -> What may happen next
```

---

## Documentation Layers

1. Vision
2. Architecture
3. Standards
4. Canonical Active State and Generated Human View
5. Infrastructure
6. Operations
7. Roadmaps
8. Generated Context

Repository Objects and engineering tools support these layers. Atlas does not catalog every document or interpret selected work.

---

## Vision

- `docs/vision.md`

## Primary Platform Architecture

- `docs/architecture/platform.md`
- `docs/architecture/capabilities.md`
- `docs/architecture/ai.md`
- `docs/architecture/repository.md`
- `docs/architecture/atlas.md`

## AI and Knowledge Architecture

- `docs/architecture/ai-operating-model.md`
- `docs/architecture/knowledge-authority.md`
- `docs/architecture/context-coordination.md` — Cross-cutting bounded source-resolution responsibility above deterministic compilation; future runtime remains deferred.
- `docs/architecture/task-scoped-agent-context-compilation.md`
- `docs/task-context/index.md`

## Learning and Research Architecture

- `docs/architecture/school-learning.md` — Semester-aware School Learning architecture, owner-controlled external state, explicit opaque intake, assessments/policies/provenance, conflict-preserving truth boundaries, and manual portable handoffs.

## Engineering Architecture

- `docs/architecture/engineering.md`
- `docs/architecture/engineering-environment.md`
- `docs/architecture/engineering-lifecycle.md`
- `docs/architecture/engineering-sessions.md`
- `docs/architecture/engineering-review.md`

## Repository Objects

- `docs/architecture/repository-object.md`

## Historical Atlas Design

Earlier capability, reasoning, metadata, synchronization, intelligence,
milestone, mission-advancement, and architecture-registration designs remain in
Git history and dated evidence. Surviving referenced design pages carry
supersession notices. `docs/architecture/atlas.md` defines the current checker
contract.

## Engineering Opportunity Architecture

These documents preserve opportunity design history and structured candidate
vocabulary. Atlas no longer assesses or selects opportunities.

- `docs/architecture/engineering-opportunity.md`
- `docs/architecture/engineering-opportunity-object.md`
- `docs/architecture/engineering-opportunity-assessment.md`
- `docs/architecture/engineering-opportunity-capability-alignment.md`
- `docs/architecture/engineering-opportunity-scope-classification.md`
- `docs/architecture/engineering-opportunity-distinctness-analysis.md`

## Artifact and Infrastructure Architecture

- `docs/architecture/artifact-transport.md`
- `docs/architecture/implementation-artifacts.md`
- `docs/architecture/compute.md`

## Standards

- `docs/standards/engineering-collaboration.md`

## Canonical Active State

- `docs/current-state.json` — Strict typed record for this repository's current phase, work
  selection, concerns, pending owner decision, active evidence, and freshness.

## Generated Current State View

- `docs/current-mission.md` — Short human-readable view generated from canonical active state by `tools/generate-context.py`.

## Infrastructure

- `docs/infrastructure.md`
- `docs/infrastructure-virtualization.md`
- `docs/services.md`
- `docs/infrastructure-snapshot.md`

These public owners contain role-based patterns and dated, non-continuous
evidence. Repository Architecture owns the accepted Homelab specialized boundary
and the requirement to separately design a restricted source for exact
non-secret desired state when a concrete durable operational artifact is
identified. No extraction or migration is implied. Live systems and fresh
observation own current reality; secret values never belong in Git.

## Operations

- `docs/knowledge-promotion.md` — Canonical human-applied procedure for reviewing candidate findings and deliberately promoting accepted knowledge.
- `docs/change-session.md`
- `docs/change-schema.md`
- `docs/changes.log`
- `docs/changes/*.yml`

## Roadmaps

- `docs/roadmaps/platform-strategy.md`
- `docs/roadmaps/ai-engineering.md`
- `docs/roadmaps/engineering-toolkit.md`

## Portfolio Reviews

- `docs/reviews/atlas-repository-substrate-simplification-evidence-2026-09-22.md` — Local simplification candidate, consumer findings, and verification boundary; acceptance and publication remain separate.
- `docs/reviews/sahale-r2-architecture-refresh-evidence-2026-09-18.md` — R2 scope, baseline, architecture reconciliation, migration couplings, verification/review boundary, and owner-acceptance handoff.

- `docs/reviews/current-state-baseline-debt-c1-evidence-2026-09-16.md` — Historical C1 baseline-cleanup evidence; the current owner confirms publication at `5dc5ccb75556aee74a6684a231fa012350d403e4`, without rewriting its pre-publication narrative.
- `docs/reviews/engineering-workflow-v1-2-evidence-2026-09-16.md` — Dated W2 publication evidence for the workflow standard; canonical current state records published I1 and intentional idle.
- `docs/reviews/school-learning-vnext-storage-spike-evidence-2026-09-08.md` — Retained provisional synthetic evidence, public-surface sanitized in C1; no architecture acceptance, promotion, or completed final spike review is claimed.

- `docs/reviews/platform-operating-model-recalibration-r1-evidence-2026-09-15.md` — Dated non-canonical Tier-3 September recalibration evidence, including the authorized baseline verification exception; distinct from the historical repository-identity R1.

- `docs/reviews/school-learning-refresh-transport-packaging-evidence-2026-09-06.md` — Dated non-canonical Tier-3 evidence preserving design, implementation/corrections, independent review, owner acceptance, substantive publication, and the refresh-packaging boundary.
- `docs/reviews/ai-operating-environment-refresh-2026-09-06.md` — Dated non-canonical September operating profile and Tier-3 documentation/ownership reconciliation evidence preserving verification, review, owner acceptance, and publication chronology.

July AI/environment records below are dated historical operating evidence, not
permanent current configuration. The September record preserves the accepted
refresh without rewriting those historical bodies.


- `docs/reviews/g14-storage-orientation-snapshot-implementation-evidence-2026-08-08.md` — Compact Tier 3 G14 metadata-only collection, analysis/reporting, sanitization, correction, residual-limitation, final verification, adversarial/privacy review, owner-acceptance, and publication-boundary evidence; no live collection, deployment, or operational runtime is claimed.
- `docs/reviews/repository-identity-r1-evidence-2026-08-02.md` — Compact
  Tier 3 record preserving the original R1 boundary, first publication and
  verified rename, post-rename identity finalization, lifecycle-correction
  cycles, fresh review and renewed owner acceptance, and final R1 publication
  at immutable commit `483f1111257c9b1608c100cb88c8304a17d85314`.
- `docs/reviews/engineering-workflow-v1-1-evidence-2026-08-01.md` — Compact dated W1 compound evidence preserving Tier-3 scope, preflight, verification, completed independent review, owner acceptance, publication at `27d99c1eb0ab30f7fcd11158f4c1d856bd6913de`, and final lifecycle synchronization; no follow-on authority.
- `docs/reviews/school-learning-v0-1-pilot-evaluation-2026-07-21.md` — Dated non-canonical pilot evidence recording confirmed v0.1 strengths and friction, the bounded v0.1.1 Guided Study Handoff decision, local verification, independent acceptance, owner acceptance, preserved human authority, and bounded publication authority.
- `docs/reviews/school-learning-v0-1-authorization-review-2026-07-21.md` — Accepted dated non-canonical owner decision evidence for the exact School Learning v0.1 implementation and publication boundary.
- `docs/reviews/school-learning-v0-2-a-semester-core-intake-evidence-2026-08-26.md` — Compact compound record covering Tier-2 SL2-A implementation, correction/review history, final product ACCEPT, owner acceptance, Tier-3 repository finalization, the accepted non-blocking public-surface review finding, publication of SL2-A, and post-publication lifecycle synchronization.
- `docs/reviews/aiden-platform-owner-intent-recalibration-2026-07-19.md` — Owner-authored and owner-accepted non-canonical dated evidence preserving durable platform purpose, desired agency outcomes, human ownership, near-term direction, cautions, and unresolved decisions.
- `docs/reviews/aiden-ai-environment-baseline-v1-2026-07-20.md` — Accepted dated non-canonical evidence preserving the complete ChatGPT Project cleanup and permissions baseline, exact Codex Baseline v1 configuration and instructions, authority boundaries, verification, hashes, rollback, limitations, and deferrals.
- `docs/reviews/aiden-platform-portfolio-recalibration-owner-decision-2026-07-20.md` — Owner-accepted non-canonical decision record preserving the bounded recalibration promotion, accepted 90-day sequence, EO-2026-013 B2b authorization and hard kill switch, next-consumer condition, rejected claims, and explicit exclusions.
- `docs/reviews/aiden-platform-operating-model-overlap-review-2026-07-17.md` — Accepted non-canonical portfolio evidence mapping July 17 operating-model concepts to existing Engineering Opportunities, identifying one distinct Human Engineering Control Surface candidate, and preserving all implementation and mission boundaries.
- `docs/reviews/aiden-platform-operating-model-owner-decision-2026-07-17.md` — Non-canonical owner decision evidence preserving the accepted hybrid task-state model, minimal console scope, four approval gates, draft-pull-request authority ceiling, pilot criteria, and open naming question.
- `docs/reviews/aiden-platform-operating-model-validation-study-2026-07-17.md` — Non-canonical dated external design-validation evidence supporting a Git-native operating model, durable task state, human approval, explicit execution evidence, and a narrowed first control-surface checkpoint. Its preserved serialized JSON study payload remains in the `.md` file; read it as historical structured evidence, not ordinary Markdown or current authority.
- `docs/reviews/aiden-platform-operating-model-validation-request-2026-07-17.md` — Non-canonical dated research request preserving the exact questions, evidence requirements, authority boundaries, and requested source ledger used for the external validation study.
- `docs/reviews/aiden-platform-operating-model-discovery-2026-07-17.md` — Non-canonical architecture discovery evidence preserving the proposed operating model, human control-surface problem, domain vocabulary, protocol model, workspace handoff, and bounded-autonomy direction.
- `docs/reviews/eo-2026-013-implementation-planning-review-2026-07-15.md` — Non-canonical evidence preserving accepted EO-2026-013 architecture completion, owner-approved mission advancement into implementation planning, the bounded vertical-slice plan and two future checkpoints, and the explicit withholding of implementation authorization.
- `docs/reviews/eo-2026-013-executable-path-review-2026-07-16.md` — Non-canonical accepted decision record preserving the revised A.1/B1/B2 executable-path sequence, exact Checkpoint A.1 authorization, and continued withholding of B1, B2, and protected-branch content.
- `docs/reviews/eo-2026-013-b1a-authorization-review-2026-07-16.md` — Non-canonical accepted decision record preserving the B1a/B1b split, exact Immutable Snapshot Boundary authorization, Git trust boundary, and continued withholding of B1b, B2, and protected-object content.
- `docs/reviews/eo-2026-013-b1b1-authorization-review-2026-07-16.md` — Non-canonical accepted decision record preserving the B1b1/B1b2 split, exact Deterministic Selector Primitives authorization, pure selector boundary, and continued withholding of B1b2, B2, protected-reference changes, and protected content.
- `docs/reviews/mission-selection-review-2026-07-15.md` — Non-canonical evidence preserving completed mission evidence, candidate directions, session-health assessment, the accepted EO-2026-013 owner decision, and the deferred AI Engineering Environment Review.
- `docs/reviews/knowledge-promotion-pilot-engineering-validation-2026-07-15.md` — Non-canonical accepted promotion-pilot record preserving the decision, application, evidence, and validation.
- `docs/reviews/engineering-opportunity-portfolio-recalibration.md` — Accepted human-reviewed interpretation of the complete Engineering Opportunity portfolio, including capability alignment, relationships, dispositions, priorities, and the Distinctness branch decision.
- `docs/reviews/ai-operating-baseline-2026-07-14.md` — Dated historical July AI access and workflow baseline, including task profiles, provider decisions, privacy boundaries, challenger policy, evaluation evidence, and reassessment triggers.
- `docs/reviews/ai-workflow-evaluation-cycle-2026-07.md` — Completed human-reviewed AI workflow evaluation cycle containing configuration checks, firsthand evidence, validation, challenger comparisons, and the final operating decision.
- `docs/reviews/ai-debugging-evaluation-g14-touchpad-2026-07-15.md` — Non-canonical sanitized dated diagnostic evidence for the G14 touchpad failure, normal-restart recovery, uncertainty boundary, and operational follow-up.
- `docs/reviews/ai-capability-landscape-work-research-2026-07-14.md` — Non-canonical dated research evidence preserving the complete ChatGPT Work cloud-AI capability landscape artifact under explicit authority and re-verification limits.
- `docs/reviews/ai-capability-landscape-claude-free-independent-audit-2026-07-14.md` — Non-canonical dated independent-audit evidence preserving the complete Claude Free challenge artifact under explicit authority, human-review findings, and re-verification limits.

## Generated Context

- `docs/aiden-context.md`
- `docs/infrastructure-snapshot.md`

## Repository Objects

- `docs/opportunities/`

---

## Recommended Reading Paths

### Platform Orientation

1. `README.md`
2. `docs/docs-map.md`
3. `docs/vision.md`
4. `docs/architecture/platform.md`
5. `docs/architecture/capabilities.md`
6. `docs/architecture/ai.md`
7. `docs/roadmaps/platform-strategy.md`
8. `docs/current-state.json`
9. `docs/current-mission.md`

### AI and Knowledge Work

For cross-source planning, read `docs/architecture/context-coordination.md`
alongside the authority and compilation owners below.

1. `docs/vision.md`
2. `docs/architecture/platform.md`
3. `docs/architecture/capabilities.md`
4. `docs/architecture/ai.md`
5. `docs/architecture/ai-operating-model.md`
6. `docs/architecture/knowledge-authority.md`
7. `docs/knowledge-promotion.md`
8. `docs/architecture/repository.md`
9. `docs/current-state.json`
10. `docs/current-mission.md`

### Engineering Session

1. `docs/vision.md`
2. `docs/architecture/platform.md`
3. `docs/architecture/repository.md`
4. `docs/architecture/atlas.md`
5. `docs/architecture/engineering.md`
6. `docs/standards/engineering-collaboration.md`
7. `AGENTS.md`
8. `docs/current-state.json`
9. `docs/current-mission.md`
10. `./atlas bootstrap`
11. Architecture relevant to the selected checkpoint

### Task-Scoped Context and Agent Work

This is a specialized reading path, not a new documentation layer.

1. `docs/architecture/platform.md`
2. `docs/architecture/repository.md`
3. `docs/architecture/atlas.md`
4. `docs/architecture/engineering-sessions.md`
5. `docs/architecture/task-scoped-agent-context-compilation.md`
6. `docs/reviews/eo-2026-013-implementation-planning-review-2026-07-15.md`
7. `docs/current-state.json`
8. `docs/current-mission.md`
9. `./atlas bootstrap`

### School Learning

1. `docs/vision.md`
2. `docs/architecture/platform.md`
3. `docs/architecture/capabilities.md`
4. `docs/architecture/school-learning.md`
5. `docs/architecture/ai-operating-model.md`
6. `docs/architecture/knowledge-authority.md`
7. `docs/current-state.json`
8. `docs/current-mission.md`
9. `./school --help`

### Infrastructure Work

1. Vision and Platform Architecture.
2. Relevant capability architecture.
3. Current infrastructure record.
4. Canonical Active State and Generated Human View.
5. Live verification.

### Engineering Opportunity Review

1. Engineering Opportunity architecture.
2. Relevant assessment architecture.
3. Objects under review.
4. Canonical Active State and Generated Human View.
5. Fresh local Git observations and Atlas validation.

Readers should not need every internal engineering document to understand the platform.

---

## Source of Truth

Use `docs/architecture/repository.md` for canonical ownership and source-of-truth order.

Architecture describes intent.

Infrastructure describes implementation.

Operations preserve evidence.

Roadmaps describe direction.

Generated context remains derived.

`docs/current-state.json` owns this repository's typed active state; neither it nor
Atlas is a universal ledger of Platform activity. `docs/current-mission.md`
provides a generated human view. `AGENTS.md` is the primary
repository-local authority-interpretation contract. None of these sources
creates current-session permission.

---

## Update Rules

Update Vision when durable purpose, principles, authority, non-goals, or long-term direction changes.

Update Architecture when structural responsibilities, capability identities, system boundaries, or design decisions change.

Update Standards when a repeatable expectation changes.

Update Canonical Active State when the effective phase, work selection,
concerns, decision, active evidence, or freshness change.

Regenerate Current Mission with `tools/generate-context.py` after canonical state changes.

Update Infrastructure when deployed state changes.

Update Operations when meaningful work or evidence must be preserved.

Update Roadmaps when strategic sequencing or planning horizons change.

Regenerate the registered outputs when their canonical sources change.

---

## Documentation Principle

Each important fact should have one canonical owner.

Other documents should reference that owner rather than reproduce the full content.
