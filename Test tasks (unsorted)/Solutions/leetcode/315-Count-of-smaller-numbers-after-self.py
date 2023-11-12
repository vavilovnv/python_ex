"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

Category - Hard

Given an integer array nums, return an integer array counts where counts[i]
is the number of smaller elements to the right of nums[i].
"""

from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result, r_nums = [0] * len(nums), [nums[len(nums) - 1]]
        for i in range(len(nums) - 2, -1, -1):
            x = bisect_left(r_nums, nums[i])
            result[i] = x
            r_nums.insert(x, nums[i])
        return result
