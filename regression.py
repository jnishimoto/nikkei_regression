# © 2025 Jun Nishimoto
# This software is released under the MIT License.
# See LICENSE file for details.

import os
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
from sklearn.preprocessing import StandardScaler
from datetime import datetime

def run_regression(df):
    """Perform multiple regression analysis and return the results as a dictionary."""
    
    #print("\n==== Debug: Missing value ====")
    #print(df.isna().sum())  # 各列の NaN の数を表示
    
    X = df[["USDJPY", "Dow"]]
    y = df["Nikkei"]

    """
    # StandardScaler を適用
    scaler_X = StandardScaler()
    X_scaled = scaler_X.fit_transform(X)
    
    # スケール変換後のデータフレームを作成
    X_scaled_df = pd.DataFrame(X_scaled, columns=["USDJPY", "Dow"], index=X.index)

    X_const = sm.add_constant(X_scaled_df)  # Add constant for intercept
    """
    
    X_const = sm.add_constant(X)  # Add constant for intercept

    # Fit the regression model
    model = sm.OLS(y, X_const).fit()

    # Predict
    y_pred = model.fittedvalues
    #print(f"\n==== 予測値のチェック ====")
    #print(y_pred.head())
    #print(f"予測値の NaN 数: {y_pred.isna().sum()}")

    # Compute Variance Inflation Factor (VIF)
    vif = pd.Series(
    [variance_inflation_factor(X_const.values, i) for i in range(X_const.shape[1])],
    index=X_const.columns  # Use column names as index
    )

    # Compute Correlation Matrix
    correlation_matrix = df.corr()

    # Return results as a dictionary
    return {
        "model": model,
        "r2": model.rsquared,
        "coefficients": model.params,
        "p_values": model.pvalues,
        "vif": vif,
        "correlation_matrix": correlation_matrix,
        "y_pred": y_pred,
        "X_original": X
    }

def display_regression_results(results, freq, save=False):
    """Display regression analysis results in a readable format."""
    
    # Extract results
    r2 = results["r2"]
    coefficients = results["coefficients"]
    p_values = results["p_values"]
    vif = results["vif"]
    correlation_matrix = results["correlation_matrix"]
    # Print results
    print(f"\n==== Regression Results for {freq} Data ====")
    print(f"R² (Coefficient of Determination): {r2:.3f}\n")

    # Display regression coefficients, p-values and Variance Inflation Factor (VIF)
    coef_df = pd.DataFrame({
        "Coefficient": coefficients.round(3),
        "p-value": p_values.round(3),
        "VIF": vif.round(3)
    })
    print("Regression Coefficients, p-values, and VIF:")
    print(coef_df, "\n")

    # Display Correlation Matrix
    print("Correlation Matrix:")
    print(results["correlation_matrix"].round(3), "\n")

    # Save results if requested
    if save:
        save_regression_results(freq, r2, coef_df, correlation_matrix)

def save_regression_results(freq, r2, coef_table, correlation_matrix):
    """Save regression results to a text and CSV file in the 'results/' directory."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    folder_path = f"results/{timestamp}"
    os.makedirs(folder_path, exist_ok=True)  # Ensure subfolder exists

    # Save as a structured text file
    txt_filepath = f"{folder_path}/regression_results_{freq}_{timestamp}.txt"
    with open(txt_filepath, "w") as f:
        f.write(f"Regression Results for {freq} Data\n")
        f.write(f"R² (Coefficient of Determination): {r2:.3f}\n\n")

        f.write("Regression Coefficients, p-values, and VIF:\n")
        f.write(coef_table.to_string() + "\n\n")

        f.write("Correlation Matrix:\n")
        f.write(correlation_matrix.to_string() + "\n")

    print(f"Regression results saved: {txt_filepath}")

    # Save coefficients, p-values, and VIF as CSV
    coef_csv_filepath = f"{folder_path}/regression_coefficients_{freq}_{timestamp}.csv"
    coef_table.to_csv(coef_csv_filepath)
    print(f"Coefficients, p-values, and VIF saved: {coef_csv_filepath}")

    # Save correlation matrix as CSV
    corr_csv_filepath = f"{folder_path}/regression_correlation_{freq}_{timestamp}.csv"
    correlation_matrix.to_csv(corr_csv_filepath)
    print(f"Correlation matrix saved: {corr_csv_filepath}")
