"""
https://leetcode.com/problems/maximum-ascending-subarray-sum/

Category - Easy

Given an array of positive integers nums, return the maximum possible sum of
an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is
ascending.
"""

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, temp = 0, nums[0]
        for i, v in enumerate(nums[1:], 1):
            if v > nums[i-1]:
                temp += v
            else:
                res = max(res, temp)
                temp = v
        return max(res, temp)
