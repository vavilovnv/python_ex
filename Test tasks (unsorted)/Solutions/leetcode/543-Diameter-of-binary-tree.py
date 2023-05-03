"""
https://leetcode.com/problems/diameter-of-binary-tree/

Category - Easy

Given the root of a binary tree, return the length of the diameter of the
tree.

The diameter of a binary tree is the length of the longest path between any
two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1
        helper(root)
        return self.res
      