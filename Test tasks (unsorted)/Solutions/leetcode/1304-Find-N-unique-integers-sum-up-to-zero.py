"""
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

Category - Easy

Given an integer n, return any array containing n unique integers such that
they add up to 0.
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [-i for i in range(n // 2, 0, -1)]
        if n % 2 != 0:
            return res + [0] + [-i for i in res]
        return res + [-i for i in res]
            