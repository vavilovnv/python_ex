"""
https://leetcode.com/problems/unique-paths-ii/

Category - Medium

You are given an m x n integer array grid. There is a robot initially located
at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that
the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach
the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to
2 * 109.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0] * m for _ in range(n)]
        for row in range(n):
            if obstacleGrid[row][0] == 1:
                break
            res[row][0] = 1
        for col in range(m):
            if obstacleGrid[0][col] == 1:
                break
            res[0][col] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[-1][-1]
