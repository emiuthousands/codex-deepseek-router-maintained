# Marketplace Edition Compatibility

This Skills-only package supports Codex 0.149 and newer through the
Desktop-compatible `direct_codex` transport.

It does not contain lifecycle Hooks and does not provide the legacy
`spawn_agent` plus plaintext-hook transport. For Codex 0.148 and older, install
the complete GitHub distribution instead:

https://github.com/emiuthousands/codex-deepseek-router-maintained

Each `direct_codex` delegation uses a temporary isolated `CODEX_HOME`. The
parent model, provider, login, and persistent session database remain
unchanged.

Supported runtime data:

- Python 3.9 or newer, standard library only.
- A compliant DeepSeek Responses API endpoint or custom compatible endpoint.
- The Desktop-bundled Codex runtime, with `CODEX_DESKTOP_BIN` as an optional
  discovery override.
