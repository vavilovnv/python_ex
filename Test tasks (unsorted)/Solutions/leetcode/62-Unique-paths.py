"""
https://leetcode.com/problems/unique-paths/

Category - Medium

There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to
2 * 10^9.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lst = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                lst[i][j] = lst[i - 1][j] + lst[i][j - 1]
        return lst[m - 1][n - 1]

"""
hint
fill the grid, then lst[i - 1][j] + lst[i][j - 1] for each i and j
"""
