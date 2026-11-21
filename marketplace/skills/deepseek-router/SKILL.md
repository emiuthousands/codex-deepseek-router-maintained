---
name: deepseek-router
description: Configure, diagnose, test, repair or uninstall the Skills-only Codex DeepSeek Router Marketplace Edition on Codex 0.149 or newer. Use only for router installation management, not everyday delegation.
---

# Codex DeepSeek Router Management

This Desktop-only edition supports Codex 0.149 and newer through the
`direct_codex` transport. It does not install or require lifecycle Hooks.

## Workflow

1. Run `python3 <plugin-root>/scripts/codex_deepseek_router.py status --json`.
2. Stop with `unsupported` when the detected Codex version is older than
   0.149 or when status does not report `transport_mode=direct_codex`.
3. For first-time configuration, run `setup --json`. If it returns
   `credential_missing`, accept the API key only through standard input with
   `--api-key-stdin`; never echo it or place it in command arguments.
4. Restart Codex or open a new task when setup reports that a new task is
   required.
5. Run `test --json` and require independent Flash and Pro proof.
6. After a parent-model upgrade or Codex update, run `repair --json`.

## Contracts

- Codex remains the parent and final decision maker.
- `deepseek_flash` uses `deepseek-v4-flash`; `deepseek_pro` uses
  `deepseek-v4-pro`.
- DeepSeek is text-only. Codex translates visual inputs into explicit text.
- Never claim success without the requested role, provider, model, transport,
  and a non-empty result.
- Never include credentials or raw event logs in user-facing output.

## Commands

- `status` — read-only configuration and runtime status.
- `setup` — install credentials, Agent definitions, and the model catalog.
- `doctor` — diagnose runtime, credentials, Agents, and connectivity.
- `test` — verify Flash and Pro independently through `direct_codex`.
- `delegate` — execute one bounded assignment through `direct_codex`.
- `repair` — refresh manager-owned configuration.
- `uninstall` — remove manager-owned state; keep credentials by default.
