"""
https://leetcode.com/problems/three-consecutive-odds/

Category - Easy

Given an integer array arr, return true if there are three consecutive odd
numbers in the array. Otherwise, return false.
"""

# TC: O(n) SC: O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        res = 0
        for num in arr:
            if num % 2 == 0:
                res = 0
            else:
                res += 1
            if res == 3:
                return True
        return False
