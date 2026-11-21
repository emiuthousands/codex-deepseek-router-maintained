# Security

## Data boundary

This Marketplace Edition sends delegated assignment text, related code context,
and tool results to the configured DeepSeek-compatible endpoint. The default is
`https://api.deepseek.com`. Users are responsible for trusting a custom endpoint.

The plugin does not send original images, screenshots, or video to DeepSeek.
Codex converts required visual facts into text before delegation.

## Credentials

- macOS: Keychain.
- Windows: Credential Manager plus the user environment variable
  `DEEPSEEK_API_KEY`, which the Windows Agent configuration reads.
- Linux: `DEEPSEEK_API_KEY`.

The installer accepts keys only through standard input. Keys must not appear in
command arguments, configuration files, JSON artifacts, temporary files, logs,
test fixtures, or user-facing output.

## Local execution

This is a Desktop-only plugin. It runs local Python and the Desktop-bundled
Codex runtime. It does not include lifecycle Hooks.

## Reporting

Report security issues privately to the repository maintainers. Do not include
API keys, private source code, or other credentials in a report.
