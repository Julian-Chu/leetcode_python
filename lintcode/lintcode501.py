# Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
            pass
# This will create a new tweet object,
# and auto fill id


class MiniTwitter:

    def __init__(self):
        self.followers = {}
        self.followings = {}
        self.tweets = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """

    def postTweet(self, user_id, tweet_text):
        tweet = Tweet.create(user_id, tweet_text)
        if user_id not in self.tweets:
            self.tweets[user_id] = [tweet]
        else:
            self.tweets[user_id].append(tweet)

        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """

    def getNewsFeed(self, user_id):
        tweets = []
        tweets += self.getTimeline(user_id)

        if user_id in self.followings:
            friends = self.followings[user_id]
            for friend_id in friends:
                tweets += self.getTimeline(friend_id)

        tweets.sort(key=lambda tweet: tweet.id, reverse=True)

        return tweets[:10]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """

    def getTimeline(self, user_id):
        if user_id not in self.tweets:
            return []
        tweets = self.tweets[user_id]
        return tweets[-10:][::-1]

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, from_user_id, to_user_id):
        if from_user_id not in self.followings:
            self.followings[from_user_id] = {to_user_id}
        if to_user_id not in self.followings[from_user_id]:
            self.followings[from_user_id].add(to_user_id)

        if to_user_id not in self.followers:
            self.followers[to_user_id] = {from_user_id}
        if from_user_id not in self.followers[to_user_id]:
            self.followers[to_user_id].add(from_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, from_user_id, to_user_id):
        self.followings[from_user_id].remove(to_user_id)
        self.followers[to_user_id].remove(from_user_id)
