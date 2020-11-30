'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''
class PubSubPattern:
    def __init__(self):
        self.channel_users = dict()


    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """
    def subscribe(self, channel, user_id):
        if channel not in self.channel_users:
            self.channel_users[channel] = set()
        self.channel_users[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def unsubscribe(self, channel, user_id):
    	if channel in self.channel_users and user_id in self.channel_users[channel]:
            self.channel_users[channel].discard(user_id)

    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """

    def publish(self, channel, message):
        if channel not in self.channel_users:
            return
        for user_id in self.channel_users[channel]:
            PushNotification.notify(user_id, message)
