"""
https://leetcode.com/problems/island-perimeter/

Category - Easy

You are given row x col grid representing a map where grid[i][j] = 1
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to
the water around the island. One cell is a square with side length 1. The grid
is rectangular, width and height don't exceed 100. Determine the perimeter of
the island.
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                for move_i, move_j in moves:
                    if (i + move_i < 0 or i + move_i == n
                        or j + move_j < 0 or j + move_j == m):
                        res += 1
                    elif grid[i + move_i][j + move_j] == 0:
                        res += 1
        return res
        