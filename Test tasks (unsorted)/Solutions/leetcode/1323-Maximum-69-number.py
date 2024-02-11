"""
https://leetcode.com/problems/decompress-run-length-encoded-list/

Category - Easy

You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes
9, and 9 becomes 6).
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        res = str(num).replace('6', '9', 1)
        return int(res)
       