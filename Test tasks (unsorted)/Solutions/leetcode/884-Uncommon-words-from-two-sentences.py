"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/

Category - Easy

A sentence is a string of single-space separated words where each word
consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and
does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You
may return the answer in any order.
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = Counter(s1.split() + s2.split())
        return [k for k, v in d.items() if v == 1]
