"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Category - Easy

Given a m x n matrix grid which is sorted in non-increasing order both
row-wise and column-wise, return the number of negative numbers in grid.
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res, m = 0, len(grid[0])
        for i in range(len(grid)):
            left, right = 0, m - 1
            while left <= right:
                mid = left + (right - left) // 2
                if grid[i][mid] < 0 and (mid == 0 or grid[i][mid - 1] >= 0):
                    res += m - mid
                    break
                elif grid[i][mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
        return res

"""
hint
use binary search
"""
