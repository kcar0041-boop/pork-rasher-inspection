import pandas as pd
from src.plotting import plot_threshold_sweep


def test_plot_threshold_sweep_returns_figure():
    df = pd.DataFrame({
        "threshold": [10, 50, 90],
        "false_pass_rate": [0.0, 0.5, 1.0],
        "false_reject_rate": [1.0, 0.0, 0.0],
    })
    fig = plot_threshold_sweep(df)
    assert fig is not None


def test_plot_threshold_sweep_saves_file(tmp_path):
    df = pd.DataFrame({
        "threshold": [10, 50],
        "false_pass_rate": [0.0, 0.5],
        "false_reject_rate": [1.0, 0.0],
    })
    save_path = str(tmp_path / "test_plot.png")
    plot_threshold_sweep(df, save_path=save_path)
    import os
    assert os.path.exists(save_path)
