# Project Scope

## Problem

Road users in Can Tho encounter visible road-surface defects such as cracks, potholes, surface deterioration, and deformation. PaveSense is a course-project prototype for analyzing road imagery and presenting evidence that can support inspection and reporting.

It is not an official road-condition certification system and does not determine legal responsibility, repair quality, or government response.

## Intended workflow

1. User uploads a road image or video.
2. The application extracts representative frames from video.
3. Each frame is normalized for model input.
4. Two complementary model branches run on the same frame: multi-label classification (C01–C07) and object detection (C02–C07).
5. Predictions are associated with timestamps and GPS metadata only when valid metadata is available.
6. The application aggregates frame-level evidence into a reviewable route/segment report.

The two image models are parallel branches, not a serial model chain. Video decoding and frame sampling happen before inference.

## Initial MVP boundary

- Localhost application first.
- Image and short-video upload.
- Configurable frame sampling.
- Classification and detection inference.
- Basic result visualization and export.
- GPS is optional; never infer missing coordinates.
- No public user platform, automated authority submission, live traffic integration, or repair-status tracking in the initial MVP.

## Evaluation

Evaluate both models on held-out data. Keep Can Tho field images separate as a local-domain evaluation set where practical. Split by source, location group, or video/session to reduce leakage.
