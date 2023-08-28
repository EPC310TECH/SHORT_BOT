# strategy.py

class TradingStrategy:
    def __init__(self, data):
        self.data = data
    
    def generate_signals(self):
        signals = []

        for stock_symbol, stock_data in self.data.items():
            rsi = self.calculate_rsi(stock_data['close'], window=14)
            rvol = self.calculate_rvol(stock_data['volume'], window=10, sma_window=1)

            if rsi < 60 and rvol > 2:
                signals.append({'symbol': stock_symbol, 'signal': 'BUY'})

        return signals
    
    def calculate_rsi(self, close_prices, window=14):
        deltas = [close_prices[i] - close_prices[i - 1] for i in range(1, len(close_prices))]
        gains = [delta if delta > 0 else 0 for delta in deltas]
        losses = [-delta if delta < 0 else 0 for delta in deltas]

        avg_gain = sum(gains[:window]) / window
        avg_loss = sum(losses[:window]) / window

        for i in range(window, len(gains)):
            avg_gain = ((window - 1) * avg_gain + gains[i]) / window
            avg_loss = ((window - 1) * avg_loss + losses[i]) / window
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def calculate_rvol(self, volume, window=10, sma_window=1):
        sma_volume = sum(volume[-window:]) / window
        rvol = volume[-1] / (sma_volume * sma_window)
        
        return rvol

# Other utility functions or methods related to your trading strategy can be added here
