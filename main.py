#%%
from data_fetch import fetch_data, fetch_stock_data
from regression import run_regression, display_regression_results, save_regression_results
from visualization import plot_results
from correlation import compute_correlation_matrix, plot_correlation_matrix, plot_cluster_map

def main():
    # Fetch data
    df_daily, df_monthly, df_yearly = fetch_data(start_date="1973-01-01", end_date="2025-03-07")
    stock_data = fetch_stock_data(start_date="2020-01-01", end_date="2024-01-01", freq="yearly")

    # Compute correlation matrix
    correlation_matrix = compute_correlation_matrix(stock_data)

    # Perform regression analysis for each dataset
    results = {}
    for freq, df in zip(["Daily", "Monthly", "Yearly"], [df_daily, df_monthly, df_yearly]):
        results[freq] = run_regression(df)
        display_regression_results(results[freq], freq, save=True)  # Display results

    # Plot and save correlation heatmap
    plot_correlation_matrix(correlation_matrix, title="Correlation Matrix: Nikkei 225 vs Dow 30 Stocks", save=True)

    # Plot and save cluster map
    plot_cluster_map(correlation_matrix, title="Clustered Correlation Matrix: Nikkei 225 and Dow 30 Stocks", save=True)

    # Generate visualizations
    for freq, result in results.items():
        plot_results(result, freq, save=True)

if __name__ == "__main__":
    main()
#%%