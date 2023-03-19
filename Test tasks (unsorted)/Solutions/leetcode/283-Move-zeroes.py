"""
https://leetcode.com/problems/move-zeroes/

Category - Easy

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == 0:
                nums.pop(left)
                nums.append(0)
                right -= 1
            else:
                left += 1
