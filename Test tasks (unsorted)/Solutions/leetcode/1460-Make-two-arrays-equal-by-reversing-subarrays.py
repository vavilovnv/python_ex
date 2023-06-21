"""
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

Category - Easy

You are given two integer arrays of equal length target and arr. In one step,
you can select any non-empty subarray of arr and reverse it. You are allowed
to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
"""

# O(nlogn) SC: O(1)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

# O(n) SC: O(1)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
