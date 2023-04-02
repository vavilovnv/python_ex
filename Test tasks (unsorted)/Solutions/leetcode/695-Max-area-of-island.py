"""
https://leetcode.com/problems/max-area-of-island/

Category - Medium

You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You
may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(a, b):
            if (not (0 <= a < rows and 0 <= b < columns)
                    or grid[a][b] == 0 or (a, b) in seen):
                return 0
            else:
                seen.add((a, b))
                return (1 + helper(a + 1, b) + helper(a - 1, b)
                        + helper(a, b + 1) + helper(a, b - 1))

        result, rows, columns, seen = 0, len(grid), len(grid[0]), set()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    result = max(result, helper(i, j))
        return result

"""
hint
use Depth-First Search (dfs) and set to store browsed items
"""
