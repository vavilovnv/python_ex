"""
https://leetcode.com/problems/rank-transform-of-an-array/

Category - Easy

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following
rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their
rank must be the same.
Rank should be as small as possible.
"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks, i = {}, 1
        for num in sorted(set(arr)):
            ranks[num] = i
            i += 1
        return [ranks[num] for num in arr]
