"""
https://leetcode.com/problems/integer-break/

Category - Easy

Given an integer n, break it into the sum of k positive integers, where 
k >= 2, and maximize the product of those integers.

Return the maximum product you can get.
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        if n % 3 == 0:
            return 3 ** (n // 3) 
        if n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4 
        return 3 ** (n // 3) * 2
