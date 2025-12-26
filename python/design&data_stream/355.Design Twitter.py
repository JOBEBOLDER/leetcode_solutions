class Twitter:
    def __init__(self):
        self.tweetMap = defaultdict(list) #userid:[(timestamp,tweetid)]
        self.followMap = defaultdict(set)
        self.count = 0


    def postTweet(self,userId:int ,tweetId:int) ->None:
        #update the count:
        self.count -= 1
        self.tweetMap[userId].append([self.count,tweetId])
        

    def getNewsFeed(self,userId:int) -> List[int]:
        res = []

        minheap = []

        for followeeid in self.followMap[userId]:
            if followeeid in self.tweetMap:
                index = len(self.tweetMap[followeeid] - 1)
                count,tweetid = self.tweetMap[followeeid][index]
                heapq.heappush(minheap,[count,tweetid,followeeid,index - 1])
        
        while minheap and len(res) < 10:
            count,tweetid,followeeid,index = heapq.heappop(minheap)
            res.append(tweetid)
            if index>= 0:
                count,tweetid = self.tweetMap[followeeid][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])

        return res


    def follow(self,followerId:int, followeeId:int)->None:
        self.followMap[followerId].add(followeeId)

    def unfollolw(self,followerId:int, followeeId:int)->None:
        if followeeId != followerId and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

