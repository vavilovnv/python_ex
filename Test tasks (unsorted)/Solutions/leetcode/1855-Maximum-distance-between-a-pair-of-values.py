"""
https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

Category - Medium

You are given two non-increasing 0-indexed integer arrays nums1 and nums2.

A pair of indices (i, j), where 0 <= i < nums1.length and 
0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The
distance of the pair is j - i.

Return the maximum distance of any valid pair (i, j). If there are no valid
pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every
1 <= i < arr.length.
"""

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = res = 0
        len1, len2 = len(nums1), len(nums2)
        while i < len1 and j < len2:
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res

"""
hint
use two pointers
"""
