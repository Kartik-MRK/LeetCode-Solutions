1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        ans=[]
5        for i in range (2*n):
6            ans.append(nums[i%n])
7
8        return ans
9
10        