"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Category - Easy

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return
        mid = n // 2
        node = TreeNode()
        node.val = nums[mid]
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        return node

"""
hint
Since nums is a sorted list, the middle element nums[len(nums)//2] must be the
root node of nums. And so on...
"""
