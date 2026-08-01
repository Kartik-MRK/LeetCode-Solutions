1from collections import deque
2class Solution:
3    def predictTheWinner(self, nums: List[int]) -> bool:
4        p1=0
5        p2=0
6        def dfs(left,right,p1,p2,turn):
7            if left>right:
8                if p1>=p2:
9                    return True
10                else:
11                    return False
12            if turn==1:
13                return dfs(left+1,right,p1+nums[left],p2,2) or dfs(left,right-1,p1+nums[right],p2,2)
14                
15            elif turn==2:
16                return dfs(left+1,right,p1,p2+nums[left],1) and dfs(left,right-1,p1,p2+nums[right],1)
17            
18        return True if dfs(0,len(nums)-1,0,0,1) else False
19
20            
21
22
23
24        