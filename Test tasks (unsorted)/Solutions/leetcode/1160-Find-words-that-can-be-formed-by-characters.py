"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

Category - Easy

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character
can only be used once).

Return the sum of lengths of all good strings in words.
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res, d = 0, Counter(chars)
        for word in words:
            if all(v <= d[k] for k, v in Counter(word).items()):
                res += len(word)
        return res
