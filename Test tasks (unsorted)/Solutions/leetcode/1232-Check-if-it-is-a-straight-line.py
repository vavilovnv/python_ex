"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/

Category - Easy

You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
represents the coordinate of a point. Check if these points make a straight
line in the XY plane.


"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]
        for x3, y3 in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False
        return True
