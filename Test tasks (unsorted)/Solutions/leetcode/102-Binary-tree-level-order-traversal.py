"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Category - Medium

Given the root of a binary tree, return the level order traversal of its 
nodes' values. (i.e., from left to right, level by level).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive solution
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, level):
            if not node:
                return []
            if level not in result:
                result[level] = []
            result[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        result = {}
        helper(root, 0)
        return result.values()

    # iterative solution
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, stack = [], [[root]]
        while stack:
            nodes = stack.pop()
            values, arr_nodes = [], []
            for node in nodes:
                values.append(node.val)
                if node.left:
                    arr_nodes.append(node.left)
                if node.right:
                    arr_nodes.append(node.right)
            res.append(values)
            if arr_nodes:
                stack.append(arr_nodes)
        return res

"""
hint
for iterative solution use stack
"""
