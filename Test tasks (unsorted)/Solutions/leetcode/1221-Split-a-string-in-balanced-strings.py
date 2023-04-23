"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/

Category - Easy

Balanced strings are those that have an equal quantity of 'L' and 'R'
characters.

Given a balanced string s, split it into some number of substrings such
that:
Each substring is balanced.

Return the maximum number of balanced strings you can obtain.
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = count_r = count_l = 0
        for i in s:
            if i == 'R':
                count_r += 1
            else:
                count_l += 1
            if count_r == count_l:
                res += 1
                count_r = count_l = 0
        return res
