"""
https://leetcode.com/problems/arranging-coins/

Category - Medium

Given an integer array nums of length n where all the integers of nums are in
the range [1, n] and each integer appears once or twice, return an array of
all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant
extra space.
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        return res
        