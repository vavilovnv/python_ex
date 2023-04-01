"""
https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

Category - Easy

Given two integer arrays arr1 and arr2, and the integer d, return the distance
value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that
there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
"""

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res, len_arr2 = len(arr1), len(arr2) - 1
        for i in arr1:
            left, right = 0, len_arr2
            while left <= right:
                mid = left + (right - left) // 2
                if abs(i - arr2[mid]) <= d:
                    res -= 1
                    break
                if arr2[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1
        return res  

"""
sort arr2 and use binary search in arr2 for each element arr 1
"""
