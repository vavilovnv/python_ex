"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/

Category - Easy

Given the root of an n-ary tree, return the postorder traversal of its
nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(root):
            if root:
                for children in root.children:
                    helper(children)
                res.append(root.val)
        res = []
        helper(root)
        return res
