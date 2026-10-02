1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        n=len(cost)
4        total=0
5        minpos=-1
6        if sum(gas)<sum(cost):
7            return -1
8        for i in range(n):
9            diff=gas[i]-cost[i]
10            if total+diff>=0:
11                total+=diff
12                if minpos==-1:
13                    minpos=i
14            else:
15                total=0
16                minpos=-1
17        return minpos
18
19