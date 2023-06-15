"""
https://leetcode.com/problems/equal-row-and-column-pairs/

Category - Medium

Given a 0-indexed n x n integer matrix grid, return the number of pairs
(ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in
the same order (i.e., an equal array).
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d, n, res = defaultdict(int), len(grid), 0
        for row in grid:
            d[str(row)] += 1
        for i in range(n):
            res += d[str([row[i] for row in grid])]
        return res
