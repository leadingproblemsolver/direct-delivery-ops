"""SignalOps distribution receipt -> Direct Delivery candidate adapter.

The adapter accepts a deterministic upstream route receipt and creates one candidate-row
shape for Direct Delivery Ops. It never marks the target selected, approved, or sent.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .contracts import CANDIDATE_COLUMNS, TRACKS


@dataclass(frozen=True, slots=True)
class ImportedRouteCandidate:
    route_key: str
    row: tuple[tuple[str, str], ...]

    def as_dict(self) -> dict[str, str]:
        return dict(self.row)


def import_signalops_route(
    receipt: Mapping[str, Any],
    *,
    track: str,
    proposed_artifact: str,
) -> ImportedRouteCandidate:
    """Import a SignalOps route without bypassing Direct Delivery's selection/approval gates."""

    if track not in TRACKS:
        raise ValueError(f"unsupported track: {track}")
    route_key = str(receipt.get("route_key") or "").strip()
    account = str(receipt.get("account_name") or "").strip()
    contact = str(receipt.get("contact_name") or "").strip()
    role = str(receipt.get("contact_title") or "").strip()
    source_url = str(receipt.get("contact_profile_url") or receipt.get("artifact_url") or "").strip()
    fit = receipt.get("fit_reasons") or ()
    if isinstance(fit, str):
        fit_reasons = (fit.strip(),) if fit.strip() else ()
    else:
        fit_reasons = tuple(str(item).strip() for item in fit if str(item).strip())
    artifact = proposed_artifact.strip()
    if not route_key or not account or not contact or not role or not source_url or not fit_reasons or not artifact:
        raise ValueError(
            "route_key, account/contact identity, role, source URL, fit_reasons, and proposed_artifact are required"
        )
    if str(receipt.get("next_action") or "").strip() != "human_review":
        raise ValueError("upstream route must terminate at human_review")

    evidence = "; ".join(fit_reasons)
    values = {
        "track": track,
        "candidate_or_operator": contact,
        "role": role,
        "project_or_community": account,
        "source_url": source_url,
        "evidence_or_corpus": f"SignalOps route {route_key}: {evidence}",
        "accessibility": "requires_live_human_review",
        "proposed_artifact": artifact,
        "target_gate_result": "",
        "selection_status": "",
        "reason": "Imported from SignalOps; Direct Delivery gate/selection/approval still required.",
    }
    row = tuple((column, values[column]) for column in CANDIDATE_COLUMNS)
    return ImportedRouteCandidate(route_key=route_key, row=row)
