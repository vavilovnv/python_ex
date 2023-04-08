"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Category - Easy

Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times as it shows
in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        for num in nums2:
            if not nums1:
                break
            left, right = 0, len(nums1) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums1[mid] == num:
                    res.append(nums1.pop(mid))
                    break 
                if nums1[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        return res

"""
use binary search
"""
