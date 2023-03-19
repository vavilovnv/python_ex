"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Category - Easy

Given an array nums of n integers where nums[i] is in the range [1, n], return
an array of all the integers in the range [1, n] that do not appear in nums.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        return [i for i, v in enumerate(nums, 1) if v > 0]
        