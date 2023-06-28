"""
https://leetcode.com/problems/neither-minimum-nor-maximum/

Category - Easy

Given an integer array nums containing distinct positive integers, find and
return any number from the array that is neither the minimum nor the maximum
value in the array, or -1 if there is no such number.

Return the selected integer.
"""

# TC: O(n) SC: O(1)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)
        for i in nums:
            if i != mn and i != mx:
                return i
        return -1
