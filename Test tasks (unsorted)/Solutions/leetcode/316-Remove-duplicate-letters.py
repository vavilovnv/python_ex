"""
https://leetcode.com/problems/remove-duplicate-letters/

Category - Medium

Given a string s, remove duplicate letters so that every letter appears once
and only once. You must make sure your result is the smallest in 
lexicographical order among all possible results.
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res, seen = [], set()
        d = {v: i for i, v in enumerate(s)}
        for i, v in enumerate(s):
            if v not in seen:
                while res and v < res[-1] and i < d[res[-1]]:
                    seen.discard(res.pop())
                seen.add(v)
                res.append(v)
        return "".join(res)
