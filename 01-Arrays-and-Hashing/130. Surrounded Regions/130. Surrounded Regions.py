1from collections import deque
2class Solution:
3    def solve(self, board: List[List[str]]) -> None:
4        
5        Do not return anything, modify board in-place instead.
6        
7        height=len(board)
8        width=len(board[0])
9        directions=[(0,1),(1,0),(0,-1),(-1,0)]
10        queue=deque()
11        for i in range(height):
12            for j in range(width):
13                if (i==0 or j==0 or j==width-1 or i==height-1) and board[i][j]==O:
14                    board[i][j]=T
15                    queue.append([i,j])
16        
17        while queue:
18            row,col=queue.popleft()
19            for dr,dc in directions:
20                nr=dr+row
21                nc=dc+col
22                if 0<=nr<height and 0<=nc<width and board[nr][nc]==O:
23                    board[nr][nc]=T
24                    queue.append([nr,nc])
25
26        for i in range(height):
27            for j in range(width):
28                if board[i][j]==O:
29                    board[i][j]=X
30                elif board[i][j]==T:
31                    board[i][j]=O
32        
33
34        
35                    
36
37        
38        