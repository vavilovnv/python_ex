"""
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

Category - Easy

You are given two integers, x and y, which represent your current location on
a Cartesian grid: (x, y). You are also given an array points where each
points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is
valid if it shares the same x-coordinate or the same y-coordinate as your
location.

Return the index (0-indexed) of the valid point with the smallest Manhattan
distance from your current location. If there are multiple, return the valid
point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is
abs(x1 - x2) + abs(y1 - y2).
"""

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = []
        for i, v in enumerate(points):
            if v[0] == x or v[1] == y:
                res.append([i, abs(x - v[0]) + abs(y - v[1])])
        return min(res, key=lambda x: x[1])[0] if res else -1
