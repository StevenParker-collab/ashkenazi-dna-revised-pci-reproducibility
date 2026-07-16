# Ashkenazi DNA revised PCI reproducibility repository

This repository accompanies the revised manuscript:

> Steven Parker. Ashkenazi Population Structure Reassessed: Reference-Panel Sensitivity and the Europe-Levant Cline.

The submitted manuscript is preserved as a PDF in `manuscript/`. The repository contains the author-generated qpAdm and FST audit trail retained from the earlier repository and the linked Global25 Experiments 1-15 used in the revised manuscript, including the Experiment 14 full-dimensional vector diagnostic.

## Repository contents

- `manuscript/`: the current revised manuscript PDF.
- `qpadm_fst/`: exact web-platform labels, model specifications, copied raw outputs, screenshots, and manuscript tables for the qpAdm and FST analyses.
- `global25_experiments/`: source panels, target coordinates where retained, raw results, grouped summaries, figures, methods, provenance notes, and validation scripts for Experiments 1-15.
- `DATA_AVAILABILITY.md`: data access, provenance, and reproducibility scope.
- `REPOSITORY_MAP.md`: reviewer-oriented file map.
- `SHA256SUMS.txt`: integrity hashes for every distributed file other than the checksum list itself.

## Start here

1. Read the manuscript PDF in `manuscript/`.
2. For the independent qpAdm and FST analyses, open `qpadm_fst/README.md`.
3. For the Global25 sensitivity suite, open `global25_experiments/README.md` and `global25_experiments/REPRODUCIBILITY_STATUS.md`.
4. Run `python3 verify_repository.py` from the repository root to verify file integrity and structural checks.

## Analysis scope

The qpAdm and FST results were generated in the IllustrativeDNA Admix Lab web interface with the Human Origins v62.0 dataset. This repository preserves the inputs, copied outputs, screenshots, and derived tables; it does not recast those web runs as local ADMIXTOOLS analyses.

The Global25 material is a linked sensitivity and validation suite rather than fifteen independent ancestry estimates. It includes fixed prehistoric panels, broad modern competitions, matched omissions, reciprocal Italki models, regional Ashkenazi replication, and ancient Levant positive controls.

The Experiment 14 Ashkenazi Germany diagnostic calculates the opposing Levantine-continuity and Northern/Eastern European displacement vectors in all twenty-five Global25 dimensions. The supplied PCA figure is illustrative and is not used to infer ancestry proportions.

Displayed Global25 coefficients are constrained, source-panel-dependent similarity weights. They are not literal historical ancestry percentages. Correlated sources can substitute for one another, and a displayed zero does not prove historical absence.

## Main experiment groups

| Experiments | Role |
|---|---|
| 1 and 8 | Fixed prehistoric component controls |
| 2 and 10 | Full modern competition panels |
| 3, 5, 11, and 12 | Matched omission and proxy-inflation tests |
| 4, 6, and 13 | Direct-distance and reciprocal Italki controls |
| 7 and 14 | Ten-region Ashkenazi stability tests |
| 9 and 15 | Ancient Levant positive controls |

## Reproducibility note

The source handoff did not contain separate target-coordinate files for every ancient target in Experiments 8 and 9. Their raw output tables, findings, and original screenshots are preserved without alteration, and their source coordinates are recoverable from the linked panels. This limitation is stated explicitly in `global25_experiments/REPRODUCIBILITY_STATUS.md`; no missing coordinates were inferred or fabricated.

## Suggested citation

Citation metadata are provided in `CITATION.cff`. After publishing the repository on GitHub, archive a versioned release in a DOI-granting repository and update the citation metadata with the permanent identifier.
