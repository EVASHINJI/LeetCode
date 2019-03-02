# Url: https://leetcode.com/problems/design-twitter/
# Related Topics:
# HashTable Heap Design

# Example:
# Twitter twitter = new Twitter();
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# // User 1 follows user 2.
# twitter.follow(1, 2);
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);


from collections import defaultdict
import itertools
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_news = defaultdict(list)
        self.user_followees = defaultdict(set)
        self.timer = itertools.count(step=1)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.user_news[userId].append((next(self.timer), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news = []
        for fId in self.user_followees[userId] | set([userId]):
            news.extend(self.user_news[fId])
        news.sort(reverse=True)
        return list(map(lambda x: x[1], news))[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_followees[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)