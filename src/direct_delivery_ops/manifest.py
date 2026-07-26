from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from typing import Any
import json


def build_manifest(root: Path) -> dict[str, Any]:
    files: dict[str, dict[str, Any]] = {}
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        data = path.read_bytes()
        files[relative] = {"sha256": sha256(data).hexdigest(), "bytes": len(data)}
    return {"schema_version": "1.0.0", "root": str(root.resolve()), "files": files, "send_actions_executed": False}


def write_manifest(root: Path, output: Path) -> None:
    output.write_text(json.dumps(build_manifest(root), indent=2, sort_keys=True) + "\n", encoding="utf-8")
