"""
https://leetcode.com/problems/largest-odd-number-in-string/

Category - Easy

You are given a string num, representing a large integer. Return the
largest-valued odd integer (as a string) that is a non-empty substring of num,
or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        res, odds = "", {"1", "3", "5", "7", "9"}
        while len(num) > 0:
            if num[-1] in odds:
                return num
            num = num[:-1]
        return res
