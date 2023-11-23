"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

Category - Medium

You are given a sorted array consisting of only integers where every element
appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                r = mid
            else:
                l = mid + 2
        return nums[l]
