"""Validate source fidelity, artifact completeness, and the human approval boundary."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
import csv
import json

from ._vendor import yaml

from .contracts import (
    ALLOWED_GATE_RESULTS,
    ALLOWED_SELECTION,
    CANDIDATE_COLUMNS,
    REQUIRED_ROOT,
    SELECTION_TARGETS,
    TRACKS,
)


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    path: str
    message: str


@dataclass(frozen=True)
class Report:
    valid: bool
    issues: tuple[Issue, ...]
    counts: dict[str, int]


def validate_workspace(root: Path, *, require_complete: bool = True) -> Report:
    root = root.resolve()
    issues: list[Issue] = []
    counts = {"candidates": 0, "selected_pain": 0, "selected_artifact": 0, "selected_operator": 0, "evidence_items": 0, "approval_items": 0}
    for relative in REQUIRED_ROOT:
        if not (root / relative).is_file():
            issues.append(Issue("error", "missing_artifact", relative, "required run artifact is absent"))
    _validate_register(root / "candidate_register.csv", issues, counts, require_complete=require_complete)
    evidence = _load_yaml(root / "evidence_log.yaml", issues)
    if evidence is not None:
        _validate_evidence(evidence, issues, counts)
    verification = _load_yaml(root / "verification_report.yaml", issues)
    if isinstance(verification, dict) and verification.get("send_actions_executed") is not False:
        issues.append(Issue("error", "send_boundary", "verification_report.yaml", "send_actions_executed must be false"))
    continuity = _load_yaml(root / "continuity.yaml", issues)
    if isinstance(continuity, dict):
        run = continuity.get("run")
        if not isinstance(run, dict) or run.get("completed_without_sending") is not True:
            issues.append(Issue("error", "continuity_boundary", "continuity.yaml", "completed_without_sending must be true"))
    _validate_approval_queue(root / "human_approval_queue.md", issues, counts)
    _validate_selected_artifacts(root, issues, counts)
    if require_complete:
        expected = {"selected_pain": 2, "selected_artifact": 2, "selected_operator": 3, "evidence_items": 7, "approval_items": 7}
        for key, target in expected.items():
            if counts[key] != target:
                issues.append(Issue("error", "release_incomplete", str(root), f"{key} must equal {target} for release readiness; found {counts[key]}"))
    return Report(valid=not any(issue.severity == "error" for issue in issues), issues=tuple(issues), counts=counts)


def _validate_register(path: Path, issues: list[Issue], counts: dict[str, int], *, require_complete: bool) -> None:
    if not path.is_file():
        return
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != CANDIDATE_COLUMNS:
            issues.append(Issue("error", "csv_schema", path.name, f"expected columns: {', '.join(CANDIDATE_COLUMNS)}"))
            return
        for line, row in enumerate(reader, start=2):
            counts["candidates"] += 1
            track = row["track"].strip()
            if track not in TRACKS:
                issues.append(Issue("error", "track", f"{path.name}:{line}", f"invalid track {track!r}"))
            gate = row["target_gate_result"].strip()
            selection = row["selection_status"].strip()
            if gate not in ALLOWED_GATE_RESULTS:
                issues.append(Issue("error", "gate", f"{path.name}:{line}", f"invalid gate result {gate!r}"))
            if selection not in ALLOWED_SELECTION:
                issues.append(Issue("error", "selection", f"{path.name}:{line}", f"invalid selection status {selection!r}"))
            if selection == "selected" and gate not in {"4/5 pass", "5/5 pass"}:
                issues.append(Issue("error", "selected_without_gate", f"{path.name}:{line}", "selected row must pass at least four of five target conditions"))
            url = row["source_url"].strip()
            parsed = urlparse(url)
            if url and (parsed.scheme not in {"http", "https"} or not parsed.netloc):
                issues.append(Issue("error", "source_url", f"{path.name}:{line}", "source_url must be absolute HTTP(S)"))
            if selection == "selected":
                key = {"pain_triggered": "selected_pain", "artifact_first": "selected_artifact", "embedded_service": "selected_operator"}.get(track)
                if key:
                    counts[key] += 1
    expected_keys = {"selected_pain": 2, "selected_artifact": 2, "selected_operator": 3}
    for key, target in expected_keys.items():
        if counts[key] > target:
            issues.append(Issue("error", "selection_overflow", path.name, f"{key} has {counts[key]} selected; maximum is {target}"))
        elif counts[key] < target:
            severity = "error" if require_complete else "warning"
            issues.append(Issue(severity, "selection_incomplete", path.name, f"{key} has {counts[key]} selected; target is {target}"))


def _load_yaml(path: Path, issues: list[Issue]) -> Any | None:
    if not path.is_file():
        return None
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        issues.append(Issue("error", "invalid_yaml", path.name, str(exc)))
        return None


def _validate_evidence(value: Any, issues: list[Issue], counts: dict[str, int]) -> None:
    if not isinstance(value, dict):
        issues.append(Issue("error", "evidence_root", "evidence_log.yaml", "root must be a mapping"))
        return
    run = value.get("run")
    if not isinstance(run, dict) or run.get("public_sources_only") is not True:
        issues.append(Issue("error", "source_boundary", "evidence_log.yaml", "public_sources_only must be true unless each exception is explicitly permissioned"))
    items = value.get("selected_items") or []
    if not isinstance(items, list):
        issues.append(Issue("error", "evidence_items", "evidence_log.yaml", "selected_items must be a list"))
        return
    counts["evidence_items"] = len(items)
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            issues.append(Issue("error", "evidence_item", f"evidence_log.yaml:selected_items[{index}]", "item must be a mapping"))
            continue
        sources = item.get("sources") or []
        if not sources:
            issues.append(Issue("error", "missing_sources", f"evidence_log.yaml:selected_items[{index}]", "selected item has no evidence sources"))
        for source in sources:
            if not isinstance(source, dict):
                continue
            url = str(source.get("url", "")).strip()
            parsed = urlparse(url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                issues.append(Issue("error", "evidence_url", f"evidence_log.yaml:selected_items[{index}]", f"invalid source URL {url!r}"))
            if source.get("public_or_permissioned") not in {"public", "permissioned"}:
                issues.append(Issue("error", "permission_status", f"evidence_log.yaml:selected_items[{index}]", "source must be labelled public or permissioned"))


def _validate_approval_queue(path: Path, issues: list[Issue], counts: dict[str, int]) -> None:
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    lowered = text.lower()
    if "send_actions_executed: false" not in lowered:
        issues.append(Issue("error", "approval_boundary", path.name, "queue must declare send_actions_executed: false"))
    if "queue_status: awaiting_human_decision" not in lowered:
        issues.append(Issue("error", "queue_status", path.name, "queue must await a human decision"))
    counts["approval_items"] = lowered.count("approval_item:")


def _validate_selected_artifacts(root: Path, issues: list[Issue], counts: dict[str, int]) -> None:
    expected = []
    for index in range(1, counts["selected_pain"] + 1):
        expected.extend([f"pain_triggered/target_{index:02d}_context_recovery_pack.md", f"pain_triggered/target_{index:02d}_delivery_draft.md"])
    for index in range(1, counts["selected_artifact"] + 1):
        expected.extend([f"artifact_first/target_{index:02d}_context_recovery_pack.md", f"artifact_first/target_{index:02d}_delivery_draft.md"])
    for index in range(1, counts["selected_operator"] + 1):
        expected.append(f"embedded_service/operator_{index:02d}_proposal.md")
    for relative in expected:
        path = root / relative
        if not path.is_file():
            issues.append(Issue("error", "selected_artifact_missing", relative, "selected item requires this artifact"))
            continue
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        if "delivery_draft" in relative and "send_status: blocked_pending_human_approval" not in text:
            issues.append(Issue("error", "draft_send_boundary", relative, "delivery draft must be blocked pending human approval"))
