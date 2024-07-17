"""
https://leetcode.com/problems/word-search/

Category - Medium

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter
cell may not be used more than once.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, visited = len(board), len(board[0]), set()
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(row, col, idx):
            if len(word) == idx:
                return True

            if (
                row >= n or row < 0
                or col >= m or col < 0
                or (row, col) in visited
                or board[row][col] != word[idx]
            ):
                return False

            res = False
            visited.add((row, col))
            for move in moves:
                if dfs(row + move[0], col + move[1], idx + 1):
                    res = True
                    break
            visited.remove((row, col))

            return res

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
