"""
https://leetcode.com/problems/pascals-triangle-ii/

Category - Easy

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above.
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                res[j] += res[j-1]
        return res
