"""
https://leetcode.com/problems/arranging-coins/

Category - Easy

You have n coins and you want to build a staircase with these coins. The
staircase consists of k rows where the ith row has exactly i coins. The last
row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you
will build.
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if mid * (1 + mid) / 2 <= n < (mid + 1) * (2 + mid) / 2:
                return mid
            if mid * (1 + mid) / 2 > n:
                right = mid - 1
            else:
                left = mid + 1

"""
hint
for full k-staircase we need exactly k * (1 + k) / 2 rows
"""
        