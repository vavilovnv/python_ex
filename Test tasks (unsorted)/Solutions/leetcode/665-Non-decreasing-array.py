"""
https://leetcode.com/problems/non-decreasing-array/

Category - Medium

Given an array nums with n integers, your task is to check if it could become
non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every
i (0-based) such that (0 <= i <= n - 2).
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        sorted_nums, modifying, n = 0, 0, len(nums)
        if n <= 2:
            return True
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                modifying += 1
                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
            else:
                sorted_nums += 1  
        if modifying == 1 or sorted_nums == n - 1:
            return True
        return False
