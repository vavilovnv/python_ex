"""
https://leetcode.com/problems/sort-array-by-increasing-frequency/

Category - Easy

Given an array of integers nums, sort the array in increasing order based on
the frequency of the values. If multiple values have the same frequency, sort
them in decreasing order.

Return the sorted array.
"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        return sorted(nums, key=lambda x: (d[x], -x))
