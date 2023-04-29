"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

Category - Easy

Given the root of a binary tree, return the inorder traversal of its nodes'
values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        res = []
        helper(root)
        return res

# iterative solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack, curr = [], [], root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
