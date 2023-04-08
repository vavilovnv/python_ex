"""
https://leetcode.com/problems/power-of-two/

Category - Easy

Given an integer n, return true if it is a power of two. Otherwise, return
false.

An integer n is a power of two, if there exists an integer x such that
n == 2^x.
"""

# recursive solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 2:
            if n in [1, 2]:
                return True
            else:
                return False
        return self.isPowerOfTwo(n / 2)


# O(log n) solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n < 0 else bin(n).count('1') == 1

"""
hint
n == 2^x always has exactly one 1 in the bin str
"""