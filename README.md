# PaveSense

**AI-powered road-surface condition analysis for Can Tho, Vietnam.**

The prototype accepts road images or videos, extracts representative frames from videos, and analyzes each frame with two complementary image-model branches:

1. **Multi-label image classification** — predicts visible conditions among C01–C07.
2. **Object detection** — localizes visible damage regions from C02–C07 with bounding boxes.

Video decoding and frame sampling happen before inference. The classification and detection models run as parallel branches on each selected image; neither model consumes raw video.

## Scope

- Seven road-condition classes, defined in `configs/taxonomy.yaml`.
- Public road-damage datasets are candidate training sources; audit each source's license, label definitions, annotation format, duplicates, and suitability before use.
- Can Tho field images are kept as a separate local-domain evaluation set where practical.
- Python/PyTorch is the intended stack. Exact model families and preprocessing are selected after dataset audit and baseline experiments.
- Initial application target: localhost demo.

## Repository layout

```text
pavesense/
├── configs/                 # Versioned taxonomy and experiment configuration
├── docs/                    # Scope, data contract, team workflow, decisions
├── notebooks/               # Exploratory analysis
├── scripts/                 # Reproducible data and experiment commands
├── src/pavesense/           # Application and ML implementation
│   ├── data/                # Dataset loading, validation, conversion
│   ├── video/               # Video decoding and frame sampling
│   ├── models/classification/
│   ├── models/detection/
│   └── application/         # Inference orchestration and UI/API adapters
└── tests/                   # Unit and integration tests
```

## Data storage

Google Drive is the source of truth for datasets and project documents:

- `01_DATASET/Raw`
- `01_DATASET/Normalized`
- `01_DATASET/CanTho`

Do **not** commit image datasets, videos, model weights, credentials, or private location metadata to Git. Commit code, configuration, schemas, and documentation only.

## Team

| Member | Role | Class ownership |
|---|---|---|
| Huy | Leader | C01 Normal Road; C02 Longitudinal Crack |
| Khánh | Secretary | C03 Transverse Crack; C04 Alligator Cracking |
| Phúc | Member | C05 Pothole; C06 Surface Deterioration; C07 Surface Deformation |

Class ownership means responsibility for collecting, auditing, mapping, and reporting those classes. It does not imply exclusive ownership of a dataset source.

GitHub usernames for Khánh and Phúc have not yet been confirmed; add them as collaborators after receiving their usernames.

## Project continuity

- [Current session handoff (2026-11-06)](docs/HANDOFF_2026-11-06.md) — taxonomy semantics, dataset acquisition status, Can Tho evidence, storage boundaries, blockers, and resume steps.
- [Dataset data contract](docs/data-contract.md)
- [Project scope](docs/project-scope.md)
- [Team workflow](docs/team-workflow.md)

## Development

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
ruff check .
pytest
```

The scaffold intentionally does not pin a CUDA-specific PyTorch build. Choose the PyTorch wheel matching the team's hardware/runtime after selecting a baseline model.
