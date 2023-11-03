"""
https://leetcode.com/problems/binary-tree-right-side-view/

Category - Medium

Given the root of a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, max_l = [], [0]

        def helper(root, lvl, max_l) -> None:
            if root is None:
                return None
            if max_l[0] < lvl:
                res.append(root.val)
                max_l[0] = lvl
            helper(root.right, lvl + 1, max_l)
            helper(root.left, lvl + 1, max_l)
        
        helper(root, 1, max_l)
        return res
