"""
https://leetcode.com/problems/ugly-number/

Category - Easy

An ugly number is a positive integer whose prime factors are limited to 2, 3,
and 5.

Given an integer n, return true if n is an ugly number.
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for num in (2, 3, 5):
            while n % num == 0:
                n /= num
        return n == 1
