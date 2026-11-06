# Dataset Data Contract

## Storage boundaries

- Google Drive stores raw datasets, normalized images/annotations, field data, and project documents.
- Git stores code, small schemas, taxonomy, configuration, and documentation.
- Do not commit datasets, videos, model checkpoints, API keys, or private location metadata to Git.

## Manifest fields

Each image should have a stable `image_id` and a manifest record containing, where available:

`image_id`, `relative_path`, `source_dataset`, `source_version`, `source_url`, `license`, `original_label`, `normalized_labels`, `annotation_path`, `width`, `height`, `sha256`, `group_id`, `capture_timestamp`, `latitude`, `longitude`, `review_status`.

Unknown values remain empty/null; do not infer provenance or GPS.

## Counting rules

- `unique_images`: unique physical images after exact/near-duplicate review.
- `class_positive_images`: unique images carrying a given class; one image may contribute to multiple classes.
- `object_instances`: individually annotated objects/regions.
- `augmented_images`: derived training samples, counted separately and never included in the original-image quota.

A class quota is not met by counting duplicate frames, augmented copies, or unreviewed/invalid samples.

## Annotation requirements

### Classification

Use multi-label targets for C01-C07. C01 Normal is mutually exclusive with visible damage labels C02-C07. Samples that cannot be assessed reliably should be marked uncertain/unassessable and excluded from ordinary supervised targets until reviewed.

### Detection

Use bounding boxes for visible damage classes C02-C07. C01 Normal images are background/negative images and have no Normal box. Preserve original annotations and conversion provenance.

## Split and leakage prevention

Group related images before splitting: frames from the same video/session must stay in one split; repeated views of the same road location should be grouped where practical; source-dataset derivatives or near-duplicates must not cross train/validation/test. Prefer group-aware splitting over random image-level splitting.
