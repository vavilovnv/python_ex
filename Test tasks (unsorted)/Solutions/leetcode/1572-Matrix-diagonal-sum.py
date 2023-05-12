"""
https://leetcode.com/problems/matrix-diagonal-sum/

Category - Easy

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the
elements on the secondary diagonal that are not part of the primary diagonal.
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum(
            mat[i][i] + (mat[i][n-i-1] if n-i-1 != i else 0) for i in range(n)
        )
