
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
    print("Welcome this is the Yahoo Finance Stock Price Checker!")
    stock_symbol = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ").upper()
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    stock_data = get_stock_price(stock_symbol, start_date, end_date)
    if stock_data is not None:
        save_option = input("Would you like to save the data to a CSV file? (yes/no): ").lower()
        if save_option == "yes":
            filename = f"{stock_symbol}_prices_{start_date}_to_{end_date}.csv"
            stock_data.to_csv(filename)
            print(f"Data saved to {filename}")
            
if __name__ == "__main__":
    main()