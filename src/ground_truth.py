"""Load ground-truth defect class names from YOLO-format label files."""

import os
import yaml


def load_class_names(data_yaml_path: str) -> list:
    """Loads the ordered list of class names from a YOLO dataset's data.yaml.

    Args:
        data_yaml_path: Path to the dataset's data.yaml file.

    Returns:
        List of class names, indexed to match YOLO label file class indices.
    """
    with open(data_yaml_path, "r") as f:
        config = yaml.safe_load(f)
    return config["names"]


def load_ground_truth_for_image(label_path: str, class_names: list) -> list:
    """Reads a single YOLO-format label file and returns its defect class names.

    Args:
        label_path: Path to a .txt label file (one line per bounding box:
            "class_index x_center y_center width height").
        class_names: Ordered list of class names (index -> name).

    Returns:
        List of class name strings present in this image. Empty list if the
        label file doesn't exist or has no annotations (i.e. no defects).
    """
    if not os.path.exists(label_path):
        return []

    classes = []
    with open(label_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            class_index = int(line.split()[0])
            classes.append(class_names[class_index])
    return classes


def load_all_ground_truths(images_dir: str, labels_dir: str, class_names: list) -> dict:
    """Loads ground-truth class names for every image in a directory.

    Args:
        images_dir: Directory containing image files (e.g. .jpg).
        labels_dir: Directory containing corresponding YOLO .txt label files.
        class_names: Ordered list of class names.

    Returns:
        Dict mapping image filename -> list of ground-truth class names.
    """
    ground_truths = {}
    for image_filename in os.listdir(images_dir):
        stem = os.path.splitext(image_filename)[0]
        label_path = os.path.join(labels_dir, f"{stem}.txt")
        ground_truths[image_filename] = load_ground_truth_for_image(label_path, class_names)
    return ground_truths
