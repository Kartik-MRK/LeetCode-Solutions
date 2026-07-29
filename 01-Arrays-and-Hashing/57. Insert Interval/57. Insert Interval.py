1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res=[]
4        newstart,newend=newInterval
5        for index,(start,end) in enumerate(intervals):
6            if start>newend:
7                res.append([newstart,newend])
8                return res+intervals[index:]
9            elif newstart>end:
10                res.append([start,end])
11            else:
12                newstart,newend=[min(newstart,start),max(newend,end)]
13                
14        res.append([newstart,newend])
15        return res
16
17        