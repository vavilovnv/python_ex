"""
https://leetcode.com/problems/remove-element/

Category - Easy

Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1

"""
hint
cheating solution is:
return haystack.find(needle)
"""
