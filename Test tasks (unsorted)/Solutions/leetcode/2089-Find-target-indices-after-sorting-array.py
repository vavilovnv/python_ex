"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/

Category - Easy

You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in
non-decreasing order. If there are no target indices, return an empty list.
The returned list must be sorted in increasing order.
"""

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, v in enumerate(sorted(nums)) if v == target]
