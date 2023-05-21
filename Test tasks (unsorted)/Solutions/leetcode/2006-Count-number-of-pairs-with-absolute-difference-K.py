"""
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

Category - Easy

Given an integer array nums and an integer k, return the number of pairs
(i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
"""

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res, d = 0, Counter(nums)
        for num in nums:
            if num + k in d:
                res += d[num + k]
        return res
