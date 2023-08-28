# user_database.py

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = {'subscriptions': [], 'notifications': config.DEFAULT_NOTIFICATION_PREFERENCE}

    def remove_user(self, user_id):
        if user_id in self.users:
            self.users.pop(user_id)

    def add_subscription(self, user_id, stock_symbol):
        if user_id in self.users and stock_symbol not in self.users[user_id]['subscriptions']:
            self.users[user_id]['subscriptions'].append(stock_symbol)

    def remove_subscription(self, user_id, stock_symbol):
        if user_id in self.users and stock_symbol in self.users[user_id]['subscriptions']:
            self.users[user_id]['subscriptions'].remove(stock_symbol)

    def set_notification_preference(self, user_id, preference):
        if user_id in self.users:
            self.users[user_id]['notifications'] = preference

    def get_user_subscriptions(self, user_id):
        return self.users.get(user_id, {}).get('subscriptions', [])

    def get_user_notification_preference(self, user_id):
        return self.users.get(user_id, {}).get('notifications', config.DEFAULT_NOTIFICATION_PREFERENCE)
