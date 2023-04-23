"""
https://leetcode.com/problems/find-greatest-common-divisor-of-array/

Category - Easy

Given an integer array nums, return the greatest common divisor of the
smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer
that evenly divides both numbers.
"""

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        for i in range(min_num, 0, -1):
            if min_num % i == 0 and max_num % i == 0:
                return i
