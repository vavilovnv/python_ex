"""
https://leetcode.com/problems/add-strings/

Category - Easy

Given two non-negative integers, num1 and num2 represented as string, return
the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling
large integers (such as BigInteger). You must also not convert the inputs to
integers directly.
"""

sys.set_int_max_str_digits(68000)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x = y = 0
        for c in num1:
            x = x * 10 + ord(c) - ord('0')
        for c in num2:
            y = y * 10 + ord(c) - ord('0')
        return str(x + y)
