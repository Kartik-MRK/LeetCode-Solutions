1from functools import cache
2import math
3class Solution:
4    def winnerSquareGame(self, n: int) -> bool:
5        dp={}
6        def backtrack(n):
7            if n==0:
8                return False
9            
10            if sqrt(n)==float(int(sqrt(n))):
11                return True
12            if n in dp:
13                return dp[n]
14            
15            for k in range(1,int(sqrt(n))+1):
16                if not backtrack(n-k*k):
17                    dp[n]=True
18                    return dp[n]
19            
20            dp[n]=False
21            return dp[n]
22
23        return backtrack(n)
24
25        