1class Solution:
2    def reverseDegree(self, s: str) -> int:
3        res,i=0,1
4        for ch in s:
5            res+=(123-ord(ch))*i
6            i+=1
7        return res
8
9        