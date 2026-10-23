# AI Use Log

## Planning and setup
Used Claude and Gemini to plan project scope, structure the GitHub repository, and reason through Roboflow preprocessing decisions (resize mode) and model architecture selection (YOLOv11 Nano vs RF-DETR, YOLO26, Roboflow 3.0). Checked the resize reasoning against the real source image dimensions and the Roboflow screens before applying it.

## Code and tests
Used Claude and Gemini (inside Google Colab) to draft the evaluation pipeline (src/), the pytest tests, the plotting module, and the GitHub/Colab workflow. All code was run and tested by me rather than trusted. Pytest results were checked directly (16 tests passing).

## Errors found and corrected
- A class-name mismatch (underscores in the labelling rule vs hyphens in the real dataset) made the first threshold sweep return all zeros. I found it by comparing the dataset's class list with the labelling module, and fixed labelling.py and its tests.
- AI-suggested shell output exposed a GitHub access token. I revoked it, generated a new one, and masked credentials in commands.
- AI-generated Colab code pushed to master although the default branch was main, so pushes failed silently. I found this with a fresh clone and fixed it.
- Stray files (a nested clone, an unrelated documentation file) were removed from the repository, and the docs were regenerated.

## Report
Used Claude to restructure and reword my draft report bullets into paragraphs, to check numbers against the threshold-sweep CSV, and to fix typos. The numbers, conclusions, threshold choice (5) and failure-mode interpretation are my own decisions, checked against my Colab outputs.
