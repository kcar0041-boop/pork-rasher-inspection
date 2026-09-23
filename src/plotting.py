"""Plotting utilities for threshold-sweep results."""

import matplotlib.pyplot as plt


def plot_threshold_sweep(df, save_path: str = None):
    """Plots false-pass rate and false-reject rate against confidence threshold.

    Args:
        df: DataFrame with columns 'threshold', 'false_pass_rate', 'false_reject_rate'.
        save_path: If provided, saves the figure to this path.

    Returns:
        The matplotlib Figure object.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df["threshold"], df["false_pass_rate"], marker="o", label="False Pass Rate (missed defects)", color="crimson")
    ax.plot(df["threshold"], df["false_reject_rate"], marker="s", label="False Reject Rate (false alarms)", color="steelblue")
    ax.set_xlabel("Confidence Threshold (%)")
    ax.set_ylabel("Rate")
    ax.set_title("Threshold Sweep: False Pass Rate vs False Reject Rate")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150)
        print(f"Saved plot to {save_path}")

    return fig
