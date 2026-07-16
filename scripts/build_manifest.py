#!/usr/bin/env python3
"""Build the subtree and repository checksum manifests."""

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EARLY = ROOT / "global25_experiments/experiments_01_07"
EXPERIMENT_14 = ROOT / "global25_experiments/experiments_08_15"


def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


early_files = sorted(
    path for path in EARLY.rglob("*") if path.is_file() and path.name != "SHA256SUMS"
)
(EARLY / "SHA256SUMS").write_text(
    "".join(f"{digest(path)}  ./{path.relative_to(EARLY).as_posix()}\n" for path in early_files),
    encoding="utf-8",
)

experiment_14_files = sorted(
    path
    for path in EXPERIMENT_14.rglob("*")
    if path.is_file()
    and (
        path.name.startswith("Experiment_14_")
        or path.parent.name == "analysis"
    )
    and path.name != "Experiment_14_SHA256SUMS.txt"
)
(EXPERIMENT_14 / "Experiment_14_SHA256SUMS.txt").write_text(
    "".join(
        f"{digest(path)}  {path.relative_to(EXPERIMENT_14).as_posix()}\n"
        for path in experiment_14_files
    ),
    encoding="utf-8",
)

files = sorted(
    path
    for path in ROOT.rglob("*")
    if path.is_file() and path.name not in {"MANIFEST.csv", "SHA256SUMS.txt"}
)
with (ROOT / "MANIFEST.csv").open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["path", "size_bytes", "sha256"])
    for path in files:
        writer.writerow([path.relative_to(ROOT).as_posix(), path.stat().st_size, digest(path)])

checksum_files = sorted(
    path for path in ROOT.rglob("*") if path.is_file() and path.name != "SHA256SUMS.txt"
)
(ROOT / "SHA256SUMS.txt").write_text(
    "".join(
        f"{digest(path)}  {path.relative_to(ROOT).as_posix()}\n" for path in checksum_files
    ),
    encoding="utf-8",
)

print(f"Wrote MANIFEST.csv with {len(files)} file records and SHA256SUMS.txt.")
