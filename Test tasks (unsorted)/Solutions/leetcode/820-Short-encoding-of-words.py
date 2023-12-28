"""
https://leetcode.com/problems/short-encoding-of-words/

Category - Medium

A valid encoding of an array of words is any reference string s and array of
indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up
to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s
possible of any valid encoding of words.
"""

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        result, s = 0, set(words)
        for word in words:
            for i in range(1, len(word)):
                if word[i:] in s:
                    s.discard(word[i:])
        return sum([len(word) for word in s]) + len(s)
