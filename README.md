# Pork Rasher Inspection

Automated pass/fail inspection and failure-mode analysis for pork rasher packaging, built for the MMA3001 (Numerical Methods and Machine Learning) individual project at Monash University.

## Project Description

This project trains an object-detection model (YOLOv11 Nano, via Roboflow) to identify packaging and meat-quality defects on pork rasher trays from RGB images, then derives a tray-level pass/fail decision from the detected defect classes using a tuned confidence threshold. A custom Python evaluation pipeline computes the false-pass and false-reject rates across a range of thresholds, and a failure-mode analysis characterises why the model misses genuine defects.

**Key finding:** at the chosen operating threshold, the model's false negatives are driven by a confidence-calibration issue, not a detection-capability issue — in all observed false-negative cases, the model did detect the correct defect class, just below the confidence cutoff.

A YOLO26 (Nano) model was also trained on the identical dataset split as a baseline comparison; YOLOv11 outperformed it on mAP@50 and precision with comparable recall.

## Repository Structure

```
pork-rasher-inspection/
├── src/              # Evaluation pipeline (labelling rule, inference aggregation, threshold sweep, plotting)
├── tests/            # pytest test suite (16 tests)
├── results/          # Threshold-sweep CSV/plot, pytest HTML test report
├── docs/             # Generated HTML documentation (pdoc) for src/
├── notebooks/        # Development notebooks
├── ai_use_log.md     # Running log of AI tool use during development
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
```

A Roboflow API key is required to pull the trained model and dataset (set as an environment variable / Colab secret, never committed to this repo).

## Running Tests

```bash
pytest --html=results/test_report.html --self-contained-html
```

## Documentation

Generated API documentation for `src/` is in `docs/` — open `docs/src.html` (or `docs/index.html`) in a browser.

## AI Acknowledgement

This project used AI assistance (Claude and Gemini) throughout development, in line with the unit's AI-use policy. AI was used for: planning project scope and the report structure; drafting and debugging the evaluation pipeline and pytest tests; reasoning through Roboflow configuration decisions (resize mode, architecture selection); and assisting with GitHub/Colab workflow debugging.

All AI-generated code and content was reviewed, tested, and verified before being incorporated including cross-checking training metrics directly against Roboflow's own reporting, and independently diagnosing bugs (e.g. a class name mismatch between the labelling rule and the real dataset classes) that AI-generated code did not itself catch. A detailed, dated log of AI use is kept in `ai_use_log.md`.

Final project framing, architecture selection, the pass/fail labelling rule, threshold selection, and interpretation of results remained the author's own decisions throughout.
