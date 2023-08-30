"""
https://leetcode.com/problems/shift-2d-grid/

Category - Easy

On a 2D plane, there are n points with integer coordinates points[i] = 
[xi, yi]. Return the minimum time in seconds to visit all the points in the
order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then
one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but
these do not count as visits.
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)-1):
            p, next_p = points[i], points[i+1]
            res += max(abs(next_p[0] - p[0]), abs(next_p[1] - p[1]))
        return res
