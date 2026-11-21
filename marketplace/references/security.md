# Security model

The Marketplace Edition is a Skills-only Desktop plugin. It contains no
lifecycle Hook.

Delegated work is sent to the configured DeepSeek-compatible OpenAI Responses
API endpoint. Images, screenshots, and video remain in the parent; only explicit
text facts may be delegated.

The parent should keep secrets, authentication headers, `.env` files, SSH keys,
and other sensitive material out of assignments and tool-result context.

Windows Agent definitions read `DEEPSEEK_API_KEY` from the user environment.
macOS uses Keychain. Linux uses the environment. The manager reports credential
presence without printing the credential.

`direct_codex` child execution uses a temporary isolated `CODEX_HOME`. The
parent model, provider, login, configuration, and persistent session database
remain unchanged.
