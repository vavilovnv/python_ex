"""
https://leetcode.com/problems/isomorphic-strings/

Category - Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to
get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = t[i]
            if t[i] not in dt:
                dt[t[i]] = s[i]
            if ds[s[i]] != t[i] or dt[t[i]] != s[i]:
                return False
        return True

"""
hint
Use additional structures to store maps
"""
