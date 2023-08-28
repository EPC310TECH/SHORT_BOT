# data_fetcher.py

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.errors import APIError
import config

class DataFetcher:
    def __init__(self):
        self.alpha_vantage = TimeSeries(key=config.ALPHA_VANTAGE_API_KEY)
    
    def fetch_historical_data(self, symbol):
        try:
            data, _ = self.alpha_vantage.get_daily(symbol=symbol, outputsize='full')
            return data
        except APIError as e:
            print(f"Failed to fetch historical data for {symbol}: {e}")
            return None
    
    def fetch_real_time_data(self, symbol):
        try:
            data, _ = self.alpha_vantage.get_quote_endpoint(symbol=symbol)
            return data
        except APIError as e:
            print(f"Failed to fetch real-time data for {symbol}: {e}")
            return None

# Usage example:
# data_fetcher = DataFetcher()
# historical_data = data_fetcher.fetch_historical_data('TSLA')
# real_time_data = data_fetcher.fetch_real_time_data('TSLA')
