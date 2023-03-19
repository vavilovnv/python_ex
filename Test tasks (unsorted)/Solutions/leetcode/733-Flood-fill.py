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
            if image[row][column] == color:
                return
            image[row][column] = color
            if row-1 >= 0 and image[row-1][column] == prev_color:
                helper(row-1, column)
            if row+1 < m and image[row+1][column] == prev_color:
                helper(row+1, column)
            if column-1 >= 0 and image[row][column-1] == prev_color:
                helper(row, column-1)
            if column + 1 < n and image[row][column+1] == prev_color:
                helper(row, column+1)
        prev_color = image[sr][sc]
        if prev_color == color:
            return image
        m, n = len(image), len(image[0])
        helper(sr, sc)
        return image
            