"""
https://leetcode.com/problems/binary-tree-preorder-traversal/

Category - Easy

Given the root of a binary tree, return the preorder traversal of its nodes'
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if root:
                res.append(root.val)
                helper(root.left)
                helper(root.right)
        res = []
        helper(root)
        return res
    
# iterative solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, temp = [], [root]
        if not root: 
            return res
        while temp:
            curr = temp.pop()
            res.append(curr.val)
            if curr.right:
                temp.append(curr.right)
            if curr.left:
                temp.append(curr.left)
        return res
