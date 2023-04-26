"""
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

Category - Easy

Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number
of occurrences (i.e., the same frequency).
"""

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = Counter(s)
        return all([v == d[s[0]] for v in d.values()])
