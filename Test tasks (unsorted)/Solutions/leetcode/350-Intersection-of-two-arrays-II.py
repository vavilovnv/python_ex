"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Category - Easy

Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must appear as many times as it shows
in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(x):
            left, right = 0, len(nums1) - 1
            while left <= right:
                middle = left + (right - left) // 2
                if nums1[middle] == x:
                    return middle
                if nums1[middle] < x:
                    left = middle + 1
                else:
                    right = middle - 1

        res = []
        nums1.sort()
        for num in nums2:
            if not nums1:
                break
            i = binary_search(num)
            if i is not None:
                res.append(nums1.pop(i))
        return res
