"""Create a complete direct-delivery workspace without overwriting evidence."""

from __future__ import annotations

from pathlib import Path
import csv

from .contracts import CANDIDATE_COLUMNS


class WorkspaceError(RuntimeError):
    pass


def initialize_workspace(root: Path, *, force: bool = False) -> list[str]:
    root = root.resolve()
    if root.exists() and any(root.iterdir()) and not force:
        raise WorkspaceError(f"workspace is not empty: {root}")
    root.mkdir(parents=True, exist_ok=True)
    if force:
        # Force only fills missing templates; it never deletes existing recipient evidence.
        pass
    for directory in ("pain_triggered", "artifact_first", "embedded_service", "artifacts", "logs"):
        (root / directory).mkdir(exist_ok=True)
    written: list[str] = []
    register = root / "candidate_register.csv"
    if not register.exists():
        with register.open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerow(CANDIDATE_COLUMNS)
        written.append(register.name)
    templates = {
        "evidence_log.yaml": "run:\n  generated_at: null\n  public_sources_only: true\n  explicit_permissioned_sources: []\n  collection_notes: []\nselected_items: []\n",
        "verification_report.yaml": "run_status: incomplete\nsend_actions_executed: false\nitems: []\nblocked_items: []\n",
        "continuity.yaml": "run:\n  current_phase: discovery\n  completed_without_sending: true\nartifact_index: {}\nunresolved: {}\napproval_state:\n  approved: []\n  revise: []\n  rejected: []\n  pending: []\n",
        "human_approval_queue.md": "---\nqueue_status: awaiting_human_decision\nsend_actions_executed: false\n---\n\n# Human Approval Queue\n\nNo item may be sent until a human records an explicit decision.\n",
        "run_summary.md": "# Direct-Delivery Run Summary\n\n## Execution status\n\nInitialized; no external action has been executed.\n",
        "pain_triggered/candidate_shortlist.md": "# Pain-Triggered Candidate Shortlist\n",
        "artifact_first/candidate_shortlist.md": "# Artifact-First Candidate Shortlist\n",
        "embedded_service/operator_shortlist.md": "# Embedded-Service Operator Shortlist\n",
    }
    for relative, content in templates.items():
        path = root / relative
        if not path.exists():
            path.write_text(content, encoding="utf-8")
            written.append(relative)
    return written
