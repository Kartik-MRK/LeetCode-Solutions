1from collections import deque
2class Solution:
3    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
4        height=len(mat)
5        width=len(mat[0])
6        res=[[[0] for i in range(width)] for i in range(height)]
7        visited=[[False for i in range(width)] for j in range(height)]
8        queue=deque()
9        dir=[(0,1),(1,0),(-1,0),(0,-1)]
10        for i in range(height):
11            for j in range(width):
12                if not mat[i][j]:
13                    queue.append([[i,j],0])
14                    visited[i][j]=True
15        
16        while queue:
17           
18            q=queue.popleft()
19            res[q[0][0]][q[0][1]]=q[1]
20
21
22            for dr,dc in dir:
23                nr=q[0][0]+dr
24                nc=q[0][1]+dc
25                if 0<=nr<height and 0<=nc<width and not visited[nr][nc]:
26                    queue.append([[nr,nc],q[1]+1])
27                    visited[nr][nc]=True
28
29        return res
30
31
32
33
34        