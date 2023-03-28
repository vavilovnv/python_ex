"""
https://leetcode.com/problems/is-subsequence/

Category - Easy

Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, len_s = 0, len(s)
        for symbol in t:
            if symbol == s[i]:
                i += 1
                if i == len_s:
                    break
        return i == len_s

"""
hint
It is necessary to compare characters s and t while t, if true - raise i.
At the end compare i and len(s)
"""
