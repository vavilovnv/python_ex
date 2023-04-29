"""
https://leetcode.com/problems/monotonic-array/

Category - Easy

An array is monotonic if it is either monotone increasing or monotone
decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An
array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or
false otherwise.
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = nums[0] < nums[-1]
        for i in range(1, len(nums)):
            if (nums[i-1] < nums[i] and not increase
                or nums[i-1] > nums[i] and increase):
                return False
        return True
