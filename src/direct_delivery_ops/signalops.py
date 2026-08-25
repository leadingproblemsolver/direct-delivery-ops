"""SignalOps route receipt -> approval-gated Direct Delivery proposal.

This adapter consumes the public mapping emitted by SignalOps
`DistributionRouteReceipt.to_dict()`. It never sends, publishes, or mutates CRM state.
Only receipts whose terminal action is `human_review` are accepted.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any, Mapping, Sequence

from .contracts import TRACKS


def _clean(value: object) -> str:
    return str(value or "").strip()


def _tuple(value: object) -> tuple[str, ...]:
    if isinstance(value, str):
        raw: Sequence[object] = (value,)
    elif isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray, str)):
        raw = value
    else:
        raw = ()
    return tuple(_clean(item) for item in raw if _clean(item))


@dataclass(frozen=True, slots=True)
class SignalOpsDeliveryProposal:
    route_key: str
    track: str
    artifact_id: str
    artifact_url: str
    account_name: str
    account_identifier: str
    contact_name: str
    contact_title: str
    contact_profile_url: str
    fit_reasons: tuple[str, ...]
    personalization_evidence: tuple[str, ...]
    identity_discrepancy: bool
    approval_state: str = "pending_human_review"
    send_actions_executed: bool = False

    @property
    def proposal_key(self) -> str:
        canonical = json.dumps(
            {
                "route_key": self.route_key,
                "track": self.track,
                "contact_profile_url": self.contact_profile_url,
                "artifact_id": self.artifact_id,
            },
            separators=(",", ":"),
            sort_keys=True,
        )
        return sha256(canonical.encode("utf-8")).hexdigest()[:24]

    def to_approval_markdown(self) -> str:
        reasons = "\n".join(f"- {item}" for item in self.fit_reasons)
        evidence = (
            "\n".join(f"- {item}" for item in self.personalization_evidence)
            if self.personalization_evidence
            else "- none supplied"
        )
        return (
            f"## {self.contact_name} — {self.account_name}\n\n"
            f"- Proposal key: `{self.proposal_key}`\n"
            f"- SignalOps route: `{self.route_key}`\n"
            f"- Track: `{self.track}`\n"
            f"- Contact role: {self.contact_title}\n"
            f"- Contact source: {self.contact_profile_url}\n"
            f"- Artifact: [{self.artifact_id}]({self.artifact_url})\n"
            f"- Account identifier: `{self.account_identifier}`\n"
            f"- Identity discrepancy: `{str(self.identity_discrepancy).lower()}`\n"
            f"- Approval state: `{self.approval_state}`\n"
            f"- Send actions executed: `{str(self.send_actions_executed).lower()}`\n\n"
            "### Explicit fit reasons\n"
            f"{reasons}\n\n"
            "### Personalization evidence\n"
            f"{evidence}\n\n"
            "**STOP:** a human must approve, revise, or reject this proposal before any external action.\n"
        )


def proposal_from_signalops_route(
    route: Mapping[str, Any],
    *,
    track: str,
) -> SignalOpsDeliveryProposal:
    """Normalize one SignalOps route into an unsent approval proposal."""

    selected_track = track.strip()
    if selected_track not in TRACKS:
        raise ValueError(f"track must be one of: {', '.join(sorted(TRACKS))}")
    if _clean(route.get("next_action")) != "human_review":
        raise ValueError("SignalOps route must terminate at human_review")

    required = {
        "route_key": _clean(route.get("route_key")),
        "artifact_id": _clean(route.get("artifact_id")),
        "artifact_url": _clean(route.get("artifact_url")),
        "account_name": _clean(route.get("account_name")),
        "account_identifier": _clean(route.get("account_search_identifier")),
        "contact_name": _clean(route.get("contact_name")),
        "contact_title": _clean(route.get("contact_title")),
        "contact_profile_url": _clean(route.get("contact_profile_url")),
    }
    missing = [key for key, value in required.items() if not value]
    if missing:
        raise ValueError(f"SignalOps route missing required fields: {', '.join(missing)}")
    fit_reasons = _tuple(route.get("fit_reasons"))
    if not fit_reasons:
        raise ValueError("SignalOps route requires explicit fit reasons")

    return SignalOpsDeliveryProposal(
        **required,
        track=selected_track,
        fit_reasons=fit_reasons,
        personalization_evidence=_tuple(route.get("personalization_evidence")),
        identity_discrepancy=bool(route.get("identity_discrepancy")),
    )
