"""
https://leetcode.com/problems/rotate-image/

Category - Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the
input 2D matrix directly. DO NOT allocate another 2D matrix and do the
rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

"""
hints:
clockwise rotate - first reverse matrix up to down, then swap the symmetry
anticlockwise rotate - first reverse left to right, then swap the symmetry
"""
