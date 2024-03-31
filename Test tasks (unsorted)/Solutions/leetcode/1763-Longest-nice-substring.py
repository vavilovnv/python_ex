"""
https://leetcode.com/problems/longest-nice-substring/

Category - Easy

A string s is nice if, for every letter of the alphabet that s contains, it
appears both in uppercase and lowercase. For example, "abABB" is nice because
'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are
multiple, return the substring of the earliest occurrence. If there are none,
return an empty string.
"""

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        letters = set(s)
        for i, v in enumerate(s):
            if v.swapcase() not in letters:
                return max(
                    self.longestNiceSubstring(s[:i]), 
                    self.longestNiceSubstring(s[i + 1:]), 
                    key=len
                )
        return s
