import collections


class FriendshipService:

    def __init__(self):
        self.followers = {}
        self.followings = {}

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """

    def getFollowers(self, user_id):
        # write your code here
        followers = self.followers.get(user_id, None)
        if not followers:
            return []
        return sorted(followers.keys())

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """

    def getFollowings(self, user_id):
        # write your code here
        followings = self.followings.get(user_id, None)
        if not followings:
            return []
        return sorted(followings.keys())

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, to_user_id, from_user_id):
        # write your code here
        followers = self.followers.get(to_user_id)
        if not followers:
            self.followers[to_user_id] = collections.OrderedDict([(from_user_id, None)])
        else:
            self.followers[to_user_id].update({from_user_id: None})

        followings = self.followings.get(from_user_id)
        if not followings:
            self.followings[from_user_id] = collections.OrderedDict([(to_user_id, None)])
        else:
            self.followings[from_user_id].update({to_user_id: None})

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, to_user_id, from_user_id):
        # write your code here
        followers = self.followers.get(to_user_id)
        if followers:
            self.followers[to_user_id].pop(from_user_id, None)

        followings = self.followings.get(from_user_id)
        if followings:
            self.followings[from_user_id].pop(to_user_id, None)