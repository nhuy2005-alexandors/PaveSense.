# Team Workflow

| Member | Role | Class ownership |
|---|---|---|
| Huy | Leader | C01 Normal Road; C02 Longitudinal Crack |
| Khánh | Secretary | C03 Transverse Crack; C04 Alligator Cracking |
| Phúc | Member | C05 Pothole; C06 Surface Deterioration; C07 Surface Deformation |

Class ownership means responsibility for collecting, auditing, mapping, and reporting those classes. It does not imply exclusive ownership of a dataset source.

## Weekly workflow

- Work is planned and tracked by week in the shared Google Sheets workbook.
- Each member updates their own worklog and the shared progress sheet.
- Khánh consolidates weekly status and blockers.
- Huy reviews taxonomy mapping, dataset quality, and integration decisions.
- Changes to shared taxonomy or data contracts must be discussed before merging.

## Git workflow

- `main` is the stable integration branch.
- Use short feature branches, e.g. `feat/frame-sampling`, `data/manifest-validator`, or `docs/taxonomy`.
- Open a Pull Request for non-trivial changes; Huy coordinates review and merge.
- Keep commits focused and descriptive.
- Do not commit data, credentials, local environments, or large model files.
- Add Khánh and Phúc as GitHub collaborators after their GitHub usernames are confirmed.
