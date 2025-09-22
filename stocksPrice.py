
# Stock Price Fetcher from Yahoo Finance
import yfinance as yf
import pandas as pd

def get_stock_price(ticker, start, end):
    
    try:
        stock_data = yf.download(ticker, start=start, end=end)
        if stock_data.empty:
            print(f"No data found for {ticker} in the given time frame.")
            return None
        print(f"Stock prices for {ticker} from {start} to {end} ")
        print(stock_data)
        return stock_data
    except Exception as e:
        print(f"An error occured while fetching the stock price: {e}")
        return None
    
def main():
    print("Welcome this is the Yahoo Finance Stock Price Checker!")
    ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ").upper()
    start = input("Enter the start date (YYYY-MM-DD): ")
    end = input("Enter the end date (YYYY-MM-DD): ")
    
    stock_data = get_stock_price(ticker, start, end)
    if stock_data is not None:
        save_option = input("Would you like to save the data to a CSV file? (yes/no): ").lower()
        if save_option == "yes":
            filename = f"{ticker}_prices_{start}_to_{end}.csv"
            stock_data.to_csv(filename)
            print(f"Data saved to {filename}")
            
if __name__ == "__main__":
    main()