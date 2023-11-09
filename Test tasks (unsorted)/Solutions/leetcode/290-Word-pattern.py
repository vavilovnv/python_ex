"""
https://leetcode.com/problems/word-pattern/

Category - Easy

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in s.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(set(s)) == len(set(pattern)) == len(set(zip_longest(pattern, s)))
