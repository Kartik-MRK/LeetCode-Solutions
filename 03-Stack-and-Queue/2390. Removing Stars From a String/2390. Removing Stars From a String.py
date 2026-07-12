1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack=[]
4        for ele in s:
5            if ele==* and stack:
6                stack.pop()
7            else:
8                stack.append(ele)
9        return .join(stack)
10
11        