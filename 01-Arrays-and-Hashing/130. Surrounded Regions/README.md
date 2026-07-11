<h2><a href="https://leetcode.com/problems/surrounded-regions">130. Surrounded Regions</a></h2>

<p>You are given an <code>m x n</code> matrix <code>board</code> containing <strong>letters</strong> <code>'X'</code> and <code>'O'</code>, <strong>capture regions</strong> that are <strong>surrounded</strong>:</p>

<ul>
	<li><strong>Connect</strong>: A cell is connected to adjacent cells horizontally or vertically.</li>
	<li><strong>Region</strong>: To form a region <strong>connect every</strong> <code>'O'</code> cell.</li>
	<li><strong>Surround</strong>: A region is surrounded if none of the <code>'O'</code> cells in that region are on the edge of the board. Such regions are <strong>completely enclosed </strong>by <code>'X'</code> cells.</li>
</ul>

<p>To capture a <strong>surrounded region</strong>, replace all <code>'O'</code>s with <code>'X'</code>s <strong>in-place</strong> within the original board. You do not need to return anything.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" style="width: 367px; height: 158px;">
<p>In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [["X"]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[["X"]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>board[i][j]</code> is <code>'X'</code> or <code>'O'</code>.</li>
</ul>


---

# 🛍️ Surrounded-Regions | Explained

## Approach 1 (Optimized)
### Intuition
The core idea behind this approach is to identify the 'O' regions connected to the border of the board and mark them as temporary ('T') to distinguish them from the surrounded 'O' regions. This works by leveraging the fact that any 'O' region connected to the border cannot be surrounded, as it has a path to the outside. 
### Approach
The algorithmic steps are as follows:
- Iterate over the border cells of the board and mark any 'O' regions as 'T' using a queue-based BFS traversal.
- After marking all border-connected 'O' regions, iterate over the entire board and flip the remaining 'O' regions to 'X' (as they are surrounded) and the 'T' regions back to 'O'.

### Detailed Code Analysis
Let's break down the code:
- Lines 7-8 calculate the height and width of the input board.
- Line 9 defines the possible directions for BFS traversal (right, down, left, up).
- Line 10 initializes a queue to store the cells to be processed.
- The nested loops in lines 11-15 iterate over the border cells of the board. If a cell is an 'O', it is marked as 'T' and added to the queue.
- The while loop in lines 17-25 performs the BFS traversal. For each cell in the queue, it checks all neighboring cells. If a neighboring cell is an 'O', it is marked as 'T' and added to the queue.
- The final nested loops in lines 26-32 iterate over the entire board. If a cell is an 'O', it is flipped to 'X' (as it is surrounded). If a cell is a 'T', it is flipped back to 'O' (as it is not surrounded).

### Code
```python
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height = len(board)
        width = len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque()
        for i in range(height):
            for j in range(width):
                if (i==0 or j==0 or j==width-1 or i==height-1) and board[i][j]=='O':
                    board[i][j] = 'T'
                    queue.append([i,j])
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col
                if 0 <= nr < height and 0 <= nc < width and board[nr][nc] == 'O':
                    board[nr][nc] = 'T'
                    queue.append([nr,nc])
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
```

### Complexity
- Time: O(M*N), where M is the number of rows and N is the number of columns in the board. This is because we are doing two passes over the board: one to mark the border-connected 'O' regions and another to flip the surrounded 'O' regions.
  * Justification:
    * The initial pass over the border cells takes O(M+N) time.
    * The BFS traversal takes O(M*N) time in the worst case (when the entire board is filled with 'O' regions).
    * The final pass over the board takes O(M*N) time.
- Space: O(M*N), where M is the number of rows and N is the number of columns in the board. This is because in the worst case, we might need to store all cells in the queue.
  * Justification:
    * The queue can store up to M*N cells in the worst case.
    * The input board itself takes O(M*N) space.

## 🕵️‍♂️ Follow-up Questions (Optional)
1. How would you optimize this solution for a very large input board?
   * Answer: To optimize the solution for a very large input board, we could consider using a more efficient data structure for the queue, such as a heap or a priority queue. However, in this case, a simple deque is sufficient.
2. Can you think of any alternative approaches to solve this problem?
   * Answer: Yes, an alternative approach could be to use a depth-first search (DFS) instead of BFS to traverse the border-connected 'O' regions. However, this would not change the overall time or space complexity of the solution.

**Core Intuition**: The algorithm leverages the fact that any 'O' region connected to the border of the board cannot be surrounded, and marks these regions as temporary ('T') to distinguish them from the surrounded 'O' regions. 
**Complexity Analysis**:
* Time: O(M*N)
* Space: O(M*N)
  * Justification:
    + Time complexity is O(M*N) due to the two passes over the board and the BFS traversal.
    + Space complexity is O(M*N) due to the queue and the input board.
**Critical Optimizations**: This approach achieves optimal runtime and space boundaries, as it only requires two passes over the board and uses a queue to efficiently traverse the border-connected 'O' regions. No further microscopic micro-optimizations are necessary.