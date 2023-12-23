"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Category - Easy

Given the root of a Binary Search Tree (BST), return the minimum difference
between the values of any two different nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lst = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        dfs(root)
        res = max(lst)
        for i in range(1, len(lst)):
            res = min(res, lst[i] - lst[i-1])
        return res
