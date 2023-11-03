"""
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

Category - Medium

Given the root of a binary tree, return the number of nodes where the value
of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and
rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def helper(self, node):
        if node is None:
            return 0, 0
        left, right  = self.helper(node.left), self.helper(node.right)
        sum_values  = left[0] + right[0] + node.val
        nodes_amount  = left[1] + right[1] + 1
        if sum_values  // nodes_amount  == node.val:
            self.res += 1
        return sum_values, nodes_amount

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res
