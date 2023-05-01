"""
https://leetcode.com/problems/maximum-average-subarray-i/

Category - Easy

You are given an integer array nums consisting of n elements, and an integer
k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error less
than 10-5 will be accepted.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[:k])
        res = temp / k
        for i in range(k, len(nums)):
            temp -= nums[i - k]
            temp += nums[i]
            res = max(res, temp / k)
        return res

"""
hint
use sliding window
"""
