# NOTICE

## Community fork and copyright notice

This repository is an independently maintained community fork of
[TheBlindM/codex-deepseek-router](https://github.com/TheBlindM/codex-deepseek-router).
It retains the original repository history and is not an official continuation
of the original project. It is not affiliated with or endorsed by the original
project maintainers, OpenAI, or DeepSeek.

The original project and the adapted upstream code identified below remain
subject to their respective MIT License terms. Changes authored by
`emiuthousands` in this fork are also released under the MIT License unless a
file explicitly states otherwise. The combined copyright notices and MIT
permission text are recorded in [LICENSE](LICENSE).

Project names, logos, service marks, and trademarks remain the property of
their respective owners. The MIT License does not grant trademark rights.

This project incorporates and adapts implementation ideas and MIT-licensed
code from:

- [oil-oil/codex-deepseek-subagent](https://github.com/oil-oil/codex-deepseek-subagent)
  (MIT) — manager CLI structure, atomic-write/backup/manifest configuration
  transactions, macOS Keychain and Windows Credential Manager credential
  handling, Codex runtime discovery, and the dual-oracle native subagent smoke
  test concept.

- [Utopia-V/codex-deepseek-subagent](https://github.com/Utopia-V/codex-deepseek-subagent)
  (MIT) — the V2 one-shot plaintext `SubagentStart` handoff transport
  (stage / claim / consume / TTL / quarantine / file locking), the PowerShell
  hardened variant of that protocol, and the standalone custom-agent TOML
  provider configuration pattern.

Reasoning-routing design is additionally inspired by:

- [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite)
  and [yjh051108/dsh-router-standard](https://github.com/yjh051108/dsh-router-standard)
  — model-specific behavioral conditioning, first-turn anchoring, convergence
  guidance and model-specific empirical evaluation. These ideas are
  independently re-implemented as compact contracts; no DSH prompt block,
  runtime, injector, tool-routing implementation or retracted internal-model
  theory is copied or adopted as fact.

The DSH reference was reviewed from the suite gitlinks on 2026-08-18:
`dsh-routing-suite@d924ed0`, `injector@f4ef59f`, and
`dsh-router-standard@eff787e`. The pinned source's system-section replacement,
first-turn tool catalog, durable-tool promotion, near-field inbox injection,
mode override, and isolated LLM mechanisms are not copied. Only independently
worded, additive policy contracts and asymmetric Flash tuning are implemented.

## Upstream license notices

Both `oil-oil/codex-deepseek-subagent` and `Utopia-V/codex-deepseek-subagent`
are distributed under the MIT License. Their copyright notices and the full
MIT permission text are included in [LICENSE](LICENSE). The corresponding
attribution for adapted files remains recorded below:

- `scripts/codex_deepseek_router.py` —
  adapted from `oil-oil/codex-deepseek-subagent`
  `codex-deepseek-subagent/scripts/codex_deepseek.py` (MIT).
- `hooks/plaintext_handoff.py` and
  `hooks/plaintext-handoff.ps1` —
  adapted from `Utopia-V/codex-deepseek-subagent`
  `hooks/plaintext_handoff.py` and `hooks/plaintext-handoff.ps1` (MIT).

A per-symbol source map is maintained in
[docs/upstream-reference-map.md](docs/upstream-reference-map.md).
