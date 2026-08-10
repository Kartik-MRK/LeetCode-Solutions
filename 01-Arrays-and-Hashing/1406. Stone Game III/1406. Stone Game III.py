1class Solution:
2    def stoneGameIII(self, stoneValue: List[int]) -> str:
3        n=len(stoneValue)
4        dp={}
5        def backtrack(start):
6            if start>=n:
7                return 0
8            
9            if start in dp:
10                return dp[start]
11            res=float(-inf)
12            piles=0
13            for i in range(start,min(n,start+3)):
14                piles+=stoneValue[i]
15                res=max(res,piles-backtrack(i+1))
16
17            dp[start]=res            
18            return res
19        
20        ans=backtrack(0)
21        if ans>0:
22            return Alice
23        elif ans<0:
24            return Bob
25        else:
26            return Tie
27                
28
29        