"""
https://leetcode.com/problems/power-of-three/

Category - Easy

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

# iterative solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


# recursive solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n / 3)

"""
hint
one liner is: `return n > 0 and 3**19 % n == 0`, because 3**19 is under 3**21-1
"""
