"""
https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

Category - Easy

The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits
only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any
string in strs.
"""

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for s in strs:
            res = max(res, int(s) if s.isdigit() else len(s))
        return res
