"""
https://leetcode.com/problems/same-tree/

Category - Easy

Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# cheating solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return hash(str(p)) == hash(str(q))
    
# recursive solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val 
                and self.isSameTree(p.left, q.left) 
                and self.isSameTree(p.right, q.right))
    
# iterative solution, bfs, TC: O(n) SC: O(1)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([p, q])
        while queue:
            p = queue.popleft()
            q = queue.popleft()
            if not p and not q:
                continue
            if not p or not q:
                return False            
            if p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)
        return True
