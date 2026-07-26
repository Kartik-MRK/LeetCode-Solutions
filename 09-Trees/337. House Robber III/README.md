<h2><a href="https://leetcode.com/problems/house-robber-iii">337. House Robber III</a></h2>

<p>The thief has found himself a new place for his thievery again. There is only one entrance to this area, called <code>root</code>.</p>

<p>Besides the <code>root</code>, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if <strong>two directly-linked houses were broken into on the same night</strong>.</p>

<p>Given the <code>root</code> of the binary tree, return <em>the maximum amount of money the thief can rob <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg" style="width: 277px; height: 293px;">
<pre><strong>Input:</strong> root = [3,2,3,null,3,null,1]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg" style="width: 357px; height: 293px;">
<pre><strong>Input:</strong> root = [3,4,5,1,3,null,1]
<strong>Output:</strong> 9
<strong>Explanation:</strong> Maximum amount of money the thief can rob = 4 + 5 = 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ House-Robber-III | Explained

## Approach 1: Depth-First Search with Memoization
### Intuition
The core idea behind this approach is to utilize a depth-first search (DFS) to traverse the binary tree, considering each node as a potential target for robbery. By using a clever memoization technique, we can keep track of the maximum amount that can be robbed at each node, either by including or excluding the current node. This approach works by recursively exploring all possible combinations of nodes to rob, while avoiding the complexity of redundant calculations through memoization.

### Approach
The algorithm starts by defining a recursive function `dfs` that takes a tree node as input. This function returns a list of two values: the maximum amount that can be robbed by including the current node, and the maximum amount that can be robbed by excluding the current node. By using this approach, we can ensure that we consider all possible combinations of nodes to rob, while avoiding the complexity of redundant calculations.

### Detailed Code Analysis
The provided code defines a `Solution` class with a `rob` method that takes the root node of the binary tree as input. The `rob` method defines a nested `dfs` function that performs the actual calculation. The `dfs` function checks if the input node is `None`, in which case it returns a list `[0, 0]`, indicating that no nodes can be robbed. Otherwise, it recursively calls itself on the left and right child nodes, and then returns a list containing the maximum amount that can be robbed by including the current node (`left[1] + right[1] + node.val`) and the maximum amount that can be robbed by excluding the current node (`max(left) + max(right)`).

### Code
```python
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            return [left[1] + right[1] + node.val, max(left) + max(right)]
        return max(dfs(root))
```

### Complexity
- **Time:** O(N), where N is the number of nodes in the binary tree, since each node is visited once by the `dfs` function.
- **Space:** O(N), due to the recursive call stack, which can reach a maximum depth of N in the worst case (when the binary tree is skewed to one side).

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common follow-up questions for this pattern include:
- How would you handle the case where the binary tree is extremely large and cannot fit into memory?
- Can you optimize the solution to use less memory? 

1. **Core Intuition**: The algorithmic strategy used is a depth-first search with memoization, allowing for efficient exploration of the binary tree while avoiding redundant calculations.
2. **Complexity Analysis**: 
    * Time complexity: O(N), where N is the number of nodes in the binary tree, due to each node being visited once.
    * Space complexity: O(N), resulting from the recursive call stack, which can reach a maximum depth of N in the worst case.
3. **Critical Optimizations**: This approach achieves optimal runtime and space boundaries by using a recursive DFS with memoization, eliminating the need for redundant calculations and reducing memory usage. No further microscopic micro-optimizations are necessary.