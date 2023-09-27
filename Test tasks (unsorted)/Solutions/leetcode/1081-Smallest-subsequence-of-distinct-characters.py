"""
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Category - Medium

Given a string s, return the lexicographically smallest subsequence
of s that contains all the distinct characters of s exactly once.
"""

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        res, seen = [], set()
        d = {v: i for i, v in enumerate(s)}
        for i, v in enumerate(s):
            if v not in seen:
                while res and v < res[-1] and i < d[res[-1]]:
                    seen.discard(res.pop())
                seen.add(v)
                res.append(v)
        return "".join(res)
