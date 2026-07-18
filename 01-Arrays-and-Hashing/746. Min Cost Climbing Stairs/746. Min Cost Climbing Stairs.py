1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        mincost=float(inf)
4        n=len(cost)
5        for i in range(n-3,-1,-1):
6            cost[i]+=min(cost[i+1],cost[i+2])
7        return min(cost[0],cost[1])
8
9        
10
11        