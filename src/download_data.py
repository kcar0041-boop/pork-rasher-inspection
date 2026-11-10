"""Download the pork rasher dataset from Roboflow."""
import os
from roboflow import Roboflow


def download_dataset(api_key: str, workspace: str, project_name: str, version: int, format: str = "yolov11"):
    """Downloads the project dataset from Roboflow into the local data/ folder.

    Args:
        api_key: Roboflow private API key.
        workspace: Roboflow workspace ID.
        project_name: Roboflow project ID.
        version: Dataset version number.
        format: Export format for the dataset.

    Returns:
        Path to the downloaded dataset directory.
    """
    rf = Roboflow(api_key=api_key)
    project = rf.workspace(workspace).project(project_name)
    dataset = project.version(version).download(format, location="data/")
    return dataset.location
