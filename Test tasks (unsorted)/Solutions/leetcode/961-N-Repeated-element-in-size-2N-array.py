"""
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

Category - Easy

You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        for k, v in Counter(nums).items():
            if v == n:
                return k
            