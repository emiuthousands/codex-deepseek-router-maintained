"""Marketplace package tests for the Skills-only desktop edition."""

import json
import zipfile
from pathlib import Path

from build_marketplace_bundle import build_marketplace_bundle


ROOT = Path(__file__).resolve().parents[1]


def test_marketplace_bundle_is_a_hookless_desktop_package(tmp_path):
    archive = build_marketplace_bundle(ROOT, tmp_path / "dist")

    with zipfile.ZipFile(archive) as package:
        names = set(package.namelist())
        manifest = json.loads(package.read("plugin.json"))
        routing_skill = package.read(
            "skills/use-deepseek-router/SKILL.md"
        ).decode("utf-8")

    assert archive.name == "codex-deepseek-router-marketplace-0.4.0.zip"
    assert "plugin.json" in names
    assert "scripts/codex_deepseek_router.py" in names
    assert "skills/deepseek-router/SKILL.md" in names
    assert "skills/use-deepseek-router/SKILL.md" in names
    assert "assets/icon.png" in names
    assert "LICENSE" in names
    assert "PRIVACY.md" in names
    assert "TERMS.md" in names

    assert not any(name.startswith("hooks/") for name in names)
    assert not any(name.startswith(".codex-plugin/") for name in names)
    assert not any(name.startswith(".agents/") for name in names)
    assert not any(name.startswith("tests/") for name in names)
    assert not any(name.startswith("eval/") for name in names)

    openai_extension = manifest["extensions"]["com.openai"]
    assert openai_extension["requires_local_executor"] is True
    assert "hooks" not in openai_extension
    assert "Hooks" not in openai_extension["interface"]["capabilities"]
    assert openai_extension["onboardingSkill"] == "./skills/deepseek-router/SKILL.md"
    assert openai_extension["interface"]["composerIcon"] == "./assets/icon.png"
    assert openai_extension["interface"]["logo"] == "./assets/icon.png"
    assert len(openai_extension["interface"]["displayName"]) <= 30
    assert len(openai_extension["interface"]["shortDescription"]) <= 30
    assert len(openai_extension["interface"]["defaultPrompt"]) <= 3
    assert all(
        len(prompt) <= 128
        for prompt in openai_extension["interface"]["defaultPrompt"]
    )
    assert "Codex 0.149+" in routing_skill
    assert "SubagentStart" not in routing_skill
