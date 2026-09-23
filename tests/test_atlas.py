from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from io import StringIO
from pathlib import Path
import runpy
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from atlas import cli
from atlas.platform.active_state import load_active_state
from atlas.platform.mission import render_mission

ROOT = Path(__file__).resolve().parents[1]


class AtlasContractTests(unittest.TestCase):
    def test_only_three_repository_commands(self) -> None:
        for command in ("bootstrap", "validate", "sync"):
            with self.subTest(command=command), redirect_stdout(StringIO()):
                self.assertEqual(cli.main([command]), 0)
        with redirect_stderr(StringIO()), self.assertRaises(SystemExit):
            cli.main(["next"])

    def test_mission_is_derived_from_typed_state(self) -> None:
        state = load_active_state()
        mission = render_mission(state)
        self.assertEqual(
            (ROOT / "docs/current-mission.md").read_text(encoding="utf-8"),
            mission,
        )
        for link in state.evidence_links:
            relative = mission.split(f"[{link.id}](", 1)[1].split(")", 1)[0]
            self.assertEqual((ROOT / "docs" / relative).resolve(), ROOT / link.path)

    def test_bootstrap_reports_missing_upstream_without_failure(self) -> None:
        def local_git(*args):
            if '@{upstream}' in args:
                raise subprocess.CalledProcessError(128, ["git", *args])
            if args[:2] == ('status', '--short'):
                return "## local"
            return "local"

        output = StringIO()
        with patch.object(cli, "git", side_effect=local_git), redirect_stdout(output):
            self.assertEqual(cli.main(["bootstrap"]), 0)
        self.assertIn("Upstream: (none)", output.getvalue())
        self.assertIn("Divergence: (unavailable)", output.getvalue())

    def test_generated_drift_is_reported_without_writing(self) -> None:
        generator = runpy.run_path(str(ROOT / "tools/generate-context.py"))
        outputs = generator["expected_outputs"]()
        with tempfile.TemporaryDirectory() as directory:
            docroot = Path(directory)
            for name, content in outputs.items():
                (docroot / name).write_text(content, encoding="utf-8")
            check = generator["check_outputs"]
            with patch.dict(check.__globals__, {"DOCS": docroot, "expected_outputs": lambda: outputs}):
                self.assertEqual(check(), [])
                (docroot / "current-mission.md").write_text("stale", encoding="utf-8")
                self.assertEqual(check(), ["current-mission.md"])
                self.assertEqual((docroot / "current-mission.md").read_text(), "stale")

    def test_generated_output_symlink_is_rejected(self) -> None:
        generator = runpy.run_path(str(ROOT / "tools/generate-context.py"))
        outputs = generator["expected_outputs"]()
        with tempfile.TemporaryDirectory() as directory:
            docroot = Path(directory)
            target = docroot / "external"
            target.write_text("untouched", encoding="utf-8")
            (docroot / "current-mission.md").symlink_to(target)
            check = generator["check_outputs"]
            generate = generator["generate_context"]
            with patch.dict(check.__globals__, {"DOCS": docroot, "expected_outputs": lambda: outputs}):
                self.assertIn("current-mission.md", check())
                with self.assertRaisesRegex(OSError, "symlink"):
                    generate()
            self.assertEqual(target.read_text(encoding="utf-8"), "untouched")

    def test_generator_has_no_moved_homelab_source_dependency(self) -> None:
        generator = runpy.run_path(str(ROOT / "tools/generate-context.py"))
        state = SimpleNamespace(
            schema_version=1,
            phase=SimpleNamespace(display_name="Synthetic Phase — Published"),
            work_selection=SimpleNamespace(status="intentional_idle", selected_checkpoint=None),
            decision_required=None,
            blockers=(),
            unknowns=(),
            evidence_links=(),
            freshness=SimpleNamespace(effective_date=date(2026, 1, 1), review_after=None),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            globals_ = generator["expected_outputs"].__globals__
            with patch.dict(globals_, {
                "ROOT": root,
                "DOCS": docs,
                "load_active_state": lambda **_: state,
            }):
                outputs = generator["expected_outputs"]()
                self.assertIn("Homelab owns public infrastructure engineering", outputs["infrastructure-snapshot.md"])
                self.assertNotIn("docs/changes", outputs["aiden-context.md"])
                generator["generate_context"]()
                self.assertEqual(generator["check_outputs"](), [])
                self.assertNotIn("docs/infrastructure.md", outputs["infrastructure-snapshot.md"])
