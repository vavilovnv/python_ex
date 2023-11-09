"""
https://leetcode.com/problems/longest-increasing-subsequence/

Category - Medium

Given an integer array nums, return the length of the longest strictly
increasing subsequence.
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res, tails = 0, [0] * len(nums)
        for num in nums:
            left, right = 0, res
            while left != right:
                mid = left + (right - left) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            res = max(res, left + 1)
            tails[left] = num
        return res
