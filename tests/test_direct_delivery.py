from __future__ import annotations

from pathlib import Path
import csv
import yaml

from direct_delivery_ops.cli import main
from direct_delivery_ops.contracts import CANDIDATE_COLUMNS
from direct_delivery_ops.manifest import build_manifest
from direct_delivery_ops.validator import validate_workspace
from direct_delivery_ops.workspace import initialize_workspace


def test_init_creates_complete_workspace(tmp_path: Path) -> None:
    root = tmp_path / "run"
    written = initialize_workspace(root)
    assert "candidate_register.csv" in written
    assert (root / "human_approval_queue.md").is_file()


def test_initialized_workspace_has_only_incomplete_warnings_or_missing_selected_artifacts(tmp_path: Path) -> None:
    root = tmp_path / "run"
    initialize_workspace(root)
    report = validate_workspace(root, require_complete=False)
    assert report.counts["candidates"] == 0
    assert report.valid
    release_report = validate_workspace(root)
    assert not release_report.valid
    assert any(issue.code == "release_incomplete" for issue in release_report.issues)


def _write_selected_run(root: Path) -> None:
    initialize_workspace(root)
    rows = []
    tracks = [("pain_triggered", 2), ("artifact_first", 2), ("embedded_service", 3)]
    for track, count in tracks:
        for index in range(1, count + 1):
            rows.append({
                "track": track,
                "candidate_or_operator": f"{track}-{index}",
                "role": "operator",
                "project_or_community": "project",
                "source_url": f"https://example.invalid/{track}/{index}",
                "evidence_or_corpus": "exact public evidence",
                "accessibility": "public reply surface",
                "proposed_artifact": "context recovery pack",
                "target_gate_result": "5/5 pass",
                "selection_status": "selected",
                "reason": "bounded and source-supported",
            })
    with (root / "candidate_register.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CANDIDATE_COLUMNS)
        writer.writeheader(); writer.writerows(rows)
    evidence_items = []
    for row in rows:
        evidence_items.append({"id": row["candidate_or_operator"], "pathway": row["track"], "sources": [{"url": row["source_url"], "public_or_permissioned": "public"}]})
    (root / "evidence_log.yaml").write_text(yaml.safe_dump({"run": {"public_sources_only": True}, "selected_items": evidence_items}), encoding="utf-8")
    for index in range(1, 3):
        (root / "pain_triggered" / f"target_{index:02d}_context_recovery_pack.md").write_text("source_boundary: public\n", encoding="utf-8")
        (root / "pain_triggered" / f"target_{index:02d}_delivery_draft.md").write_text("send_status: blocked_pending_human_approval\n", encoding="utf-8")
        (root / "artifact_first" / f"target_{index:02d}_context_recovery_pack.md").write_text("source_boundary: public\n", encoding="utf-8")
        (root / "artifact_first" / f"target_{index:02d}_delivery_draft.md").write_text("send_status: blocked_pending_human_approval\n", encoding="utf-8")
    for index in range(1, 4):
        (root / "embedded_service" / f"operator_{index:02d}_proposal.md").write_text("send_status: blocked_pending_human_approval\n", encoding="utf-8")
    queue = "queue_status: awaiting_human_decision\nsend_actions_executed: false\n" + "\n".join("approval_item:\n  id: item-%d" % i for i in range(1, 8)) + "\n"
    (root / "human_approval_queue.md").write_text(queue, encoding="utf-8")


def test_complete_selected_run_validates(tmp_path: Path) -> None:
    root = tmp_path / "run"
    _write_selected_run(root)
    report = validate_workspace(root)
    assert report.valid, report.issues
    assert report.counts["selected_operator"] == 3


def test_selected_without_gate_fails(tmp_path: Path) -> None:
    root = tmp_path / "run"
    initialize_workspace(root)
    with (root / "candidate_register.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CANDIDATE_COLUMNS); writer.writeheader()
        writer.writerow({key: "" for key in CANDIDATE_COLUMNS} | {"track": "pain_triggered", "candidate_or_operator": "x", "source_url": "https://example.invalid", "target_gate_result": "reject", "selection_status": "selected"})
    report = validate_workspace(root)
    assert not report.valid
    assert any(issue.code == "selected_without_gate" for issue in report.issues)


def test_approval_boundary_fails_when_send_executed(tmp_path: Path) -> None:
    root = tmp_path / "run"
    initialize_workspace(root)
    (root / "human_approval_queue.md").write_text("queue_status: awaiting_human_decision\nsend_actions_executed: true\n", encoding="utf-8")
    report = validate_workspace(root)
    assert not report.valid
    assert any(issue.code == "approval_boundary" for issue in report.issues)


def test_invalid_evidence_url_fails(tmp_path: Path) -> None:
    root = tmp_path / "run"
    initialize_workspace(root)
    (root / "evidence_log.yaml").write_text(yaml.safe_dump({"run": {"public_sources_only": True}, "selected_items": [{"sources": [{"url": "/relative", "public_or_permissioned": "public"}]}]}), encoding="utf-8")
    report = validate_workspace(root)
    assert not report.valid
    assert any(issue.code == "evidence_url" for issue in report.issues)


def test_manifest_hashes_files(tmp_path: Path) -> None:
    root = tmp_path / "run"
    initialize_workspace(root)
    manifest = build_manifest(root)
    assert manifest["send_actions_executed"] is False
    assert "candidate_register.csv" in manifest["files"]


def test_cli_roundtrip(tmp_path: Path) -> None:
    root = tmp_path / "run"
    assert main(["init", str(root)]) == 0
    assert main(["validate", str(root), "--allow-incomplete"]) == 0
    assert main(["validate", str(root)]) == 1
    assert main(["manifest", str(root), "--output", str(tmp_path / "manifest.json")]) == 0
