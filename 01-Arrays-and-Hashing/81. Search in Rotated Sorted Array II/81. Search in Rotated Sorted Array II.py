1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        n=len(nums)
4        left=0
5        right=n-1
6        while left<=right:
7            mid=(left+right)//2
8            if nums[mid]==target:
9                return True
10            if nums[mid]<nums[right]:
11                if nums[mid]<target<=nums[right]:
12                    left=mid+1
13                else:
14                    right=mid-1
15            elif nums[right]<nums[mid]:
16                if nums[left]<=target<nums[mid]:
17                    right=mid-1
18                else:
19                    left=mid+1
20            else:
21                right-=1
22
23        return False
24        