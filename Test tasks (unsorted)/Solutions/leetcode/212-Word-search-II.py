"""
https://leetcode.com/problems/word-search-ii/description/

Category - Hard

Given an m x n board of characters and a list of strings words, return all
words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, seen = set(), set()
        root = TrieNode()
        rows, cols = len(board), len(board[0])
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for word in words:
            root.add(word)

        def dfs(row, col, node, word):
            if (
                row < 0 or col < 0
                or row == rows or col == cols
                or (row, col) in seen
                or board[row][col] not in node.children
            ):
                return

            seen.add((row, col))

            node = node.children[board[row][col]]
            word += board[row][col]
            if node.is_word:
                res.add(word)

            for r, c in moves:
                dfs(row + r, col + c, node, word)

            seen.remove((row, col))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(res)
