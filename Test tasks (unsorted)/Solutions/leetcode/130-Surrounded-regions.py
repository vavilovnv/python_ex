"""
https://leetcode.com/problems/surrounded-regions/

Category - Medium

Given an m x n matrix board containing 'X' and 'O', capture all regions that
are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def on_board(i, j):
            return 0 <= i < n and 0 <= j < m

        n, m, dq = len(board), len(board[0]), deque()
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(n):
            if board[i][0] == "O":
                dq.append((i, 0))
            if board[i][m-1] == "O":
                dq.append((i, m-1))

        for j in range(m):
            if board[0][j] == "O":
                dq.append((0, j))
            if board[n-1][j] == "O":
                dq.append((n-1, j))

        while dq:
            i, j = dq.popleft()
            board[i][j] = "#"
            for move in moves:
                x, y = i + move[0], j + move[1]
                if not on_board(x, y) or board[x][y] != "O":
                    continue
                dq.append((x, y))
                board[x][y] = "#"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    board[i][j] = "O" 
                elif board[i][j] == "O":
                    board[i][j] = "X"
