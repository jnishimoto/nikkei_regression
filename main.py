import pandas as pd
from data_fetch import fetch_data
from regression import run_regression
from visualization import plot_results

def main():
    # データ取得
    df_daily, df_monthly, df_yearly = fetch_data()

    # 各データで回帰分析
    results = {}
    for freq, df in zip(["Daily", "Monthly", "Yearly"], [df_daily, df_monthly, df_yearly]):
        print(f"\n==== {freq} Data Regression ====")
        results[freq] = run_regression(df)

    # 可視化
    for freq, result in results.items():
        plot_results(result, freq)

if __name__ == "__main__":
    main()
