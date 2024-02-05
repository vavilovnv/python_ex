"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Category - Easy

Given a string s, find the first non-repeating character in it and return its
index. If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for i, v in enumerate(s):
            if d[v] == 1:
                return i
        return -1
