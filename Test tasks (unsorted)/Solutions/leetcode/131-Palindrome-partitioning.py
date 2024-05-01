"""
https://leetcode.com/problems/palindrome-partitioning/

Category - Medium

Given a string s, partition s such that every substring of the partition is
a palindrome. Return all possible palindrome partitioning of s.
"""

class Solution:
    @lru_cache
    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return [[]]
        res = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for suffix in self.partition(s[i:]):
                    res.append([s[:i]] + suffix)
        return res
