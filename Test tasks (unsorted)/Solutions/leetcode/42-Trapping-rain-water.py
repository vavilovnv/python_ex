"""
https://leetcode.com/problems/trapping-rain-water/

Category - Hard

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        len_arr = len(height) - 1
        res, max_l, max_r = 0, height[0], height[len_arr]
        left, right = 0, len_arr
        while left < right:
            if height[left] <= height[right]:
                res += max(0, max_l - height[left])
                max_l = max(max_l, height[left])
                left += 1
            else:
                res += max(0, max_r - height[right])
                max_r = max(max_r, height[right])
                right -= 1
        return res

"""
hint:
use two pointers
"""
