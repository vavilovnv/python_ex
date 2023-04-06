"""
https://leetcode.com/problems/search-a-2d-matrix/

Category - Medium

You are given an m x n integer matrix matrix with the following two
properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous
row.
Given an integer target, return true if target is in matrix or false
otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res, m = False, len(matrix[0])
        for i in range(len(matrix)):
            if target > matrix[i][m-1]:
                continue
            left, right = 0, m - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1                    
        return res

"""
hint
use binary search
"""
