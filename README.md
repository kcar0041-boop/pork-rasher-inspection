# Automated Pass/Fail Inspection for Pork Rasher Packaging

Automated defect detection and pass/fail decision-making for pork rasher packaging quality control, using a YOLOv11 object detector trained via Roboflow.

## Setup
```bash
pip install -r requirements.txt
```

## Dataset
Fetched via `src/download_data.py` using the Roboflow API (not committed to this repo — see `.gitignore`). Requires a `ROBOFLOW_API_KEY` environment variable.

## Repository Structure
- `data/` — downloaded dataset (gitignored)
- `notebooks/` — exploration, training, threshold-sweep notebooks
- `src/` — reusable Python modules
- `tests/` — pytest test suite
- `results/` — output plots, metrics, tables

## Running Tests
```bash
pytest
```
