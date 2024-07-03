"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Category - Easy

Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times as it shows
in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res, i, j = [], 0, 0
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
