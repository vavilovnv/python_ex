"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

Category - Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

# TC: O(nlog(m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = sorted(nums1 + nums2)
        len_lst = len(lst)
        if len_lst % 2 == 0:
            return (lst[(len_lst // 2) - 1] + lst[len_lst // 2]) / 2
        else:
            return lst[len_lst // 2]
        
# TC: O(log(m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            if partitionX == 0:
                maxX = float('-inf') 
            else: 
                maxX = nums1[partitionX - 1]
            if partitionY == 0:
                maxY = float('-inf')  
            else:
                maxY = nums2[partitionY - 1]
            if partitionX == m:
                minX = float('inf') 
            else:
                minX = nums1[partitionX]
            if partitionY == n:
                minY = float('inf') 
            else:
                minY = nums2[partitionY]
            if maxX <= minY and maxY <= minX:
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1
