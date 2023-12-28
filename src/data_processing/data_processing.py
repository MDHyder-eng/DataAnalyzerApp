import pandas as pd

def process_data(data):
    # Remove rows with any missing values
    data = data.dropna()
    
    # Convert the 'Date' column to datetime type
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Set the 'Date' column as the index of the DataFrame
    data.set_index('Date', inplace=True)
    
    # Sort data by date (from oldest to newest)
    data.sort_index(inplace=True)
    
    # Calculate daily returns
    data['Daily Return'] = data['Close'].pct_change()
    
    # Calculate moving averages
    data['30 Day Avg'] = data['Close'].rolling(window=30).mean()
    data['100 Day Avg'] = data['Close'].rolling(window=100).mean()
    
    # Dropping all 'NaN' values
    data.dropna(inplace=True)
    
    return data
