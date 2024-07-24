"""
https://leetcode.com/problems/n-queens-ii/

Category - Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens
puzzle.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        board = [['.'] * n for _ in range(n)]
        cols, pos_diag, neg_diag = set(), set(), set()

        def backtrack(row):
            if row == n:
                self.res += 1
                return

            for col in range(n):
                if (
                    row + col in pos_diag 
                    or row - col in neg_diag 
                    or col in cols
                ):
                    continue

                cols.add(col)
                neg_diag.add(row - col)
                pos_diag.add(row + col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                cols.remove(col)
                neg_diag.remove(row - col)
                pos_diag.remove(row + col)
                board[row][col] = '.'

        backtrack(0)
        return self.res
