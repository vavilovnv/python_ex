"""
https://leetcode.com/problems/01-matrix/

Category - Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for
each cell.

The distance between two adjacent cells is 1.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q, seen = deque(), set()
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        while q:
            x, y = q.popleft()
            for (i, j) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= i < n and 0 <= j < m and (i, j) not in seen:
                    mat[i][j] = mat[x][y] + 1
                    seen.add((i, j))
                    q.append((i, j))
        return mat

"""
hints
use the queue and first add items with a 0-value to the queue
"""
      