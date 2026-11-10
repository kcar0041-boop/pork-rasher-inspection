# Pork Rasher Inspection

Automated pass/fail inspection and failure-mode analysis for pork rasher packaging, built for the MMA3001 (Numerical Methods and Machine Learning) individual project at Monash University.

## Project Description

This project trains an object-detection model (YOLOv11 Nano, via Roboflow) to identify packaging and meat-quality defects on pork rasher trays from RGB images, then derives a tray-level pass/fail decision from the detected defect classes using a tuned confidence threshold. A custom Python evaluation pipeline computes the false-pass and false-reject rates across a range of thresholds, and a failure-mode analysis characterises why the model misses genuine defects.

**Key finding:** the model scores most real defects too low rather than failing to see them. At a threshold of 25, 32 of the 33 false negatives had a fail-worthy detection scored below the cutoff (highest 0.24), so the operating threshold was lowered to 5. At threshold 5 the false pass rate is about 5.3% (4 of 75 defective test trays), at the cost of flagging almost every tray (the one good test tray is also rejected).

A YOLO26 (Nano) model was also trained on the identical dataset split as a baseline comparison; YOLOv11 outperformed it on mAP@50 and precision with comparable recall.

## Results

| Model | mAP@50 | Precision | Recall |
| --- | --- | --- | --- |
| YOLOv11 Nano (final) | 66.2% | 80.0% | 50.7% |
| YOLO26 Nano (baseline) | 50.4% | 66.6% | 51.8% |

| Threshold | False pass rate | Note |
| --- | --- | --- |
| 25 | 44% (33 of 75 defective trays missed) | 32 of 33 had a fail-worthy detection scored below the cutoff |
| 5 (chosen) | 5.3% (4 of 75) | flags 72 of 76 trays and rejects the one good tray |

The threshold sweep over the 76 test images takes about 4 ms. Model inference runs on Roboflow's hosted API, so model speed and memory were not profiled.

## Limitations

- The test set has only one true-pass image, so the false reject rate is indicative only.
- The threshold was chosen on the test set, so the rates are optimistic.
- Labels are per image, not per tray.

## Dataset

Fetched via src/download_data.py using the Roboflow API (not committed to this repo, see .gitignore). Requires a ROBOFLOW_API_KEY environment variable or Colab secret; never commit the key. Roboflow version 1: 1,955 images (1,764 train / 115 valid / 76 test); classes loose-meat, packaging-error, twisted-meat, unsealed, wrinkle. The workspace is private, so access is needed.

## Repository Structure

    src/       Evaluation pipeline (labelling rule, inference aggregation, threshold sweep, plotting)
    tests/     pytest test suite (16 tests)
    results/   Threshold-sweep CSV and plot, pytest HTML test report
    docs/      Generated HTML documentation (pdoc) for src/
    ai_use_log.md   Log of AI tool use during development
    requirements.txt

## Setup

    pip install -r requirements.txt

## Running Tests

    pytest --html=results/test_report.html --self-contained-html

## Documentation

Generated API documentation for src/ is in docs/. Open docs/src.html (or docs/index.html) in a browser.

## AI Acknowledgement

This project used AI assistance (Claude and Gemini) throughout development, in line with the unit's AI-use policy. AI was used for planning project scope and the report structure; drafting and debugging the evaluation pipeline and pytest tests; reasoning through Roboflow configuration decisions; and assisting with GitHub/Colab workflow debugging.

All AI-generated code and content was reviewed, tested, and verified before being incorporated. A detailed log of AI use is kept in ai_use_log.md.

Final project framing,
