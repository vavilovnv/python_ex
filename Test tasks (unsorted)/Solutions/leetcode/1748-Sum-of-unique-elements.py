"""
https://leetcode.com/problems/sum-of-unique-elements/

Category - Easy

You are given an integer array nums. The unique elements of an array are the
elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([k for k, v in Counter(nums).items() if v == 1])
