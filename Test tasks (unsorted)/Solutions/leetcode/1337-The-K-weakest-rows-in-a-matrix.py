"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

Category - Easy

You are given an m x n binary matrix mat of 1's (representing soldiers) and
0's (representing civilians). The soldiers are positioned in front of the
civilians. That is, all the 1's will appear to the left of all the 0's in each
row.

A row i is weaker than a row j if one of the following is true:
The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to
strongest.
"""

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n, m, res = len(mat), len(mat[0]), []
        for i in range(n):
            if mat[i][0] == 0:
                res.append((i, 0))
                continue
            left, right = 0, m - 1
            while left <= right:
                mid = left + (right - left) // 2
                if mat[i][mid] == 1 and (mid == m - 1 or mat[i][mid + 1] == 0):
                    res.append((i, mid + 1))
                    break
                elif mat[i][mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
        return [i[0] for i in sorted(res, key=lambda x:(x[1], x[0]))[:k]]

"""
hint
use binary search
"""
