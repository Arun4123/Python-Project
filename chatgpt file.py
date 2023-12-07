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
def plot_stock_data(data, window):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['SMA'], label=f'SMA ({window} days)')
    plt.title('Stock Price with SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Get external input for stock symbol, start date, end date, and SMA window size
    stock_symbol = input("Enter stock symbol: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    window = int(input("Enter SMA window size: "))

    # Fetch historical stock prices
    stock_data = get_stock_data(stock_symbol, start_date, end_date)

    # Calculate Simple Moving Average (SMA)
    stock_data = calculate_sma(stock_data, window=window)

    # Display and plot the data
    print(stock_data.head())
    plot_stock_data(stock_data, window)
