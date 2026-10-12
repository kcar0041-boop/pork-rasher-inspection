import os
from roboflow import Roboflow

def download_dataset(workspace: str = "your-workspace", project: str = "your-project", version: int = 1) -> str:
    """Downloads a dataset from Roboflow using the Roboflow Python SDK.

    Args:
        workspace (str): The Roboflow workspace ID.
        project (str): The Roboflow project ID.
        version (int): The dataset version number.

    Returns:
        str: The path to the downloaded dataset directory.

    Raises:
        ValueError: If the ROBOCFLOW_API_KEY environment variable is not set.
    """
    api_key = os.environ.get("ROBOFLOW_API_KEY")
    if not api_key:
        raise ValueError("ROBOFLOW_API_KEY environment variable not set. Please add your Roboflow API key to Colab Secrets or environment.")

    rf = Roboflow(api_key=api_key)
    proj = rf.workspace(workspace).project(project)
    dataset = proj.version(version).download("yolov8") # Example format, adjust as needed
    return dataset.location

if __name__ == '__main__':
    print("This script provides a function to download data from Roboflow.")
    print("Run `download_dataset()` with your specific workspace, project, and version.")
