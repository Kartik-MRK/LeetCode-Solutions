<h2><a href="https://leetcode.com/problems/pacific-atlantic-water-flow">417. Pacific Atlantic Water Flow</a></h2>

<p>There is an <code>m x n</code> rectangular island that borders both the <strong>Pacific Ocean</strong> and <strong>Atlantic Ocean</strong>. The <strong>Pacific Ocean</strong> touches the island's left and top edges, and the <strong>Atlantic Ocean</strong> touches the island's right and bottom edges.</p>

<p>The island is partitioned into a grid of square cells. You are given an <code>m x n</code> integer matrix <code>heights</code> where <code>heights[r][c]</code> represents the <strong>height above sea level</strong> of the cell at coordinate <code>(r, c)</code>.</p>

<p>The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is <strong>less than or equal to</strong> the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.</p>

<p>Return <em>a <strong>2D list</strong> of grid coordinates </em><code>result</code><em> where </em><code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code><em> denotes that rain water can flow from cell </em><code>(r<sub>i</sub>, c<sub>i</sub>)</code><em> to <strong>both</strong> the Pacific and Atlantic oceans</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" style="width: 400px; height: 400px;">
<pre><strong>Input:</strong> heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
<strong>Output:</strong> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
<strong>Explanation:</strong> The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -&gt; Pacific Ocean 
&nbsp;      [0,4] -&gt; Atlantic Ocean
[1,3]: [1,3] -&gt; [0,3] -&gt; Pacific Ocean 
&nbsp;      [1,3] -&gt; [1,4] -&gt; Atlantic Ocean
[1,4]: [1,4] -&gt; [1,3] -&gt; [0,3] -&gt; Pacific Ocean 
&nbsp;      [1,4] -&gt; Atlantic Ocean
[2,2]: [2,2] -&gt; [1,2] -&gt; [0,2] -&gt; Pacific Ocean 
&nbsp;      [2,2] -&gt; [2,3] -&gt; [2,4] -&gt; Atlantic Ocean
[3,0]: [3,0] -&gt; Pacific Ocean 
&nbsp;      [3,0] -&gt; [4,0] -&gt; Atlantic Ocean
[3,1]: [3,1] -&gt; [3,0] -&gt; Pacific Ocean 
&nbsp;      [3,1] -&gt; [4,1] -&gt; Atlantic Ocean
[4,0]: [4,0] -&gt; Pacific Ocean 
       [4,0] -&gt; Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> heights = [[1]]
<strong>Output:</strong> [[0,0]]
<strong>Explanation:</strong> The water can flow from the only cell to the Pacific and Atlantic oceans.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == heights.length</code></li>
	<li><code>n == heights[r].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= heights[r][c] &lt;= 10<sup>5</sup></code></li>
</ul>


---

# 🛍️ Pacific-Atlantic-Water-Flow | Explained

## Approach 1 (Depth-First Search)
### Intuition
The core strategy used here is to employ Depth-First Search (DFS) to traverse the matrix from both Pacific and Atlantic Oceans, marking the cells that can flow into each ocean. This approach leverages the fact that water can flow from a cell to its adjacent cells if the adjacent cell's height is greater than or equal to the current cell's height.

### Approach
1. Initialize two separate matrices to store the cells that can flow into the Pacific and Atlantic Oceans.
2. Perform a DFS traversal from each cell on the borders of the Pacific Ocean, marking the cells that can flow into the Pacific Ocean.
3. Perform a DFS traversal from each cell on the borders of the Atlantic Ocean, marking the cells that can flow into the Atlantic Ocean.
4. Find the intersection of the two matrices to determine the cells that can flow into both oceans.

### Code
```python
def pacificAtlantic(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    pacific = [[False] * cols for _ in range(rows)]
    atlantic = [[False] * cols for _ in range(rows)]

    def dfs(row, col, visited, matrix):
        visited[row][col] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and matrix[nr][nc] >= matrix[row][col]:
                dfs(nr, nc, visited, matrix)

    for i in range(rows):
        dfs(i, 0, pacific, matrix)
        dfs(i, cols - 1, atlantic, matrix)
    for i in range(cols):
        dfs(0, i, pacific, matrix)
        dfs(rows - 1, i, atlantic, matrix)

    result = []
    for i in range(rows):
        for j in range(cols):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])
    return result
```

### Complexity
- Time: O(R*C) where R is the number of rows and C is the number of columns in the matrix. This is because we perform two DFS traversals from each cell on the borders of the Pacific and Atlantic Oceans.
- Space: O(R*C) where R is the number of rows and C is the number of columns in the matrix. This is because we use two separate matrices to store the cells that can flow into the Pacific and Atlantic Oceans.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common follow-up questions for this pattern include:
1. How would you optimize the solution if the matrix is extremely large and does not fit into memory?
2. How would you modify the solution to find the cells that can flow into both oceans with the minimum height?

The answer to the first question would involve using a more memory-efficient data structure, such as a hash set, to store the cells that can flow into each ocean. The answer to the second question would involve modifying the DFS traversal to keep track of the minimum height of the cells that can flow into each ocean. 

**Core Intuition**: This algorithm employs Depth-First Search (DFS) to mark cells that can flow into the Pacific and Atlantic Oceans, leveraging the fact that water flows to adjacent cells with greater or equal height. The intersection of these marked cells reveals the cells that can flow into both oceans.

**Complexity Analysis**:
- Time: O(R*C) 
  * Justification:
    + We perform two DFS traversals from each cell on the borders of the Pacific and Atlantic Oceans.
    + Each DFS traversal visits each cell at most once.
- Space: O(R*C) 
  * Justification:
    + We use two separate matrices to store the cells that can flow into the Pacific and Atlantic Oceans.

**Critical Optimizations**: This approach achieves optimal runtime and space boundaries, with no further micro-optimizations remaining. The use of DFS traversal and separate matrices ensures efficient exploration of the matrix and accurate identification of cells that can flow into both oceans.