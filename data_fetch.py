import yfinance as yf
import pandas as pd

def fetch_data(start_date="1973-01-01", end_date="2025-03-07"):
    """Yahoo Finance から日経平均・ドル円・ダウのデータを取得し、日次・月次・年次データを生成"""
    
    # データ取得
    nikkei = yf.download("^N225", start=start_date, end=end_date, interval="1d", progress=False)["Adj Close"].rename("Nikkei")
    dow = yf.download("^DJI", start=start_date, end=end_date, interval="1d", progress=False)["Adj Close"].rename("Dow")
    usdjpy = yf.download("USDJPY=X", start=start_date, end=end_date, interval="1d", progress=False)["Adj Close"].rename("USDJPY")

    # データ結合
    df_daily = pd.concat([nikkei, usdjpy, dow], axis=1, join="inner").dropna()

    # 月次・年次データ作成
    df_monthly = df_daily.resample('M').last()
    df_yearly = df_daily.resample('Y').last()

    return df_daily, df_monthly, df_yearly
