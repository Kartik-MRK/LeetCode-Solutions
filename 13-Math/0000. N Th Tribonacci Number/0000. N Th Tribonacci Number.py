1class Solution:
2    def tribonacci(self, n: int) -> int:
3        one=0
4        two=1
5        three=1
6        if n<=2:
7            if n:
8                return 1
9            else:
10                return 0
11        for i in range(3,n+1):
12            temp1=three
13            temp2=two
14            three=one+two+three
15            two=temp1
16            one=temp2
17        return three
18        