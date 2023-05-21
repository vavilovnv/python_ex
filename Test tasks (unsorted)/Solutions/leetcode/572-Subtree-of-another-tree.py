"""
https://leetcode.com/problems/subtree-of-another-tree/

Category - Easy

Given the roots of two binary trees root and subRoot, return true if there is
a subtree of root with the same structure and node values of subRoot and
false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and
all of this node's descendants. The tree tree could also be considered as a
subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return (is_same_tree(root1.left, root2.left) 
                    and is_same_tree(root1.right, root2.right))
        
        if not root:
            return False
        if is_same_tree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) 
                or self.isSubtree(root.right, subRoot))

"""
hint
helper is solution task # 100 Same tree
"""
