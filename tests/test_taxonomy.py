"""Contract tests for the shared road-condition taxonomy."""

from pathlib import Path

import yaml


def load_taxonomy() -> dict:
    taxonomy_path = Path(__file__).parents[1] / "configs" / "taxonomy.yaml"
    return yaml.safe_load(taxonomy_path.read_text(encoding="utf-8"))


def test_classification_taxonomy_contains_seven_ordered_classes() -> None:
    taxonomy = load_taxonomy()
    classes = taxonomy["classification"]["classes"]

    assert [item["id"] for item in classes] == [f"C{i:02d}" for i in range(1, 8)]
    assert [item["index"] for item in classes] == list(range(7))
    assert len({item["name"] for item in classes}) == 7


def test_normal_class_is_exclusive_with_damage_classes() -> None:
    classes = load_taxonomy()["classification"]["classes"]
    normal = classes[0]
    damage_ids = [item["id"] for item in classes[1:]]

    assert normal["id"] == "C01"
    assert set(normal["mutually_exclusive_with"]) == set(damage_ids)


def test_detection_taxonomy_maps_only_the_six_damage_classes() -> None:
    taxonomy = load_taxonomy()
    detection_classes = taxonomy["detection"]["classes"]

    assert [item["taxonomy_id"] for item in detection_classes] == [
        f"C{i:02d}" for i in range(2, 8)
    ]
    assert [item["detection_id"] for item in detection_classes] == list(range(6))
    assert taxonomy["detection"]["background_only_classification_label"] == "C01"
