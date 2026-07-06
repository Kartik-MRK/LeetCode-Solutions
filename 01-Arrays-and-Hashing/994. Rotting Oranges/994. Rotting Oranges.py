1from collections import deque
2class Solution:
3    def orangesRotting(self, grid: List[List[int]]) -> int:
4        height=len(grid)
5        width=len(grid[0])
6        queue=deque()
7        minutes=0
8        directions=[(1,0),(0,1),(-1,0),(0,-1)]
9        visited=[[False for i in range(width)] for i in range(height)]
10        for i in range(height):
11            for j in range(width):
12                if grid[i][j]==2:
13                    queue.append([i,j])
14                    visited[i][j]=True
15
16        while queue:
17            n=len(queue)
18            for i in range(n):
19                row,col=queue.popleft()
20                for dr,dc in directions:
21                    nr=row+dr
22                    nc=col+dc
23                    if 0<=nr<height and 0<=nc<width and grid[nr][nc] and not visited[nr][nc]:
24                        queue.append([nr,nc])
25                        grid[nr][nc]=2
26                        visited[nr][nc]=True
27            if queue:
28                minutes+=1
29        for i in range(height):
30            for j in range(width):
31                if grid[i][j]==1:
32                    return -1
33        return minutes
34
35
36                
37        