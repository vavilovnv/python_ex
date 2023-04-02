"""
https://leetcode.com/problems/sqrtx/description/

Category - Easy

Given a non-negative integer x, return the square root of x rounded down to
the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

"""
hint
use binary search
"""
