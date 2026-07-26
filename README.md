# Direct-Delivery Operations

A repository-ready control plane for producing source-linked Context Recovery Packs across pain-triggered, artifact-first, and embedded-service pathways—while enforcing provenance, selection gates, artifact completeness, and a hard stop before any send.

## Quick start

```bash
python -m pip install -e '.[test]'
direct-delivery init direct_delivery_run
direct-delivery validate direct_delivery_run
direct-delivery manifest direct_delivery_run --output direct_delivery_run/manifest.json
```

Use the exact prompt systems in `prompts/` to populate the workspace. The code does not search, scrape, message, or publish. It ensures that LLM/browser execution leaves behind auditable artifacts and cannot be presented as delivered before human approval.

## Dependency order

```text
requirements
→ candidate discovery
→ candidate register
→ target gate
→ selected targets
→ frozen artifact contract
→ bounded evidence log
→ recipient artifacts or operator proposals
→ verification
→ human approval queue
→ stop before sending
```

## Verified behavior

- Exact candidate CSV contract.
- 4-of-5 selection enforcement.
- Selection-count limits of 2 + 2 + 3.
- Public/permissioned evidence labels and absolute source URLs.
- Required artifacts for every selected target.
- Delivery drafts blocked pending human approval.
- Continuity and verification records preserve `send_actions_executed: false`.
- Content-hash manifest generation.

Live link validity, source terms, target identity, relationship safety, and recipient response require human review and live evidence.

## Validation modes

`direct-delivery validate RUN` is a strict release gate requiring exactly 2 pain-triggered targets, 2 artifact-first targets, 3 operators, 7 evidence items, and 7 approval items. Use `--allow-incomplete` only while the workspace is still being assembled.
