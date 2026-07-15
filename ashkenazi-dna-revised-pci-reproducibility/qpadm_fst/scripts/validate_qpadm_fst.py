#!/usr/bin/env python3
"""Cross-check retained qpAdm and FST specifications against manuscript tables."""

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
errors = []


def read_dicts(path, delimiter=","):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


qpadm_specs = read_dicts(ROOT / "models/qpadm_model_specifications.tsv", "\t")
qpadm_table = read_dicts(ROOT / "tables/table9_qpadm_results.csv")
if len(qpadm_specs) != 3 or len(qpadm_table) != 3:
    errors.append("Expected three qpAdm model rows")

for spec, table in zip(qpadm_specs, qpadm_table):
    source_values = {}
    for item in spec["coefficients_percent"].split(";"):
        label, value = item.split("=", 1)
        source_values[label] = float(value)
    if abs(sum(source_values.values()) - 100.0) > 0.01:
        errors.append(f"{spec['model_id']}: coefficients do not sum to 100")
    if abs(float(spec["p_value"]) - float(table["p_value"])) > 1e-8:
        errors.append(f"{spec['model_id']}: p-value mismatch")
    expected_feasible = "Yes" if spec["feasible"] == "TRUE" else "No"
    if table["feasible"] != expected_feasible:
        errors.append(f"{spec['model_id']}: feasibility mismatch")
    raw_path = ROOT / spec["raw_output_file"].replace("outputs/raw", "raw_outputs")
    if not raw_path.is_file():
        errors.append(f"{spec['model_id']}: raw output missing")


fst_specs = read_dicts(ROOT / "models/fst_comparisons.tsv", "\t")
fst_table = read_dicts(ROOT / "tables/table10_fst_results.csv")
table_by_population = {row["population"]: row for row in fst_table}
for spec in fst_specs:
    table = table_by_population.get(spec["population_2"])
    if table is None:
        errors.append(f"FST table missing {spec['population_2']}")
        continue
    if abs(float(spec["fst_distance"]) - float(table["fst_distance"])) > 1e-10:
        errors.append(f"FST distance mismatch for {spec['population_2']}")
    if abs(float(spec["standard_error"]) - float(table["standard_error"])) > 1e-10:
        errors.append(f"FST standard-error mismatch for {spec['population_2']}")


cal_specs = read_dicts(ROOT / "models/fst_calibration_comparisons.tsv", "\t")
cal_table = read_dicts(ROOT / "tables/table11_fst_calibration.csv")
cal_keys = {
    (row["population_1"], row["population_2"], row["fst_distance"])
    for row in cal_table
}
for spec in cal_specs:
    key = (spec["population_1"], spec["population_2"], spec["fst_distance"])
    if key not in cal_keys:
        errors.append(f"Calibration table mismatch for {spec['population_1']} vs {spec['population_2']}")


if errors:
    print("qpAdm/FST validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("qpAdm/FST validation passed.")
