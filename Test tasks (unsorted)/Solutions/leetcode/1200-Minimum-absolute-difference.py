"""
https://leetcode.com/problems/minimum-absolute-difference/

Category - Easy

Given an array of distinct integers arr, find all pairs of elements with the
minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair
[a, b] follows
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = [
            ([arr[i-1], arr[i]], abs(arr[i] - arr[i-1]))
            for i in range(1, len(arr))
            ]
        min_res = min(res, key=lambda x: x[1])[1]
        return [i[0] for i in res if i[1] == min_res]
