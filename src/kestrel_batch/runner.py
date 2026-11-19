"""kestrel-batch: lane scheduling and manifest fan-out."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

MAX_PARALLEL_PER_LANE = 4


@dataclass(frozen=True)
class WorkUnit:
    lane: str
    unit_id: str
    payload: bytes


def split_manifest(manifest: dict, lane: str, chunk_size: int) -> list[WorkUnit]:
    """Split a manifest into lane-sized work units."""
    items = manifest.get("items", [])
    units: list[WorkUnit] = []
    for start in range(0, len(items), chunk_size):
        chunk = items[start:start + chunk_size]
        unit_id = f"{lane}-{start // chunk_size:04d}"
        units.append(WorkUnit(lane=lane, unit_id=unit_id, payload=repr(chunk).encode()))
    return units


def schedule(units: Iterable[WorkUnit], inflight: int = 0) -> list[WorkUnit]:
    """Return units that may start now given the in-flight count."""
    budget = max(0, MAX_PARALLEL_PER_LANE - inflight)
    return list(units)[:budget]
