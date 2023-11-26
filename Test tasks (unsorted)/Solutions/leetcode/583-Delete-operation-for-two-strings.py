"""
https://leetcode.com/problems/delete-operation-for-two-strings/

Category - Medium

Given two strings word1 and word2, return the minimum number of steps required
to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        lst = [0] * (len(word2) + 1)    
        d = defaultdict(list)
        for i, c in enumerate(word2):
            d[c].append(i)
        for c in word1:
            for i in reversed(d[c]):
                lst[i + 1] = max(lst[:i + 1]) + 1
        return len(word1) + len(word2) - 2 * max(lst)
