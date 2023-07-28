"""
https://leetcode.com/problems/powx-n/

Category - Medium

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
"""

# Slow but easy solution =)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == -1:
            return 1 / x
        temp = n // 2
        if n % 2 == 0:
            return self.myPow(x * x, temp)
        return x * self.myPow(x * x, temp)
