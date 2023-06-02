"""
https://leetcode.com/problems/largest-local-values-in-a-matrix/

Category - Easy

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid
centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3
matrix in grid.

Return the generated matrix.
"""

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [
            [max(
                max(grid[i][j:j+3]),
                max(grid[i+1][j:j+3]),
                max(grid[i+2][j:j+3]))
                for j in range(0, len(grid)-2)]
            for i in range(0, len(grid)-2)
        ]
