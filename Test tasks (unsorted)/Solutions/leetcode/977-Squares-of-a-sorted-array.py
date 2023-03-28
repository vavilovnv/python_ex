"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Category - Easy

Given an integer array nums sorted in non-decreasing order, return an array of
the squares of each number sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res, left, right = [], 0, len(nums) - 1
        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        return res[::-1]
        
# cheating solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(i ** 2 for i in nums)
