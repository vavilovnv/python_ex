"""
https://leetcode.com/problems/permutation-in-string/

Category - Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of s1's permutations is the substring of
s2.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, target = len(s1), Counter(s1)
        for i in range(len(s2)):
            if target == Counter(s2[i:i + len_s1]):
                return True
        return False

"""
hint
we can use sorted instead of Counter
"""
