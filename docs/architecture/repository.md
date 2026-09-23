# Repository Architecture

## Purpose

`sahale` is the accepted I1 target for the root Sahale engineering repository. It owns Platform-wide architecture, shared capabilities and systems, cross-domain contracts, root engineering coordination, and responsibilities explicitly assigned to it.

It preserves vision, architecture, standards, infrastructure, operations, roadmaps, Repository Objects, generated context, and engineering tools.

Every file and directory should have one clear responsibility.

## Source-Scoped Engineering Ownership

Canonical authority follows explicitly designated responsibilities, not physical
centralization. This root repository does not own every Platform fact or all
engineering activity. Specialized engineering repositories, restricted
operational records, external systems, and live systems may own distinct facts
and responsibilities. Each durable responsibility has one explicit owner;
references preserve scope, provenance, and freshness instead of copying truth.
`docs/architecture/knowledge-authority.md` owns those authority principles.

A specialized canonical engineering repository is permitted when independent
engineering responsibility, recurring maintenance or change, clearer ownership
or audience, or meaningful independent lifecycle value earns the boundary.
This is selective, not one repository per capability or domain. Root Platform
architecture and cross-domain contracts remain here; a specialized repository
owns only its designated project or system engineering scope.

Homelab is the first accepted specialized-repository candidate and boundary,
based on the owner's current evidence outside this repository together with
repository evidence. The September 2026 recalibration accepts that boundary;
it does not create a repository, extract or migrate Homelab material, or claim
that external evidence was independently inspected in this checkpoint.

The Homelab workspace, source/engineering domain, and execution environment
are distinct roles under `docs/architecture/platform.md`. Hosting a Sahale
service does not transfer its capability ownership to Homelab.

Atlas remains local to this root repository. This ownership model introduces no
repository registry, synchronization protocol, federation runtime, or change
to task-context compilation.

## Repository Identity

Sahale is the human-facing platform identity. It is broader than this repository,
ChatGPT, Homelab, or any execution environment. Presentation identity does not
rename machine, schema, compatibility, persisted-data, or historical identities.
I1 is a local implementation candidate. The observed origin still names
`aidenm727/aiden-platform`; the checkout remains `~/src/t430-homelab`.
The accepted cutover targets are `aidenm727/sahale` and `~/src/sahale`.
GitHub rename, publication, checkout movement, and application updates are
pending separate authority and fresh external verification.

The local candidate canonical compiler identity is
`github.com/aidenm727/sahale`. The accepted future public clone target is
`https://github.com/aidenm727/sahale.git`; until cutover, the observed public
repository remains `aidenm727/aiden-platform`.

Supported current-origin locator forms are SCP-style SSH, `ssh://`, and HTTPS
with or without `.git`. The equivalent `aidenm727/aiden-platform` and `aidenm727/t430-homelab` forms are
explicit legacy origin locators only: they normalize to the current canonical
identity and are not accepted as a requested current identity. This narrow
compatibility preserves deterministic use of older local origin configuration;
it does not make the former slug canonical again.

GitHub repository ID `1161282866` is a stable externally observed fact across
the rename. It is not a compiler input or permission source. Requested identity,
raw observed origin locators, and normalized identity establish scope and
provenance; they grant no task, implementation, publication, deployment, or
external-write authority.

---

## Repository Layers

```text
Vision
Architecture
Standards
Canonical Active State
Infrastructure
Operations
Roadmaps
Engineering Toolkit
```

### Vision

Explains why the platform exists and where it is going.

Canonical owner:

- `docs/vision.md`

### Architecture

Explains how the platform should be designed.

Primary owners:

- `docs/architecture/platform.md`
- `docs/architecture/capabilities.md`
- `docs/architecture/ai.md`
- `docs/architecture/ai-operating-model.md`
- `docs/architecture/knowledge-authority.md`
- `docs/architecture/context-coordination.md`
- `docs/architecture/repository.md`
- `docs/architecture/atlas.md`
- `docs/architecture/task-scoped-agent-context-compilation.md`
- `docs/architecture/school-learning.md`

Specialized architecture covers engineering, reasoning, Repository Objects, opportunities, infrastructure capabilities, artifacts, collaboration, and future systems.

### Standards

Define repeatable expectations and quality bars.

Current owner:

- `docs/standards/engineering-collaboration.md`

### Canonical Active State

`docs/current-state.json` is the strict typed owner of this repository's effective active state:
phase, selected work or intentional idle, blockers, unknowns, pending owner
decision, active evidence links, and freshness.

`docs/current-mission.md` is its short generated human-readable view.
The generator reads typed state, and missing or invalid typed state
fails closed. These records and Atlas describe their declared repository scope,
not a universal ledger of Platform or domain activity. They grant no task,
implementation, publication, deployment, or external-write authority.

### Infrastructure

Describes public-safe infrastructure patterns and dated operational evidence.

- `docs/infrastructure.md`
- `docs/infrastructure-virtualization.md`
- `docs/services.md`
- `docs/infrastructure-snapshot.md` as a generated summary

These documents do not own exact live state or prove continuous availability.
Live systems and fresh observation own current operational reality.

### Operations

Preserve active workflow and history.

- `docs/knowledge-promotion.md` as the repeatable manual Canonical Knowledge Promotion operating procedure
- `docs/change-session.md`
- `docs/change-schema.md`
- `docs/changes.log`
- `docs/changes/*.yml`

Knowledge Authority Architecture owns promotion principles and authority requirements. `docs/knowledge-promotion.md` owns the repeatable manual workflow that applies those requirements, preserving the distinction between architecture intent and operational procedure.

### Roadmaps

Describe likely future direction and sequencing.

- `docs/roadmaps/platform-strategy.md`
- `docs/roadmaps/ai-engineering.md`
- `docs/roadmaps/engineering-toolkit.md`

### Engineering Toolkit

Contains Atlas and supporting tools.

The primary interface is:

```text
./atlas <command>
```

Tools expose platform concepts and should not become hidden owners of repository facts.

---

## Repository Objects

Repository Objects are structured repository-native entities with identity and lifecycle.

Current examples include Engineering Opportunity Objects under `docs/opportunities/`.

Objects preserve structured candidates.

They are not automatically architecture, current mission, or committed work.

---

## Generated Content

Generated files summarize canonical records but do not replace them.

Examples:

- `docs/current-mission.md`
- `docs/aiden-context.md`
- `docs/infrastructure-snapshot.md`

The output and source registration lives in `tools/generate-context.py`.
`docs/aiden-context.md` retains its compatibility filename and generator-owned
Sahale heading. `AIDEN_CONTEXT_GENERATED_FROM` remains a stable generator
symbol. No duplicate context file or alias is introduced.

---

## Public and Private Ownership

Within its assigned scope, the public root repository owns vision, architecture,
standards, code, tests, public repository state, sanitized infrastructure
patterns, and dated public evidence.

Exact non-secret Homelab desired operational state is accepted as deserving a
separately designed restricted canonical source when a concrete durable
operational artifact is identified. Possible artifacts include deployment
configuration, inventory, addressing, private DNS, backup destinations, or
recovery procedures. A private operations repository is one possible form;
its design and creation require separate authority. No restricted source is
created by this checkpoint or merely by generalizing public prose.

Restricted desired state describes intended operation. Dated restricted
observations or incidents, when explicitly assigned an owner, remain evidence
rather than continuous live truth. Specialized Homelab engineering ownership
and restricted operational ownership are distinct responsibilities.

Secret values, private keys, tokens, and recovery keys belong only in a secret
manager or protected operational storage and never in either Git repository.
Current live reality belongs to live systems and fresh observation. GitHub
metadata and settings belong to GitHub and require authorized observation.

Public infrastructure records follow these rules:

1. Use role aliases rather than real host or network identities.
2. Describe capabilities and trust boundaries rather than reachability.
3. Date operational evidence and make its non-continuous nature explicit.
4. Include hardware only when it explains an engineering constraint, using a
   class or range where possible.
5. Publish backup and recovery patterns or redacted outcomes, never
   destinations, key locations, or executable recovery detail.
6. Exclude credential values and references, internal endpoints, private DNS,
   exact inventory, ports, container IDs, storage paths, and management paths.
7. Treat generated documents and images as public releases.
8. Keep one canonical owner for each public fact and link to it.

---

## Source of Truth Hierarchy

GitHub is the canonical documentation source for this repository.

The repository is the canonical source of truth for its assigned root Platform
engineering responsibilities. The hierarchy below applies within that scope;
it does not override a designated external or specialized owner.

Architecture documents define intent.

The hierarchy is:

1. Vision defines purpose and durable direction.
2. Architecture records describe intent and structural design.
3. Standards records describe expected engineering behavior.
4. Canonical Active State defines the effective phase and selected work.
5. The generated Current Mission view presents that state for humans.
6. Infrastructure records describe documented implementation and state.
7. Operations records describe change evidence and history.
8. Roadmaps describe likely future direction and sequencing.
9. Repository Objects preserve structured candidates and lifecycle state.
10. Generated context summarizes canonical documentation and never replaces it.
11. Git history records repository evolution.
12. Live verification resolves current operational reality.

Conversation context may explain intent but does not replace canonical repository knowledge.

Repository state selects work but grants no current task, implementation,
publication, deployment, or external-write authority. `AGENTS.md` is the primary
repository-local contract for interpreting those authority dimensions. Atlas,
generated context, historical records, and roadmaps do not grant permission.

---

## Canonical Ownership Rules

- Purpose and long-term direction belong in `docs/vision.md`.
- Platform structure belongs in `docs/architecture/platform.md`.
- Capability taxonomy belongs in `docs/architecture/capabilities.md`.
- AI architecture belongs in `docs/architecture/ai.md`.
- Recurring model, provider, deployment, and AI-use decisions belong in `docs/architecture/ai-operating-model.md`.
- Knowledge authority, provenance, and promotion belong in `docs/architecture/knowledge-authority.md`.
- Cross-source context coordination belongs in `docs/architecture/context-coordination.md`; its future runtime does not replace deterministic compilation.
- Deterministic compilation of bounded, task-specific generated context packages and their authority, selection, provenance, size, validation, and consumer boundaries belongs in `docs/architecture/task-scoped-agent-context-compilation.md`.
- The bounded School Learning workflow, local course-data contract, manual approved-AI handoff, and generated local views belong in `docs/architecture/school-learning.md`.
- Personal course materials, answers, learning history, and generated personal views remain outside the engineering repository. The repository owns School Learning architecture and implementation, not personal school data.
- The repeatable manual knowledge-promotion workflow belongs in `docs/knowledge-promotion.md`.
- Strategic sequencing belongs in `docs/roadmaps/platform-strategy.md`.
- This repository's typed active phase and work selection belong in `docs/current-state.json`.
- The concise human-readable view of current state is generated at `docs/current-mission.md`.
- Repository-local authority interpretation belongs in `AGENTS.md`.
- Public-safe infrastructure patterns and dated evidence belong in
  infrastructure records; live systems own current reality.
- Repeatable behavior belongs in standards.
- Change evidence belongs in operations.
- Candidate work belongs in roadmaps or Repository Objects.
- Generated summaries remain derived.

Reference the canonical owner instead of duplicating full content.

---

## Document Navigation

Add a new canonical document to `docs/docs-map.md` when it helps readers find
the owner. Register generated output in its generator only when a real consumer
needs a drift check. Atlas does not require a definition for every document.
Human judgment decides whether a document should exist. Publication remains a
separate owner decision under `AGENTS.md`.

---

## Placement Rules

- Durable purpose belongs in Vision.
- Durable design belongs in Architecture.
- Repeatable expectations belong in Standards.
- Public-safe implementation patterns and dated operational evidence belong in
  Infrastructure.
- Change evidence belongs in Operations.
- Future sequencing belongs in Roadmaps.
- Structured lifecycle entities belong in registered Repository Object locations.
- Helper software belongs in `tools/`.
- Rebuildable summaries belong in generated files.

Identify canonical responsibility before creating another overlapping document.

---

## Repository Health Standard

A healthy repository should make it easy to answer:

- Why does the platform exist?
- How is it structured?
- Which capabilities does it develop?
- What remains human-owned?
- What currently exists?
- What changed?
- What is active now?
- What may happen next?
- Which evidence supports the conclusion?
- Which tool or workflow owns the next action?

---

## Future Direction

The repository should evolve as the root engineering knowledge system for its assigned Platform scope through repository-owned metadata, search, impact analysis, reliable artifacts, bounded task context, versioned skills, human-reviewed knowledge promotion, and clearer roadmap relationships.

It should become more capable without becoming the platform's primary outcome.
