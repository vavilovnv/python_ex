"""
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

Category - Medium

You are given a rectangular cake of size h x w and two arrays of integers
horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the
ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the
jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal
and vertical position provided in the arrays horizontalCuts and verticalCuts.
Since the answer can be a large number, return this modulo 109 + 7.
"""

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        row = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            row = max(row, horizontalCuts[i] - horizontalCuts[i-1])
        row = max(row, h - horizontalCuts[-1])
        verticalCuts.sort()
        column = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            column = max(column, verticalCuts[i] - verticalCuts[i-1])
        column = max(column, w - verticalCuts[-1])
        return (row * column)  % (10**9 + 7)
