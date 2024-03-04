"""
https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

Category - Easy

Given an array of positive integers arr, find a pattern of length m that is
repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or
more values, repeated multiple times consecutively without overlapping. A
pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more
times, otherwise return false.
"""

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            if arr[i:i + m] * k == arr[i:i + m * k]:
                return True
        return False
