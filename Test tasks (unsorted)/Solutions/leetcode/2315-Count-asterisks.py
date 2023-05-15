"""
https://leetcode.com/problems/count-asterisks/

Category - Easy

You are given a string s, where every two consecutive vertical bars '|' are
grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd
and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.
"""

class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        for i in [v for i, v in enumerate(s.split('|')) if i % 2 == 0]:
            res += i.count('*')
        return res
