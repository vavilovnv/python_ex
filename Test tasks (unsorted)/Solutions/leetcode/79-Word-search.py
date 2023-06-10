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
        def helper(x, y, ind):
            if ind == len(word):
                return True
            if (x < 0 or y < 0 
                or x >= n or y >= m
                or board[x][y] != word[ind]
                or (x, y) in visited):
                return False
            res = False
            visited.add((x, y))
            for move_i, move_j in moves:
                res = res or helper(x + move_i, y + move_j, ind + 1)
            visited.remove((x, y))
            return res

        visited = set()
        n, m = len(board), len(board[0])
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if helper(i, j, 0):
                    return True
        return False
