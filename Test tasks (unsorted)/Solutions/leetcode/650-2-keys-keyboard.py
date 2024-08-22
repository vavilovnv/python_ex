"""
https://leetcode.com/problems/2-keys-keyboard/

Category - Medium

There is only one character 'A' on the screen of a notepad. You can perform
one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial
copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the
character 'A' exactly n times on the screen.
"""

class Solution:
    def minSteps(self, n: int) -> int:
        res, copy, paste = 0, 0, 1
        while paste < n:
            if n % paste == 0:
                copy = paste
                res += 1
            paste += copy
            res += 1
        return res
