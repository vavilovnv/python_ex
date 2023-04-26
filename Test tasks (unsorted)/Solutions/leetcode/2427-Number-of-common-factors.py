"""
https://leetcode.com/problems/number-of-common-factors/

Category - Easy

Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.
"""

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                res +=1
        return res
