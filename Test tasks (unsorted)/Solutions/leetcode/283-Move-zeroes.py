"""
https://leetcode.com/problems/move-zeroes/

Category - Easy

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

# O(n^2)
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

# O(n)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_index = 0
        for i, v in enumerate(nums):
            if v != 0:
                num_index += 1
            else:
                break
        for i in range(num_index, len(nums)):
            if nums[i] != 0:
                nums[num_index], nums[i] = nums[i], nums[num_index]
                num_index += 1
        return nums
