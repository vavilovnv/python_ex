"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Category - Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if not left:
                return 1 + right
            if not right:
                return 1 + left
            return 1 + min(left, right)
        return helper(root)
