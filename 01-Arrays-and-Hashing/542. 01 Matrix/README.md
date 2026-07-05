<h2><a href="https://leetcode.com/problems/01-matrix">542. 01 Matrix</a></h2>

<p>Given an <code>m x n</code> binary matrix <code>mat</code>, return <em>the distance of the nearest </em><code>0</code><em> for each cell</em>.</p>

<p>The distance between two cells sharing a common edge is <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg" style="width: 253px; height: 253px;">
<pre><strong>Input:</strong> mat = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> [[0,0,0],[0,1,0],[0,0,0]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg" style="width: 253px; height: 253px;">
<pre><strong>Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]]
<strong>Output:</strong> [[0,0,0],[0,1,0],[1,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>There is at least one <code>0</code> in <code>mat</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1765: <a href="https://leetcode.com/problems/map-of-highest-peak/description/" target="_blank">https://leetcode.com/problems/map-of-highest-peak/</a></p>


---

# 🛍️ 01-Matrix | Explained

## Approach 1 (Breadth-First Search)
### Intuition
The code utilizes a Breadth-First Search (BFS) strategy to update the matrix, where each cell's value represents the minimum distance to the nearest zero. This approach is analogous to a flood fill algorithm, where the "flood" originates from the zero-valued cells and propagates to the neighboring cells, incrementing the distance at each step.

### Approach
The algorithm iteratively explores the matrix, starting from the cells with a value of 0. For each cell, it checks all four possible directions (up, down, left, and right) and updates the distance value of the neighboring cells if they have not been visited before. This process continues until all cells have been visited, resulting in a matrix where each cell's value represents the minimum distance to the nearest zero.

### Code
```python
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height=len(mat)
        width=len(mat[0])
        res=[[[0] for i in range(width)] for i in range(height)]
        visited=[[False for i in range(width)] for j in range(height)]
        queue=deque()
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(height):
            for j in range(width):
                if not mat[i][j]:
                    queue.append([[i,j],0])
                    visited[i][j]=True
        
        while queue:
            q=queue.popleft()
            res[q[0][0]][q[0][1]]=q[1]

            for dr,dc in dir:
                nr=q[0][0]+dr
                nc=q[0][1]+dc
                if 0<=nr<height and 0<=nc<width and not visited[nr][nc]:
                    queue.append([[nr,nc],q[1]+1])
                    visited[nr][nc]=True

        return res
```

### Complexity
- Time: **O(m \* n)**, where m and n are the dimensions of the input matrix, since we visit each cell at most once.
- Space: **O(m \* n)**, for the queue and the visited matrix in the worst-case scenario (when the matrix is filled with zeros).

## 🕵️‍♂️ Follow-up Questions (Optional)
1. **What if the input matrix is empty?** In this case, the algorithm will return an empty matrix, as there are no cells to update.
2. **Can we optimize the algorithm further?** While the current approach has a time complexity of O(m \* n), it is already optimal for this problem, as we need to visit each cell at least once to update its distance value.

**Core Intuition:** The algorithm employs a BFS strategy to update the matrix, where each cell's value represents the minimum distance to the nearest zero. This is achieved by iteratively exploring the matrix, starting from the cells with a value of 0, and propagating the distance values to the neighboring cells.

**Complexity Analysis:**
* Time complexity: **O(m \* n)**, where m and n are the dimensions of the input matrix.
	+ Justification:
		- We visit each cell at most once.
		- The queue operations (enqueue and dequeue) take constant time.
* Space complexity: **O(m \* n)**, for the queue and the visited matrix in the worst-case scenario.
	+ Justification:
		- We need to store the visited status of each cell.
		- In the worst-case scenario, the queue can contain m \* n cells.

**Critical Optimizations:** The current approach achieves optimal runtime and space boundaries, with a time complexity of O(m \* n) and a space complexity of O(m \* n). No further micro-optimizations are necessary, as we need to visit each cell at least once to update its distance value.