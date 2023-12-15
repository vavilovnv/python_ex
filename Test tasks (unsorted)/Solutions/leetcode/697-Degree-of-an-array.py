"""
https://leetcode.com/problems/degree-of-an-array/

Category - Easy

Given a non-empty array of non-negative integers nums, the degree of this
array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray
of nums, that has the same degree as nums.
"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        l, r, amounts = {}, {}, {} 
        for i, num in enumerate(nums):
            if num not in l:
                l[num] = i
            r[num], amounts[num] = i, amounts.get(num, 0) + 1
        deegre, res = max(amounts.values()), len(nums)
        for num, count in amounts.items():
            if count == deegre:
                res = min(res, r[num] - l[num] + 1)
        return res
