import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch historical stock prices
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Function to calculate Simple Moving Average (SMA)
def calculate_sma(data, window=20):
    data['SMA'] = data['Close'].rolling(window=window).mean()
    return data

# Function to plot stock prices and SMA
def plot_stock_data(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['SMA'], label=f'SMA ({window} days)')
    plt.title('Stock Price with SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Define stock symbol and date range
    stock_symbol = 'CVS'
    start_date = '2018-01-01'
    end_date = '2023-11-01'

    # Fetch historical stock prices
    stock_data = get_stock_data(stock_symbol, start_date, end_date)

    # Calculate Simple Moving Average (SMA)
    window = 20  # Adjust the window size as needed
    stock_data = calculate_sma(stock_data, window=window)

    # Display and plot the data
    print(stock_data.head())
    plot_stock_data(stock_data)
