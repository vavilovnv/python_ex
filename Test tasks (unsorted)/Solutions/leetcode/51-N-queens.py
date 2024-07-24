"""
https://leetcode.com/problems/n-queens/

Category - Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You
may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space, 
respectively.
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, board = [], [["."] * n for _ in range(n)]
        cols, pos_diag, neg_diag = set(), set(), set()

        def backtracking(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if (
                    col in cols or
                    col + row in pos_diag or
                    col - row in neg_diag
                ):
                    continue 

                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(col + row)
                neg_diag.add(col - row)
                backtracking(row + 1)
                cols.remove(col)
                pos_diag.remove(col + row)
                neg_diag.remove(col - row)
                board[row][col] = "."

        backtracking(0)

        return res
