"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/

Category - Easy

Given the root of a binary search tree (BST) with duplicates, return all the
mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to
the node's key.
The right subtree of a node contains only nodes with keys greater than or
equal to the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: TreeNode)-> None:
            if not root: 
                return
            d[root.val]+=1
            dfs(root.left)
            dfs(root.right)
            return
        d, ans = defaultdict(int), []
        dfs(root)
        mx = max(d.values())
        return [k for k, v in d.items() if v == mx]
