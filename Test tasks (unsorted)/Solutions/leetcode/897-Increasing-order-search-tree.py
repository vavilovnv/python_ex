"""
https://leetcode.com/problems/monotonic-array/

Category - Easy

Given the root of a binary search tree, rearrange the tree in in-order so that
the leftmost node in the tree is now the root of the tree, and every node has
no left child and only one right child.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        temp = x = root
        stack, i = [], 0
        while temp or stack:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                node = stack.pop()
                if i == 0:
                    root = x = node
                    i += 1
                else:
                    x.right = node
                    x = node
                    x.left = None
                temp = node.right
        return root	
