"""
https://leetcode.com/problems/single-number/

Category - Easy

Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seek = {}
        for num in nums:
            if num not in seek:
                seek[num] = 1
            else:
                seek[num] += 1
        return [k for k, v in seek.items() if v == 1][0]
