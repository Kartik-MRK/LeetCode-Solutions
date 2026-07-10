1import heapq
2class Solution:
3    def lastStoneWeight(self, stones: List[int]) -> int:
4        heap=[]
5        for ele in stones:
6            heapq.heappush(heap,-ele)
7        while len(heap)>1:
8            x=heapq.heappop(heap)
9            y=heapq.heappop(heap)
10            x-=y
11            if x<0:
12                heapq.heappush(heap,x)
13        return abs(heap[0]) if heap else 0
14
15
16        