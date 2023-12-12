"""
https://leetcode.com/problems/course-schedule-iii/

Category - Hard

There are n different online courses numbered from 1 to n. You are given an
array courses where courses[i] = [durationi, lastDayi] indicate that the ith
course should be taken continuously for durationi days and must be finished
before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses
simultaneously.

Return the maximum number of courses that you can take.
"""

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        day, planned = 0, []
        courses.sort(key=lambda x: x[1])
        for course in courses:
            if day + course[0] <= course[1]:
                day += course[0]
                heapq.heappush(planned, -course[0])
            elif len(planned) > 0 and course[0] < -planned[0]:
                day += course[0] + heapq.heapreplace(planned, -course[0])
        return len(planned)
