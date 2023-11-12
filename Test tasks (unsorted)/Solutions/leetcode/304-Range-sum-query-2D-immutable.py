"""
https://leetcode.com/problems/range-sum-query-2d-immutable/

Category - Medium

Given a 2D matrix matrix, handle multiple queries of the following type:
Calculate the sum of the elements of matrix inside the rectangle defined by
its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix
matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of
the elements of matrix inside the rectangle defined by its upper left
corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
"""

# TC - O(n), but O(1) in progress...
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(1, len(matrix[i])):
                self.matrix[i][j] += self.matrix[i][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not col1:
            return sum([self.matrix[i][col2] for i in range(row1, row2+1)])
        return sum([self.matrix[i][col2] - self.matrix[i][col1 - 1] for i in range(row1, row2+1)])
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
