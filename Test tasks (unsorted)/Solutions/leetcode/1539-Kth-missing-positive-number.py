"""
https://leetcode.com/problems/kth-missing-positive-number/

Category - Easy

Given an array arr of positive integers sorted in a strictly increasing order,
and an integer k.

Return the kth positive integer that is missing from this array.
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            miss = arr[mid] - mid - 1
            if miss >= k:
                right = mid
            else:
                left = mid + 1
        return left + k

"""
hint
if there are no missing numbers in arr, then the index of any element equals
i - 1, but if there are missing numbers in arr, then we should look for the
closest element to k, for which arr[i] - 1 - i <= k. Because arr[i] is the
index value of the element in the arr without missing elements, and i is the
index value in the arr with missing elements.
"""
