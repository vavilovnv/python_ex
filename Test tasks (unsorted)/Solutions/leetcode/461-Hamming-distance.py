"""
https://leetcode.com/problems/hamming-distance/

Category - Easy

The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a, b, res = format(x, '0b'), format(y, '0b'), 0
        len_a, len_b = len(a), len(b)
        if len_a < len_b:
            a = '0' * (len_b - len_a) + a
        else:
            b = '0' * (len_a - len_b) + b
        for i in range(max(len_a, len_b)):
            if a[i] != b[i]:
                res += 1
        return res

"""
hint
use format(a, '0b'), not bin(a) to add prefix '0' * diff(len_a, len_b)
"""
        