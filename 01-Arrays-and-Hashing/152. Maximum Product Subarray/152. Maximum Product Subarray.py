1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        stack=[]
4        curr=None
5        prefix=1
6        suffix=1
7        res=float(-inf)
8        n=len(nums)
9        for i in range(n):
10            if nums[i]==0:
11                prefix=1
12                res=max(res,nums[i])
13            else:
14                prefix*=nums[i]
15                res=max(res,prefix,nums[i])
16
17            if nums[n-i-1]==0:
18                res=max(res,nums[n-i-1])
19                suffix=1
20            else:
21                suffix*=nums[n-i-1]
22                res=max(res,suffix,nums[n-i-1])
23            
24
25        
26        return res
27            
28            
29                
30
31            
32        
33        
34        