"""
https://leetcode.com/problems/number-of-1-bits/

Category - Easy

Write a function that takes the binary representation of an unsigned integer
and returns the number of '1' bits it has (also known as the Hamming weight).

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

"""
hint
use the bin function to convert n in binary string
"""
