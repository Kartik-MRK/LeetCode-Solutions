1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        nums=sorted(nums)
4        for i in range (1,len(nums)):
5            if nums[i]==nums[i-1]:
6                return True
7        return False
8        