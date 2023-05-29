"""
https://leetcode.com/problems/course-schedule/

Category - Medium

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi first if
you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to
first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def helper(i):
            if not courses[i]:
                return False
            if i in visited:
                return True
            visited.add(i)
            for j in courses[i]:
                if helper(j):
                    return True
            visited.remove(i)
        
        courses = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            courses[c].append(p)
        for i in range(numCourses):
            visited = set()
            if helper(i):
                return False
            courses[i] = []
        return True
