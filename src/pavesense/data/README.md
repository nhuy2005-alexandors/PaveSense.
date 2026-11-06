# Data Module

Responsibilities: read manifests; validate file existence, image readability, labels, and annotation references; convert source annotations into the canonical schema; detect exact duplicates and flag near-duplicates for review; create group-aware dataset splits.

Keep source-specific adapters separate from canonical schemas. Never overwrite raw source data.
