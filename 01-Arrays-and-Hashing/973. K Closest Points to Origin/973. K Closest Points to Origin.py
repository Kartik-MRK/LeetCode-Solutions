1import math
2import heapq
3class Solution:
4    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
5        heap=[]
6        res=[]
7        for x,y in points:
8            
9            dorigin=-sqrt(x**2+y**2)
10            if len(heap)<k:
11                heapq.heappush(heap,(dorigin,[x,y]))
12            else:
13                if heap[0][0]<=dorigin:
14                    dele=heapq.heappop(heap)
15
16                    heapq.heappush(heap,(dorigin,[x,y]))
17        for key,value in heap:
18            res.append(value)
19        return res
20        
21
22
23        