## Step 4 — Dispatch

1. Decide whether delegation materially improves cost, isolation, or quality.
2. Classify modality and keep sensitive or critical visual work in the parent.
3. Select Flash or Pro and a bounded FAST, REACT, SPEC, or DEEP policy.
4. Build a self-contained assignment with objective, scope, exclusions,
   permissions, output contract, acceptance criteria, verification owner, and
   stopping condition.
5. Read `status.transport_mode`. This Marketplace Edition requires
   `direct_codex` and Codex 0.149+. If that transport is unavailable,
   report `unsupported`; do not attempt a lifecycle Hook path.
6. Invoke
   `python3 <plugin-root>/scripts/codex_deepseek_router.py delegate --agent-type <role> --policy <POLICY> --modality <MODALITY> --workspace <workspace> --json`
   and send the complete assignment on stdin.
7. Require a successful result identifying `direct_codex`, the requested role,
   the expected DeepSeek model, and a non-empty message.
8. Validate the contribution against the assignment and integrate the final
   answer in the parent.

Ordinary assignments default to 900 seconds. Complex Pro + REACT assignments
containing the required standalone `QUALITY CLOSURE` section default to 1800
seconds. `--delegate-timeout <seconds>` is the only positive explicit override.

## Parent acceptance gate

- `BLOCKED`, `interrupted`, `cancelled`, and `failed` are not successful
  completion.
- Verify artifacts, diffs, tests, runtime output, and other observable evidence.
- Mark unavailable visual evidence as `UNVERIFIED`.
- Do not duplicate, overwrite, or take over an active child assignment.
- At most one bounded follow-up is permitted for a concrete material gap.

## Data boundary

DeepSeek receives the assignment text, related code context, and tool results.
Never include `.env` files, credentials, tokens, private keys, or authentication
headers. Original screenshots and visual media must remain in the parent.
