1class Solution:
2    def sumOfSquares(self, nums: List[int]) -> int:
3        res=0
4        n=len(nums)
5        for i in range(1,n+1):
6            if n%(i)==0:
7                res+=nums[i-1]**2
8        return res
9
10        