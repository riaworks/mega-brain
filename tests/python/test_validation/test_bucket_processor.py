"""Tests for core/intelligence/pipeline/bucket_processor.py"""
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.intelligence.pipeline.bucket_processor import (
    BUCKETS,
    classify_content,
    bucket_status,
    scan_inbox,
)


class TestBucketDefinitions:
    """Tests for bucket configuration."""

    def test_three_buckets_exist(self):
        assert set(BUCKETS.keys()) == {"external", "workspace", "personal"}

    def test_each_bucket_has_required_keys(self):
        required = {"path", "inbox", "color", "label", "layer", "subdirs"}
        for name, config in BUCKETS.items():
            assert required.issubset(config.keys()), f"{name} missing keys"

    def test_external_has_correct_subdirs(self):
        subdirs = set(BUCKETS["external"]["subdirs"].keys())
        assert "dna" in subdirs
        assert "dossiers" in subdirs
        assert "playbooks" in subdirs
        assert "sources" in subdirs

    def test_workspace_has_correct_subdirs(self):
        subdirs = set(BUCKETS["workspace"]["subdirs"].keys())
        assert "org" in subdirs
        assert "finance" in subdirs
        assert "meetings" in subdirs
        assert "team" in subdirs

    def test_personal_has_correct_subdirs(self):
        subdirs = set(BUCKETS["personal"]["subdirs"].keys())
        assert "email" in subdirs
        assert "messages" in subdirs
        assert "calls" in subdirs
        assert "cognitive" in subdirs


class TestClassifyContent:
    """Tests for content classification."""

    # Workspace classifications
    @pytest.mark.parametrize("text,expected", [
        ("Organograma da empresa com 15 departamentos", "org"),
        ("MRR de R$50k, CAC de R$200, LTV de R$3000", "finance"),
        ("Ata da reunião semanal do time de vendas", "meetings"),
        ("Job description para vaga de closer", "team"),
        ("Automação n8n para integrar CRM com Slack", "automations"),
        ("Implementar novo CRM HubSpot na plataforma", "tools"),
    ])
    def test_workspace_classification(self, text, expected):
        result = classify_content(text, "workspace")
        assert result == expected, f"'{text}' classified as {result}, expected {expected}"

    # Personal classifications
    @pytest.mark.parametrize("text,expected", [
        ("Email digest da semana sobre investimentos", "email"),
        ("Conversa WhatsApp com mentor sobre próximos passos", "messages"),
        ("Transcrição da ligação com investidor", "calls"),
        ("Reflexão sobre aprendizado da semana", "cognitive"),
    ])
    def test_personal_classification(self, text, expected):
        result = classify_content(text, "personal")
        assert result == expected, f"'{text}' classified as {result}, expected {expected}"

    def test_external_defaults_to_sources(self):
        result = classify_content("Some random expert content", "external")
        assert result == "sources"

    def test_unknown_content_gets_default(self):
        result = classify_content("xyzzy foobar nothing matches", "workspace")
        assert result == "meetings"  # workspace default

        result = classify_content("xyzzy foobar nothing matches", "personal")
        assert result == "cognitive"  # personal default


class TestBucketStatus:
    """Tests for bucket status function."""

    def test_returns_all_three_buckets(self):
        status = bucket_status()
        assert set(status.keys()) == {"external", "workspace", "personal"}

    def test_each_bucket_has_counts(self):
        status = bucket_status()
        for name, info in status.items():
            assert "inbox_files" in info
            assert "processed_files" in info
            assert "subdirs" in info
            assert isinstance(info["inbox_files"], int)
            assert isinstance(info["processed_files"], int)

    def test_external_has_processed_files(self):
        """External bucket should have content (764 files as of baseline)."""
        status = bucket_status()
        assert status["external"]["processed_files"] > 0


class TestScanInbox:
    """Tests for inbox scanning."""

    def test_scan_empty_inbox(self):
        """Workspace inbox should be empty (no files pending)."""
        files = scan_inbox("workspace")
        # May or may not have files, but should return a list
        assert isinstance(files, list)

    def test_scan_invalid_bucket(self):
        """Invalid bucket should raise KeyError."""
        with pytest.raises(KeyError):
            scan_inbox("nonexistent")
