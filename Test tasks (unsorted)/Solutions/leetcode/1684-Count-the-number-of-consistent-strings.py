"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/

Category - Easy

You are given a string allowed consisting of distinct characters and an array
of strings words. A string is consistent if all characters in the string
appear in the string allowed.

Return the number of consistent strings in the array words.
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            for k in word:
                if k not in allowed:
                    break
            else:
                res += 1
        return res
