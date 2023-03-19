"""
https://leetcode.com/problems/reverse-integer/

Category - Easy

Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or
unsigned).
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            value = -int(''.join(list(str(x)[1:])[::-1]))
        else:
            value = int(''.join(list(str(x))[::-1]))
        return value if -2 ** 31 <= value <= 2 ** 31 - 1 else 0
