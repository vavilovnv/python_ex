"""
https://leetcode.com/problems/balanced-binary-tree/

Category - Easy

Given a binary tree, determine if it is height-balanced
.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return True, 0
            left = helper(root.left)
            right = helper(root.right)
            return (left[0] and right[0] and abs(left[1] - right[1]) < 2, 
                  1 + max(left[1], right[1]))
        return helper(root)[0]

"""
hint
we need to know that root.left and root.right are balanced in height and the
difference between the heights is no more than one
"""
