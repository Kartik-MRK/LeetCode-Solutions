1class Solution:
2    def replaceElements(self, arr: List[int]) -> List[int]:
3        n=len(arr)
4        maxele=-1
5        for i in range(n-1,-1,-1):
6            curr=maxele
7            maxele=max(maxele,arr[i])
8            arr[i]=curr
9        
10        return arr
11
12        