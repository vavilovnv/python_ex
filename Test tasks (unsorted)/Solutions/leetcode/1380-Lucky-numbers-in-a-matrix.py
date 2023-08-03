"""
https://leetcode.com/problems/lucky-numbers-in-a-matrix/

Category - Easy

Given an m x n matrix of distinct numbers, return all lucky numbers in the
matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element
in its row and maximum in its column.  
"""

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res, m, n = [], len(matrix), len(matrix[0])
        for i in range(m):
            temp = min(matrix[i])
            for j in range(n):
                if matrix[i][j] == temp == max(matrix[x][j] for x in range(m)):
                    res.append(matrix[i][j])
                    break
        return res
