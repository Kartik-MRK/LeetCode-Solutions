1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n=len(s)
4        count=0
5        for i in range(n):
6            count+=1
7            left=i-1
8            right=i+1
9            while left>=0 and right<n:
10                if s[left]==s[right]:
11                    count+=1
12                    left-=1
13                    right+=1
14                else:
15                    break
16        for i in range(n-1):
17            # count+=1
18            left=i
19            right=i+1
20            while left>=0 and right<n:
21                if s[left]==s[right]:
22                    count+=1
23                    left-=1
24                    right+=1
25                else:
26                    break
27        return count
28
29
30        