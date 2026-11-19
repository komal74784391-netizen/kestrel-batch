# kestrel-batch

Batch lane orchestrator for the kestrel ingestion track.

**Status:** Released - v2.7.0 (production).

`kestrel-batch` splits incoming manifests into lane-sized work units, enforces
per-lane concurrency, and reports completion to the batch scheduler. Lanes are
configured with `BATCH_LANE`; runtime mode is read from `APP_MODE`.

## Layout

- `src/kestrel_batch/runner.py` - lane scheduling and manifest fan-out
- `src/kestrel_batch/manifest.py` - manifest parsing helpers
- `pyproject.toml` - build metadata
