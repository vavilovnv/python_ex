"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

Category - Easy

Given the root of an n-ary tree, return the preorder traversal of its
nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(reversed(node.children))
        return res

"""
hint
use the stack and the inverted list of child nodes to add nodes to the stack
"""
