<h2><a href="https://leetcode.com/problems/min-cost-climbing-stairs">746. Min Cost Climbing Stairs</a></h2>

<p>You are given an integer array <code>cost</code> where <code>cost[i]</code> is the cost of <code>i<sup>th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.</p>

<p>You can either start from the step with index <code>0</code>, or the step with index <code>1</code>.</p>

<p>Return <em>the minimum cost to reach the top of the floor</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> cost = [10,<u>15</u>,20]
<strong>Output:</strong> 15
<strong>Explanation:</strong> You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> cost = [<u>1</u>,100,<u>1</u>,1,<u>1</u>,100,<u>1</u>,<u>1</u>,100,<u>1</u>]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= cost.length &lt;= 1000</code></li>
	<li><code>0 &lt;= cost[i] &lt;= 999</code></li>
</ul>


---

# 🛍️ Min-Cost-Climbing-Stairs | Explained

## Approach 1: Depth-First Search with Memoization
### Intuition
The core idea behind this approach is to use a depth-first search strategy with memoization to efficiently explore all possible stair-climbing paths and calculate their minimum costs. This approach works by recursively exploring the minimum cost paths from each stair, storing the intermediate results to avoid redundant calculations.

### Algorithm Visualized
```mermaid
graph TD
    A[Start] --> B{Choose Stair}
    B --> C1[Stair 1: Cost + min(Cost of Stair 2, Cost of Stair 3)]
    B --> C2[Stair 2: Cost + min(Cost of Stair 3, Cost of Stair 4)]
    C1 --> D1{Base Case: Last Two Stairs}
    C2 --> D2{Base Case: Last Two Stairs}
    D1 --> E1[Return Minimum Cost]
    D2 --> E2[Return Minimum Cost]
    E1 --> F[Return Minimum Cost of Both Paths]
    E2 --> F
```

### Approach
The algorithm starts at the beginning of the stairs and recursively explores two possible paths: climbing one stair or two stairs at a time. It calculates the minimum cost of each path by adding the current stair's cost to the minimum cost of the next two possible paths. This process continues until it reaches the base case, where it returns the minimum cost of the last two stairs. The algorithm uses memoization to store the intermediate results and avoid redundant calculations.

### Detailed Code Analysis
The code defines a recursive function `dfs` that takes a stair index `step` as input. It first checks if the stair index is out of bounds, in which case it returns 0. If the stair index is at the last two stairs, it returns the cost of that stair. If the result is already memoized, it returns the stored result. Otherwise, it calculates the minimum cost by recursively calling `dfs` for the next two stairs, adds the current stair's cost, and stores the result in the memoization array.

### Code
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1 for i in range(n + 1)]

        def dfs(step):
            if step >= n + 1:
                return 0
            if step >= n - 2:
                return cost[step]
            if memo[step] != -1:
                return memo[step]

            memo[step] = min(dfs(step + 1), dfs(step + 2)) + cost[step]
            return memo[step]

        return min(dfs(0), dfs(1))
```

### Complexity
- **Time:** O(n) because each stair is visited at most twice (once from the previous stair and once from the stair before that), and the recursive function has a memoization mechanism to avoid redundant calculations.
- **Space:** O(n) because the algorithm uses a memoization array of size n + 1 to store the intermediate results.

## 🕵️‍♂️ Follow-up Questions (Optional)
- What would happen if the input array is empty? The current implementation would throw an error, so you could add a check for an empty input array and return 0 in that case.
- How would you optimize the algorithm if the input array is extremely large? You could use an iterative approach with a dynamic programming table to avoid the recursive function call overhead.