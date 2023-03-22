"""
https://leetcode.com/problems/maximum-subarray/

Category - Medium

Given an integer array nums, find the subarray with the largest sum, and
return its sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, s = nums[0], 0
        for num in nums:
            if s < 0:
                s = 0
            s += num
            res = max(res, s)
        return res

"""
hint
if s < 0 - it's bad sequence. take the max from all s =)
"""
