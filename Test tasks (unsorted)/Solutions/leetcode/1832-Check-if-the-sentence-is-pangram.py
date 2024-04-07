"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/

Category - Easy

A pangram is a sentence where every letter of the English alphabet appears at
least once.

Given a string sentence containing only lowercase English letters, return true
if sentence is a pangram, or false otherwise.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
