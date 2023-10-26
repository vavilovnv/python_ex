"""
https://leetcode.com/problems/longest-consecutive-sequence/

Category - Medium

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, s = 0, set(nums)
        for i in s:
            if (i - 1) not in s:
                j = 1
                while i + j in s:
                    j += 1
                res = max(res, j)
        return res
