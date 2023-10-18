"""
https://leetcode.com/problems/divide-two-integers/

Category - Medium

Given two integers dividend and divisor, divide two integers without using
multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its
fractional part. For example, 8.345 would be truncated to 8, and -2.7335
would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem,
if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and
if the quotient is strictly less than -2^31, then return -2^31.
"""

class Solution:
    def output_n(self, n: int) -> int:
        if n > (2**31 - 1):
            return 2**31 - 1
        if n < -(2**31):
            return -(2**31)
        return n
                
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0
        n, dividend, divisor = 0, abs(dividend), abs(divisor)
        if divisor == 1:
            return self.output_n(-dividend) if is_negative else self.output_n(dividend)
        if dividend == divisor:
            return -1 if is_negative else 1
        if dividend < divisor:
            return n
        len_dr = len(str(divisor))
        s = str(dividend)
        while int(s) > divisor:
            i = len_dr + 1 if int(s[:len_dr]) < divisor else len_dr
            dividend = int(s[:i])
            s = s[i:]
            zeros = ''.join(['0' for _ in range(len(s))])
            while dividend - divisor >= 0:
                n += int(str(1) + zeros)
                dividend -= divisor
            s = str(dividend) + s    
        return self.output_n(-n) if is_negative else self.output_n(n)
