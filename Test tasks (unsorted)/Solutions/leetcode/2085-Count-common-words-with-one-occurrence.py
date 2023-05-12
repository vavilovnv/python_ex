"""
https://leetcode.com/problems/count-common-words-with-one-occurrence/

Category - Easy

Given two string arrays words1 and words2, return the number of strings that
appear exactly once in each of the two arrays.
"""

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res, d1, d2 = 0, Counter(words1), Counter(words2)
        for k, v in d1.items():
            if v == 1 and d2.get(k, 0) == 1:
                res += 1
        return res
