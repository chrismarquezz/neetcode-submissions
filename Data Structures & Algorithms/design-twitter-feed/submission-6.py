class Twitter:

    def __init__(self):
        self.time = 0
        self.twitter = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.twitter.setdefault(userId, []).append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        sources = {userId} | self.follows.get(userId, set())
        for user in sources:
            for t, tweet in self.twitter.get(user, []):
                heapq.heappush_max(heap, (t, tweet))
        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop_max(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()        
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
