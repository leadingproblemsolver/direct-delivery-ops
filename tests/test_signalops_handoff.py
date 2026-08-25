from __future__ import annotations

import pytest

from direct_delivery_ops.signalops import proposal_from_signalops_route


def route() -> dict[str, object]:
    return {
        "route_key": "route-123",
        "artifact_key": "artifact-key",
        "artifact_id": "tracecrumb-first60-incident-memory",
        "artifact_url": "https://github.com/leadingproblemsolver/TraceCrumb",
        "account_name": "Example Reliability Co",
        "account_search_identifier": "example.com",
        "account_observed_domain": "example.com",
        "account_source_id": "account-source",
        "contact_name": "A. Maintainer",
        "contact_title": "SRE Lead",
        "contact_profile_url": "https://www.linkedin.com/in/example",
        "contact_source_id": "contact-source",
        "fit_reasons": ["Public incident-response evidence matches the artifact wedge"],
        "personalization_evidence": ["Public talk about repeated diagnostic branches"],
        "identity_discrepancy": False,
        "next_action": "human_review",
    }


def test_signalops_route_becomes_unsent_human_review_proposal() -> None:
    proposal = proposal_from_signalops_route(route(), track="artifact_first")
    assert proposal.approval_state == "pending_human_review"
    assert proposal.send_actions_executed is False
    assert proposal.fit_reasons == (
        "Public incident-response evidence matches the artifact wedge",
    )
    markdown = proposal.to_approval_markdown()
    assert "STOP" in markdown
    assert "Send actions executed: `false`" in markdown
    assert "route-123" in markdown


def test_non_human_terminal_action_is_rejected() -> None:
    payload = route()
    payload["next_action"] = "send"
    with pytest.raises(ValueError, match="human_review"):
        proposal_from_signalops_route(payload, track="artifact_first")


def test_missing_fit_reasons_are_rejected() -> None:
    payload = route()
    payload["fit_reasons"] = []
    with pytest.raises(ValueError, match="fit reasons"):
        proposal_from_signalops_route(payload, track="artifact_first")


def test_track_must_be_existing_direct_delivery_track() -> None:
    with pytest.raises(ValueError, match="track must be one of"):
        proposal_from_signalops_route(route(), track="cold_spam")


def test_proposal_identity_is_deterministic() -> None:
    one = proposal_from_signalops_route(route(), track="artifact_first")
    two = proposal_from_signalops_route(route(), track="artifact_first")
    assert one.proposal_key == two.proposal_key
