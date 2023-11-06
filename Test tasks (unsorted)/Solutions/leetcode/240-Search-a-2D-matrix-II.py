"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

Category - Medium

Write an efficient algorithm that searches for a value target in an m x n
integer matrix matrix. This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)
        row, column = 0, n-1
        while column >= 0 and row < m:
            if target == matrix[row][column]:
                return True
            elif target < matrix[row][column]:
                column -= 1
            else:
                row += 1
        return False
