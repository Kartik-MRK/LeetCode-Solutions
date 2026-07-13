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
30
31        