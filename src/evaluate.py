"""Evaluation utilities: aggregating detections, deriving pass/fail decisions,
computing confusion counts, and running a confidence-threshold sweep."""

from typing import Iterable


def aggregate_detections_to_classes(predictions: list, confidence_threshold: float) -> list:
    """Filters a list of raw detections down to class names meeting a confidence threshold."""
    return [
        det["class"] for det in predictions
        if det.get("confidence", 0) * 100 >= confidence_threshold
    ]


def pass_fail_decision(predictions: list, confidence_threshold: float, labelling_fn) -> str:
    """Derives a tray-level pass/fail decision from raw detections at a given threshold."""
    classes = aggregate_detections_to_classes(predictions, confidence_threshold)
    return labelling_fn(classes)


def compute_confusion_counts(y_true, y_pred) -> dict:
    """Computes confusion matrix counts and derived rates for pass/fail decisions."""
    tp = fp = fn = tn = 0
    for true_label, pred_label in zip(y_true, y_pred):
        if true_label == "fail" and pred_label == "fail":
            tp += 1
        elif true_label == "pass" and pred_label == "fail":
            fp += 1
        elif true_label == "fail" and pred_label == "pass":
            fn += 1
        elif true_label == "pass" and pred_label == "pass":
            tn += 1

    false_pass_rate = fn / (fn + tp) if (fn + tp) > 0 else 0.0
    false_reject_rate = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    return {
        "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "false_pass_rate": false_pass_rate,
        "false_reject_rate": false_reject_rate,
    }


def threshold_sweep(all_predictions, all_ground_truths, labelling_fn, thresholds):
    """Runs a confidence-threshold sweep, computing confusion counts at each threshold."""
    y_true = [labelling_fn(gt) for gt in all_ground_truths]

    results = []
    for threshold in thresholds:
        y_pred = [
            pass_fail_decision(preds, threshold, labelling_fn)
            for preds in all_predictions
        ]
        counts = compute_confusion_counts(y_true, y_pred)
        results.append({"threshold": threshold, **counts})

    return results
