# Engineering Environment Architecture

## Purpose

Sahale should provide an integrated engineering environment that reduces cognitive load while increasing engineering understanding.

The goal is not to automate engineering decisions.

The goal is to automate engineering coordination so the engineer can focus on architecture, implementation, verification, and learning.

---

## Vision

Engineering the platform should feel like working within a coherent operating environment rather than manually coordinating independent tools, documentation, AI systems, and infrastructure.

The engineering environment should continuously answer questions such as:

- What is the current engineering state within this repository's scope?
- What should I work on next?
- Is my documentation current?
- Is my AI context synchronized?
- Is my repository healthy?
- What changed recently?
- What requires my attention?

The engineer should spend time making decisions rather than remembering workflow steps.

---

## Architecture

The engineering environment consists of four primary layers.

```
                    Engineer
                        │
                        ▼
              AI Assistants
      (ChatGPT, Local AI, Future AI)
                        │
                        ▼
                    Atlas
          Deterministic Engineering Interface
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Documentation      Engineering       Repository
   Workflows          Workflows         State
                        │
                        ▼
             Canonical Repository
                        │
                        ▼
               Sahale
```

---

## Canonical Source of Truth

The GitHub repository remains authoritative for its assigned root Platform
engineering responsibilities. Other designated sources retain their scoped
authority under `docs/architecture/knowledge-authority.md`; repository state
and Atlas are not a universal ledger of Platform activity.

Architecture documents describe intent.

Infrastructure documents describe implementation.

Operations documents describe engineering workflow.

Generated AI context summarizes the repository but never replaces it.

Atlas coordinates engineering activities but never becomes the source of truth.

AI systems assist engineering but never replace canonical documentation.

---

## Atlas

Atlas is the repository-local deterministic engineering interface for
the root repository, whose accepted I1 target is `sahale`; external cutover
is pending. Extraction, generalization, and multi-repository coordination
are not part of the current operating model.

Atlas should:

- Observe engineering state.
- Coordinate engineering workflows.
- Prepare engineering context.
- Validate repository consistency.

Atlas should integrate existing engineering capabilities rather than duplicate them.

---

## Engineering Context Management

Engineering context is a first-class platform capability.

Its responsibilities include:

- Preparing AI-readable engineering context.
- Detecting stale generated context.
- Tracking engineering documentation.
- Supporting multiple AI systems.
- Reducing manual synchronization effort.

Engineering context should evolve independently from any individual AI platform.

---

## Engineering Workflow Integration

Existing engineering tools should become coordinated capabilities of the engineering environment rather than independent utilities.

Atlas should integrate or orchestrate existing engineering tools whenever practical.

Examples include:

- Context generation
- Structured change management
- Documentation validation
- Repository validation
- Engineering state inspection

The Sahale `generate-context.py` remains a repository-local generated-context
tool. The former Homelab change helper is retired by the H1 candidate; its
dated records remain historical evidence.

The engineering environment should continuously evolve toward a single coherent engineering interface.

## AI Integration

AI should assist engineering rather than replace engineering.

Different AI systems may require different context preparation.

Atlas should eventually prepare context for multiple engineering environments including:

- ChatGPT Projects
- Local AI
- Future AI assistants

The repository remains canonical for its assigned engineering scope regardless of which AI systems are used.

---

## Desktop and Native Execution

The desktop, editor, browser, or assistant UI may run in a different environment
from repository tools and tests. Select the native execution environment
explicitly and verify its runtime, filesystem, permissions, and temporary
fixture boundary under `docs/architecture/engineering-sessions.md`.

A local desktop interface does not imply local inference or local-only data
handling. `docs/architecture/ai-operating-model.md` owns those distinctions.
Exact current products, distributions, and operating recommendations are dated
evidence in `docs/reviews/ai-operating-environment-refresh-2026-09-06.md`;
they are not machine configuration owned by this architecture.

## AI Session Bootstrap

The engineering environment should help new AI sessions regain engineering context quickly and accurately.

A new AI session should not depend on the engineer manually reconstructing the platform state.

The implemented `./atlas bootstrap` reports local Git facts, canonical phase
and work selection, typed-state validation, and registered generated-output
drift. Startup
and native preflight remain owned by
`docs/architecture/engineering-sessions.md`; bootstrap does not establish
execution-environment readiness or action authority by itself.

Provider-specific source/instruction synchronization, continuous environment
assistance, and automatic preparation for additional AI surfaces remain
deferred. The bounded task-context library described in
`docs/architecture/task-scoped-agent-context-compilation.md` is implemented;
it does not provide those integrations.

The goal is to reduce the cognitive effort required to begin a new AI-assisted engineering session while preserving source-scoped canonical ownership.

## Design Principles

The engineering environment should:

- Reduce cognitive load.
- Increase engineering understanding.
- Prefer integration over duplication.
- Keep architecture authoritative.
- Keep implementation verifiable.
- Build capabilities incrementally.
- Coordinate existing tools before creating new ones.
- The engineer should never have to remember the state of the engineering system.

---

## Long-Term Goal

The long-term objective is an engineering environment where:

- The repository records engineering knowledge.
- Atlas checks local repository facts.
- AI reads canonical architecture and bounded context under owner authority.
- The engineer focuses on architecture and engineering decisions rather than workflow coordination.

The platform should continuously reduce friction while preserving engineering understanding.
