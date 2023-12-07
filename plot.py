import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Function to fetch historical stock prices
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Function to decompose time series into seasonal, trend, and residual components
def decompose_time_series(data, frequency=252):  # Assuming daily trading (252 days in a year)
    result = seasonal_decompose(data['Close'], model='additive', freq=frequency)
    return result

# Function to plot the decomposed components
def plot_components(data, result):
    plt.figure(figsize=(12, 8))
    plt.subplot(411)
    plt.plot(data['Close'], label='Original')
    plt.legend()
    plt.subplot(412)
    plt.plot(result.trend, label='Trend')
    plt.legend()
    plt.subplot(413)
    plt.plot(result.seasonal, label='Seasonal')
    plt.legend()
    plt.subplot(414)
    plt.plot(result.resid, label='Residual')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Define stock symbol and date range
    stock_symbol = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2023-01-01'

    # Fetch historical stock prices
    stock_data = get_stock_data(stock_symbol, start_date, end_date)

    # Decompose time series
    decomposition_result = decompose_time_series(stock_data)

    # Plot the decomposed components
    plot_components(stock_data, decomposition_result)


