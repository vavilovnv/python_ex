"""
https://leetcode.com/problems/valid-mountain-array/

Category - Easy

Given an array of integers arr, return true if and only if it is a valid
mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        up, changed = True, arr[0] > arr[1]
        for i in range(1, len(arr) - 1):
            if (arr[i] == arr[i + 1] 
                or up and changed and arr[i] > arr[i + 1]
                or not up and changed and arr[i] < arr[i + 1]):
                return False
            if up and arr[i] > arr[i + 1] and not changed:
                up, changed = False, True
        return not up
            