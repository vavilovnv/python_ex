"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/

Category - Easy

Given the root of a binary tree, return the average value of the nodes on each
level in the form of an array. Answers within 10-5 of the actual answer will
be accepted.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def helper(root, level):
            if root:
                if level not in d:
                    d[level] = []    
                d[level].append(root.val)
                helper(root.left, level + 1)
                helper(root.right, level + 1)
        d, level = {}, 0
        helper(root, level)
        return [sum(v)/len(v) for v in d.values()]

# iterative solution
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q, res = deque([root]), []
        while q:
            n, level_sum = len(q), 0
            for _ in range(n):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum / n)
        return res
