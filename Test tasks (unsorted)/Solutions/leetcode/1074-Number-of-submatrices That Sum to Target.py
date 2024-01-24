"""
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Category - Hard

Given a matrix and a target, return the number of non-empty submatrices that
sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with
x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
they have some coordinate that is different: for example, if x1 != x1'.
"""

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        res, n, m = 0, len(matrix) , len(matrix[0])
        for i in range(n):
            for j in range(1,m):
                matrix[i][j] += matrix[i][j-1]
        for i in range(m):
            for j in range(i,m):
                d = defaultdict(lambda:0)
                d[0], s = 1, 0
                for k in range(n):
                    temp = matrix[k][j]
                    if i > 0: 
                        temp -= matrix[k][i-1]
                    s += temp
                    res += d[s-target]
                    d[s] += 1
        return res
