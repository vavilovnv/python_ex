"""
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

Category - Easy

You are given two strings s1 and s2 of equal length. A string swap is an
operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most
one string swap on exactly one of the strings. Otherwise, return false.
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        count = 0
        for i, j in zip(s1, s2):
            if i != j:
                count += 1
            if count > 2:
                return False
        return sorted(s1) == sorted(s2)
