"""
https://leetcode.com/problems/non-overlapping-intervals/

Category - Medium

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of
the intervals non-overlapping.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prev, count = 0, 1
        intervals.sort(key=lambda x: x[1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1
        return len(intervals) - count
        