"""
https://leetcode.com/problems/number-of-islands/

Category - Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(a, b):
            if (not (0 <= a < n and 0 <= b < m)
                or (a, b) in seen or grid[a][b] == '0'):
                return
            if grid[a][b] == '1':
                seen.add((a, b))
                helper(a - 1, b)
                helper(a + 1, b)
                helper(a, b - 1)
                helper(a, b + 1)

        res, seen, n, m = 0, set(), len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in seen:
                    res += 1
                    helper(i, j)
        return res

"""
hint
use dfs
"""
