# Architecture

The prompt engine and browser tools are external executors. This package owns the durable run state and release gate.

- `workspace.py`: creates all expected artifact paths without deleting existing evidence.
- `validator.py`: enforces candidate, source, artifact, and approval contracts.
- `manifest.py`: produces deterministic SHA-256 provenance for the run.
- Human: approves, revises, or rejects each proposed send.

No component has authority to contact a recipient.
