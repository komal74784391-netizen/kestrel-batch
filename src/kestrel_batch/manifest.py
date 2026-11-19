"""Manifest parsing helpers for kestrel-batch."""

from __future__ import annotations

import json


class ManifestError(ValueError):
    """Raised when a manifest cannot be parsed."""


def load_manifest(raw: str) -> dict:
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ManifestError("manifest is not valid JSON") from exc
    if not isinstance(parsed, dict) or "items" not in parsed:
        raise ManifestError("manifest must be an object with an items list")
    return parsed


def validate_manifest(manifest: dict, max_items: int = 5000) -> None:
    items = manifest.get("items")
    if not isinstance(items, list):
        raise ManifestError("items must be a list")
    if len(items) > max_items:
        raise ManifestError("manifest exceeds the item limit")
