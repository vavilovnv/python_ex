"""
https://leetcode.com/problems/divide-array-into-equal-pairs/

Category - Easy

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
"""

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all([v % 2 == 0 for v in Counter(nums).values()])
