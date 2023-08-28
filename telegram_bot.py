import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.errors import APIError
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, InlineQueryHandler
import logging
import config

# Access configuration settings
bot_token = config.BOT_TOKEN
alpha_vantage_api_key = config.ALPHA_VANTAGE_API_KEY
default_notification_preference = config.DEFAULT_NOTIFICATION_PREFERENCE
available_stocks = config.AVAILABLE_STOCKS

# Load environment variables from .env file
load_dotenv()

# Retrieve the API token and Alpha Vantage API key from the environment variables
TOKEN = os.getenv("BOT_TOKEN")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# Initialize Alpha Vantage API
alpha_vantage = TimeSeries(key=ALPHA_VANTAGE_API_KEY)

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Dictionary to simulate a simple user database
user_database = {}

# ... Your other code ...

# Command handler for displaying the main menu
def main_menu(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    keyboard = [
        [InlineKeyboardButton("Subscribe", callback_data="subscribe"),
         InlineKeyboardButton("Unsubscribe", callback_data="unsubscribe")],
        [InlineKeyboardButton("Notification Preference", callback_data="notification")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=user_id, text="Main Menu:", reply_markup=reply_markup)

# Fetch historical data with error handling
def fetch_historical_data(symbol, interval):
    try:
        data, meta_data = alpha_vantage.get_daily(symbol=symbol, outputsize='full')
        return data
    except APIError as e:
        logging.error(f"Failed to fetch historical data: {e}")
        return None

# Inline query handler for displaying subscribed stocks
def inline_query(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    user_id = update.inline_query.from_user.id

    if query.lower() == "subscriptions":
        subscribed_stocks = get_user_subscriptions(user_id)
        if subscribed_stocks:
            results = [
                InlineKeyboardButton(stock_symbol, callback_data=stock_symbol)
                for stock_symbol in subscribed_stocks
            ]
            reply_markup = InlineKeyboardMarkup([results])
            update.inline_query.answer([reply_markup])
        else:
            update.inline_query.answer([])
    else:
        update.inline_query.answer([])

# Callback query handler
def callback_query(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == "subscribe":
        subscribe_user(user_id, ['SHOP', 'TSLA', 'NIO', 'M', 'W', 'AI'])
        context.bot.send_message(chat_id=user_id, text="Subscribed to notifications.")
    elif query.data == "unsubscribe":
        unsubscribe_user(user_id)
        context.bot.send_message(chat_id=user_id, text="Unsubscribed from notifications.")
    elif query.data == "notification":
        context.bot.send_message(chat_id=user_id, text="Change notification preference using /notification true or /notification false.")
    elif query.data in user_database.get(user_id, {}).get('subscriptions', []):
        context.bot.send_message(chat_id=user_id, text=f"Signal detected for {query.data}")

# Set up command handlers
main_menu_handler = CommandHandler('menu', main_menu)

# Set up inline query and callback query handlers
inline_query_handler = InlineQueryHandler(inline_query)
callback_query_handler = CallbackQueryHandler(callback_query)

dispatcher.add_handler(main_menu_handler)
dispatcher.add_handler(inline_query_handler)
dispatcher.add_handler(callback_query_handler)

# ... Your other code ...

# Start the bot
updater.start_polling()
updater.idle()
