"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Category - Medium

Given the root of a binary tree, return the zigzag level order traversal of
its nodes' values. (i.e., from left to right, then right to left for the next
level and alternate between).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        dq, to_right = deque([root]), True
        while dq:
            len_dq, temp, sub_dq = len(dq), [], deque([])
            for _ in range(len_dq):
                if v := dq.popleft() if to_right else dq.pop():
                    temp.append(v.val)
                    if to_right:
                        sub_dq.append(v.left)
                        sub_dq.append(v.right)
                    else:
                        sub_dq.appendleft(v.right)
                        sub_dq.appendleft(v.left)
            if temp:
                res.append(temp)
            for v in sub_dq:
                 dq.append(v)
            to_right = not to_right
        return res
