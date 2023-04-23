"""
https://leetcode.com/problems/relative-sort-array/

Category - Easy

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all
elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are
the same as in arr2. Elements that do not appear in arr2 should be placed at
the end of arr1 in ascending order.
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res, d = [], Counter(arr1)
        for i in arr2:
            for _ in range(d[i]):
                res.append(i)
            d.pop(i)
        for k in sorted(d):
            for _ in range(d[k]):
                res.append(k)
        return res
