"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

Category - Easy

A sequence of numbers is called an arithmetic progression if the difference
between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to
form an arithmetic progression. Otherwise, return false.
"""

# TC: O(nlogn) SC: O(1)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        x = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != x:
                return False
        return True
