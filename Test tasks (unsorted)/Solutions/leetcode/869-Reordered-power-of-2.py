"""
https://leetcode.com/problems/reordered-power-of-2/

Category - Medium

You are given an integer n. We reorder the digits in any order (including the
original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a
power of two.
"""

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n1 = Counter(str(n))
        for i in range(30):
            n2 = Counter(str(2 ** i))
            if n1 == n2 :
                return True
        return False
