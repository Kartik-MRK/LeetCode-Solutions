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

## Approach 1: Dynamic Programming Bottom-Up
### Intuition
The core idea behind this approach is to iterate through the stairs from bottom to top, at each step considering the minimum cost of reaching the current step by either climbing from the step below or the step below that. This dynamic programming strategy works because it breaks down the problem into smaller sub-problems and leverages the optimal solutions to these sub-problems to construct the overall optimal solution.
### Algorithm Visualized
```mermaid
graph LR
    A[Start] -->|Initialize cost array|> B[Iterate from n-3 to 0]
    B -->|At each step i, calculate cost[i] = cost[i] + min(cost[i+1], cost[i+2])|> C[Update cost array]
    C -->|Return min(cost[0], cost[1])|> D[End]
```
### Approach
The algorithm iterates through the stairs from the third step from the end to the first step, updating the cost of each step based on the minimum cost of reaching the next two steps. This approach ensures that the cost of reaching each step is optimized based on the costs of the subsequent steps.
### Detailed Code Analysis
- Line 1-2: The solution class and method are defined, with `minCostClimbingStairs` taking a list of integers `cost` as input and returning the minimum cost of reaching the top.
- Line 3: The variable `mincost` is initialized with positive infinity, but it is not used in the computation.
- Line 4: The length of the `cost` array is stored in the variable `n`.
- Line 5-6: The loop iterates from the third step from the end to the first step. For each step `i`, the cost of reaching that step is updated by adding the minimum cost of reaching the next two steps (`cost[i+1]` and `cost[i+2]`).
- Line 7: The minimum cost of reaching the top is the minimum cost of reaching the first or second step.
- Line 8: The function returns this minimum cost.
### Code
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(n-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
```
### Complexity
- **Time:** O(n), where n is the number of stairs. The algorithm iterates through the stairs once, performing a constant amount of work at each step.
- **Space:** O(1), as the algorithm only uses a constant amount of space to store the variables `n`, `i`, and the updated costs in the `cost` array.

## 🕵️‍♂️ Follow-up Questions (Optional)
1. What if the input array is empty or contains only one element? The function should handle these edge cases by returning 0 or the single element's cost, respectively.
2. How can this solution be generalized to handle more complex stair-climbing scenarios, such as varying step costs or additional constraints? The dynamic programming approach can be extended to accommodate these scenarios by modifying the recurrence relation and the state transition diagram accordingly.