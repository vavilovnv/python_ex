"""
https://leetcode.com/problems/minimum-distance-to-the-target-element/

Category - Easy

Given an integer array nums (0-indexed) and two integers target and start,
find an index i such that nums[i] == target and abs(i - start) is minimized.
Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.
"""

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float("inf")
        for i, v in enumerate(nums):
            if v == target:
                res = min(res, abs(i - start))
        return res
        
