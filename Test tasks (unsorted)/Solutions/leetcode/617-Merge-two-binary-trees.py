"""
https://leetcode.com/problems/merge-two-binary-trees/description/

Category - Easy

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the
two trees are overlapped while the others are not. You need to merge the two
trees into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise, the
NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root, root1, root2):
            if not root1 and not root2:
                return
            if root1 and root2:
                root.val = root1.val + root2.val
                root.left = helper(TreeNode(), root1.left, root2.left)
                root.right = helper(TreeNode(), root1.right, root2.right)
            else:
                root = root1 if root1 else root2
            return root
        return helper(TreeNode(), root1, root2)
