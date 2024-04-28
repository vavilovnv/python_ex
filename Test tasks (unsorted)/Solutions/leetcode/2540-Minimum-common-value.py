"""
https://leetcode.com/problems/minimum-common-value/

Category - Easy

Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
return the minimum integer common to both arrays. If there is no common
integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays
have at least one occurrence of that integer.
"""

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = set(nums2)
        for i in nums1:
            if i in nums2:
                return i
        return -1
