"""
https://leetcode.com/problems/valid-perfect-square/

Category - Easy

Given a positive integer num, return true if num is a perfect square or false
otherwise.

A perfect square is an integer that is the square of an integer. In other
words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return mid
            if mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1

"""
hint
use binary search
"""
