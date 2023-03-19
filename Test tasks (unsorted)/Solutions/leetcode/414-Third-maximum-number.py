"""
https://leetcode.com/problems/third-maximum-number/

Category - Easy

Given an integer array nums, return the third distinct maximum number in this
array. If the third maximum does not exist, return the maximum number.
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        return sorted(nums, reverse=True)[:3][-1]
        