1class Solution:
2    def makesquare(self, matchsticks: List[int]) -> bool:
3        matchsticks.sort(reverse=True)
4        n=len(matchsticks)
5        if n<4:
6            return False
7        perimeter=sum(matchsticks)
8        if perimeter%4!=0:
9            return False
10        side=perimeter//4
11
12        def dfs(sides,count):
13            
14            if count==n:
15                return True
16            for i in range(4):    
17                if i>0 and sides[i]==sides[i-1]:
18                    continue
19                if sides[i]+matchsticks[count]<=side:
20                    sides[i]+=matchsticks[count]
21                    if dfs(sides,count+1):
22                        return True
23                    sides[i]-=matchsticks[count]               
24                if sides[i]==0:
25                    break
26            return False
27        return dfs([0,0,0,0],0)      
28