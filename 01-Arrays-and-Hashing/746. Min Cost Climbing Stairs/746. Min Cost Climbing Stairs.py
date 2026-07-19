1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n=len(cost)
4        memo=[-1 for i in range(n+1)]
5        def dfs(step):
6            if step>=n+1:
7                return 0
8            if step>=n-2:
9                return cost[step]
10            if memo[step]!=-1:
11                return memo[step]
12            
13            memo[step]=min(dfs(step+1),dfs(step+2))+cost[step]
14            return memo[step]
15
16        return min(dfs(0),dfs(1))
17
18
19        
20
21        