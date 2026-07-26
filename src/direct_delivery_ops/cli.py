from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .manifest import write_manifest
from .validator import validate_workspace
from .workspace import WorkspaceError, initialize_workspace


def build_parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="direct-delivery", description="Initialize and validate human-approval-gated direct-delivery runs.")
    sub = root.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("root", type=Path)
    init.add_argument("--force", action="store_true")
    validate = sub.add_parser("validate")
    validate.add_argument("root", type=Path)
    validate.add_argument("--allow-incomplete", action="store_true", help="Validate an initialized or in-progress workspace without enforcing 2+2+3 release counts")
    manifest = sub.add_parser("manifest")
    manifest.add_argument("root", type=Path)
    manifest.add_argument("--output", type=Path, required=True)
    return root


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "init":
            print(json.dumps({"written": initialize_workspace(args.root, force=args.force)}, indent=2))
            return 0
        if args.command == "validate":
            report = validate_workspace(args.root, require_complete=not args.allow_incomplete)
            print(json.dumps({"valid": report.valid, "counts": report.counts, "issues": [issue.__dict__ for issue in report.issues]}, indent=2))
            return 0 if report.valid else 1
        if args.command == "manifest":
            write_manifest(args.root, args.output)
            print(json.dumps({"written": str(args.output)}, indent=2))
            return 0
    except (WorkspaceError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
