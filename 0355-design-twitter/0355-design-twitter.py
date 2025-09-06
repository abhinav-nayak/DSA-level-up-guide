import heapq

class Twitter:

    def __init__(self):
        # create a variable to keep track of time of tweet
        self.counter = 0
        # create a hash map to map users with their tweets
        self.user_tweet_map = {}
        # create a hash map to map user to the users they are following
        self.user_following_map = {}

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrement time as max heap later needs time in negative
        self.counter -= 1
        # update current tweet in the list of tweets for current user
        tweets = self.user_tweet_map.get(userId, list())
        tweets.append((self.counter, tweetId))
        self.user_tweet_map[userId] = tweets
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # This is a kind of 'Find maximum/ minimum' problrem as we have to find top 10 latest tweet.
        # So, we use heap
        # Important to create copy of list, else maxHeap will have reference to list in map and
        # corrupt the map
        maxHeap = list(self.user_tweet_map.get(userId, []))
        for followingUserId in self.user_following_map.get(userId, []):
            if self.user_tweet_map.get(followingUserId):
                maxHeap.extend(self.user_tweet_map[followingUserId])
        
        # heapify the tweets of current user and all the users he will following
        heapq.heapify(maxHeap)

        # return 10 latest tweets
        result = []
        count=0
        while count<10 and maxHeap:
            result.append(heapq.heappop(maxHeap)[1])
            count += 1
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # add the followee Id in hash set of follower Id
        following = self.user_following_map.get(followerId, set())
        following.add(followeeId)
        self.user_following_map[followerId] = following
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
         # remove the followee Id from hash set of follower Id
        following = self.user_following_map.get(followerId)
        if following:
            following.remove(followeeId)
            self.user_following_map[followerId] = following


# Time compelxity: O(n)
# Space complexity: O(N∗m+N∗M+n)
# where n is total number of tweets a user can get in his feed, m is the maximum number of tweets by any 
# user (m can be at most 10), N is the total number of userIds and M is the maximum number of 
# followees for any user.

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)