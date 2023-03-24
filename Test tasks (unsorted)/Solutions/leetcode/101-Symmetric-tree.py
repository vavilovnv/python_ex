"""
https://leetcode.com/problems/symmetric-tree/

Category - Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (node1.val == node2.val 
                    and helper(node1.left, node2.right) 
                    and helper(node1.right, node2.left))
        
        return helper(root, root)

"""
hint
divide the tree into two parts and compare the left node with the right one
and vice versa
"""
