
# Stock Price Fetcher from Yahoo Finance
import yfinance as yf
import pandas as pd

def get_stock_price(stock_symbol, start_date, end_date):
    # Fetches the stock price with a ticker symbol and time frame using yfinance
    # Returns:pd.DataFrame: A dataframe containing the stock prices in the specified time frame
    
    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        if stock_data.empty:
            print(f"No data found for {stock_symbol} in the given time frame.")
            return None
        print(f"Stock prices for {stock_symbol} from {start_date} to {end_date} ")
        print(stock_data)
        return stock_data
    except Exception as e:
        print(f"An error occured while fetching the stock price: {e}")
        return None
    
def main():
    pass