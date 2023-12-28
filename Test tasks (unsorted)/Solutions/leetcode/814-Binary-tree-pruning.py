"""
https://leetcode.com/problems/binary-tree-pruning/

Category - Medium

Given the root of a binary tree, return the same tree where every subtree (of
the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        if root.left or root.right or root.val == 1:
            return root 
        else:
            return None
