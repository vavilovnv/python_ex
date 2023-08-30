"""
https://leetcode.com/problems/strictly-palindromic-number/

Category - Medium

An integer n is strictly palindromic if, for every base b between 2 and n - 2
(inclusive), the string representation of the integer n in base b is
palindromic.

Given an integer n, return true if n is strictly palindromic and false
otherwise.

A string is palindromic if it reads the same forward and backward.
"""

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def get_base(x, b):
            res = []
            while x > 0:
                res.append(str(x % b))
                x //= b
            return int("".join(res[::-1]))
        
        for i in range(2, n-1):
            if get_base(n, i) != n:
                return False
        return True

# =)
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
