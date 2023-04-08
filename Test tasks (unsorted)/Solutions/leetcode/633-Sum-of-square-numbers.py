"""
https://leetcode.com/problems/sum-of-square-numbers/description/

Category - Medium

Given a non-negative integer c, decide whether there're two integers a and b
such that a^2 + b^2 = c.
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(c ** 0.5)
        while a <= b:
            temp = a ** 2 + b ** 2
            if temp == c:
                return True
            elif temp < c:
                a += 1
            else:
                b -= 1
        return False

"""
hints
use binary search and math
we know that a^2 + b^2 = c, so if a == 0 then b == sqrt(c)
"""
