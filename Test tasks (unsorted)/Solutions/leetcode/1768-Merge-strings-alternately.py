"""
https://leetcode.com/problems/merge-strings-alternately/

Category - Easy

You are given two strings word1 and word2. Merge the strings by adding letters
in alternating order, starting with word1. If a string is longer than the
other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_l = min(len(word1), len(word2))
        return (''.join(word1[i] + word2[i] for i in range(min_l))
                + ''.join(word1[min_l:]) + ''.join(word2[min_l:]))

