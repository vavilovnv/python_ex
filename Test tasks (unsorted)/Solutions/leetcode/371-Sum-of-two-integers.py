"""
https://leetcode.com/problems/sum-of-two-integers/

Category - Medium

Given two integers a and b, return the sum of the two integers without using
the operators + and -.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b & mask) > 0:
            carry = a ^ b
            b = (a & b) << 1
            a = carry
        return (a & mask) if b > 0 else a
