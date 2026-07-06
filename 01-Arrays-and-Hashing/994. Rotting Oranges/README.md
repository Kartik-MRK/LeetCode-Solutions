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

## Approach 1 (BFS with Queue)
### Intuition
The core idea behind this solution is to utilize a Breadth-First Search (BFS) approach, where we start from the rotten oranges and gradually spread the rot to the adjacent fresh oranges, keeping track of the time it takes for this process. This strategy leverages the concept of a queue data structure to efficiently manage the order in which the oranges are visited.

### Approach
Here's a step-by-step breakdown of how the algorithm works:
1. Initialize a queue with the coordinates of all rotten oranges in the grid.
2. Perform a BFS traversal, where at each level, we visit all the neighboring fresh oranges of the current rotten orange.
3. Mark these fresh oranges as rotten and add them to the queue.
4. Repeat this process until the queue is empty, keeping track of the number of minutes passed.

### Code
```python
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height=len(grid)
        width=len(grid[0])
        queue=deque()
        minutes=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        visited=[[False for i in range(width)] for i in range(height)]
        for i in range(height):
            for j in range(width):
                if grid[i][j]==2:
                    queue.append([i,j])
                    visited[i][j]=True

        while queue:
            n=len(queue)
            for i in range(n):
                row,col=queue.popleft()
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if 0<=nr<height and 0<=nc<width and grid[nr][nc] and not visited[nr][nc]:
                        queue.append([nr,nc])
                        grid[nr][nc]=2
                        visited[nr][nc]=True
            if queue:
                minutes+=1
        for i in range(height):
            for j in range(width):
                if grid[i][j]==1:
                    return -1
        return minutes
```
### Complexity
- Time: O(m \* n), where m and n are the dimensions of the grid, as we potentially visit each cell once.
- Space: O(m \* n), as in the worst-case scenario, the queue can store all cells of the grid.

## 💡 Key Insights
1. **Core Intuition**: The algorithm leverages a BFS strategy, using a queue to spread the rot from rotten oranges to fresh ones, tracking the time taken for this process. This approach ensures that we visit each cell in the most efficient order possible.
2. **Complexity Analysis**:
    * Time: O(m \* n) because we might visit each cell once.
    * Space: O(m \* n) as the queue can store all cells in the worst case.
3. **Critical Optimizations**: This solution achieves optimal runtime and space boundaries. However, a microscopic optimization could involve reducing the number of times we check the boundaries of the grid by using a more efficient data structure or pruning the search space.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common follow-up questions for this pattern and their brief answers are:
- Q: How would you handle a scenario where there are no rotten oranges initially?
  A: In such a case, the algorithm would simply return 0, as there's no rot to spread, and all oranges remain fresh.
- Q: Can we further optimize the solution for extremely large grids?
  A: Yes, potential optimizations include parallelizing the BFS traversal or utilizing a more efficient data structure, such as a heap, to manage the order of visited cells. However, these optimizations would depend on the specific constraints and requirements of the problem.