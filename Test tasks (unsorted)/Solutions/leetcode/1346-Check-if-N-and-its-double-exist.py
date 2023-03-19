"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/

Category - Easy

Given an array arr of integers, check if there exist two indices i and j such
that:
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, v in enumerate(arr):
            for j, v2 in enumerate(arr):
                if i != j and 2 * v == v2:
                    return True
        return False
            