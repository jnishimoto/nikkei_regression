# Nikkei & Dow Stock Analysis

This project performs regression analysis and correlation visualization for Nikkei 225 and Dow 30 stocks, including heatmaps, cluster maps, and regression plots.

## Features
- Fetch historical stock data (Nikkei 225 & Dow 30 and USDJPY)
- Analyze regression models (R², VIF, correlation matrix)
- Visualize results with:
  - Correlation Heatmap
  - Cluster Map
  - Regression Analysis Plots
- Save results (plots & regression data) in timestamped directories

---

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/nikkei_regression.git
cd nikkei_regression
```

### 2. Install Dependencies
Make sure you have Python 3.7+ installed, then run:
```sh
pip install -r requirements.txt
```

### 3. Run the Analysis
```sh
python main.py
```

---

## Project Structure
```
nikkei_regression/
│── data_fetch.py        # Fetch stock data from Yahoo Finance
│── regression.py        # Run multiple regression analysis
│── visualization.py     # Generate plots and graphs
│── correlation.py       # Compute and visualize correlation matrices
│── main.py              # Main script to execute all tasks
│── results/             # Folder to save regression outputs
│── plots/               # Folder to store visualization results
│── README.txt           # Project documentation
│── requirements.txt     # List of dependencies
│── LICENSE              # MIT License
```

---

## Example Output

### Regression Results
```
Regression Results for Daily Data
R² (Coefficient of Determination): 0.895

Coefficients:
       Coefficient  p-value  VIF
const   -8613.027      0.00  47.7
USDJPY     141.063      0.00   1.2
Dow          0.595      0.00   1.2
```

### Generated Plots
- `plots/20240308_153000/correlation_matrix.png`
- `plots/20240308_153000/cluster_map.png`
- `plots/20240308_153000/regression_plot.png`

#### Daily Price Regression
![Daily Regression](https://github.com/jnishimoto/nikkei_regression/blob/main/plots/20250309_1245/Daily_chart.png?raw=true)

#### Monthly Price Regression
![Monthly Regression](https://github.com/jnishimoto/nikkei_regression/blob/main/plots/20250309_1245/Monthly_chart.png?raw=true)

#### Yearly Price Regression
![Yearly Regression](https://github.com/jnishimoto/nikkei_regression/blob/main/plots/20250309_1245/Yearly_chart.png?raw=true)

#### Correlation Heatmap
![Correlation Heatmap](https://github.com/jnishimoto/nikkei_regression/blob/main/plots/20250309_1245/correlation_matrix.png?raw=true)

#### Cluster Map
![Cluster Map](https://github.com/jnishimoto/nikkei_regression/blob/main/plots/20250309_1245/cluster_map.png?raw=true)

#### Daily Return Regression
![Daily Regression](https://github.com/jnishimoto/nikkei_regression/blob/main/plots/20250316_1159/Daily%20Returns_chart.png?raw=true)

#### Monthly Return Regression
![Monthly Regression](https://github.com/jnishimoto/nikkei_regression/blob/main/plots/20250316_1159/Monthly%20Returns_chart.png?raw=true)

#### Yearly Return Regression
![Yearly Regression](https://github.com/jnishimoto/nikkei_regression/blob/main/plots/20250316_1159/Yearly%20Returns_chart.png?raw=true)

---

## Contributing
Feel free to open an issue or submit a pull request if you have improvements or bug fixes.

---

## License
This project is licensed under the MIT License.

---

Thank you for using this project. If you found it useful, consider sharing your feedback.
