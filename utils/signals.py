# signals.py

class SignalGenerator:
    def __init__(self, strategy, data_fetcher):
        self.strategy = strategy
        self.data_fetcher = data_fetcher
    
    def generate_signals(self):
        signals = []

        for stock_symbol in self.strategy.data:
            historical_data = self.data_fetcher.fetch_historical_data(stock_symbol)
            if historical_data:
                signals.extend(self.strategy.generate_signals(stock_symbol, historical_data))

        return signals

# Other utility functions or methods related to signal generation can be added here
