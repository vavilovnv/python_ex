"""
https://leetcode.com/problems/binary-tree-postorder-traversal/

Category - Easy

Given the root of a binary tree, return the postorder traversal of its nodes'
values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                res.append(root.val)
        res = []
        helper(root)
        return res
