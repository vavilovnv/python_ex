"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Category - Medium

You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the following
definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no
next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(parent, left, right):
            if parent and left and right:
                left.next = right
                if parent.next:
                    right.next = parent.next.left
                helper(left, left.left, left.right)
                helper(right, right.left, right.right)
        if root:
            helper(root, root.left, root.right)
        return root

"""
hint
For right nodes next = parent.next.left if parent not is None
"""
