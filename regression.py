import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

def run_regression(df):
    """回帰分析を実行し、結果を辞書で返す"""
    X = df[["USDJPY", "Dow"]]
    y = df["Nikkei"]
    X_const = sm.add_constant(X)

    # 回帰モデルの適用
    model = sm.OLS(y, X_const).fit()

    # VIF 計算
    vif = {col: variance_inflation_factor(X_const.values, i) for i, col in enumerate(X_const.columns)}

    # 相関行列
    correlation_matrix = df.corr()

    # 結果を辞書で返す
    return {
        "model": model,
        "r2": model.rsquared,
        "coefficients": model.params,
        "p_values": model.pvalues,
        "vif": vif,
        "correlation_matrix": correlation_matrix
    }
