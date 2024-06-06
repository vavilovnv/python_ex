"""
https://leetcode.com/problems/house-robber-ii/

Category - Medium

You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed. All houses at this place are
arranged in a circle. That means the first house is the neighbor of the last
one. Meanwhile, adjacent houses have a security system connected, and it will
automatically contact the police if two adjacent houses were broken into on
the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            prev = prev2 = 0
            for num in nums:
                prev, prev2 = max(prev2 + num, prev), prev
            return prev
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))
