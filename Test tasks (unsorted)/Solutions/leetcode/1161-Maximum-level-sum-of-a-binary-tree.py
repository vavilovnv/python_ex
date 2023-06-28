"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Category - Medium

Given the root of a binary tree, the level of its root is 1, the level of its
children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at
level x is maximal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res, level, max, d = 1, 0, root.val, deque([root])
        while d:
            level += 1
            s, temp = 0, deque([])
            while d:
                node = d.pop()
                s += node.val
                temp.append(node)
            if s > max:
                res = level
                max = s
            for node in temp:
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return res