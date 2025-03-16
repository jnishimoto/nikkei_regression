# © 2025 Jun Nishimoto
# This software is released under the MIT License.
# See LICENSE file for details.

#%%
from data_fetch import fetch_data, fetch_stock_data
from regression import run_regression, display_regression_results, save_regression_results
from visualization import plot_results
from correlation import compute_correlation_matrix, plot_correlation_matrix, plot_cluster_map

def main():
    # Fetch data (original price-based data)
    df_daily, df_monthly, df_yearly = fetch_data(start_date="1973-01-01", end_date="2025-03-07")

    # Fetch stock data for correlation analysis
    stock_data = fetch_stock_data(start_date="2020-01-01", end_date="2024-01-01", freq="yearly")

    # Compute correlation matrix
    correlation_matrix = compute_correlation_matrix(stock_data)

    # Compute returns for additional regression analysis
    returns_daily = df_daily.pct_change().dropna()
    returns_monthly = df_monthly.pct_change().dropna()
    returns_yearly = df_yearly.pct_change().dropna()

    # Perform regression analysis for prices
    results_prices = {}
    for freq, df in zip(["Daily", "Monthly", "Yearly"], [df_daily, df_monthly, df_yearly]):
        results_prices[freq] = run_regression(df)
        display_regression_results(results_prices[freq], f"{freq} Prices", save=True)  # Save results

    # Perform regression analysis for returns
    results_returns = {}
    for freq, df in zip(["Daily", "Monthly", "Yearly"], [returns_daily, returns_monthly, returns_yearly]):
        results_returns[freq] = run_regression(df)
        display_regression_results(results_returns[freq], f"{freq} Returns", save=True)  # Save results

    # Plot and save correlation heatmap
    plot_correlation_matrix(correlation_matrix, title="Correlation Matrix: Nikkei 225 vs Dow 30 Stocks", save=True)

    # Plot and save cluster map
    plot_cluster_map(correlation_matrix, title="Clustered Correlation Matrix: Nikkei 225 and Dow 30 Stocks", save=True)

    # Generate visualizations for prices
    for freq, result in results_prices.items():
        plot_results(result, f"{freq} Prices", save=True)

    # Generate visualizations for returns
    for freq, result in results_returns.items():
        plot_results(result, f"{freq} Returns", save=True)

if __name__ == "__main__":
    main()
#%%