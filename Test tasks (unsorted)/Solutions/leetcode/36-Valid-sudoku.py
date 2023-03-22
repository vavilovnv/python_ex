"""
https://leetcode.com/problems/valid-sudoku/description/

Category - Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily
solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s1, s2 = set(), set()
            for j in range(9):
                if (i + 1) % 3 == 0 and (j + 1) % 3 == 0:
                    s3 = set()
                    for x in range(i - 2, i + 1):
                        for y in range(j - 2, j + 1):
                            if board[x][y] != '.':
                                if board[x][y] in s3:
                                    return False
                                s3.add(board[x][y])
                if board[i][j] != '.':
                    if board[i][j] in s1:
                        return False
                    s1.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in s2:
                        return False
                    s2.add(board[j][i])
        return True

"""
hint
just brute force solving
"""
