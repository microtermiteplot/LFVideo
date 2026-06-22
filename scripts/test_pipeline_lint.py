"""Unit + smoke tests for scripts/pipeline_lint.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pipeline_lint as P  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent


def _write_stage(ep: Path, dirname: str, frontmatter: str, body: str = "# Title\n") -> None:
    stage = ep / dirname
    stage.mkdir(parents=True, exist_ok=True)
    (stage / "README.md").write_text(f"---\n{frontmatter}\n---\n\n{body}", encoding="utf-8")


def _script_block(sections: int, forbidden: list[str] | None = None) -> str:
    secs = ",\n".join(
        f'{{"id":"{i}","track":"A","voice":"v","visual_instructions":"x","duration_hint_seconds":10}}'
        for i in range(sections)
    )
    extra = f'"anti_hype_forbidden": {forbidden!r},\n  ' if forbidden else ""
    extra = extra.replace("'", '"')
    return (
        "# ep 脚本\n\n```json\n{\n  "
        + extra
        + f'"title":"t","sections":[{secs}],'
        '"judgment_layer_coverage":{"highlights_pitfall":true,'
        '"explains_boundary":true,"acceptance_standard":true}\n}\n```\n'
    )


def _script_block_sections(sections: list[dict]) -> str:
    """Render a 04 contract block from explicit section dicts."""
    payload = {
        "title": "t",
        "sections": sections,
        "judgment_layer_coverage": {
            "highlights_pitfall": True,
            "explains_boundary": True,
            "acceptance_standard": True,
        },
    }
    return "# ep 脚本\n\n```json\n" + json.dumps(payload, ensure_ascii=False) + "\n```\n"


def _section(sid: str, dur: int, **extra) -> dict:
    base = {
        "id": sid,
        "track": "A",
        "voice": "v",
        "visual_instructions": "x",
        "duration_hint_seconds": dur,
    }
    base.update(extra)
    return base


def _lint(ep: Path) -> P.Report:
    report = P.Report()
    P.lint_episode(ep, report)
    return report


def test_provenance_mismatch_is_error(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", _script_block(3))
    _write_stage(
        ep,
        "06-tts",
        "stage: 06-tts-synthesis\nstatus: approved\nupstream_inputs:\n  - 04-script/README.md (status: draft)",
    )
    report = _lint(ep)
    assert any("provenance" in e and "04-script" in e for e in report.errors)


def test_provenance_match_is_clean(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", _script_block(3))
    _write_stage(
        ep,
        "06-tts",
        "stage: 06-tts-synthesis\nstatus: approved\nupstream_inputs:\n  - 04-script/README.md (status: approved)",
    )
    report = _lint(ep)
    assert not report.errors


def test_gating_blocks_approved_on_draft_upstream(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: draft", _script_block(3))
    _write_stage(
        ep,
        "07-assembly",
        "stage: 07-video-assembly\nstatus: approved\nupstream_inputs:\n  - 04-script/README.md (status: draft)",
    )
    report = _lint(ep)
    assert any("gating" in e for e in report.errors)


def test_assembly_scene_count_drift_is_error(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", _script_block(16))
    body = '# ep 组装\n\n```json\n{"stage":"07-video-assembly","total_scenes":5}\n```\n'
    _write_stage(
        ep,
        "07-assembly",
        "stage: 07-video-assembly\nstatus: approved\nupstream_inputs:\n  - 04-script/README.md (status: approved)",
        body,
    )
    report = _lint(ep)
    assert any("consistency" in e and "5 scenes" in e for e in report.errors)


def test_anti_hype_title_is_flagged(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    _write_stage(
        ep, "04-script", "stage: 04-script\nstatus: approved",
        _script_block(3, forbidden=["100 行"]),
    )
    _write_stage(
        ep,
        "06-distribute",
        "stage: 06-distribute-adapt\nstatus: approved\nupstream_inputs:\n  - 04-script/README.md (status: approved)",
        "# 如何用 100 行 React 编译视频\n",
    )
    report = _lint(ep)
    assert any("anti-hype" in e and "100 行" in e for e in report.errors)


def test_superseded_stage_is_skipped(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    _write_stage(
        ep, "04-script", "stage: 04-script\nstatus: approved",
        _script_block(16, forbidden=["100 行"]),
    )
    body = '# 如何用 100 行 React\n\n```json\n{"scenes":[1,2,3]}\n```\n'
    _write_stage(ep, "05-assembly", "stage: 05-video-assembly\nstatus: superseded", body)
    report = _lint(ep)
    assert not report.errors
    assert any("skipped" in n for n in report.notes)


def test_draft_violation_warns_but_does_not_error(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    _write_stage(
        ep, "04-script", "stage: 04-script\nstatus: approved",
        _script_block(3, forbidden=["100 行"]),
    )
    _write_stage(
        ep,
        "06-distribute",
        "stage: 06-distribute-adapt\nstatus: draft\nupstream_inputs:\n  - 04-script/README.md (status: approved)",
        "# 如何用 100 行 React 编译视频\n",
    )
    report = _lint(ep)
    assert not report.errors
    assert any("anti-hype" in w for w in report.warnings)


def _write_named_doc(
    ep: Path, dirname: str, filename: str, frontmatter: str, body: str = "# Title\n"
) -> None:
    stage = ep / dirname
    stage.mkdir(parents=True, exist_ok=True)
    (stage / filename).write_text(f"---\n{frontmatter}\n---\n\n{body}", encoding="utf-8")


def test_stage_doc_falls_back_to_numbered_md(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", _script_block(3))
    # The 05 stage keeps its doc as 05-b-roll.md (no README.md in the folder).
    _write_named_doc(
        ep,
        "05-assembly",
        "05-b-roll.md",
        "stage: 05-b-roll-recording\nstatus: suspended\n"
        "upstream_inputs:\n  - 04-script/README.md (status: approved)",
        "# ep B 轨录屏\n",
    )
    # 07 references the 05 doc by file path and by directory; both must resolve.
    _write_stage(
        ep,
        "07-assembly",
        "stage: 07-video-assembly\nstatus: approved\nupstream_inputs:\n"
        "  - 04-script/README.md (status: approved)\n"
        "  - 05-assembly/05-b-roll.md (status: suspended)",
        '# ep 组装\n\n```json\n{"stage":"07-video-assembly","total_scenes":3}\n```\n',
    )
    report = _lint(ep)
    assert report.errors == [], "\n".join(report.errors)
    # The 05 stage must be discovered despite having no README.md.
    stages = P.load_stages(ep)
    assert any(
        s.dirname == "05-assembly" and s.stage == "05-b-roll-recording" for s in stages
    )
    # A bare directory reference resolves to the numbered doc too.
    assert P._resolve_upstream_status(ep, "05-assembly/") == "suspended"


def test_deadtime_long_section_no_shots_no_beats_errors_when_approved(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    block = _script_block_sections(
        [_section("1", 10), _section("2", 10), _section("3", 90)]
    )
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", block)
    report = _lint(ep)
    assert any(
        "anti-deadtime" in e and "section '3'" in e and "single" in e
        for e in report.errors
    ), "\n".join(report.errors)


def test_deadtime_long_section_only_warns_on_draft(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    block = _script_block_sections(
        [_section("1", 10), _section("2", 10), _section("3", 90)]
    )
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: draft", block)
    report = _lint(ep)
    assert not report.errors
    assert any("anti-deadtime" in w and "section '3'" in w for w in report.warnings)


def test_deadtime_legacy_visual_beats_only_warns_even_when_approved(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    block = _script_block_sections(
        [
            _section("1", 10),
            _section("2", 10),
            _section(
                "3",
                90,
                visual_beats=[{"at_seconds": 0, "action": "a"}],
            ),
        ]
    )
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", block)
    report = _lint(ep)
    assert not any("anti-deadtime" in e for e in report.errors)
    assert any("anti-deadtime" in w and "migrate to shots" in w for w in report.warnings)


def test_deadtime_enough_shots_is_clean(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    shots = [
        {"id": f"3.{i}", "scene_template": "@TableScene", "duration_seconds": 15}
        for i in range(6)
    ]
    block = _script_block_sections(
        [_section("1", 10), _section("2", 10), _section("3", 90, shots=shots)]
    )
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", block)
    report = _lint(ep)
    assert not any("anti-deadtime" in e for e in report.errors), "\n".join(report.errors)
    assert not any("anti-deadtime" in w for w in report.warnings), "\n".join(report.warnings)


def test_deadtime_too_few_shots_errors_when_approved(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    shots = [
        {"id": "3.1", "scene_template": "@TableScene", "duration_seconds": 45},
        {"id": "3.2", "scene_template": "@SplitLayout", "duration_seconds": 45},
    ]
    block = _script_block_sections(
        [_section("1", 10), _section("2", 10), _section("3", 90, shots=shots)]
    )
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", block)
    report = _lint(ep)
    assert any(
        "anti-deadtime" in e and "needs >= 6" in e for e in report.errors
    ), "\n".join(report.errors)


def test_shots_drive_assembly_unit_count(tmp_path: Path) -> None:
    ep = tmp_path / "ep99-test"
    shots = [
        {"id": "3.1", "scene_template": "@TableScene", "duration_seconds": 45},
        {"id": "3.2", "scene_template": "@SplitLayout", "duration_seconds": 45},
    ]
    # 2 single-shot sections + 1 section with 2 shots = 4 renderable scenes.
    block = _script_block_sections(
        [_section("1", 10), _section("2", 10), _section("3", 90, shots=shots)]
    )
    _write_stage(ep, "04-script", "stage: 04-script\nstatus: approved", block)
    body = '# ep 组装\n\n```json\n{"stage":"07-video-assembly","total_scenes":3}\n```\n'
    _write_stage(
        ep,
        "07-assembly",
        "stage: 07-video-assembly\nstatus: approved\nupstream_inputs:\n  - 04-script/README.md (status: approved)",
        body,
    )
    report = _lint(ep)
    assert any(
        "consistency" in e and "3 scenes" in e and "4 renderable" in e
        for e in report.errors
    ), "\n".join(report.errors)


def test_real_ep02_has_no_errors() -> None:
    """The production chain for ep02 must lint clean after the guardrail fixes."""
    ep = REPO_ROOT / "content-library" / "ep02-video-render"
    if not ep.exists():
        pytest.skip("ep02 content not present")
    report = _lint(ep)
    assert report.errors == [], "\n".join(report.errors)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
