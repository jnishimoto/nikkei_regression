import matplotlib.pyplot as plt
import seaborn as sns
from visualization import save_plot

def compute_correlation_matrix(stock_data):
    """株価のリターンから相関行列を計算"""
    returns = stock_data.pct_change().dropna()
    return returns.corr()

def plot_correlation_matrix(corr_matrix, title="Correlation Matrix", save=False):
    """Visualize correlation matrix as a heatmap with an option to save."""
    
    num_labels = len(corr_matrix)
    fig_height = min(50, max(20, num_labels * 0.7))  # Adjust figure height dynamically
    plt.figure(figsize=(fig_height, fig_height))
    
    # Create heatmap
    ax = sns.heatmap(corr_matrix, cmap="coolwarm", annot=False, linewidths=0.5, square=True)

    # Set title
    plt.title(title, fontsize=16)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save the plot if required
    if save:
        save_plot("correlation_matrix")
    
    plt.show()

def plot_cluster_map(corr_matrix, title="Clustered Correlation Matrix", save=False):
    """Visualize the correlation matrix as a cluster map with an option to save."""
    
    num_labels = len(corr_matrix)
    fig_height = min(50, max(20, num_labels * 0.5))  # Adjust figure size dynamically
    
    # Create cluster map
    g = sns.clustermap(
        corr_matrix, 
        cmap="coolwarm",
        linewidths=0.5,
        figsize=(fig_height, fig_height),
        method="ward",
        metric="euclidean",
        col_cluster=False
    )

    # Set title
    g.ax_heatmap.set_title(title, fontsize=16)

    # Save the plot if required
    if save:
        save_plot("cluster_map")

    plt.show()
