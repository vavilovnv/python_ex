"""
https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

Category - Easy

Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and
finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More
formally, return the number of students where queryTime lays in the interval
[startTime[i], endTime[i]] inclusive.
"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(
            startTime[i] <= queryTime <= endTime[i]
            for i in range(len(startTime))
        )
