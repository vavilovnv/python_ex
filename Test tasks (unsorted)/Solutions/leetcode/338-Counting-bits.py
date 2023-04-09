"""
https://leetcode.com/problems/counting-bits/

Category - Easy

Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            res.append(count)
        return res
