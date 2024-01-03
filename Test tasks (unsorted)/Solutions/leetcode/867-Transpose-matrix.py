"""
https://leetcode.com/problems/transpose-matrix/

Category - Easy

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices.
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            res.append([matrix[j][i] for j in range(len(matrix))])
        return res
