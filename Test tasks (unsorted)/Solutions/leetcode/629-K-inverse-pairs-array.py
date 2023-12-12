"""
https://leetcode.com/problems/k-inverse-pairs-array/

Category - Hard

For an integer array nums, an inverse pair is a pair of integers [i, j] where
0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of
numbers from 1 to n such that there are exactly k inverse pairs. Since the
answer can be huge, return it modulo 109 + 7.
"""

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        d = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        d[0][0], m = 1, 10 ** 9 + 7
        for i in range(1, n + 1):
            s = 0
            for j in range(k + 1):
                s += d[i - 1][j]
                if j >= i:
                    s -= d[i - 1][j - i]
                d[i][j] = (d[i][j] + s) % m
        return d[n][k]
