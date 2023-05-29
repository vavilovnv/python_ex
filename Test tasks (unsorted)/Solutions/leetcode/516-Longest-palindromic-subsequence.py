"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Category - Medium

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements.
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        res = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for left in range(n):
            for right in range(n, 0, -1):
                if s[left] == s[right - 1]:
                    scores = res[left][right] + 1
                else:
                    scores =  max(res[left + 1][right], res[left][right - 1])
                res[left + 1][right - 1] = scores
        return res[n][0] 
        