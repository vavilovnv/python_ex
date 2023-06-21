"""
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

Category - Easy

There is an m x n matrix that is initialized to all 0's. There is also a 2D
array indices where each indices[i] = [ri, ci] represents a 0-indexed location
to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix
after applying the increment to all locations in indices.
"""

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        res, matrix = 0, [[0 for _ in range(n)] for _ in range(m)]
        for i, j in indices:
            for x in range(m):
                matrix[x][j] += 1
            for y in range(n):
                matrix[i][y] += 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 != 0:
                    res += 1
        return res
