1class Solution:
2    def maxSumOfSquares(self, num: int, sum: int) -> str:
3        res=
4        if 9*num<sum:
5            return 
6        while sum>0:
7            if sum-9>0:
8                res+='9'
9                sum-=9
10            else:
11                res+=str(sum)
12                sum=0
13        n=num-len(res)
14        return res+'0'*n
15
16
17
18
19        