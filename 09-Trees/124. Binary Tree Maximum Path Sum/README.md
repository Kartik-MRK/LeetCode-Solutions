<h2><a href="https://leetcode.com/problems/binary-tree-maximum-path-sum">124. Binary Tree Maximum Path Sum</a></h2>

<p>A <strong>path</strong> in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence <strong>at most once</strong>. Note that the path does not need to pass through the root.</p>

<p>The <strong>path sum</strong> of a path is the sum of the node's values in the path.</p>

<p>Given the <code>root</code> of a binary tree, return <em>the maximum <strong>path sum</strong> of any <strong>non-empty</strong> path</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;">
<pre><strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The optimal path is 2 -&gt; 1 -&gt; 3 with a path sum of 2 + 1 + 3 = 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg">
<pre><strong>Input:</strong> root = [-10,9,20,null,null,15,7]
<strong>Output:</strong> 42
<strong>Explanation:</strong> The optimal path is 15 -&gt; 20 -&gt; 7 with a path sum of 15 + 20 + 7 = 42.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3 * 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


---

# 🛍️ Binary-Tree-Maximum-Path-Sum | Explained

## Approach 1 (Optimized Recursive Depth-First Search)
### Intuition
The core idea behind this solution is to utilize a recursive depth-first search (DFS) approach to explore all possible paths within the binary tree, keeping track of the maximum path sum encountered. This approach works by recursively calculating the maximum path sum for each subtree and updating the global maximum path sum whenever a larger sum is found.

### Approach
The algorithmic steps can be broken down as follows:

1. Define a recursive DFS function that takes a node as input and returns the maximum path sum that can be obtained by including the current node.
2. Within the DFS function, recursively calculate the maximum path sums for the left and right subtrees.
3. Calculate the maximum path sum for the current node by considering the following cases: 
   - The current node's value only.
   - The current node's value plus the maximum path sum of the left subtree.
   - The current node's value plus the maximum path sum of the right subtree.
   - The current node's value plus the maximum path sums of both the left and right subtrees.
4. Update the global maximum path sum if the calculated maximum path sum for the current node exceeds the current global maximum.
5. Return the maximum path sum that can be obtained by including the current node, which is either the current node's value or the current node's value plus the maximum path sum of one of its subtrees.

### Detailed Code Analysis
Let's dive into the code block:

```python
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        maxsum=float(-inf)
10        def dfs(node):
11            if node is None:
12                return
13            nonlocal maxsum
14            
15            left=dfs(node.left)
16            left=left if left else 0
17            right=dfs(node.right)
18            right=right if right else 0
19            maxsubtree=float(-inf)
20            maxsubtree=max(maxsubtree,node.val)
21            maxsubtree=max(maxsubtree,node.val+left+right)
22            maxsubtree=max(maxsubtree,node.val+max(left,right))
23            
24            maxsum=max(maxsum,maxsubtree)
25
26            return max(node.val+max(left,right),node.val)
27
28        dfs(root)
29        return maxsum
```

Here's a line-by-line explanation:

- Lines 1-6 define the binary tree node class, which is not part of the solution but is included for completeness.
- Line 7 defines the solution class, and line 8 defines the `maxPathSum` method, which takes the root of the binary tree as input.
- Line 9 initializes the `maxsum` variable to negative infinity, which will store the global maximum path sum.
- Line 10 defines the nested `dfs` function, which takes a node as input and returns the maximum path sum that can be obtained by including the current node.
- Lines 11-13 handle the base case where the input node is `None`. In this case, the function returns `None`, but due to the recursive nature of the function, this will be treated as 0 in the calculation.
- Lines 15-18 recursively calculate the maximum path sums for the left and right subtrees. If a subtree is `None`, the function returns 0.
- Lines 19-22 calculate the maximum path sum for the current node by considering the four cases mentioned earlier.
- Line 24 updates the global `maxsum` if the calculated `maxsubtree` exceeds it.
- Line 26 returns the maximum path sum that can be obtained by including the current node.
- Line 28 calls the `dfs` function on the root node to initiate the recursive traversal.
- Line 29 returns the global `maxsum`, which now holds the maximum path sum for the entire binary tree.

### Complexity
- Time: O(N), where N is the number of nodes in the binary tree, since each node is visited once during the recursive traversal.
- Space: O(H), where H is the height of the binary tree, due to the recursive call stack. In the worst case, the binary tree is completely unbalanced (e.g., a linked list), and the space complexity is O(N). In the best case, the binary tree is completely balanced, and the space complexity is O(log N).

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common follow-up questions for this problem include:

1. How would you modify the solution to handle the case where the binary tree can contain negative values?
   - The solution already handles negative values correctly, as it calculates the maximum path sum by considering all possible cases.
2. How would you optimize the solution to reduce the space complexity?
   - The solution already has an optimal space complexity of O(H) due to the recursive call stack. However, an iterative approach could be used to reduce the space complexity to O(1), but this would come at the cost of increased code complexity.

**Core Intuition:** The algorithmic strategy used is a recursive depth-first search approach, exploring all possible paths within the binary tree and keeping track of the maximum path sum encountered. This approach works by recursively calculating the maximum path sum for each subtree and updating the global maximum path sum whenever a larger sum is found.

**Complexity Analysis:**
* Time: O(N), where N is the number of nodes in the binary tree, with justification:
  + Each node is visited once during the recursive traversal.
  + The recursive function call stack has a maximum depth of N in the worst case.
* Space: O(H), where H is the height of the binary tree, with justification:
  + The recursive call stack has a maximum depth of H.
  + In the worst case, the binary tree is completely unbalanced (e.g., a linked list), and the space complexity is O(N).

**Critical Optimizations:** The approach achieves optimal runtime boundaries, with a time complexity of O(N), but there is room for microscopic micro-optimizations, such as using an iterative approach to reduce the space complexity to O(1). However, this would come at the cost of increased code complexity.