import pytest
from src.evaluate import (
    aggregate_detections_to_classes,
    pass_fail_decision,
    compute_confusion_counts,
    threshold_sweep,
)
from src.labelling import derive_pass_fail


def test_aggregate_detections_filters_by_confidence():
    predictions = [
        {"class": "loose_meat", "confidence": 0.85},
        {"class": "wrinkle", "confidence": 0.30},
    ]
    result = aggregate_detections_to_classes(predictions, confidence_threshold=50)
    assert result == ["loose_meat"]


def test_pass_fail_decision_fail_case():
    predictions = [{"class": "twisted_meat", "confidence": 0.90}]
    assert pass_fail_decision(predictions, 50, derive_pass_fail) == "fail"


def test_pass_fail_decision_pass_case_low_confidence():
    predictions = [{"class": "twisted_meat", "confidence": 0.20}]
    assert pass_fail_decision(predictions, 50, derive_pass_fail) == "pass"


def test_compute_confusion_counts_basic():
    y_true = ["fail", "fail", "pass", "pass"]
    y_pred = ["fail", "pass", "pass", "fail"]
    result = compute_confusion_counts(y_true, y_pred)
    assert result["tp"] == 1
    assert result["false_pass_rate"] == 0.5
    assert result["false_reject_rate"] == 0.5


def test_threshold_sweep_runs_across_thresholds():
    all_predictions = [
        [{"class": "loose_meat", "confidence": 0.90}],
        [{"class": "wrinkle", "confidence": 0.90}],
    ]
    all_ground_truths = [["loose_meat"], ["wrinkle"]]
    results = threshold_sweep(all_predictions, all_ground_truths, derive_pass_fail, thresholds=[10, 50, 95])
    assert len(results) == 3
