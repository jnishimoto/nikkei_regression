import matplotlib.pyplot as plt

def plot_results(result, freq):
    """回帰モデルの結果を可視化"""
    model = result["model"]
    y_pred = model.fittedvalues
    y_actual = model.model.endog  # 実測値
    resid = model.resid

    # 実測値 vs 予測値
    plt.figure(figsize=(6,4))
    plt.scatter(y_pred, y_actual, alpha=0.5)
    plt.plot([y_actual.min(), y_actual.max()], [y_actual.min(), y_actual.max()], color='red', linewidth=2)
    plt.xlabel('Predicted Nikkei')
    plt.ylabel('Actual Nikkei')
    plt.title(f'{freq} Data: Actual vs Predicted')
    plt.show()

    # 残差ヒストグラム
    plt.figure(figsize=(6,4))
    plt.hist(resid, bins=30, color='gray', edgecolor='black')
    plt.xlabel('Residual')
    plt.ylabel('Frequency')
    plt.title(f'{freq} Data: Residuals Distribution')
    plt.show()
