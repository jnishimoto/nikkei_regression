# © 2025 Jun Nishimoto
# This software is released under the MIT License.
# See LICENSE file for details.

import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def save_plot(name):
    """Save the plot as a PNG file in the 'plots' directory with a timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    folder_path = f"plots/{timestamp}"
    os.makedirs(folder_path, exist_ok=True)  # Ensure subfolder exists
    filepath = f"{folder_path}/{name}.png"
    plt.savefig(filepath, dpi=300, bbox_inches="tight")  # Save as high-resolution PNG
    print(f"Graph saved: {filepath}")

def plot_results(result, freq, save=False):
    """Plot actual Nikkei, predicted Nikkei, Dow, and USDJPY on the same graph."""
    model = result["model"]
    y_pred = result["y_pred"]  # Predicted values from regression
    y_actual = model.model.endog  # Actual Nikkei values
    X_original = result["X_original"]  # Original scale of X
    coefficients = result["coefficients"]

    # Extract the original dataset from the regression model
    exog_names = model.model.exog_names  # Get variable names
    df = pd.DataFrame(model.model.exog, columns=exog_names, index=model.model.data.row_labels)  # Create DataFrame from exog
    df["Nikkei"] = y_actual
    df["Predicted_Nikkei"] = y_pred
    df[["USDJPY", "Dow"]] = X_original # Inverse scale of X

    # Equation of regression
    r2 = result["r2"]
    intercept = coefficients["const"]
    coef_usdjpy = coefficients["USDJPY"]
    coef_dow = coefficients["Dow"]

    equation = f"Nikkei = {intercept:.2f} + {coef_usdjpy:.2f} * USDJPY + {coef_dow:.2f} * Dow\nR² = {r2:.3f}"

    # Restore the correct index from the actual dataset (correlation_matrix index is incorrect)
    df.index = model.model.data.row_labels  # Correctly restores the date index

    # Plot all data
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Primary Y-axis (for Nikkei & Dow)
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Stock Index", color="tab:blue")
    ax1.plot(df.index, df["Nikkei"], label="Actual Nikkei 225", color="tab:blue", linewidth=2)
    ax1.plot(df.index, df["Predicted_Nikkei"], label="Predicted Nikkei", linestyle="dashed", color="tab:cyan")
    ax1.plot(df.index, df["Dow"], label="Dow Jones", color="tab:purple", linewidth=2, alpha=0.6)
    ax1.tick_params(axis="y", labelcolor="tab:blue")

    # Secondary Y-axis (for USDJPY)
    ax2 = ax1.twinx()
    ax2.set_ylabel("USD/JPY", color="tab:red")
    ax2.plot(df.index, df["USDJPY"], label="USDJPY", color="tab:red", linewidth=2, alpha=0.7)
    ax2.tick_params(axis="y", labelcolor="tab:red")

    # Equation
    ax1.text(0.98, 0.05, equation, transform=ax1.transAxes, fontsize=10,
         verticalalignment="bottom", horizontalalignment="right",
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="none", facecolor="white"))

    # Titles and legend
    plt.title(f"{freq} Data: Nikkei, Predicted Model, Dow, and USDJPY")
    fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
    fig.tight_layout()

    # Save the plot if required
    if save:
        save_plot(f"{freq}_chart")

    plt.show()
