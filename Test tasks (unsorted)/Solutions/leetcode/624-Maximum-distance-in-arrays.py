"""
https://leetcode.com/problems/maximum-distance-in-arrays/

Category - Medium

You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one)
and calculate the distance. We define the distance between two integers a and
b to be their absolute difference |a - b|.

Return the maximum distance.
"""

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, tmp_min, tmp_max = 0, arrays[0][0], arrays[0][-1]
        for curr in arrays[1:]:
            res = max(res, tmp_max - curr[0], curr[-1] - tmp_min)
            tmp_max = max(tmp_max, curr[-1])
            tmp_min = min(tmp_min, curr[0])    

        return res
