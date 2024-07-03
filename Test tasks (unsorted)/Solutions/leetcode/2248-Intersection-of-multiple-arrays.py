"""
https://leetcode.com/problems/intersection-of-multiple-arrays/

Category - Easy

Given a 2D integer array nums where nums[i] is a non-empty array of distinct
positive integers, return the list of integers that are present in each array
of nums sorted in ascending order.
"""

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for row in nums[1:]:
            res &= set(row)
        return sorted(list(res))
