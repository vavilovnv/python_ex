"""
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

Category - Easy

Given an array of positive integers arr, return the sum of all possible
odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
"""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res, arr_len = 0, len(arr)
        for i in range(arr_len):
            for j in range(i,arr_len,2):
                res += sum(arr[i:j+1])
        return res
