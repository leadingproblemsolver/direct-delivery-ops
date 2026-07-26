from __future__ import annotations

CANDIDATE_COLUMNS = (
    "track",
    "candidate_or_operator",
    "role",
    "project_or_community",
    "source_url",
    "evidence_or_corpus",
    "accessibility",
    "proposed_artifact",
    "target_gate_result",
    "selection_status",
    "reason",
)
TRACKS = {"pain_triggered", "artifact_first", "embedded_service"}
SELECTION_TARGETS = {"pain_triggered": 2, "artifact_first": 2, "embedded_service": 3}
ALLOWED_GATE_RESULTS = {"5/5 pass", "4/5 pass", "reject"}
ALLOWED_SELECTION = {"selected", "qualified_not_selected", "rejected"}
REQUIRED_ROOT = (
    "candidate_register.csv",
    "evidence_log.yaml",
    "verification_report.yaml",
    "human_approval_queue.md",
    "continuity.yaml",
    "run_summary.md",
)
