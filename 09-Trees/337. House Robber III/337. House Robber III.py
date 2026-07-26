1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        def dfs(node):
10            if node is None:
11                return [0,0]
12            left=dfs(node.left)
13            right=dfs(node.right)
14
15            return [left[1]+right[1]+node.val,max(left)+max(right)]
16
17        return max(dfs(root))