"""
https://leetcode.com/problems/out-of-boundary-paths/

Category - Medium

There is an m x n grid with a ball. The ball is initially at the position
[startRow, startColumn]. You are allowed to move the ball to one of the four
adjacent cells in the grid (possibly out of the grid crossing the grid
boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the
number of paths to move the ball out of the grid boundary. Since the answer
can be very large, return it modulo 109 + 7..
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def helper(i, j, maxMove):
            if maxMove < 0:
                return 0
            if 0 > i or i >= m or 0 > j or j >= n:
                return 1
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            a = helper(i-1, j, maxMove - 1)
            b = helper(i+1, j, maxMove - 1)
            c = helper(i, j-1, maxMove - 1)
            d = helper(i, j+1, maxMove - 1)
            dp[i][j][maxMove] = a + b + c + d
            return dp[i][j][maxMove]
            
        dp = [[[-1] * (maxMove + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        result = helper(startRow, startColumn, maxMove)
        return result % (pow(10, 9) + 7)
