1from collections import deque
2import heapq
3class Twitter:
4
5    def __init__(self):
6        self.follower=defaultdict(set)
7        self.count=0
8        self.post=defaultdict(list)
9        
10
11    def postTweet(self, userId: int, tweetId: int) -> None:
12        if userId not in self.post:
13            self.post[userId]=[]
14        self.post[userId].append([self.count,tweetId])
15        self.count-=1
16        
17
18    def getNewsFeed(self, userId: int) -> List[int]:
19        res=[]
20        minheap=[]
21        self.follower[userId].add(userId)
22        for followeeId in self.follower[userId]:
23            if self.post[followeeId]:
24                index=len(self.post[followeeId])-1
25                count,tweetId=self.post[followeeId][index]
26                minheap.append([count,tweetId,followeeId,index-1])
27        heapq.heapify(minheap)
28        
29        while minheap and len(res)<10:
30            count,tweetId,followeeId,index=heapq.heappop(minheap)
31            res.append(tweetId)
32            if index>=0:
33                count,tweetId=self.post[followeeId][index]
34                heapq.heappush(minheap,[count,tweetId,followeeId,index-1])
35
36        return res
37
38
39        
40
41    def follow(self, followerId: int, followeeId: int) -> None:
42        
43        self.follower[followerId].add(followeeId)
44        
45
46    def unfollow(self, followerId: int, followeeId: int) -> None:
47        if followerId in self.follower:
48            self.follower[followerId].remove(followeeId)
49
50        
51
52
53# Your Twitter object will be instantiated and called as such:
54# obj = Twitter()
55# obj.postTweet(userId,tweetId)
56# param_2 = obj.getNewsFeed(userId)
57# obj.follow(followerId,followeeId)
58# obj.unfollow(followerId,followeeId)