"""
https://leetcode.com/problems/unique-number-of-occurrences/

Category - Easy

Given an array of integers arr, return true if the number of occurrences of
each value in the array is unique or false otherwise.
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        return len(set(d.values())) == len(d)
