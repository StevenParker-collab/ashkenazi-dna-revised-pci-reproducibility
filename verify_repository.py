#!/usr/bin/env python3
"""Verify repository integrity and run the component validators."""

import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
errors = []

required = [
    ROOT / "README.md",
    ROOT / "DATA_AVAILABILITY.md",
    ROOT / "CITATION.cff",
    ROOT / "manuscript/Ashkenazi_Population_Structure_Reassessed_Geometry_Update_2026-07-16.pdf",
    ROOT / "qpadm_fst/tables/table9_qpadm_results.csv",
    ROOT / "qpadm_fst/tables/table10_fst_results.csv",
    ROOT / "qpadm_fst/tables/table11_fst_calibration.csv",
    ROOT / "global25_experiments/experiments_08_15/Experiment_15_Raw_Data.tsv",
    ROOT / "MANIFEST.csv",
    ROOT / "SHA256SUMS.txt",
]
for path in required:
    if not path.is_file():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")

pdf = required[3]
if pdf.is_file() and not pdf.read_bytes().startswith(b"%PDF-"):
    errors.append("Manuscript does not have a PDF header")

checksums = ROOT / "SHA256SUMS.txt"
if checksums.is_file():
    for number, raw in enumerate(checksums.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            expected, relative = raw.split("  ", 1)
        except ValueError:
            errors.append(f"SHA256SUMS.txt:{number}: malformed line")
            continue
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Checksum target missing: {relative}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            errors.append(f"Checksum mismatch: {relative}")

validators = [
    ROOT / "qpadm_fst/scripts/validate_qpadm_fst.py",
    ROOT / "global25_experiments/scripts/validate_experiment_suite.py",
    ROOT / "global25_experiments/experiments_01_07/scripts/validate_repository.py",
    ROOT / "global25_experiments/experiments_08_15/analysis/verify_experiment14_germany_geometry.py",
]
for validator in validators:
    result = subprocess.run(
        [sys.executable, str(validator)], cwd=ROOT, text=True, capture_output=True
    )
    print(result.stdout, end="")
    if result.returncode:
        errors.append(f"Validator failed: {validator.relative_to(ROOT)}")
        if result.stderr:
            print(result.stderr, file=sys.stderr, end="")

if errors:
    print("Repository verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("Repository integrity verification passed.")
