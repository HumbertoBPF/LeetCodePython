from collections import deque
from typing import List
import heapq

class User:
    def __init__(self, userId):
        self.userId = userId
        self.followees = set()
        self.tweets = deque()

    def __repr__(self):
        return str(self.userId)

class Twitter:

    def __init__(self):
        self.user_database = {}
        self.current_date = 0

    def get_or_create_user(self, userId):
        user = self.user_database.get(userId)
        if user is None:
            user = User(userId)
            self.user_database[userId] = user
        return user

    def keep_ten_last_tweets(self, last_ten_tweets, tweets):
        for tweet in tweets:
            if len(last_ten_tweets) < 10:
                heapq.heappush(last_ten_tweets, tweet)
                continue

            oldest_tweet = last_ten_tweets[0]

            if tweet[0] > oldest_tweet[0]:
                heapq.heappushpop(last_ten_tweets, tweet)
    # Time complexity: O(1)
    # Space complexity: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.get_or_create_user(userId)
        tweet = [self.current_date, tweetId]
        # We ust need to store the 10 last tweets
        if len(user.tweets) < 10:
            user.tweets.append(tweet)
        else:
            user.tweets.popleft()
            user.tweets.append(tweet)
        # Incrementing the current date because tweets must be ordered from most recent to least recent
        self.current_date += 1
    # Time complexity: O(n)
    # Space complexity: O(1), notice that the data structures created here always have at most 10 items
    # where n is the number of followees of the specified user
    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.get_or_create_user(userId)
        # This is a min heap containing the 10 most recent tweets
        last_ten_tweets = []
        heapq.heapify(last_ten_tweets)

        self.keep_ten_last_tweets(last_ten_tweets, user.tweets)
        # Get followees' tweets
        for followee in user.followees:
            self.keep_ten_last_tweets(last_ten_tweets, followee.tweets)
        # Sorting the 10 last tweets in decreasing order by date (constant time since we have at most 10 tweets)
        last_ten_tweets.sort(key=lambda x: x[0], reverse=True)

        return [tweet[1] for tweet in last_ten_tweets]

    # Time complexity: O(1)
    # Space complexity: O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self.get_or_create_user(followerId)
        followee = self.get_or_create_user(followeeId)
        follower.followees.add(followee)
    # Time complexity: O(1)
    # Space complexity: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.get_or_create_user(followerId)
        followee = self.get_or_create_user(followeeId)
        if followee in follower.followees:
            follower.followees.remove(followee)

twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
