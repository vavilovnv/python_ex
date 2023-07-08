"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Category - Medium

Given an array of positive integers nums and a positive integer target, return
the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, left, total = 2 ** 32, 0, 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res if res != 2 ** 32 else 0
