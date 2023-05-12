"""
https://leetcode.com/problems/spiral-matrix-ii/

Category - Medium

Given a positive integer n, generate an n x n matrix filled with elements from
1 to n2 in spiral order.
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)] 
        rows, cols, count = n, n, 1
        top, bottom, left, right = 0, rows-1, 0, cols-1
        while count <= n ** 2:
            for i in range(left, right+1):
                matrix[top][i] = count
                count += 1
            top += 1
            for i in range(top, bottom+1):
                matrix[i][right] = count
                count += 1
            right -= 1
            if top <= bottom:
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = count
                    count += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = count
                    count += 1
                left += 1
        return matrix
