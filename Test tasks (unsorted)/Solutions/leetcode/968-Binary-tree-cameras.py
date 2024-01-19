"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Category - Hard

You are given the root of a binary tree. We install cameras on the tree nodes
where each camera at a node can monitor its parent, itself, and its immediate
children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def find_camera(node, parent):
            c = 0
            if node:
                c = find_camera(node.left, node) + find_camera(node.right, node)
                added = False
                if node.left not in stack:
                    stack.add(node.left)
                    added = True
                if node.right not in stack:    
                    stack.add(node.right)
                    added = True
                if added:
                    stack.add(parent)
                    stack.add(node)
                    c += 1
                return c
            return 0
        
        stack = {None}
        с = find_camera(root, None)
        return [с + 1, с][root in stack]
