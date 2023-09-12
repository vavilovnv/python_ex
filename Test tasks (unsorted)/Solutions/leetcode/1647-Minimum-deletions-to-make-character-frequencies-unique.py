"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

Category - Medium

A string s is called good if there are no two different characters in s that
have the same frequency.

Given a string s, return the minimum number of characters you need to delete
to make s good.

The frequency of a character in a string is the number of times it appears in
the string. For example, in the string "aab", the frequency of 'a' is 2, while
the frequency of 'b' is 1.
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        res, freq = 0, set()
        for v in collections.Counter(s).values():
            while v in freq and v > 0:
                v -= 1
                res += 1
            freq.add(v)
        return res
