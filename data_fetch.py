import yfinance as yf
import pandas as pd

def fetch_data(start_date="1973-01-01", end_date="2025-03-07"):
    """Yahoo Finance から日経平均・ドル円・ダウのデータを取得し、日次・月次・年次データを生成"""
    
    # Yahoo Finance からデータ取得
    nikkei_df = yf.download("^N225", start=start_date, end=end_date, interval="1d", auto_adjust=True, progress=False)
    dow_df = yf.download("^DJI", start=start_date, end=end_date, interval="1d", auto_adjust=True, progress=False)
    usdjpy_df = yf.download("USDJPY=X", start=start_date, end=end_date, interval="1d", auto_adjust=True, progress=False)

    # MultiIndex の "Close" レベルのデータのみ取得
    nikkei = nikkei_df.xs("Close", level=0, axis=1)["^N225"].rename("Nikkei")
    dow = dow_df.xs("Close", level=0, axis=1)["^DJI"].rename("Dow")
    usdjpy = usdjpy_df.xs("Close", level=0, axis=1)["USDJPY=X"].rename("USDJPY")

    # データ結合
    df_daily = pd.concat([nikkei, usdjpy, dow], axis=1, join="inner").dropna()

    # 月次・年次データ作成
    df_monthly = df_daily.resample('M').last()
    df_yearly = df_daily.resample('Y').last()

    return df_daily, df_monthly, df_yearly

# 日経平均225の代表銘柄（20銘柄を抜粋、本来は225）
ticker_to_name_nikkei = {
    "9983.T": "Fast Retailing",  # ファーストリテイリング
    "9984.T": "SoftBank Group",  # ソフトバンクグループ
    "8035.T": "Tokyo Electron",  # 東京エレクトロン
    "6954.T": "Fanuc",  # ファナック
    "2413.T": "M3",  # エムスリー
    "6861.T": "Keyence",  # キーエンス
    "6098.T": "Recruit Holdings",  # リクルートホールディングス
    "4063.T": "Shin-Etsu Chemical",  # 信越化学工業
    "6857.T": "Advantest",  # アドバンテスト
    "2801.T": "Kikkoman",  # キッコーマン
    "2802.T": "Ajinomoto",  # 味の素
    "7751.T": "Canon",  # キヤノン
    "7203.T": "Toyota",  # トヨタ自動車
    "9432.T": "NTT",  # 日本電信電話 (NTT)
    "9433.T": "KDDI",  # KDDI
    "4502.T": "Takeda Pharmaceutical",  # 武田薬品工業
    "8001.T": "Itochu",  # 伊藤忠商事
    "8031.T": "Mitsui & Co.",  # 三井物産
    "8316.T": "Sumitomo Mitsui Financial Group",  # 三井住友フィナンシャルグループ
    "8411.T": "Mizuho Financial Group"  # みずほフィナンシャルグループ
}

# ダウ30の代表銘柄（20銘柄を抜粋、本来は30）
ticker_to_name_dow = {
    "AAPL": "Apple",  # アップル
    "MSFT": "Microsoft",  # マイクロソフト
    "V": "Visa",  # ビザ
    "JNJ": "Johnson & Johnson",  # ジョンソン・エンド・ジョンソン
    "WMT": "Walmart",  # ウォルマート
    "PG": "Procter & Gamble",  # P&G
    "NVDA": "NVIDIA",  # エヌビディア
    "DIS": "Walt Disney",  # ウォルト・ディズニー
    "HD": "Home Depot",  # ホーム・デポ
    "UNH": "UnitedHealth",  # ユナイテッドヘルス
    "KO": "Coca-Cola",  # コカ・コーラ
    "MCD": "McDonald's",  # マクドナルド
    "NKE": "Nike",  # ナイキ
    "JPM": "JPMorgan Chase",  # JPモルガン・チェース
    "IBM": "IBM",  # IBM
    "MMM": "3M",  # スリーエム
    "DOW": "Dow Inc.",  # ダウ
    "BA": "Boeing",  # ボーイング
    "CSCO": "Cisco",  # シスコシステムズ
    "CVX": "Chevron",  # シェブロン
    "GS": "Goldman Sachs",  # ゴールドマンサックス
    "HON": "Honeywell",  # ハネウェル
    "INTC": "Intel",  # インテル
    "MRK": "Merck",  # メルク
    "MS": "Morgan Stanley",  # モルガン・スタンレー
    "PFE": "Pfizer",  # ファイザー
    "TRV": "Travelers",  # トラベラーズ
    "VZ": "Verizon",  # ベライゾン
    "WBA": "Walgreens Boots Alliance",  # ウォルグリーン・ブーツ・アライアンス
    "XOM": "ExxonMobil"  # エクソンモービル
}

def fetch_stock_data(start_date="2020-01-01", end_date="2024-01-01", freq="daily"):
    """
    日経平均225とダウ30の構成銘柄の株価データを取得。
    - freq="daily": 日次データ
    - freq="monthly": 月次データ
    - freq="quarterly": 四半期データ
    - freq="yearly": 年次データ
    """
    ticker_to_name = {**ticker_to_name_nikkei, **ticker_to_name_dow}
    tickers = list(ticker_to_name.keys())
    data = yf.download(tickers, start=start_date, end=end_date, interval="1d")["Close"]
    
    # Resampling
    if freq == "monthly":
        data = data.resample("ME").last()
    elif freq == "quarterly":
        data = data.resample("Q").last()
    elif freq == "yearly":
        data = data.resample("YE").last()

    # Rename ticker to corporate name
    data.rename(columns=ticker_to_name, inplace=True)

    return data