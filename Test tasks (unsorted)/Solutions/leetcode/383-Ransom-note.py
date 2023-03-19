"""
https://leetcode.com/problems/ransom-note/

Category - Easy

Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)
        for s in ransomNote:
            if s not in d or d[s] - 1 < 0:
                return False
            d[s] -= 1
        return True
