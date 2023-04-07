"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/

Category - Easy

Given an array arr of integers, check if there exist two indices i and j such
that:
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
"""

# O(nlog(n))
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr) - 1
        for i, v in enumerate(arr):
            left, right = 0, n
            while left <= right:
                mid = left + (right - left) // 2
                if v == 2 * arr[mid] and i != mid:
                    return True
                if v > 2 * arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

# O(n^2)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, v in enumerate(arr):
            for j, v2 in enumerate(arr):
                if i != j and 2 * v == v2:
                    return True
        return False

"""
hint
use binary search
"""            
