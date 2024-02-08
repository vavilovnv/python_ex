"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Category - Easy

Given an integer number n, return the difference between the product of its
digits and the sum of its digits.
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = list(map(int, list(str(n))))
        return reduce(mul, lst) - reduce(add, lst)
