"""
https://leetcode.com/problems/missing-number/

Category - Easy

Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s, nums_s = 0, 0
        for i, v in enumerate(nums, 1):
            s += i
            nums_s += v
        return s - nums_s

"""
hint
calculate digits in range(1, n+1) and digits in nums, then take the diff
"""