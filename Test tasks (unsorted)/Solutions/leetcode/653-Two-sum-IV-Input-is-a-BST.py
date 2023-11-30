"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Category - Easy

Given the root of a binary search tree and an integer k, return true if there
exist two elements in the BST such that their sum is equal to k, or false
otherwise.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes, num_cache = [root], set()
        for node in nodes:
            if k - node.val in num_cache: 
                return True
            num_cache.add(node.val)
            if node.left: 
                nodes.append(node.left)
            if node.right: 
                nodes.append(node.right)
        return False
