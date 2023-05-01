"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

Category - Easy

You are given an array of unique integers salary where salary[i] is the salary
of the ith employee.

Return the average salary of employees excluding the minimum and maximum
salary. Answers within 10-5 of the actual answer will be accepted.
"""

# TC: O(n) SC: O(1)
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))  
        salary.remove(max(salary))
        return sum(salary) / len(salary)
    
# TC: O(n) SC: O(n)
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / len(salary[1:-1])
