"""
https://leetcode.com/problems/climbing-stairs/

Category - Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        i, a, b = 0, 0, 1
        while i < n:
            a, b = b, a + b
            i += 1
        return b
