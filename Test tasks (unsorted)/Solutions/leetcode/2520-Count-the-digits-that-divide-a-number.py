"""
https://leetcode.com/problems/count-the-digits-that-divide-a-number/

Category - Easy

Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.
"""

class Solution:
    def countDigits(self, num: int) -> int:
        return len([i for i in str(num) if num % int(i) == 0])
