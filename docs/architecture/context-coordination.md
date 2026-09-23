# Sahale Context Coordination Architecture

## Purpose and Position

Sahale has a cross-cutting coordination responsibility: resolve the context
needed for an owner's task across distributed authoritative sources and deliver
bounded, provenance-aware context to an appropriate AI or capability.

The goal is automatic context resolution, not automatic centralization. This
is an accepted architectural direction; no production coordination runtime,
source registry, database, retrieval service, connector, or routing system is
implemented by this document. It adds no top-level Platform Foundation.

## Intended Flow

    owner intent
    -> interaction environment
    -> semantic task/context planning
    -> deterministic source metadata and authority resolution
    -> appropriate source adapters
    -> bounded deterministic context compilation
    -> selected AI/capability
    -> result and evidence

The interaction environment helps express intent and scope. Conversation,
persistent workspace, Project/context environment, and durable capability are
distinct concepts owned by `docs/architecture/platform.md`. An interface's
available files or memories do not define Sahale's knowledge boundary.

AI may reason probabilistically about categories of context relevant to a task.
That proposal is not an authoritative source selection. Deterministic Sahale
metadata and designated source contracts must determine whether and how a
source can contribute. AI must not invent authoritative ownership because
information is available, plausible, remembered, or semantically relevant.

## Deterministic Source Contract

The resolution boundary must establish these facts from designated owners:

- Source identity and canonical ownership.
- Authority class and sensitivity.
- Freshness semantics and any required live/fresh observation.
- Retrieval mechanism and applicable access boundary.
- Allowed cross-domain use.
- Provenance and relevant bounded projections.
- Failure and fallback behavior where defined.

These are contract responsibilities, not a new schema or registry design.
`docs/architecture/knowledge-authority.md` owns authority classes, promotion,
conflicts, and source-scoped ownership. Sources can remain in specialized
repositories, structured domain state, restricted records, external services,
live systems, supplied evidence, or other explicitly designated locations.
No universal personal database is required.

Resolution must expose missing ownership, unavailable sources, stale evidence,
conflicts, and omissions rather than silently filling them with inference.
Where no permitted fallback exists, return the unresolved boundary or request
an owner decision. A source's defined fallback cannot expand access, substitute
a lower-authority source as canonical, or imply current live truth from a dated
observation. Fresh retrieval is not by itself evidence of authoritative ownership.

## Relationship to Task-Scoped Compilation

`docs/architecture/task-scoped-agent-context-compilation.md` owns the implemented
lower-level deterministic primitive: explicit task/constraint declarations,
pinned repository snapshots, versioned selection and budget policies, explicit
freshness inputs, bounded materialization, provenance, validation, and generated
non-canonical packages.

Coordination may eventually provide semantic task interpretation and cross-source
planning above that layer. It does not replace the compiler, broaden its current
repository-only inputs, or change its schema, identity, source-selection,
validation, or protected-reference contracts. The model must not independently
choose its own authoritative source material. A future planner must submit
inputs whose source authority and selection are resolved by deterministic
contracts; an AI proposal cannot bypass those contracts.

The existing library does not establish cross-domain retrieval or adapters.
Connecting non-repository sources requires separately accepted contracts and
bounded implementation, not an assumption that the current compiler supports
them. Compiled context remains generated and non-canonical even when every
selected source is authoritative for its assigned facts.

## Foundation Responsibilities

| Existing foundation | Contribution |
| --- | --- |
| Knowledge and Context | Source/context responsibilities, bounded projections, provenance, and compilation; authority rules remain in Knowledge Authority Architecture. |
| Artificial Intelligence | Semantic task interpretation and context-category proposals; AI operating rules govern model/provider suitability and evidence. |
| Automation and Integration | Future source adapters and repeatable orchestration within explicit retrieval/action boundaries. |
| Interaction and Experience | Intent capture, conversational workspaces, context/omission explanations, results, and review surfaces; any Sahale UI remains deferred. |
| Security, Privacy, and Resilience | Sensitivity, access, data minimization, and protected boundaries across the flow. |
| Engineering and Evolution | Engineering contracts, verification, and evidence within each assigned repository scope. |

`docs/architecture/capabilities.md` owns foundation identities;
`docs/architecture/ai.md` and `docs/architecture/ai-operating-model.md` own AI
responsibilities and task-specific operating decisions. Coordination does not
become a universal ledger of domain activity or a multi-repository Atlas.

## Authority and Execution

Automatic context retrieval does not grant automatic action authority.
Owner intent, allowed source access, allowed data transfer, and authorized action
are separate boundaries. A usable context package, healthy repository, model
recommendation, or available adapter grants none of them. Results and execution
evidence preserve what actually occurred; promotion follows Knowledge Authority.

Execution location does not determine capability ownership. A future Sahale
context service running on Homelab infrastructure remains Sahale-owned. The
three Homelab roles are defined in `docs/architecture/platform.md`; repository
and restricted-source placement remain owned by `docs/architecture/repository.md`.

## Maturity and Deferrals

Manual use and the existing compilation primitive provide the current starting
point. Recurring friction must earn any next capability under the incubation
principle in Platform Architecture. A useful next step may be instructions,
structured state, a dedicated Project, integration, automation, UI, backend
software, or no software at all.

This architecture authorizes no MCP server, API, connector, registry, database,
retrieval/context daemon, automatic cross-domain retrieval, context routing,
model routing, or Sahale UI. Those require separately bounded implementation
checkpoints. Published H1 establishes the Homelab public engineering repository
without designing a restricted operational source.
