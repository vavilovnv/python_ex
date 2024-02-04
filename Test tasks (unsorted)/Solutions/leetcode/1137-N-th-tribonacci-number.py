"""
https://leetcode.com/problems/n-th-tribonacci-number/

Category - Easy

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    d = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n < 3:
            return self.d[n]
        for i in range(1, 4):
            if n - i not in self.d:
                self.d[n - i] = self.tribonacci(n - i)
        self.d[n] = self.d[n - 1] + self.d[n - 2] + self.d[n - 3]
        return self.d[n]
