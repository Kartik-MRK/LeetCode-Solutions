1import heapq
2class Solution:
3    def findKthLargest(self, nums: List[int], k: int) -> int:
4        heap=[]
5        for ele in nums:
6            if len(heap)<k:
7                heapq.heappush(heap,ele)
8            else:
9                if heap[0]<ele:
10                    heapq.heappop(heap)
11                    heapq.heappush(heap,ele)
12        return heap[0]
13
14        