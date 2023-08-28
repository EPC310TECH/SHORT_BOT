# config.py

# Telegram Bot API token
BOT_TOKEN = "your_telegram_bot_token"

# Alpha Vantage API key
ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"

# Default notification preference
DEFAULT_NOTIFICATION_PREFERENCE = True

# List of available stocks for subscription
AVAILABLE_STOCKS = ['SHOP', 'TSLA', 'NIO', 'M', 'W', 'AI']

# Timezone settings
TIMEZONE = 'America/Los_Angeles'

# Data fetching interval for real-time data (in seconds)
REAL_TIME_INTERVAL = 300  # 5 minutes

# Maximum number of subscribed stocks per user
MAX_SUBSCRIBED_STOCKS = 5

# Stop loss and take profit percentages
STOP_LOSS_PERCENT = 2
TAKE_PROFIT_PERCENT = 4

# Message templates
SUBSCRIBE_MESSAGE = "You are now subscribed to trading signals for {}."
UNSUBSCRIBE_MESSAGE = "You are unsubscribed from trading signals."
NOTIFICATION_ON_MESSAGE = "Notifications are now enabled."
NOTIFICATION_OFF_MESSAGE = "Notifications are now disabled."

# ... Add other configuration settings here ...
