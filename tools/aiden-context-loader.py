from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TOOLS = ROOT / "tools"


ARCHITECTURE_DOCS = [
    "docs/architecture/platform.md",
    "docs/architecture/engineering.md",
    "docs/architecture/capabilities.md",
    "docs/architecture/compute.md",
    "docs/architecture/ai.md",
]

CONTEXT_DOCS = [
    "docs/current-mission.md",
    "docs/aiden-context.md",
    "docs/infrastructure-snapshot.md",
]

ROADMAP_DOCS = [
    "docs/roadmaps/ai-engineering.md",
]

TOOL_FILES = [
    "tools/generate-context.py",
    "tools/aiden-context-loader.py",
]


def exists(relative_path: str) -> bool:
    return (ROOT / relative_path).exists()


def read_heading(path: Path) -> str:
    if not path.exists():
        return "Missing"

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    return path.name


def git_status() -> str:
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
    except Exception as exc:
        return f"Unable to read git status: {exc}"

    output = result.stdout.strip()
    return output if output else "Clean"


def print_checklist(title: str, files: list[str]) -> None:
    print(f"\n{title}")
    print("-" * len(title))

    for relative in files:
        marker = "✓" if exists(relative) else "✗"
        heading = read_heading(ROOT / relative) if exists(relative) else "Missing"
        print(f"{marker} {relative} — {heading}")


def main() -> None:
    print("# Sahale Engineering State\n")

    print("Git Status")
    print("----------")
    print(git_status())

    print_checklist("Architecture Documents", ARCHITECTURE_DOCS)
    print_checklist("Context Documents", CONTEXT_DOCS)
    print_checklist("Roadmaps", ROADMAP_DOCS)
    print_checklist("Engineering Tools", TOOL_FILES)

    print("\nSuggested Next Step")
    print("-------------------")
    if git_status() != "Clean":
        print("Review and commit or discard current working tree changes.")
    else:
        print("Review the canonical current state and select work with the owner.")


if __name__ == "__main__":
    main()
