class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userId -> newsFeed which is [time, tweetIds]
        self.followMap = defaultdict(set) # followees who i am following

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from most recent
        minHeap = []

        self.followMap[userId].add(userId)
         # should be a set: andrew -> thomas, braden, thy
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][index]
                minHeap.append([time, tweetId, followee, index - 1])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [time, tweetId, followee, index - 1])
            
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
