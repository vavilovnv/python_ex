"""
https://leetcode.com/problems/set-matrix-zeroes/

Category - Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's.

You must do it in place.
"""
# TC: O(n * m) SC: O(n + m)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        rows, columns = set(), set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in rows:
            for j in range(m):
                matrix[i][j] = 0
        for i in range(n):
            for j in columns:
                matrix[i][j] = 0
