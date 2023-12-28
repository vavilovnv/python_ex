"""
https://leetcode.com/problems/mirror-reflection/

Category - Medium

There is a special square room with mirrors on each of the four walls. Except
for the southwest corner, there are receptors on each of the remaining
corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest
corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray
meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.
"""

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        tmp = p
        while tmp % q != 0:
            tmp += p
        height, width = tmp // p, tmp // q
        return height % 2 + (width + 1) % 2
