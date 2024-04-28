"""
https://leetcode.com/problems/alternating-digit-sum/

Category - Easy

You are given a positive integer n. Each digit of n has a sign according to
the following rules:
- The most significant digit is assigned a positive sign.
- Each other digit has an opposite sign to its adjacent digits.

Return the sum of all digits with their corresponding sign.
"""

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum([int(v) if i % 2 == 0 else -int(v) for i, v in enumerate(str(n))])
