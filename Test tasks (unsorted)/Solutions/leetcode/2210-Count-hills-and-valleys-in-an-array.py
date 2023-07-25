"""
https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

Category - Easy

You are given a 0-indexed integer array nums. An index i is part of a hill in
nums if the closest non-equal neighbors of i are smaller than nums[i].
Similarly, an index i is part of a valley in nums if the closest non-equal
neighbors of i are larger than nums[i]. Adjacent indices i and j are part of
the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a
non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.
"""

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res, prev = 0, nums[0]
        for i in range(len(nums) - 1):
            if prev == nums[i] or nums[i] == nums[i+1]:
                continue
            if (prev < nums[i] > nums[i + 1] or
                    prev > nums[i] < nums[i + 1]):
                res += 1
            prev = nums[i]
        return res
