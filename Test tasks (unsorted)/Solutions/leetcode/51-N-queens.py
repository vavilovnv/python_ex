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
        solutions, column = [], set()
        board = [['.'] * n for _ in range(n)]
        pos_d, neg_d = set(), set()

        def backtrack(row):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return
            for c in range(n):
                if row + c in pos_d or row - c in neg_d or c in column:
                    continue
                column.add(c)
                neg_d.add(row - c)
                pos_d.add(row + c)
                board[row][c] = 'Q'
                backtrack(row + 1)
                column.remove(c)
                neg_d.remove(row - c)
                pos_d.remove(row + c)
                board[row][c] = '.'

        backtrack(0)
        return solutions
