"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/

Category - Easy

Given a string s, return the length of the longest substring between two equal
characters, excluding the two characters. If there is no such substring
return -1.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        visited, res = {}, -1
        for i, c in enumerate(s):
            if c not in visited:
                visited[c] = i
            else:
                res = max(res, i - visited[c] - 1)
        return res
