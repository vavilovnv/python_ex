"""
https://leetcode.com/problems/surface-area-of-3d-shapes/

Category - Medium

You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each
value v = grid[i][j] represents a tower of v cubes placed on top of cell
(i, j).

After placing these cubes, you have decided to glue any directly adjacent
cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.
"""

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res, rows, cols = 0, len(grid), len(grid[0])      
        for i in range(rows):
            for j in range(cols):
                temp = grid[i][j]
                if not temp:
                    continue
                res += 4 * temp + 2
                if rows - 1 - i:
                    res -= 2 * min(temp, grid[i + 1][j])
                if cols - 1 - j:
                    res -= 2 * min(temp, grid[i][j + 1])        
        return res
