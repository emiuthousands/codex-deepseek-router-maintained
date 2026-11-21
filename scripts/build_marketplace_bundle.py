"""Build the Skills-only package for the OpenAI public plugin directory."""

from __future__ import annotations

import json
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Iterable


COPY_IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def _copy_tree(source: Path, target: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(f"required marketplace source directory is missing: {source}")
    shutil.copytree(source, target, ignore=COPY_IGNORE, dirs_exist_ok=True)


def _copy_file(source: Path, target: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"required marketplace source file is missing: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def _manifest(source_root: Path) -> dict:
    config = json.loads(
        (source_root / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    repository = config["repository"]
    interface = config["interface"]
    return {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": config["name"],
        "version": config["version"],
        "description": "Skills-only DeepSeek routing for Codex 0.149 and newer.",
        "author": config["author"],
        "homepage": config["homepage"],
        "repository": repository,
        "license": "MIT",
        "keywords": ["codex", "deepseek", "subagent", "router"],
        "extensions": {
            "com.openai": {
                "requires_local_executor": True,
                "onboardingSkill": "./skills/deepseek-router/SKILL.md",
                "interface": {
                    "displayName": interface["displayName"],
                    "shortDescription": "DeepSeek routing for Codex",
                    "longDescription": (
                        "Skills-only, Desktop-only routing of bounded text work "
                        "from Codex 0.149+ to DeepSeek Flash or Pro through the "
                        "direct_codex transport. The full GitHub edition retains "
                        "the legacy Hook transport for older Codex versions."
                    ),
                    "developerName": interface["developerName"],
                    "category": "Developer Tools",
                    "capabilities": ["Subagents", "Routing"],
                    "websiteURL": repository,
                    "supportURL": f"{repository}/issues",
                    "privacyPolicyURL": f"{repository}/blob/main/PRIVACY.md",
                    "termsOfServiceURL": f"{repository}/blob/main/TERMS.md",
                    "defaultPrompt": interface["defaultPrompt"],
                    "brandColor": interface["brandColor"],
                    "composerIcon": "./assets/icon.png",
                    "logo": "./assets/icon.png",
                },
                "publication": {
                    "release_notes": (
                        "Initial Skills-only Desktop edition for Codex 0.149+ "
                        "through direct_codex. No lifecycle Hook is included."
                    )
                },
            }
        },
    }


def _write_routing_skill(source_root: Path, stage: Path) -> None:
    source = source_root / "skills" / "use-deepseek-router" / "SKILL.md"
    fragment = (
        source_root
        / "marketplace"
        / "fragments"
        / "use-deepseek-router-tail.md"
    )
    text = source.read_text(encoding="utf-8")
    marker = "## Step 4 — Dispatch"
    if marker not in text:
        raise ValueError(f"routing skill is missing expected marker: {marker}")
    prefix = text.split(marker, 1)[0].rstrip() + "\n\n"
    prefix = prefix.replace(
        "description: Use the DeepSeek-backed deepseek_flash / deepseek_pro child agents "
        "through the installed one-shot plaintext SubagentStart handoff. Use whenever "
        "Codex considers spawning, continuing, or troubleshooting these agents; it "
        "governs modality classification, Flash/Pro model routing, FAST/REACT/SPEC/DEEP "
        "reasoning policy, plaintext staging, native fork_turns=none spawning and "
        "return, Flash-to-Pro escalation, one-shot state recovery, and the configured "
        "provider/DeepSeek data boundary.",
        "description: Route bounded work from Codex 0.149+ to DeepSeek Flash or Pro "
        "through the Desktop-only direct_codex transport. Use when Codex considers "
        "delegation, model or policy routing, escalation, verification, or "
        "troubleshooting of the configured DeepSeek provider.",
        1,
    )
    target = stage / "skills" / "use-deepseek-router" / "SKILL.md"
    target.write_text(prefix + fragment.read_text(encoding="utf-8"), encoding="utf-8")


def _iter_files(root: Path) -> Iterable[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def build_marketplace_bundle(source_root: Path, output_dir: Path) -> Path:
    """Create a ZIP that can be uploaded to the OpenAI plugin portal."""
    source_root = source_root.resolve()
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = _manifest(source_root)
    archive = output_dir / (
        f"codex-deepseek-router-marketplace-{manifest['version']}.zip"
    )

    with tempfile.TemporaryDirectory(prefix="codex-router-marketplace-") as temp:
        stage = Path(temp) / "plugin"
        stage.mkdir()

        for directory in ("agents", "runtime", "schemas", "assets"):
            _copy_tree(source_root / directory, stage / directory)
        _copy_tree(source_root / "skills", stage / "skills")
        _copy_tree(
            source_root / "marketplace" / "skills" / "deepseek-router",
            stage / "skills" / "deepseek-router",
        )

        references = stage / "references"
        references.mkdir()
        for name in ("multimodal.md", "routing-policy.md"):
            _copy_file(source_root / "references" / name, references / name)
        _copy_file(
            source_root / "marketplace" / "references" / "compatibility.md",
            references / "compatibility.md",
        )
        _copy_file(
            source_root / "marketplace" / "references" / "security.md",
            references / "security.md",
        )

        scripts = stage / "scripts"
        scripts.mkdir()
        _copy_file(
            source_root / "scripts" / "codex_deepseek_router.py",
            scripts / "codex_deepseek_router.py",
        )

        for name in (
            "LICENSE",
            "NOTICE.md",
            "PRIVACY.md",
            "TERMS.md",
        ):
            _copy_file(source_root / name, stage / name)
        _copy_file(source_root / "marketplace" / "SECURITY.md", stage / "SECURITY.md")
        _copy_file(source_root / "marketplace" / "README.md", stage / "README.md")
        _write_routing_skill(source_root, stage)
        (stage / "plugin.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
            for path in _iter_files(stage):
                bundle.write(path, path.relative_to(stage).as_posix())

    return archive
