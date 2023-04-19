"""
https://leetcode.com/problems/binary-tree-paths/

Category - Easy

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, path):
            if not root.left and not root.right:
                res.append(path)
            if root.left:
                helper(root.left, f'{path}->{root.left.val}')
            if root.right:
                helper(root.right, f'{path}->{root.right.val}')
        res = []
        helper(root, str(root.val))
        return res 
