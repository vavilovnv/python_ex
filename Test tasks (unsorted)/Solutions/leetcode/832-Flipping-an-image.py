"""
https://leetcode.com/problems/flipping-an-image/

Category - Easy

Given an n x n binary matrix image, flip the image horizontally, then invert
it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced
by 0.

For example, inverting [0,1,1] results in [1,0,0].
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 if i == 0 else 0 for i in row[::-1]] for row in image]
