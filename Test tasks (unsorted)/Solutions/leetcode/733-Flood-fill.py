"""
https://leetcode.com/problems/flood-fill/

Category - Easy

An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color), and so on. Replace the color of all of the
aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def helper(row, column):
            if (not (0 <= row < m and 0 <= column < n)
                or image[row][column] != prev_color):
                return
            image[row][column] = color
            helper(row - 1, column)
            helper(row + 1, column)
            helper(row, column - 1)
            helper(row, column + 1)
        
        prev_color = image[sr][sc]
        if prev_color != color:
            m, n = len(image), len(image[0])
            helper(sr, sc)
        return image

"""
hint
use bfs while 0 <= row < m and 0 <= column < n and
image[row][column] == prev_color
"""
