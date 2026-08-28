1class Solution:
2    def maxChunksToSorted(self, arr: List[int]) -> int:
3        maxseen=-1
4        partition=0
5        for i in range(len(arr)):
6            maxseen=max(maxseen,arr[i])
7            if i==maxseen:
8                partition+=1
9                maxseen=-1
10        return partition
11        
12
13
14
15        