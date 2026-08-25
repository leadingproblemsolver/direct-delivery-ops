from __future__ import annotations

import pytest

from direct_delivery_ops.routing import import_signalops_route


def _receipt() -> dict[str, object]:
    return {
        "route_key": "route-123",
        "artifact_id": "driftguard-v1",
        "artifact_url": "https://github.com/leadingproblemsolver/driftguard",
        "account_name": "Example AI",
        "contact_name": "A. Maintainer",
        "contact_title": "Platform Engineer",
        "contact_profile_url": "https://www.linkedin.com/in/example",
        "fit_reasons": ["Owns the runtime surface exercised by this artifact."],
        "next_action": "human_review",
    }


def test_import_preserves_route_and_stops_before_selection_or_send() -> None:
    imported = import_signalops_route(
        _receipt(),
        track="artifact_first",
        proposed_artifact="DriftGuard settlement preflight proof",
    )
    row = imported.as_dict()
    assert imported.route_key == "route-123"
    assert row["candidate_or_operator"] == "A. Maintainer"
    assert row["project_or_community"] == "Example AI"
    assert row["source_url"] == "https://www.linkedin.com/in/example"
    assert row["target_gate_result"] == ""
    assert row["selection_status"] == ""
    assert row["accessibility"] == "requires_live_human_review"


def test_rejects_upstream_route_that_bypasses_human_review() -> None:
    receipt = _receipt() | {"next_action": "send"}
    with pytest.raises(ValueError, match="human_review"):
        import_signalops_route(
            receipt,
            track="artifact_first",
            proposed_artifact="proof",
        )


def test_rejects_missing_source_url_and_unsupported_track() -> None:
    receipt = _receipt() | {"contact_profile_url": "", "artifact_url": ""}
    with pytest.raises(ValueError, match="source URL"):
        import_signalops_route(receipt, track="artifact_first", proposed_artifact="proof")
    with pytest.raises(ValueError, match="unsupported track"):
        import_signalops_route(_receipt(), track="cold_blast", proposed_artifact="proof")
