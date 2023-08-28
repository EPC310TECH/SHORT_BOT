# subscription_manager.py

class SubscriptionManager:
    def __init__(self, user_database):
        self.user_database = user_database
    
    def subscribe_user(self, user_id, stocks):
        if user_id not in self.user_database:
            self.user_database[user_id] = {'subscriptions': [], 'notifications': config.DEFAULT_NOTIFICATION_PREFERENCE}
        
        for stock in stocks:
            if stock not in self.user_database[user_id]['subscriptions']:
                self.user_database[user_id]['subscriptions'].append(stock)
    
    def unsubscribe_user(self, user_id):
        if user_id in self.user_database:
            self.user_database.pop(user_id)
    
    def set_notification_preference(self, user_id, preference):
        if user_id in self.user_database:
            self.user_database[user_id]['notifications'] = preference
    
    def get_user_subscriptions(self, user_id):
        return self.user_database.get(user_id, {}).get('subscriptions', [])

    def get_user_notification_preference(self, user_id):
        return self.user_database.get(user_id, {}).get('notifications', config.DEFAULT_NOTIFICATION_PREFERENCE)

# Other utility functions or methods related to subscription management can be added here
