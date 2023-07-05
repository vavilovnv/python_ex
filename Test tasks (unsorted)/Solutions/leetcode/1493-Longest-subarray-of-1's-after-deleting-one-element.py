"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Category - Medium

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the
resulting array. Return 0 if there is no such subarray.
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = left = count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left)
        return res
