"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Category - Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root,p,q):
            if not root:
                return None
            if root == p or root == q:
                return root
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            if left and right:
                return root
            if not left:
                return right
            return left
        
        return helper(root, p, q)