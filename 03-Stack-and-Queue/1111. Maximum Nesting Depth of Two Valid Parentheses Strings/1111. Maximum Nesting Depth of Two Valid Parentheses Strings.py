1class Solution:
2    def maxDepthAfterSplit(self, seq: str) -> list[int]:
3        astack=[]
4        bstack=[]
5        res=[]
6        for ch in seq:
7            if ch=='(':
8                if len(astack)==len(bstack) or len(astack)<len(bstack):
9                    astack.append(ch)
10                    res.append(0)
11                else:
12                    bstack.append(ch)
13                    res.append(1)
14            else:
15                if len(astack)==len(bstack) or len(astack)<len(bstack):
16                    bstack.pop()
17                    res.append(1)
18                else:
19                    astack.pop()
20                    res.append(0)
21        return res
22
23
24
25
26
27        