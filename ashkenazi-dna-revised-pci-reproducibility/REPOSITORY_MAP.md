# Repository map

## Manuscript

`manuscript/Ashkenazi_DNA_Under_the_Microscope_Revised_G25_Experiments_1_to_15.pdf`

Authoritative revised manuscript supplied for this repository package.

## qpAdm and FST

| Path | Contents |
|---|---|
| `qpadm_fst/inputs/` | Target, source, right-set, and comparator labels |
| `qpadm_fst/models/` | qpAdm model specifications and FST comparison records |
| `qpadm_fst/raw_outputs/` | Copied web-platform outputs |
| `qpadm_fst/tables/` | Manuscript Tables 9-11 in CSV form |
| `qpadm_fst/figures/` | Output and table screenshots |
| `qpadm_fst/scripts/` | Structural validation for retained qpAdm/FST materials |

## Global25 Experiments 1-15

| Path | Contents |
|---|---|
| `global25_experiments/experiments_01_07/experiments/` | Paste-ready source and target panels for Experiments 1-7 |
| `global25_experiments/experiments_01_07/results/` | Raw, contextual, and derived results for Experiments 1-7 |
| `global25_experiments/experiments_01_07/figures/` | Experiment and contextual figures supplied with Experiments 1-7 |
| `global25_experiments/experiments_01_07/scripts/` | Derivation and validation scripts supplied with Experiments 1-7 |
| `global25_experiments/experiments_08_15/` | Setups, inputs where retained, raw results, comparisons, screenshots, and findings for Experiments 8-15 |
| `global25_experiments/scripts/` | Linked-input assembly and cross-experiment validation |

## Integrity and citation

- `MANIFEST.csv`: one row per distributed file with size and SHA-256 digest.
- `SHA256SUMS.txt`: checksum list compatible with `sha256sum -c`.
- `verify_repository.py`: repository-level validation.
- `CITATION.cff`: citation metadata for GitHub and archival services.
