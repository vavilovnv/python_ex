"""
https://leetcode.com/problems/find-right-interval/

Category - Medium

You are given an array of intervals, where intervals[i] = [starti, endi] and
each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi
and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right
interval exists for interval i, then put -1 at index i.
"""

class Solution:
    def binary_search(self, start_time, num):
        if num > start_time[-1][0]:
            return -1

        left, right = 0, len(start_time) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if start_time[mid][0] >= num:
                right = mid - 1
            else:
                left = mid + 1
        return start_time[left][1]

    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        res = []
        start = [[intervals[i][0], i] for i in range(len(intervals))]
        start.sort()
        for end_time in (intervals[i][1] for i in range(len(intervals))):
            res.append(self.binary_search(start, end_time))
        return res
   