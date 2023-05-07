"""
https://leetcode.com/problems/row-with-maximum-ones/

Category - Easy

Given a m x n binary matrix mat, find the 0-indexed position of the row that
contains the maximum count of ones, and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row
with the smallest row number should be selected.

Return an array containing the index of the row, and the number of ones in it.
"""

# TC: O(n) SC: O(n)
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [(i, sum(row)) for i, row in enumerate(mat)]
        return max(res, key=lambda x: (x[1], -x[0]))


# TC: O(n) SC: O(1)
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = i = 0 
        for ind, row in enumerate(mat):
            curr = sum(row)
            if res < curr:
                res = curr
                i = ind
        return [i, res]
