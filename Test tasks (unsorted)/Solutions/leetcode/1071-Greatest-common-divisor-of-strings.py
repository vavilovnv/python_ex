"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/

Category - Easy

For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x
divides both str1 and str2.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        len1, len2 = len(str1), len(str2)
        if len1 < len2:
            len1, len2 = len2, len1
        while len2:
            len1, len2 = len2, len1 % len2
        return str2[:len1]
