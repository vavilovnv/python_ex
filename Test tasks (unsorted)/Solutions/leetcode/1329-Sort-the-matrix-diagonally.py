"""
https://leetcode.com/problems/sort-the-matrix-diagonally/

Category - Medium

A matrix diagonal is a diagonal line of cells starting from some cell in
either the topmost row or leftmost column and going in the bottom-right
direction until reaching the matrix's end. For example, the matrix
diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes
cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in
ascending order and return the resulting matrix.
"""

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        count, len1, len2 = [0] * 101, len(mat), len(mat[0])
        for i in range(len1 + len2 - 1):
            x, y = max(0, len1 - 1 - i), max(0, i - (len1 - 1))
            for d in range(min(len1 - x, len2 - y)):
                count[mat[x + d][y + d]] += 1
            d = 0
            for j in range(1, 101):
                while count[j]:
                    mat[x + d][y + d] = j
                    count[j] -= 1
                    d += 1
        return mat
