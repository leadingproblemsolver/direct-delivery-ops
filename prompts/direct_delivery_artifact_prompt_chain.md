# DIRECT-DELIVERY ARTIFACT PROMPT CHAIN

Run these prompts **in order** inside the same browser-use workspace.

Each prompt must:
- read the existing contents of `direct_delivery_run/`;
- create or finalize the named artifact;
- preserve source URLs and provenance;
- use public sources only unless explicit permission is documented;
- separate evidence from inference;
- stop before sending, publishing, commenting, or messaging anyone;
- return only a one-line completion status after writing the artifact.

Do not skip ahead. Do not replace weak targets merely to satisfy a quota.

---

# PROMPT 01 — `candidate_register.csv`

Act as the discovery and qualification operator for a direct-delivery market-validation run.

## Current wedge

Recover and reconnect valuable project knowledge that already exists but has become operationally difficult to re-find across public or explicitly permissioned files, repositories, discussions, posts, papers, notes, exports, and project materials.

The deliverable to recipients is a compact, source-linked **Context Recovery Pack**. Do not sell “AI memory,” a second brain, or a broad knowledge platform.

## Task

Create:

```text
direct_delivery_run/candidate_register.csv
```

Search all three pathways:

1. `pain_triggered`
2. `artifact_first`
3. `embedded_service`

Build exactly five credible candidates for each pathway when the evidence supports that number. Do not pad the register with weak candidates.

### Pain-triggered candidates

Find accessible people who have publicly stated a concrete retrieval, continuity, fragmented-context, lost-decision, or project-memory problem.

Record the exact public quote and URL. Do not infer pain beyond the statement.

### Artifact-first candidates

Find accessible technical founders, maintainers, developer-researchers, researchers, consultants, analysts, or public builders with at least three relevant public sources and one real retrieval, navigation, orientation, or continuity job.

Do not claim that a person is disorganized merely because their work spans several sources.

### Embedded-service operators

Find accessible operators with:
- a visible community or member base;
- direct interaction with members;
- a reachable contact surface;
- plausible members with fragmented project material;
- enough trust or authority to nominate three to five cases.

## Universal target gate

A row passes only when at least four of these five conditions are true:

1. explicit pain or a visible multi-source public corpus exists;
2. the person or operator is realistically reachable;
3. a genuinely useful artifact can be produced from ethical sources;
4. the artifact or proposal can be completed in 60 minutes or less;
5. delivery could plausibly produce reuse, correction, extension, referral, or learning.

Reject:
- prestige targets selected mainly for visibility;
- inaccessible flagship projects;
- targets requiring private data before value can be shown;
- outputs that would primarily criticize the recipient;
- generic AI audiences;
- candidates with no visible corpus or declared problem;
- abandoned projects with no active human relationship surface;
- any case requiring deception, paywall bypass, login circumvention, or prohibited scraping.

## Selection rule

Mark:
- the best two passing `pain_triggered` candidates as `selected`;
- the best two passing `artifact_first` candidates as `selected`;
- the best three passing `embedded_service` operators as `selected`.

Rank by evidence quality, accessibility, bounded usefulness, ethical deliverability, and practical learning value.

## Exact CSV schema

```csv
track,candidate_or_operator,role,project_or_community,source_url,evidence_or_corpus,accessibility,proposed_artifact,target_gate_result,selection_status,reason
```

Use:
- `target_gate_result`: `5/5 pass`, `4/5 pass`, or `reject`;
- `selection_status`: `selected`, `qualified_not_selected`, or `rejected`;
- semicolon-separated URLs or evidence summaries where one CSV cell must contain several sources.

Do not create recipient artifacts or outreach drafts yet.

Write the CSV, validate that it opens correctly, and stop.

---

# PROMPT 02 — `pain_triggered/candidate_shortlist.md`

Act as the pain-triggered selection analyst.

Read:

```text
direct_delivery_run/candidate_register.csv
```

Create:

```text
direct_delivery_run/pain_triggered/candidate_shortlist.md
```

## Required content

Include all pain-triggered candidates in ranked order.

For each candidate record:

```yaml
pain_candidate:
  rank:
  handle_or_name:
  role_or_context:
  source_url:
  exact_quote:
  quote_date:
  stated_problem:
  visible_source_or_corpus:
  stated_or_visible_workaround:
  consequence:
  recurrence:
  reachable_channel:
  plausible_context_recovery_pack:
  target_gate_result:
  selection_status:
  selection_reason:
  disqualifying_risk:
```

Rules:
- preserve the exact quote and direct source URL;
- do not infer unstated consequences, recurrence, or emotional state;
- write `unknown` where public evidence does not establish a field;
- identify exactly two selected candidates only when both pass the gate;
- explain why the selected pair has the strongest combination of declared pain, usable sources, reachability, and bounded artifact value;
- do not produce the packs yet.

End with:

```yaml
selected_targets:
  target_01:
  target_02:
selection_locked: true
```

Write the file and stop.

---

# PROMPT 03 — `artifact_first/candidate_shortlist.md`

Act as the artifact-first selection analyst.

Read:

```text
direct_delivery_run/candidate_register.csv
```

Create:

```text
direct_delivery_run/artifact_first/candidate_shortlist.md
```

## Required content

Include all artifact-first candidates in ranked order.

For each candidate record:

```yaml
artifact_first_candidate:
  rank:
  person:
  role:
  project_or_body_of_work:
  public_sources:
    - title:
      url:
      source_type:
  source_count:
  visible_retrieval_orientation_or_continuity_job:
  reachable_channel:
  proposed_artifact:
  exact_function:
  immediate_use:
  target_gate_result:
  selection_status:
  selection_reason:
  disqualifying_risk:
```

Rules:
- require at least three relevant public sources for a selected candidate;
- define a real job, not a generic biography;
- do not infer pain, disorder, neglect, or incompetence;
- favor a source set that can be bounded and inspected immediately;
- identify exactly two selected candidates only when both pass the gate;
- do not produce the packs yet.

End with:

```yaml
selected_targets:
  target_01:
  target_02:
selection_locked: true
```

Write the file and stop.

---

# PROMPT 04 — `embedded_service/operator_shortlist.md`

Act as the embedded-service operator analyst.

Read:

```text
direct_delivery_run/candidate_register.csv
```

Create:

```text
direct_delivery_run/embedded_service/operator_shortlist.md
```

## Required content

Include all embedded-service candidates in ranked order.

For each operator record:

```yaml
operator_candidate:
  rank:
  name:
  role:
  community:
  community_url:
  member_type:
  evidence_of_active_operation:
  reachable_contact_surface:
  plausible_member_problem:
  suggested_artifact_type:
  stable_pilot_function:
  nomination_path:
  privacy_boundary:
  target_gate_result:
  selection_status:
  selection_reason:
  disqualifying_risk:
```

Rules:
- verify that the operator actively interacts with members;
- define a plausible route for the operator to nominate three to five cases;
- do not request or imply access to an entire member list;
- do not treat the operator as a lead broker;
- identify exactly three selected operators only when all pass the gate.

End with:

```yaml
selected_operators:
  operator_01:
  operator_02:
  operator_03:
selection_locked: true
```

Write the file and stop.

---

# PROMPT 05 — `evidence_log.yaml`

Act as the source-boundary and evidence custodian.

Read:

```text
direct_delivery_run/candidate_register.csv
direct_delivery_run/pain_triggered/candidate_shortlist.md
direct_delivery_run/artifact_first/candidate_shortlist.md
direct_delivery_run/embedded_service/operator_shortlist.md
```

Create:

```text
direct_delivery_run/evidence_log.yaml
```

## Scope

Collect and verify only the evidence needed for:
- two selected pain-triggered targets;
- two selected artifact-first targets;
- three selected embedded-service operators.

Do not expand the corpus merely because more sources exist.

## Required YAML structure

```yaml
run:
  generated_at:
  public_sources_only: true
  explicit_permissioned_sources:
  collection_notes:

selected_items:
  - id:
    pathway:
    subject:
    artifact_or_proposal_function:
    source_boundary:
    sources:
      - source_id:
        title:
        url:
        source_type:
        publication_or_update_date:
        accessed_at:
        public_or_permissioned:
        relevant_excerpt_or_factual_summary:
        relevance:
        supports:
        limitations:
        link_status:
    evidence_claims:
      - claim_id:
        claim:
        support_source_ids:
        status: supported
    permitted_inferences:
      - inference_id:
        inference:
        supporting_source_ids:
        required_label: inference
    explicit_unknowns:
    excluded_sources:
    privacy_or_relationship_risks:
```

Requirements:
- preserve direct links;
- distinguish verbatim public quotes from paraphrased factual summaries;
- never convert inference into evidence;
- record broken, inaccessible, stale, or ambiguous links;
- exclude private, gated, personal, or unnecessary data;
- state the exact source boundary for each selected item;
- leave unsupported claims out rather than rationalizing them.

Write valid YAML, parse-check it, and stop.

---

# PROMPT 06 — `pain_triggered/target_01_context_recovery_pack.md`

Act as the Context Recovery Pack producer for the first selected pain-triggered target.

Read:

```text
direct_delivery_run/pain_triggered/candidate_shortlist.md
direct_delivery_run/evidence_log.yaml
```

Create:

```text
direct_delivery_run/pain_triggered/target_01_context_recovery_pack.md
```

Use only the target identified as `target_01`.

## Artifact contract

Choose the narrowest useful variant:
- source-linked project context pack;
- decision-history map;
- cross-source retrieval index;
- repository orientation file;
- forgotten-work inventory;
- recovered-source map.

The artifact must perform exactly one real function tied to the target’s publicly stated problem.

## Required structure

```yaml
context_recovery_pack:
  title:
  recipient_or_project:
  exact_function:
  source_boundary:
  sources_used:
    - title:
      url:
      source_type:
      relevance:
  recovered_context:
  decisions_or_threads:
  unresolved_or_disconnected_material:
  direct_retrieval_paths:
  explicit_unknowns:
  public_source_limitations:
  suggested_immediate_use:
```

Production rules:
- one recipient;
- one bounded body of work;
- one clear function;
- direct links to original sources;
- evidence explicitly separated from inference;
- no diagnosis;
- no critique;
- no completeness claim;
- no generic biography;
- no product pitch;
- one to three pages unless evidence genuinely requires more;
- every consequential statement must be supported by `evidence_log.yaml`;
- remove any section that has no useful supported content rather than filling it with generic text.

Finish the file with:

```yaml
artifact_self_check:
  one_real_function:
  source_fidelity:
  evidence_inference_separated:
  no_private_source_violation:
  no_unsolicited_critique:
  no_product_pitch:
  within_scope:
```

Write the artifact and stop.

---

# PROMPT 07 — `pain_triggered/target_01_delivery_draft.md`

Act as the delivery-message writer for the first pain-triggered target.

Read:

```text
direct_delivery_run/pain_triggered/candidate_shortlist.md
direct_delivery_run/pain_triggered/target_01_context_recovery_pack.md
direct_delivery_run/evidence_log.yaml
```

Create:

```text
direct_delivery_run/pain_triggered/target_01_delivery_draft.md
```

## Message contract

Write one concise, relationship-safe message that:
- refers accurately to the target’s public statement;
- makes the completed value visible before any request;
- names the artifact’s exact function;
- links or points to the artifact location;
- asks one correction-oriented validation question;
- contains no pitch, call request, follow-up sequence, urgency, flattery, or claim of completeness.

Use this shape, adapting it to the evidence:

```text
You mentioned [precise stated problem].

I used the public material connected to it to assemble a small [artifact name] that [specific function]. Sharing it in case it saves some reconstruction.

[artifact location]

What is the most important thing this still gets wrong or leaves hard to find?
```

Add a small internal metadata block after the draft:

```yaml
delivery_metadata:
  recipient:
  channel:
  source_statement_url:
  artifact_path:
  validation_signal_tested:
  send_status: blocked_pending_human_approval
```

Do not send. Write the draft and stop.

---

# PROMPT 08 — `pain_triggered/target_02_context_recovery_pack.md`

Repeat the production contract from **PROMPT 06**, but use only `target_02` and create:

```text
direct_delivery_run/pain_triggered/target_02_context_recovery_pack.md
```

The target, source boundary, artifact variant, exact function, and retrieval paths must be independently derived from `target_02`; do not clone the structure or conclusions of target 01 merely for consistency.

Write the artifact and stop.

---

# PROMPT 09 — `pain_triggered/target_02_delivery_draft.md`

Repeat the delivery contract from **PROMPT 07**, but use only `target_02` and create:

```text
direct_delivery_run/pain_triggered/target_02_delivery_draft.md
```

Do not reuse target 01’s wording unless the evidence genuinely warrants the same language.

Do not send. Write the draft and stop.

---

# PROMPT 10 — `artifact_first/target_01_context_recovery_pack.md`

Act as the Context Recovery Pack producer for the first selected artifact-first target.

Read:

```text
direct_delivery_run/artifact_first/candidate_shortlist.md
direct_delivery_run/evidence_log.yaml
```

Create:

```text
direct_delivery_run/artifact_first/target_01_context_recovery_pack.md
```

Use only the target identified as `target_01`.

## Artifact contract

Define one real function, such as:
- reopen key project decisions;
- navigate a public source set;
- recover unfinished public threads;
- orient a contributor to major components;
- connect papers, repositories, talks, and active questions.

Choose the narrowest suitable pack variant:
- source-linked project context pack;
- decision-history map;
- cross-source retrieval index;
- repository orientation file;
- forgotten-work inventory;
- recovered-source map.

Use this exact structure:

```yaml
context_recovery_pack:
  title:
  recipient_or_project:
  exact_function:
  source_boundary:
  sources_used:
    - title:
      url:
      source_type:
      relevance:
  recovered_context:
  decisions_or_threads:
  unresolved_or_disconnected_material:
  direct_retrieval_paths:
  explicit_unknowns:
  public_source_limitations:
  suggested_immediate_use:
```

Rules:
- state prominently that only public sources were used;
- never imply that the recipient has a problem they did not state;
- separate evidence from inference;
- no diagnosis, critique, completeness claim, biography, or pitch;
- keep the artifact to one to three pages;
- make it immediately inspectable and useful without a call;
- support every consequential statement from `evidence_log.yaml`.

Finish with the same `artifact_self_check` block used in PROMPT 06.

Write the artifact and stop.

---

# PROMPT 11 — `artifact_first/target_01_delivery_draft.md`

Act as the delivery-message writer for the first artifact-first target.

Read:

```text
direct_delivery_run/artifact_first/candidate_shortlist.md
direct_delivery_run/artifact_first/target_01_context_recovery_pack.md
direct_delivery_run/evidence_log.yaml
```

Create:

```text
direct_delivery_run/artifact_first/target_01_delivery_draft.md
```

Use one of these structures, choosing the one that best fits the target.

### Structure A

```text
I used only the public material around [project/body of work] to create a small [artifact name] that [specific function].

No pitch—I’m testing whether source-linked context-recovery artifacts like this are actually useful in practice.

[artifact location]

What did you expect this to surface that it missed?
```

### Structure B

```text
I noticed the public work around [topic/project] spans [named source types].

I assembled a small source-linked [artifact] so the key [materials/decisions/threads] can be scanned and reopened from one place.

[artifact location]

Is this useful enough to keep, or is it solving a problem you do not actually have?
```

Rules:
- no unsupported pain claim;
- no flattery;
- no request for a call;
- no product pitch;
- no follow-up sequence;
- one direct validation question testing usefulness, correction, or rejection.

Append:

```yaml
delivery_metadata:
  recipient:
  channel:
  public_source_boundary:
  artifact_path:
  validation_signal_tested:
  send_status: blocked_pending_human_approval
```

Do not send. Write the draft and stop.

---

# PROMPT 12 — `artifact_first/target_02_context_recovery_pack.md`

Repeat the production contract from **PROMPT 10**, but use only `target_02` and create:

```text
direct_delivery_run/artifact_first/target_02_context_recovery_pack.md
```

Derive its exact function and artifact variant independently.

Write the artifact and stop.

---

# PROMPT 13 — `artifact_first/target_02_delivery_draft.md`

Repeat the delivery contract from **PROMPT 11**, but use only `target_02` and create:

```text
direct_delivery_run/artifact_first/target_02_delivery_draft.md
```

Do not send. Write the draft and stop.

---

# PROMPT 14 — `embedded_service/operator_01_proposal.md`

Act as the embedded-service proposal writer for the first selected operator.

Read:

```text
direct_delivery_run/embedded_service/operator_shortlist.md
direct_delivery_run/evidence_log.yaml
```

Create:

```text
direct_delivery_run/embedded_service/operator_01_proposal.md
```

Use only `operator_01`.

## Proposal requirements

Tailor:
- the member type;
- the stable Context Recovery Pack function;
- the nominee criteria;
- the public or permissioned source boundary;
- the operator’s nomination pathway;
- behavioral success criteria.

Use this base structure, rewriting it for the actual operator:

```text
I’m testing a narrow source-linked Context Recovery Pack for [member type] who work across fragmented project material and need to recover prior decisions, resources, or active context.

Rather than promote a tool to the community, I’d like to produce 3–5 completed packs for people you nominate and let the results determine whether the capability is genuinely useful.

I would use only public material or sources explicitly approved by each participant. Each pack would return direct source links, recovered context, unresolved threads, and clear source limitations. I would share aggregate patterns with you without exposing private member material.

A strong nominee would have:
- [criterion 1]
- [criterion 2]
- [criterion 3]

The pilot is successful only if recipients reuse the pack, expand the source set, request another version, refer someone, or ask for continued access.
```

Then add:

```yaml
proposal_metadata:
  operator:
  community:
  reachable_channel:
  member_type:
  proposed_case_count: 3-5
  stable_artifact_function:
  nomination_path:
  source_boundary:
  privacy_boundary:
  behavioral_success_signals:
  send_status: blocked_pending_human_approval
```

Rules:
- do not request the member list;
- do not ask the operator to market a product;
- do not imply access to private community data;
- do not treat members as leads;
- do not send.

Write the proposal and stop.

---

# PROMPT 15 — `embedded_service/operator_02_proposal.md`

Repeat the proposal contract from **PROMPT 14**, but use only `operator_02` and create:

```text
direct_delivery_run/embedded_service/operator_02_proposal.md
```

Tailor the member type, nomination criteria, artifact function, source boundary, and success signals independently.

Do not send. Write the proposal and stop.

---

# PROMPT 16 — `embedded_service/operator_03_proposal.md`

Repeat the proposal contract from **PROMPT 14**, but use only `operator_03` and create:

```text
direct_delivery_run/embedded_service/operator_03_proposal.md
```

Tailor the member type, nomination criteria, artifact function, source boundary, and success signals independently.

Do not send. Write the proposal and stop.

---

# PROMPT 17 — `verification_report.yaml`

Act as the CTO verifier and release gate.

Read every artifact currently inside:

```text
direct_delivery_run/
```

Create:

```text
direct_delivery_run/verification_report.yaml
```

## Verify every selected target, pack, draft, operator, and proposal

For each item check:

```yaml
verification:
  target_gate_passed:
  source_fidelity:
  direct_links_work:
  evidence_inference_separated:
  one_real_function:
  within_time_and_scope:
  no_private_source_violation:
  no_unsupported_pain_claim:
  no_unsolicited_critique:
  no_product_pitch:
  no_call_required_before_value:
  recipient_can_judge_without_call:
  validation_question_tests_pull:
  relationship_safety:
  send_has_not_occurred:
```

## Repair policy

If a failure can be repaired by:
- narrowing scope;
- deleting unsupported text;
- explicitly labelling inference;
- correcting a source link;
- replacing vague wording with source-supported wording;
- removing pitch language;
- strengthening the validation question;

make the smallest safe edit to the affected artifact, record it under `repairs_made`, and verify again.

Do not:
- replace a weak selected target with a lower-quality one;
- invent evidence;
- broaden the source boundary;
- turn a critique into softer-sounding critique;
- approve a send merely to hit the target count.

## Required YAML structure

```yaml
run_verification:
  overall_status:
  verified_at:
  source_link_check_method:
  items:
    - id:
      pathway:
      subject:
      artifact_or_proposal_path:
      message_or_proposal_path:
      checks:
        target_gate_passed:
        source_fidelity:
        direct_links_work:
        evidence_inference_separated:
        one_real_function:
        within_time_and_scope:
        no_private_source_violation:
        no_unsupported_pain_claim:
        no_unsolicited_critique:
        no_product_pitch:
        no_call_required_before_value:
        recipient_can_judge_without_call:
        validation_question_tests_pull:
        relationship_safety:
        send_has_not_occurred:
      repairs_made:
      unresolved_failures:
      release_status:
  blocked_items:
  aggregate_counts:
    selected_targets:
    completed_recipient_artifacts:
    completed_delivery_drafts:
    selected_operators:
    completed_operator_proposals:
    verified_for_human_review:
```

Allowed `release_status` values:
- `verified_for_human_review`
- `revise_before_review`
- `rejected`

Parse-check the YAML and stop.

---

# PROMPT 18 — `human_approval_queue.md`

Act as the human-approval queue compiler.

Read:

```text
direct_delivery_run/verification_report.yaml
direct_delivery_run/pain_triggered/
direct_delivery_run/artifact_first/
direct_delivery_run/embedded_service/
```

Create:

```text
direct_delivery_run/human_approval_queue.md
```

Create one approval item for each of:
- two pain-triggered delivery drafts;
- two artifact-first delivery drafts;
- three embedded-service operator proposals.

Use:

```yaml
approval_item:
  id:
  pathway:
  recipient:
  channel:
  artifact_or_proposal:
  message:
  why_this_target:
  source_boundary:
  risks:
  verifier_status:
  approval_needed:
    - send
    - revise
    - reject
```

Rules:
- quote the finalized message or proposal exactly;
- include the artifact path;
- make all unresolved risks visible;
- mark failed items `revise` or `reject`, never `send`;
- do not send, publish, comment, or message anyone;
- do not include strategic commentary outside the queue.

Begin the file with:

```yaml
queue_status: awaiting_human_decision
send_actions_executed: false
```

End with:

> Review the human approval queue and approve, revise, or reject each proposed send.

Write the queue and stop.

---

# PROMPT 19 — `run_summary.md`

Act as the run summarizer.

Read every finalized file in:

```text
direct_delivery_run/
```

Create:

```text
direct_delivery_run/run_summary.md
```

## Required sections

```markdown
# Direct-Delivery Run Summary

## Execution status

## Candidate volume
- Pain-triggered:
- Artifact-first:
- Embedded-service:

## Selected pain-triggered targets
### Target 01
### Target 02

## Selected artifact-first targets
### Target 01
### Target 02

## Selected embedded-service operators
### Operator 01
### Operator 02
### Operator 03

## Completed recipient artifacts

## Completed delivery drafts

## Completed operator proposals

## Verification result

## Blocked or unresolved items

## Human approval status

## Exact next action
```

Requirements:
- use the actual counts and statuses;
- link every completed artifact by relative path;
- do not claim completion for missing or failed files;
- state explicitly that nothing has been sent;
- do not end with more strategy.

The exact next action must be:

> Review the human approval queue and approve, revise, or reject each proposed send.

Write the summary and stop.

---

# PROMPT 20 — `continuity.yaml`

Act as the continuity-state writer for the next execution session.

Read every finalized file in:

```text
direct_delivery_run/
```

Create:

```text
direct_delivery_run/continuity.yaml
```

## Required structure

```yaml
run:
  run_id:
  current_phase: human_approval
  started_at:
  finalized_at:
  current_wedge:
  completed_without_sending: true

artifact_index:
  candidate_register:
  evidence_log:
  pain_triggered_shortlist:
  pain_triggered_packs:
  pain_triggered_drafts:
  artifact_first_shortlist:
  artifact_first_packs:
  artifact_first_drafts:
  operator_shortlist:
  operator_proposals:
  verification_report:
  human_approval_queue:
  run_summary:

selected_items:
  pain_triggered:
    - id:
      subject:
      artifact:
      delivery_draft:
      verification_status:
  artifact_first:
    - id:
      subject:
      artifact:
      delivery_draft:
      verification_status:
  embedded_service:
    - id:
      operator:
      proposal:
      verification_status:

unresolved:
  evidence_gaps:
  broken_links:
  blocked_items:
  relationship_risks:
  required_revisions:

approval_state:
  queue_path:
  approved:
  revise:
  rejected:
  pending:

next_action:
  exact_instruction: Review the human approval queue and approve, revise, or reject each proposed send.
  do_not_execute_without_approval:
    - send
    - publish
    - comment
    - post
    - message
```

Requirements:
- include only paths that actually exist;
- preserve exact selected IDs and names;
- make every unresolved issue machine-readable;
- do not introduce new targets, recommendations, or strategy;
- parse-check the YAML.

Write the file and stop.
