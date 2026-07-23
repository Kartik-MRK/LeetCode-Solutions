1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        left=1
4        right=num
5        while left<=right:
6            mid=(left+right)//2
7            sqr=mid*mid
8            if sqr==num:
9                return True
10            if sqr>num:
11                right=mid-1
12            else:
13                left=mid+1
14        
15        return False
16        