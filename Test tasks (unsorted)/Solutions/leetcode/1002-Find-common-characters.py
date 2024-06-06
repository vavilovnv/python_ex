"""
https://leetcode.com/problems/find-common-characters/

Category - Easy

Given a string array words, return an array of all characters that show up in
all strings within the words (including duplicates). You may return the answer
in any order.
"""

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res, chars_count = [], reduce(lambda x, y: x & y, map(Counter, words))
        for k, v in chars_count.items():
            for _ in range(v):
                res.append(k)
        return res
