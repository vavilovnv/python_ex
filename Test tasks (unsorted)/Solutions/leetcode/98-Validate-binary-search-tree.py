"""
https://leetcode.com/problems/merge-sorted-array/

Category - Medium

Given the root of a binary tree, determine if it is a valid binary search
tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the
node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return (helper(node.left, low, node.val) 
            and helper(node.right, node.val, high))
        return helper(root, pow(-2, 31) - 1, pow(2, 31))

"""
hint
Use helper! Without this we need extra checks that the left/right node is
not None
"""
