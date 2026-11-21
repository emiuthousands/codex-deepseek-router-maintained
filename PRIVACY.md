# Privacy

This document describes the privacy boundary of the
`codex-deepseek-router-maintained` plugin.

## Local execution

The plugin runs locally through Codex Desktop and Python. It does not operate a
personal-data backend or relay service.

## Data sent to DeepSeek

When a user explicitly delegates work, the plugin sends the assignment text,
relevant code context, and tool results to the configured DeepSeek-compatible
API endpoint. The default endpoint is `https://api.deepseek.com`. A user who
configures another endpoint is responsible for trusting that provider.

Screenshots, images, and video are not sent directly. Codex must convert the
relevant visual facts into text before delegation.

## Credentials

API keys are supplied by the user. The manager writes keys only through
standard input and stores them using the platform credential store where
available. Windows agents read the user environment variable
`DEEPSEEK_API_KEY`; macOS uses Keychain; Linux uses the environment variable.
The plugin does not send the key to OpenAI.

## Local state

Configuration, backups, and MCP handoff state may be stored under
`$CODEX_HOME/deepseek-router/`. Temporary delegation state is removed when the
execution ends. The user can remove manager-owned state with the `uninstall`
command.

## Contact

Report privacy or security concerns through the repository's GitHub Issues
page. For sensitive security reports, follow `SECURITY.md` and do not include
credentials or private source data.
