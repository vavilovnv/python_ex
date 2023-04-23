"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Category - Easy

Given the array nums, for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i] you have to count the number of
valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i, v in enumerate(sorted(nums)):
            if v not in d:
                d[v] = i
        return [d[i] for i in nums]
