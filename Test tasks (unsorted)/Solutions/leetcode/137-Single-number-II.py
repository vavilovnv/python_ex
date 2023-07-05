"""
https://leetcode.com/problems/single-number-ii/

Category - Medium

Given an integer array nums where every element appears three times except for
one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only
constant extra space.
"""

# Complexity O(n), memory O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [k for k, v in Counter(nums).items() if v == 1][0]
    
# Complexity O(n), memory O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res, cap = 0, 2 ** 32
        for i in range(32):
            bit_sum = 0
            for num in nums:
                if num < 0:
                    num = num & (cap - 1)
                bit_sum += (num >> i) & 1
            bit_sum %= 3
            res |= bit_sum << i
        if res >= 2 ** 31:
            res -= cap
        return res
