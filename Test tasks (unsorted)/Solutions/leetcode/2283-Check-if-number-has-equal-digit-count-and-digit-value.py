"""
https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

Category - Easy

You are given a 0-indexed string num of length n consisting of digits.

Return true if for every index i in the range 0 <= i < n, the digit i occurs
num[i] times in num, otherwise return false.
"""

class Solution:
    def digitCount(self, num: str) -> bool:
        return all([num.count(str(i)) == int(v) for i, v in enumerate(num)])
