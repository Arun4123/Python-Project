# Trend Analysis
# Covert Month column
import yfinance as yf
import pandas as pd
# Function to fetch historical stock prices
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data
# Function to generate features from historical stock prices
def generate_features(data):
    data['MA5'] = data['Close'].rolling(window=5).mean()
    data['MA10'] = data['Close'].rolling(window=10).mean()
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()

    # Create binary labels for trend (1: Up, 0: Down)
    data['Trend'] = (data['Close'].shift(-1) > data['Close']).astype(int)

    return data.dropna()

# Function to train a Support Vector Machine (SVM) model
def train_svm_model(features, target):
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train SVM model
    svm_model = SVC(kernel='linear', C=1)
    svm_model.fit(X_train_scaled, y_train)

    # Make predictions
    predictions = svm_model.predict(X_test_scaled)

    # Evaluate accuracy
    accuracy = accuracy_score(y_test, predictions)
    print(f'Accuracy: {accuracy * 100:.2f}%')

# Example usage
    # Define stock symbol and date range
    stock_symbol = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2018-01-01'

    # Fetch historical stock prices
    stock_data = get_stock_data(stock_symbol, start_date, end_date)

    # Generate features and labels
    processed_data = generate_features(stock_data)

    # Select features and target variable
    features = processed_data[['Close', 'MA5', 'MA10', 'MA20', 'MA50']]
    target = processed_data['Trend']

   # plot the points in the graph
    plt.figure(figsize=(10,12))
    plt.plot(get_stock_data('IG221A22N'), Linestyle='-')
    plt.grid(True)
    plt.xlabel('year')
    plt.legend()
    plt.show()
