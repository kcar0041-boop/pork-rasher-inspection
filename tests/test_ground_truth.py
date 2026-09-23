import os
import pytest
from src.ground_truth import load_ground_truth_for_image, load_all_ground_truths


def test_load_ground_truth_missing_file_returns_empty(tmp_path):
    result = load_ground_truth_for_image(str(tmp_path / "nonexistent.txt"), ["wrinkle", "loose_meat"])
    assert result == []


def test_load_ground_truth_parses_class_indices(tmp_path):
    label_file = tmp_path / "sample.txt"
    label_file.write_text("1 0.5 0.5 0.2 0.2\n0 0.3 0.3 0.1 0.1\n")
    class_names = ["wrinkle", "loose_meat"]
    result = load_ground_truth_for_image(str(label_file), class_names)
    assert result == ["loose_meat", "wrinkle"]


def test_load_ground_truth_skips_blank_lines(tmp_path):
    label_file = tmp_path / "sample.txt"
    label_file.write_text("0 0.5 0.5 0.2 0.2\n\n")
    class_names = ["wrinkle"]
    result = load_ground_truth_for_image(str(label_file), class_names)
    assert result == ["wrinkle"]


def test_load_all_ground_truths_maps_every_image(tmp_path):
    images_dir = tmp_path / "images"
    labels_dir = tmp_path / "labels"
    images_dir.mkdir()
    labels_dir.mkdir()

    (images_dir / "img1.jpg").write_text("")
    (images_dir / "img2.jpg").write_text("")
    (labels_dir / "img1.txt").write_text("0 0.5 0.5 0.2 0.2\n")
    # img2 has no label file -> should map to empty list

    class_names = ["wrinkle"]
    result = load_all_ground_truths(str(images_dir), str(labels_dir), class_names)

    assert result["img1.jpg"] == ["wrinkle"]
    assert result["img2.jpg"] == []
