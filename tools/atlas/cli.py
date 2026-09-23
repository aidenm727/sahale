"""Small deterministic checks for the current Sahale repository."""

import argparse
from pathlib import Path
import runpy
import subprocess

from atlas.platform.active_state import ActiveStateError, load_active_state

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = (
    "AGENTS.md",
    "README.md",
    "docs/current-state.json",
    "docs/architecture/repository.md",
    "docs/architecture/knowledge-authority.md",
    "docs/architecture/engineering-sessions.md",
    "docs/standards/engineering-collaboration.md",
    "tools/generate-context.py",
)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def validate() -> tuple[object | None, list[str]]:
    errors = [
        f"missing or unsafe required repository path: {path}"
        for path in REQUIRED
        if (ROOT / path).is_symlink() or not (ROOT / path).is_file()
    ]
    try:
        state = load_active_state(repository_root=ROOT)
    except ActiveStateError as error:
        state = None
        errors.append(f"docs/current-state.json: {error}")
    return state, errors


def sync() -> list[str]:
    try:
        generator = runpy.run_path(str(ROOT / "tools/generate-context.py"))
        return [f"generated output differs: docs/{name}" for name in generator["check_outputs"]()]
    except (ActiveStateError, OSError, KeyError, ValueError) as error:
        return [f"generated output check failed: {error}"]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="atlas", description="Check Sahale repository state and generated outputs."
    )
    parser.add_argument("command", choices=("bootstrap", "validate", "sync"))
    args = parser.parse_args(argv)

    if args.command == "sync":
        errors = sync()
        print("Atlas sync: " + ("synchronized" if not errors else "drift"))
    else:
        state, errors = validate()
        if args.command == "bootstrap":
            try:
                print(f"Branch: {git('branch', '--show-current') or '(detached)'}")
                print(f"HEAD: {git('rev-parse', 'HEAD')}")
                try:
                    upstream = git('rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{upstream}')
                except subprocess.CalledProcessError:
                    upstream = None
                print(f"Upstream: {upstream or '(none)'}")
                print(f"Divergence: {git('rev-list', '--left-right', '--count', 'HEAD...@{upstream}') if upstream else '(unavailable)'}")
                print("Status:")
                print(git('status', '--short', '--branch') or "(empty)")
            except (OSError, subprocess.CalledProcessError) as error:
                errors.append(f"local Git observation failed: {error}")
            if state:
                print(f"Phase: {state.phase.display_name}")
                checkpoint = state.work_selection.selected_checkpoint
                print(f"Work: {checkpoint.name if checkpoint else 'intentional idle'}")
                if state.decision_required:
                    print(f"Pending decision: {state.decision_required.summary}")
            errors.extend(sync())
        print("Atlas " + args.command + ": " + ("valid" if not errors else "failed"))
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
