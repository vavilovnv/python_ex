"""
https://leetcode.com/problems/number-of-good-pairs/

Category - Easy

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

# TC: O(n^2) SC: O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i, v in enumerate(nums):
            for j in range(i, len(nums)):
                if v == nums[j] and i < j:
                    res += 1
        return res

# TC: O(n) SC: O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res, d = 0, {}
        for i in nums:
            if i in d:
                res += d[i]
                d[i] += 1
            else:
                d[i] = 1
        return res
