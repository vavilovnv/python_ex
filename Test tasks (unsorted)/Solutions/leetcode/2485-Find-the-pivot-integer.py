"""
https://leetcode.com/problems/find-the-pivot-integer/

Category - Easy

Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all
elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is
guaranteed that there will be at most one pivot index for the given input.
"""

# TC: O(n) SC: O(n)
class Solution:
    def pivotInteger(self, n: int) -> int:
        c1, c2, s = 1, n, set()
        for i in range(1, n+1):
            if (i, c1) in s:
                return i
            s.add((i, c1))
            if (n + 1 - i, c2) in s:
                return n + 1 - i
            s.add((n + 1 - i, c2))
            c1 += i + 1
            c2 += n-i
        return -1
