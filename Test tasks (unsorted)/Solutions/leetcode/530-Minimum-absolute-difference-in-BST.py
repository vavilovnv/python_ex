"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Category - Easy

Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(nlogn) SC: O(n)
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res, q = [], deque([root])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.sort()
        return min([res[i] - res[i-1] for i in range(1, len(res))])

# TC: O(n) SC: O(n)
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        res = []
        helper(root)
        return min([res[i] - res[i-1] for i in range(1, len(res))])
      