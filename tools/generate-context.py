from pathlib import Path

from atlas.platform.active_state import load_active_state
from atlas.platform.mission import render_mission


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AIDEN_CONTEXT_GENERATED_FROM = (
    "docs/current-state.json",
    "docs/current-mission.md",
    "docs/infrastructure-snapshot.md",
)


def render_generated_context_active_state(state) -> str:
    checkpoint = state.work_selection.selected_checkpoint
    decision = state.decision_required
    evidence = "\n".join(
        f"- `{link.id}`: `{link.path}` at `{link.commit}` ({link.relation})"
        for link in state.evidence_links
    ) or "- None"
    return f"""## Canonical Active State

- Schema version: {state.schema_version}
- Effective date: {state.freshness.effective_date.isoformat()}
- Phase: {state.phase.display_name}
- Work selection: {state.work_selection.status}
- Selected checkpoint: {checkpoint.name if checkpoint else 'None'}
- Decision required: {decision.summary if decision else 'None'}

### Blockers

{chr(10).join('- ' + item.summary for item in state.blockers) or '- None'}

### Unknowns

{chr(10).join('- ' + item.summary for item in state.unknowns) or '- None'}

### Evidence

{evidence}

Authority for every action remains with the owner under `AGENTS.md`."""


def prepare_embedded_markdown(text: str) -> str:
    lines = text.splitlines()

    if lines and lines[0].startswith("# "):
        lines = lines[1:]

    prepared = []
    for line in lines:
        if line.startswith("### "):
            prepared.append("#" + line)
        elif line.startswith("## "):
            prepared.append("#" + line)
        else:
            prepared.append(line)

    return "\n".join(prepared).strip()


def build_infrastructure_snapshot() -> str:
    return f"""# Infrastructure Snapshot

> Generated public context artifact.
> Template owner: `build_infrastructure_snapshot()` in `tools/generate-context.py`.
> Update that template and regenerate the registered outputs to change this text.

Homelab owns public infrastructure engineering and dated operational evidence
in its published repository: https://github.com/aidenm727/homelab.
Sahale retains shared compute and execution policy in
`docs/architecture/compute.md`. Hosting a Sahale capability on Homelab does
not transfer design ownership. Current runtime reality requires fresh
authorized observation.

"""


def render_source_graph() -> str:
    return "\n".join(f"- {path}" for path in AIDEN_CONTEXT_GENERATED_FROM)


def expected_outputs() -> dict[str, str]:
    active_state = load_active_state(repository_root=ROOT)
    active_state_projection = render_generated_context_active_state(active_state)
    mission_text = render_mission(active_state)
    mission = prepare_embedded_markdown(mission_text)
    snapshot_text = build_infrastructure_snapshot().rstrip() + "\n"
    snapshot = prepare_embedded_markdown(snapshot_text)
    source_graph = render_source_graph()
    generated_date = active_state.freshness.effective_date.isoformat()

    output = f"""# Sahale Context

Generated: {generated_date} (canonical-state effective date; deterministic)

## Purpose

This file is an AI-readable generated context packet for the public Sahale
engineering repository within its assigned root/shared scope. It
projects repository-local canonical active state, its human companion, and the
registered bounded infrastructure reference. It is generated and
non-canonical, not a universal ledger of Platform activity. Designated sources
retain their own authority; see docs/architecture/knowledge-authority.md and
docs/architecture/repository.md for ownership.

{active_state_projection}

## Current Mission Companion

{mission}

## Infrastructure Snapshot

{snapshot}

## Registered Source Graph

{source_graph}

The generated infrastructure snapshot is a bounded reference to Homelab's
public engineering owner. Git history records repository evolution but is not
a generator input.

## Use Boundary

- Canonical repository sources win over this generated view.
- Live branch, worktree, infrastructure, and external-system state require fresh observation.
- Task, implementation, publication, deployment, and external-write authority require explicit owner instruction outside repository state.
- Exact private operations, secrets, credentials, and personal School Learning data are excluded.
"""

    return {
        "current-mission.md": mission_text,
        "infrastructure-snapshot.md": snapshot_text,
        "aiden-context.md": output.rstrip() + "\n",
    }


def check_outputs() -> list[str]:
    return [
        name for name, expected in expected_outputs().items()
        if (DOCS / name).is_symlink()
        or not (DOCS / name).is_file()
        or (DOCS / name).read_text(encoding="utf-8") != expected
    ]


def generate_context() -> None:
    outputs = expected_outputs()
    if any((DOCS / name).is_symlink() for name in outputs):
        raise OSError("refusing to write through a generated-output symlink")
    for name, content in outputs.items():
        (DOCS / name).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    import sys

    if sys.argv[1:] == ["--check"]:
        try:
            drift = check_outputs()
        except OSError as error:
            raise SystemExit(f"Context check failed: {error}") from error
        for name in drift:
            print(f"Drift: docs/{name}")
        raise SystemExit(1 if drift else 0)
    if sys.argv[1:]:
        raise SystemExit("usage: generate-context.py [--check]")
    try:
        generate_context()
    except OSError as error:
        raise SystemExit(f"Context generation failed: {error}") from error
    print("Generated docs/current-mission.md, docs/infrastructure-snapshot.md, docs/aiden-context.md")
