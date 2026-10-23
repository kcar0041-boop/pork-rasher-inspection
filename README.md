# Pork Rasher Inspection

Automated pass/fail inspection and failure-mode analysis for pork rasher packaging, built for the MMA3001 (Numerical Methods and Machine Learning) individual project at Monash University.

## Project Description

This project trains an object-detection model (YOLOv11 Nano, via Roboflow) to identify packaging and meat-quality defects on pork rasher trays from RGB images, then derives a tray-level pass/fail decision from the detected defect classes using a tuned confidence threshold. A custom Python evaluation pipeline computes the false-pass and false-reject rates across a range of thresholds, and a failure-mode analysis characterises why the model misses genuine defects.

**Key finding:** the model scores most real defects too low rather than failing to see them. At a threshold of 25, 32 of the 33 false negatives had a fail-worthy detection scored below the cutoff (highest 0.24), so the operating threshold was lowered to 5. At threshold 5 the false pass rate is about 5.3% (4 of 75 defective test trays), at the cost of flagging almost every tray (the one good test tray is also rejected).

A YOLO26 (Nano) model was also trained on the identical dataset split as a baseline comparison; YOLOv11 outperformed it on mAP@50 and precision with comparable recall.

## Repository Structure

    src/         Evaluation pipeline (labelling rule, inference aggregation, threshold sweep, plotting)
    tests/       pytest test suite (16 tests)
    results/     Threshold-sweep CSV/plot, pytest HTML test report
    docs/        Generated HTML documentation (pdoc) for src/
    ai_use_log.md   Running log of AI tool use during development
    requirements.txt

## Setup

    pip install -r requirements.txt

A Roboflow API key is required to pull the trained model and dataset (set as an environment variable / Colab secret, never committed to this repo).

## Running Tests

    pytest --html=results/test_report.html --self-contained-html

## Documentation

Generated API documentation for src/ is in docs/. Open docs/src.html (or docs/index.html) in a browser.

## AI Acknowledgement

This project used AI assistance (Claude and Gemini) throughout development, in line with the unit's AI-use policy. AI was used for planning project scope and the report structure; drafting and debugging the evaluation pipeline and pytest tests; reasoning through Roboflow configuration decisions; and assisting with GitHub/Colab workflow debugging.

All AI-generated code and content was reviewed, tested, and verified before being incorporated. A detailed log of AI use is kept in ai_use_log.md.

Final project framing, architecture selection, the pass/fail labelling rule, threshold selection, and interpretation of results remained the author's own decisions throughout.
