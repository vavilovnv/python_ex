"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Category - Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes in the sequence has an edge connecting them. A node can only appear
in the sequence at most once. Note that the path does not need to pass
through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any
non-empty path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]    

        def dfs(node):
            if not node:
                return 0
            
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            res[0] = max(res[0], node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]
