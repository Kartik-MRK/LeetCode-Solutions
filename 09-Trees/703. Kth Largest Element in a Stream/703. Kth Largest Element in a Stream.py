1import heapq
2class KthLargest:
3
4    def __init__(self, k: int, nums: List[int]):
5        self.heap=[]
6        self.k=k
7        for ele in nums[:k]:
8            heapq.heappush(self.heap,ele)
9        
10        for ele in nums[k:]:
11            if ele>=self.heap[0]:
12                heapq.heappop(self.heap)
13                heapq.heappush(self.heap,ele)
14            
15        
16
17    def add(self, val: int) -> int:
18        if len(self.heap)<self.k:
19            heapq.heappush(self.heap,val)
20        elif val>=self.heap[0]:
21                heapq.heappop(self.heap)
22                heapq.heappush(self.heap,val)
23        return self.heap[0]
24
25        
26
27
28# Your KthLargest object will be instantiated and called as such:
29# obj = KthLargest(k, nums)
30# param_1 = obj.add(val)