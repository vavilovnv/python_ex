"""
https://leetcode.com/problems/number-of-matching-subsequences/

Category - Medium

Given a string s and an array of strings words, return the number of words[i]
that is a subsequence of s.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative
order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
"""

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        for element, count in Counter(words).items():
            finded, i = True, 0
            for c in element:
                i = s.find(c, i) + 1
                if i == 0:
                    finded = False
                    break
            if finded:
                result += count
        return result
