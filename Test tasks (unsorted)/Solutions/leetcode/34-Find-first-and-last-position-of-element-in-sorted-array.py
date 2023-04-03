"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Category - Medium

Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res1 = res2 = -1
        len_nums = len(nums) - 1
        left, right = 0, len_nums
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != nums[mid]):
                res1 = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left, right = max(res1, 0), len_nums
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target and (mid == len_nums or nums[mid+1] != nums[mid]):
                res2 = mid
                break
            elif nums[mid] > target:
                right = mid - 1                
            else:
                left = mid + 1
        return [res1, res2]

"""
hint
use binary search twice
"""
