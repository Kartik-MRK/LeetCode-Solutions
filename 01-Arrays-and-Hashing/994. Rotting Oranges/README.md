<h2><a href="https://leetcode.com/problems/rotting-oranges">994. Rotting Oranges</a></h2>

<p>You are given an <code>m x n</code> <code>grid</code> where each cell can have one of three values:</p>

<ul>
	<li><code>0</code> representing an empty cell,</li>
	<li><code>1</code> representing a fresh orange, or</li>
	<li><code>2</code> representing a rotten orange.</li>
</ul>

<p>Every minute, any fresh orange that is <strong>4-directionally adjacent</strong> to a rotten orange becomes rotten.</p>

<p>Return <em>the minimum number of minutes that must elapse until no cell has a fresh orange</em>. If <em>this is impossible, return</em> <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/16/oranges.png" style="width: 650px; height: 137px;">
<pre><strong>Input:</strong> grid = [[2,1,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> grid = [[2,1,1],[0,1,1],[1,0,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> grid = [[0,2]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there are already no fresh oranges at minute 0, the answer is just 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>grid[i][j]</code> is <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>


---

# 🛍️ Rotting-Oranges | Explained
## Approach 1: Breadth-First Search (BFS)
### Intuition
The core idea behind this solution is to utilize a Breadth-First Search (BFS) algorithm to simulate the rotting process of oranges in a grid, where each rotten orange can potentially rot its adjacent fresh oranges. This approach leverages a queue data structure to efficiently process the oranges level by level.
### Approach
The algorithm starts by initializing a queue with all the rotten oranges (marked as 2) in the grid and marking them as visited. Then, it enters a loop where it dequeues each rotten orange, attempts to rot its adjacent fresh oranges (marked as 1), and enqueues these newly rotten oranges. This process continues until all reachable fresh oranges have been rotten or no more fresh oranges can be reached. The number of minutes passed is tracked by incrementing a counter after each level of BFS is completed.
### Code
```python
queue = deque()
minutes = 0
directions = [(1,0),(0,1),(-1,0),(0,-1)]
visited = [[False for i in range(width)] for i in range(height)]
for i in range(height):
    for j in range(width):
        if grid[i][j]==2:
            queue.append([i,j])
            visited[i][j]=True

while queue:
    n = len(queue)
    for i in range(n):
        row, col = queue.popleft()
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] and not visited[nr][nc]:
                queue.append([nr, nc])
                grid[nr][nc] = 2
                visited[nr][nc] = True
    if queue:
        minutes += 1
```
### Complexity
- Time: O(m*n) where m is the number of rows and n is the number of columns in the grid, because each cell is visited at most once.
- Space: O(m*n) for the queue in the worst case when the grid is filled with rotten oranges.

## 🔍 Analysis
1. **Core Intuition**: This algorithm uses BFS to simulate the rotting process of oranges in a grid, efficiently tracking the number of minutes required to rot all fresh oranges. The approach utilizes a queue to maintain the order of oranges to be processed, ensuring that each level of rotting is handled before moving on to the next level.
2. **Complexity Analysis**: 
   - Time: O(m*n) because each cell in the grid is visited at most once.
   - Space: O(m*n) for the queue in the worst-case scenario where the grid is filled with rotten oranges.
3. **Critical Optimizations**: This approach achieves optimal runtime boundaries as it visits each cell at most once, making it efficient for large grids. However, micro-optimizations such as using a more compact queue representation or reducing the number of boundary checks could further improve performance in specific scenarios. 

## 🕵️‍♂️ Follow-up Questions (Optional)
Some potential follow-up questions include:
- How would you adapt this solution to handle a 3D grid of oranges?
- What modifications would be necessary to prioritize the rotting of oranges based on their distance from a specific point in the grid?