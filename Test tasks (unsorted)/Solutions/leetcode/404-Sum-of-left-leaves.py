"""
https://leetcode.com/problems/sum-of-left-leaves/

Category - Easy

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left
child of another node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iterative solution
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        res, stack = 0, [(root, 0)]
        while stack:
            curr, flag = stack.pop()
            if not curr.left and not curr.right:
                if flag==1:
                    res += curr.val
            if curr.right:
                stack.append((curr.right, 0))
            if curr.left:
                stack.append((curr.left, 1))
        return res

# recursive solution
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root:
                if root.left and not root.left.left and not root.left.right:
                    res.append(root.left.val)
                helper(root.left)
                helper(root.right)
        res = []
        helper(root)
        return sum(res)
