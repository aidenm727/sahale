"""A small human view derived from the canonical repository state."""

from posixpath import relpath

from atlas.platform.active_state import ActiveState


def render_mission(state: ActiveState) -> str:
    checkpoint = state.work_selection.selected_checkpoint
    selection = (
        checkpoint.name if checkpoint else "Intentional idle; no checkpoint selected."
    )
    decision = state.decision_required.summary if state.decision_required else "None."
    blockers = "\n".join(f"- {item.summary}" for item in state.blockers) or "- None"
    unknowns = "\n".join(f"- {item.summary}" for item in state.unknowns) or "- None"
    evidence = "\n".join(
        f"- [{link.id}]({relpath(link.path, 'docs')}) at `{link.commit}`"
        for link in state.evidence_links
    ) or "- None"
    review_after = (
        state.freshness.review_after.isoformat()
        if state.freshness.review_after else "not set"
    )
    return f"""# Current Repository State

Generated from `docs/current-state.json` by `tools/generate-context.py`.

## Phase

{state.phase.display_name}

## Work Selection

{selection}

## Blockers

{blockers}

## Unknowns

{unknowns}

## Pending Decision

{decision}

## Freshness

Effective {state.freshness.effective_date.isoformat()}; review after {review_after}.

## Active Evidence

{evidence}
"""
