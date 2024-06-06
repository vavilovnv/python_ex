"""
https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

Category - Easy

You are working in a ball factory where you have n balls numbered from
lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and
an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to
the sum of digits of the ball's number. For example, the ball number 321 will
be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in
the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the
box with the most balls.
"""

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        res, d = 0, defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            num = sum(map(int, list(str(i))))
            d[num] += 1
            res = max(res, d[num])
        return res
